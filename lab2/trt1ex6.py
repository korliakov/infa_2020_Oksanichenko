import turtle as trt
def spudeer (n):
    for i in range(n):
        trt.forward(100)
        trt.stamp()
        trt.left(180)
        trt.forward(100)
        trt.left(180)
        trt.left(360/n)
trt.shape('turtle')
spudeer(12)