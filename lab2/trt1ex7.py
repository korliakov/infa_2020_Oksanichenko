import turtle as trt
def spirrral (n):
    for i in range(36*n):
        trt.forward(i/10)
        trt.left(10)
trt.shape('turtle')
trt.speed(20)
spirrral(20)