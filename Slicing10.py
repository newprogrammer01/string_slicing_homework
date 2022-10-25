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
   
    if n<k or n>k:
        return s[n:k]
    if n==k:
        return s[n] or s[k]
print(main("codeschooluz",2,7))
