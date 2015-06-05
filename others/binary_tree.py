class TreeNode(object):
    def __init__(self, left = 0, right = 0, value = 0):
        self.left = left
        self.right = right
        self.value = value


def recover_binary_tree(in_seq, post_seq):
    tree_node = TreeNode(value = post_seq[-1])
    root_in_index = in_seq.find(tree_node.value)
    if(len(in_seq) == 1):
        return tree_node
    if 0 < root_in_index:
        tree_node.left = recover_binary_tree(in_seq[0: root_in_index], post_seq[0: root_in_index])
    if root_in_index+1 < len(in_seq):
        tree_node.right = recover_binary_tree(in_seq[root_in_index+1: len(in_seq)], post_seq[root_in_index: len(in_seq)-1])
    return tree_node

def deepest_path(tree):
    ret_str = tree.value
    ret_str1 = ''
    ret_str2 = ''
    if(tree.left):
        ret_str1 = deepest_path(tree.left)
    if(tree.right):
        ret_str2 = deepest_path(tree.right)
    if len(ret_str1) >= len(ret_str2):
        ret_str += ret_str1
    else:
        ret_str += ret_str2
    return ret_str


if __name__ == '__main__':
    in_order = 'TbHVh3ogPWFLuAfGrm1xJ7we0iQYnZ8Kvqk9y5CNBD24UlcpIEMaj6SROXsdzt'
    post_order = 'TVHo3hPgbFfAumr7Jxew1YQi0ZnGLKy9kqvNDBC54clU28EIRS6jdsXOaMpWtz'
    root = recover_binary_tree(in_order,post_order)
    print deepest_path(root)
