import turtle as trt
def kv (n):
    for i in range(n):
        trt.forward(i*20+10)
        trt.left(90)
        trt.forward(i*20+10)
        trt.left(90)
        trt.forward(i*20+10)
        trt.left(90)
        trt.forward(i*20+10)
        trt.penup()
        trt.forward(10)
        trt.right(90)
        trt.forward(10)
        trt.right(180)
        trt.pendown()
    
trt.shape('turtle')
kv(10)