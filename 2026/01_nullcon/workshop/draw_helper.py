import ast
from graphviz import Digraph
from IPython.display import display

def draw_ast(node):
    dot = Digraph(comment='Expression Tree')
    dot.attr('node', shape='box', style='filled,rounded', color='lightgreen', fontname='Courier')
    
    def extract_nodes(n):
        """Recursively pulls ONLY math/logical elements, discarding AST wrapper objects."""
        if isinstance(n, (ast.Module, ast.Expr)):
            # Drill straight down through top-level wrappers
            if hasattr(n, 'body'):
                body = n.body[0] if isinstance(n.body, list) and n.body else n.body
                return extract_nodes(body)
            return extract_nodes(n.value) if hasattr(n, 'value') else (None, [])
            
        elif isinstance(n, ast.BinOp):
            return type(n.op).__name__, [n.left, n.right]
            
        elif isinstance(n, ast.UnaryOp):
            return type(n.op).__name__, [n.operand]
            
        elif isinstance(n, ast.BoolOp):
            return type(n.op).__name__, n.values
            
        elif isinstance(n, ast.Compare):
            # Condenses complex Python multi-comparisons into a single operator string
            op_label = ", ".join([type(op).__name__ for op in n.ops])
            return op_label, [n.left] + n.comparators
            
        elif isinstance(n, ast.Name):
            return f"{n.id}", []
            
        elif isinstance(n, ast.Constant):
            return f"{n.value}", []
            
        elif isinstance(n, ast.Call):
            # For functions or Z3 specific wrappers (e.g., Real('x'))
            func_name = n.func.id if isinstance(n.func, ast.Name) else "func"
            return func_name, n.args
            
        return None, []

    def build_graph(n, parent_id=None):
        label, children = extract_nodes(n)
        if not label:
            return
            
        # Create a completely unique identifier for this specific node placement
        node_id = str(id(n))
        dot.node(node_id, label)
        
        if parent_id:
            dot.edge(parent_id, node_id)
            
        for child in children:
            if isinstance(child, ast.AST):
                build_graph(child, node_id)

    build_graph(node)
    return display(dot)