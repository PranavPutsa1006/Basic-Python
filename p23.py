def func_def(n1=5, n2=2):
    print(n1,n2)
    print(n1*n2)


func_def()           # no parameters => default values used
func_def(2)          # 1 parameter as shown => n1 value updated to 2, n2 unchanged
func_def(3,6)
func_def(3,4)
func_def()