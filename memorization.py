def fibo(k): 
    pad = {0: 0, 1: 1} 
    def fib_inner(k): 
        if k not in pad: 
            pad[k] = fib_inner(k - 1) + fib_inner(k - 2) 
        return pad[k] 
    return fib_inner(k) 
if __name__ == "__main__": 
    print(fibo(10))
