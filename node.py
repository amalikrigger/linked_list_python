from typing import Any, Optional

class Node:
    def __init__(self, value: Any, next: Optional['Node'] = None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"Node({self.value})"
