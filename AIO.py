NullPointer = -1

class ListNode:
    def __init__(self, Data, Pointer):
        self.Data = Data
        self.Pointer = Pointer


class ListNode:
    def __init__(self):
        self.Data = None
        self.Pointer = NullPointer



StartPointer = NullPointer
FreeListPointer = 0
List = [ListNode() for i in range(7)]


def InitialiseList():
    global StartPointer, FreeListPointer, List
    StartPointer =NullPointer
    FreeListPointer = 0
    for Index in range(6):
        List[Index].Pointer = Index + 1

    List[6].Pointer = NullPointer


InitialiseList()
counter = 0
for item in List:
    print(f"Item {counter} is pointing to item {item.Pointer}")
    counter += 1


def InsertNode(NewItem):
    global FreeListPointer,StartPointer
    if FreeListPointer != NullPointer:
        NewNodePointer = FreeListPointer
        FreeListPointer = List[FreeListPointer].Pointer
        ThisNodePointer = StartPointer
        PreviousNodePointer = NullPointer
        while ThisNodePointer != NullPointer and List[ThisNodePointer].Data < NewItem:
            PreviousNodePointer = ThisNodePointer
            ThisNodePointer = List[ThisNodePointer].Pointer

        if PreviousNodePointer == StartPointer:
            List[NewNodePointer].Pointer = StartPointer
            StartPointer = NewNodePointer

        else:
            List[NewNodePointer].Pointer = List[PreviousNodePointer].Pointer
            List[PreviousNodePointer].Pointer = NewNodePointer

InsertNode(5)
counter = 0
    
