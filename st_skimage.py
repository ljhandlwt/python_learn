#jh:func-base,lazy-type
import skimage
import skimage.io
import skimage.transform
import skimage.morphology
import skimage.filters
from matplotlib import pyplot as plt

#io.imread
#返回值:np.array,uint8
#shape:RGB(m,n,3),grey(m,n)
skimage.io.imread('a.jpg')#读入图片
skimage.io.imread('https://xxx.jpg')#网络图片
#其他参数
'''
as_grey:bool,是否变成灰度图片(浮点表示)
'''

#io.imshow
#输入是浮点,整数都行(还有自动根据范围调整)
skimage.io.imshow(img)#显示图片(调用matplotlib接口)
#io.show
skimage.io.show()#本质是plt.show()

#io.imsave
#输入是浮点,整数都行
skimage.io.imsave('a.jpg', img)

#transform.resize
#输入是浮点,整数都行
#输出是浮点
skimage.transform.resize(img, (224,224))
#其他参数
'''
order:int(0~5,默认1),样条插值的order
mode:'constant'(默认)|'edge'|'symmetric'|'reflect'|'wrap'
cval:float,?
clip:bool,?
preserve_range:bool,?
'''

