def fib(n):
  """Recursive implementation of a Fibonacci sequence"""
   if n==0:
      return 0
   elif n == 1:
      return 1
   else:
      return fib(n-1) + fib(n-2)