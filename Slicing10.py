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
    if a>=n and a>=k and n<=k:
        return s[n:k] or s[n]
    else:
        return "False"
print(main("codeschooluz",2,5))

      