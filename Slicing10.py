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
   
    if n<k:
        return s[n:k]
    if n==k:
        return s[n]
print(main("codeschooluz",2,5))
