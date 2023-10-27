# FUNCTION Factorial(n: INTEGER) RETURN INTEGER
#     Result <- 1
#     FOR i <- 1 TO n
#         Result <- Result * i
#     NEXT i
#     RETURN Result
# ENDFUNCTION
'''
def Factorial(n):
    result = 1
    for i in range(1,n):
        result = result * i
    print(result)
'''
'''
def Factorial(n):
    if n == 1:
        result = 1
    else:
        result = (n* Factorial(n-1))

    return result


print(Factorial(10))
'''
'''
PROCEDURE CountDown(n : INTEGER)
    FOR i <- n TO 1
        OUTPUT i
    Next i - 1
ENDPROCEDURE

PROCEDURE CountDown(n : INTEGER)
    IF n > 0 
        THEN
            OUTPUT n
            CALL CountDown(n-1)
    ENDIF
ENDPROCEDURE
'''

def CountDown(n):
    if n > 0:
        print(n)
        CountDown(n-1)

    return(n)

CountDown(10)