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
    if   n>=0 and n<=a and n<k and k<=a:
        return s[n:k]
    if n==k and n>=0 and n<=a:
        return s[k] or s[n]
    if n>a and k>a:
        return False
    
print(main("codeschooluz",22,22))
      