def fibo(n): 
    pad = {0: 0, 1: 1} 
    def fib_inner(n): 
        if n not in pad: 
            pad[n] = fib_inner(n - 1) + fib_inner(n - 2) 
        return pad[n] 
    return fib_inner(n) 
if __name__ == "__main__": 
    print(fibo(10))
