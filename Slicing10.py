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
    if k>n and k>0 and n>0:
      return s[n:k]
    if n==k and k>0 and n>0:
        return s[n]
    if n>k:
        return False
print(main("codeschooluz",2,-5))
