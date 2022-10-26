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
    answer=s[n:k] or s[n] or s[k]
    if a>=n and a>=k and n<=k:
        return answer
    else:
        return "False"
print(main("apple",2,2))



      