def main(s,n,k):
    """
    The s string variable is given. return from index n to index k.
    Args:
        s(str): parameter
        n(int): parameter
        k(int): parameter
    Returns:
        str: answer
    """
    a=len(s)
    b=a%2
    c=a//2
    if b==1:
        return s[c]
    if b==0:
        return s[n:k]
    
print(main("codeschooluz",2,2))
