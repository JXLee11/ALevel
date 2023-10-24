NullPointer = -1
class TreeNode:
    Data = ""
    LeftPointer = NullPointer
    RightPointer = NullPointer

RootPointer = NullPointer
FreePointer = 0
Tree = [TreeNode() for i in range(7)]
def InitialiseTree():
    for Index in range(0,5):
        Tree[Index].LeftPointer = Index + 1
    Tree[6].LeftPointer = NullPointer



def InsertNode(NewItem, RootPointer):
    FreePointer = 0
    if FreePointer != NullPointer:
        NewNodePointer = FreePointer
        FreePointer = Tree[FreePointer].LeftPointer
        Tree[NewNodePointer].Data = NewItem
        Tree[NewNodePointer].LeftPointer = NullPointer
        Tree[NewNodePointer].RightPointer = NullPointer
        if RootPointer == NullPointer:
            RootPointer = NewNodePointer
        else:
            ThisNodePointer = RootPointer
            while ThisNodePointer != NullPointer:
                PreviousNodePointer = ThisNodePointer
                if NewItem < Tree[ThisNodePointer].Data:
                    TurnedLeft = True
                    ThisNodePointer = Tree[ThisNodePointer].LeftPointer
                else:
                    TurnedLeft - False
                    ThisNodePointer = Tree[ThisNodePointer].RightPointer
            if TurnedLeft:
                Tree[PreviousNodePointer].LeftPointer = NewNodePointer
            else:
                Tree[PreviousNodePointer].RightPointer = NewNodePointer


def FindNode(SearchItem):
    ThisNodePointer = RootPointer
    while ThisNodePointer != NullPointer:
        if SearchItem < Tree[ThisNodePointer].Data:
            ThisNodePointer = Tree[ThisNodePointer].LeftPointer
        else:
            ThisNodePointer = Tree[ThisNodePointer].RightPointer
    return ThisNodePointer
