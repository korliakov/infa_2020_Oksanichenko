import turtle as trt
def kvspirrral (n):
    for i in range(4*n):
        trt.forward(10*i)
        trt.left(90)
trt.shape('turtle')
trt.speed(5)
kvspirrral(10)