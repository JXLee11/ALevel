# Found <- FALSE
# SearchFailed <- FALSE
# // Assume that we have a list of items called List
# // We are assuming that the search item is called SearchItem
# //Set boundaries of our search
# first <- 1
# last <- LEN(List)
# // Search for the item until we find it or we have searched the entire list
# WHILE NOT Found AND NOT SearchFailed DO
#     // find the middle item
#     Middle <- (first + last) DIV 2
#     // if the middle item is the item we are looking for, we are done
#     IF List[Middle] = SearchItem
#         THEN
#             Found <- TRUE
#         ELSE
#             IF first >= last
#                 THEN
#                     SearchFailed <- TRUE
#                 ELSE
#                     IF List[Middle] > SearchItem
#                         THEN
#                             // Search the first half of the list
#                             last <- Middle - 1
#                         ELSE
#                             // Search the second half of the list
#                             first <- Middle + 1
#                     ENDIF
#             ENDIF
#     ENDIF
# ENDWHILE
# IF Found
#     THEN
#         OUTPUT "Item found at position ", Middle
#     ELSE
#         OUTPUT "Item not found"
# ENDIF

found = False
Searchfailed = False
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
last = len(list)
first = 0
step = 0
SearchItem = int(input("SearchITem : "))
while not found and not Searchfailed:
    Middle = (first + last )// 2
    if list[Middle] == SearchItem:
        found = True
    elif first >= last:
        SearchFailed = True
    elif list[Middle] > SearchItem:
        last = Middle -1
        step = step + 1
    else:
        first = Middle + 1
        step = step + 1
print(step )
