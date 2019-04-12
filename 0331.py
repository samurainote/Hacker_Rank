"""
もっとも大事になってくるのはデータ構造とアルゴリズム。
出題された問題に対して、
- 計算時間
- メモリ使用量
の観点から、最も優れたデータ構造を選び出し、高速なアルゴリズムを実装する。
"""

"""
1. 連結リスト(Linked List)
2. スタック(Stack)
3. キュー(Queue)
4. ハッシュテーブル(Hashtable)
"""

"""
標準クラス
.yield()
sys
math
"""

"""
データ型
1. 追加 insert()
2. 削除 remove()
3. 更新 uodate()
4. 並び替え sort()
5. 検索 search()
"""

"""
Tree
1. Root
2. Node -> None
3. Leaf -> True
- parent
- child
* 重複は許されない
* 検索と更新に優れている
"""

"""
None
True
あるかないか
"""
# user
bst = Tree()
bst.insert(14)
bst.preorder()
bst.postorder()
bst.inorder()

class Node():
    # Attribution * 3
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None

    # 追加
    def insert(self, data):
        # 探索木で重複は許されない
        if self.value == data:
            return False
        # Nodeより値が小さい時
        elif self.value > data:
            # すでに左子ノードが存在する場合は更新
            if self.leftChild:
                return self.leftChild.insert(data)
            # 左子ノードが存在しない場合は新規作成
            else:
                self.leftChild = Node(data)
                return True
        # Nodeより値が大きい時
        else:
            # すでに右子ノードが存在する場合は更新
            if self.rightChild:
                return self.rightChild.insert(data)
            # 右子ノードが存在しない場合は新規作成
            else:
                self.rightChild = Node(data)
                return True

    # 検索
    def find(self, data):
        # クエリの値とマッチしたらTrue
		if(self.value == data):
			return True
        # クエリの値がノードの値より小さい時 -> 左
		elif self.value > data:
            # すでに左子ノードが存在する場合は更新
			if self.leftChild == True:
				return self.leftChild.find(data)
            # 左子ノードが存在しないLeafの場合はFalse
			else:
				return False
        # クエリの値がノードの値より小さい時 -> 右
		else:
            # すでに右子ノードが存在する場合は更新
			if self.rightChild:
				return self.rightChild.find(data)
            # 右子ノードが存在しないLeafの場合はFalse
			else:
				return False

    # 高さ（エッジ数）を計る関数
	def getHeight(self):
		if self.leftChild and self.rightChild:
			return 1 + max(self.leftChild.getHeight(), self.rightChild.getHeight())
		elif self.leftChild:
			return 1 + self.leftChild.getHeight()
		elif self.rightChild:
			return 1 + self.rightChild.getHeight()
		else:
			return 1

    # 高さ（エッジ数）を計る関数
	def preorder(self):
		if self:
			print (str(self.value))
			if self.leftChild:
				self.leftChild.preorder()
			if self.rightChild:
				self.rightChild.preorder()

	def postorder(self):
		if self:
			if self.leftChild:
				self.leftChild.postorder()
			if self.rightChild:
				self.rightChild.postorder()
			print (str(self.value))

	def inorder(self):
		if self:
			if self.leftChild:
				self.leftChild.inorder()
			print (str(self.value))
			if self.rightChild:
				self.rightChild.inorder()
