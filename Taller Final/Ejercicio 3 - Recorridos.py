def postOrden(inorder, preorder):
    postorden = _postOrden(inorder, preorder)
    postorden.reverse()
    return postorden

def _postOrden(inorder, preorder, post=[]):

    if len(preorder) == 0:
        return post

    pos_root = inorder.index(preorder[0])
    left_inorder, right_inorder = [], []
    
    for i in range(pos_root):
        left_inorder.append(inorder[i])

    for i in range(pos_root+1, len(preorder)):
        right_inorder.append(inorder[i])

    left_preorder = []
    for i in range(1,len(left_inorder)+1):
        left_preorder.append(preorder[i])

    right_preorder = []
    for i in range(len(left_inorder)+1,len(preorder)):
        right_preorder.append(preorder[i])

    post.append(preorder[0])
    _postOrden(right_inorder, right_preorder,post=post)
    _postOrden(left_inorder, left_preorder,post=post)

    return post

preorder = ["G","E","A","I","B","M","C","L","D","F","K","J","H"]
inorder  = ["I","A","B","E","G","L","C","D","F","M","K","H","J"]
post     = ["I","B","A","E","L","F","D","C","H","J","K","M","G"]

print(postOrden(inorder, preorder))