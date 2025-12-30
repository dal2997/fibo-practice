def fn(n): 
    pad = {0: 0, 1: 1} 
    def sub_func(n):
        if n not in pad: 
            pad[n] = fib_inner(n - 1) + sub_func(n - 2) 
        return pad[n] 
    return sub_func(n) 
if __name__ == "__main__": 
    fn = fibo()
    print(fn(10))def fibo(k): 

