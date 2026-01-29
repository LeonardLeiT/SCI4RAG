import uuid
import json
from enum import Enum, auto
from typing import Dict, Optional, Any, List

class Role(Enum):
    USER = auto()
    ASSISTANT = auto()

class DialogueNode:
    def __init__(self, role: Role, message: str, parent: Optional['DialogueNode'] = None):
        if not isinstance(role, Role):
            raise ValueError("role must be in Role_Enum")

        self.role = role        # AI or Human
        self.message = message  
        self.parent = parent    
        self.children: List['DialogueNode'] = []
        self.id = str(uuid.uuid4())

    def add_child(self, child_node: 'DialogueNode') -> None:           
        if child_node.role == self.role:
            raise ValueError("child node must differ parent")
            
        self.children.append(child_node)
        child_node.parent = self
        
    def is_user_node(self) -> bool:
        return self.role == Role.USER
        
    def __repr__(self) -> str:
        role_str = "user" if self.is_user_node() else "assistant"
        return f"DialogueNode(id={self.id[:8]}, role={role_str}, msg='{self.message[:20]}...', children={len(self.children)})"
    
    def get_full_path(self) -> List[str]:
        path = [self.id]
        current = self.parent
        while current:
            path.append(current.id)
            current = current.parent
        return path[::-1]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the node to a dictionary format"""
        return {
            "id": self.id,
            "role": self.role.name,  # Use the enum name
            "message": self.message,
            "children": [child.id for child in self.children],
            "parent": self.parent.id if self.parent else None
        }


class DialogueTree:
    def __init__(self):
        self.root: Optional[DialogueNode] = None
        self.node_index: Dict[str, DialogueNode] = {}  # Mapping from ID to node
        
    def add_node(self, role: Role, message: str, parent_id: Optional[str] = None) -> DialogueNode:
        """Add a new node to the tree"""
        parent = self.node_index.get(parent_id) if parent_id else None
        
        if parent_id and not parent:
            raise ValueError(f"Parent Node ID {parent_id} does not exist")
            
        new_node = DialogueNode(role, message, parent)
        
        if parent:
            parent.add_child(new_node)
        elif self.root is None:
            self.root = new_node
        else:
            raise ValueError("Tree already has a root node. Non-root nodes must specify a parent_id")
            
        self.node_index[new_node.id] = new_node
        return new_node
        
    def get_node(self, node_id: str) -> Optional[DialogueNode]:
        """Get a node by its ID"""
        return self.node_index.get(node_id)
        
    def __contains__(self, node_id: str) -> bool:
        """Check if a node ID exists"""
        return node_id in self.node_index
    
    def to_json(self, file_path: str = None) -> str:
        """Convert the dialogue tree to JSON format
        
        Args:
            file_path: Optional, if provided, save the JSON to the file
            
        Returns:
            JSON string
        """
        if not self.root:
            return "{}"
        
        # Build dictionary representations of all nodes
        nodes_dict = {
            node_id: node.to_dict()
            for node_id, node in self.node_index.items()
        }
        
        tree_dict = {
            "root_id": self.root.id,
            "nodes": nodes_dict
        }
        
        json_str = json.dumps(tree_dict, indent=2, ensure_ascii=False)
        
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(json_str)
        
        return json_str
    
    @classmethod
    def from_json(cls, file_path: str = None) -> 'DialogueTree':
        """Reconstruct the dialogue tree from a JSON string
        
        Args:
            json_str: JSON string
            
        Returns:
            Reconstructed DialogueTree instance
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            json_str = f.read()
        tree_dict = json.loads(json_str)
        tree = cls()
        
        if not tree_dict:
            return tree
        
        # First, create all nodes without establishing relationships
        nodes_data = tree_dict["nodes"]
        id_to_node = {}
        
        for node_id, node_data in nodes_data.items():
            role = Role[node_data["role"]]  # Convert string to enum
            node = DialogueNode(role, node_data["message"])
            node.id = node_id  # Preserve the original ID
            id_to_node[node_id] = node
        
        # Then, establish parent-child relationships
        for node_id, node_data in nodes_data.items():
            node = id_to_node[node_id]
            parent_id = node_data["parent"]
            
            if parent_id:
                parent = id_to_node[parent_id]
                node.parent = parent
                parent.children.append(node)  # Add the current node to the parent's children list
        
        # Set the tree's root node and index
        tree.root = id_to_node.get(tree_dict["root_id"])
        tree.node_index = id_to_node
        
        return tree

    def get_full_context(self, node_id: str) -> List[str]:
        """Get the full dialogue context based on the node ID (chooses the first child node when encountering a branch)
        
        Args:
            node_id: The node ID to start backtracking from
            
        Returns:
            List of complete dialogue messages in chronological order
        """
        if node_id not in self.node_index:
            raise ValueError(f"Node ID {node_id} does not exist")
            
        # Find the target node
        target_node = self.node_index[node_id]
        
        # Backtrack to the root node
        path = []
        current = target_node
        while current:
            path.append(current)
            current = current.parent
            
        # Reverse the path to start from the root node
        path = path[::-1]
        messages = []
        # First add all messages from root to target node
        for node in path:
            messages.append(f"{node.role.name}: {node.message}")
        
        # Then continue with the first child path if available
        if target_node.children:
            self._collect_messages_first_child(target_node.children[0], messages)
        return messages
    
    def _collect_messages_first_child(self, node: DialogueNode, messages: List[str]) -> None:
        """Recursively collect messages, always choosing the first child node"""
        messages.append(f"{node.role.name}: {node.message}")
        
        # If there are child nodes, choose the first child node to continue
        if node.children:
            self._collect_messages_first_child(node.children[0], messages)


if __name__ == "__main__":
    tree = DialogueTree.from_json("dialogue_tree.json")
    print(tree)
    print(tree.get_node("a478b637-2f0a-4264-a3c6-f7767fa6673a"))
    context = tree.get_full_context("a478b637-2f0a-4264-a3c6-f7767fa6673a")
    print(context)
    for message in context:
        print(message)