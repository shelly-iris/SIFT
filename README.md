# SIFT
基于SIFT关键点检测的图像匹配

**简介：**

BFmatcher（Brute-Force Matching）暴力匹配，应用BFMatcher.knnMatch( )函数来进行核心的匹配，knnMatch（k-nearest neighbor classification）k近邻分类算法。

**效果展示：**

**eg1:首先测试的一组图像是之前在实验室调低曝光后的免驱相机拍摄的角点发光收集框，模拟的是双目相机看到的效果（从不同角度）。**

原图：

![image](https://user-images.githubusercontent.com/75011654/225857325-a16ecb8b-f94f-4eab-a6e9-24d7fad5f010.png)
![image](https://user-images.githubusercontent.com/75011654/225857510-a78297bc-1327-4053-a551-e67c093ea17c.png)

算法处理效果图：

![image](https://user-images.githubusercontent.com/75011654/225856768-adbff9f8-3a77-4802-8ea2-06f82a106194.png)

**eg2:第二组图片选取一组目标物体呈90角且视角偏移光线不同的图像（用手机拍摄自己的鼠标）**

原图：

![image](https://user-images.githubusercontent.com/75011654/225858192-e8bdc5f5-1b3c-4ed6-acc0-afa71ff5c9f6.png)
![image](https://user-images.githubusercontent.com/75011654/225858226-7fa57f61-df9e-446e-a81d-9f20540ed10f.png)

算法处理效果图：

![image](https://user-images.githubusercontent.com/75011654/225856798-3687d810-20a2-4f38-8269-7a22a1a599a0.png)

**eg3:第三组图像选择的是目标物体特写以及目标物体在复杂环境中的两张图片，也就是检测SIFT算法在目标检测中的应用效果：**

原图：

![image](https://user-images.githubusercontent.com/75011654/225858531-5092362c-4e72-441e-ae2e-337c798de800.png)
![Uploading image.png…]()

算法处理效果图：

![image](https://user-images.githubusercontent.com/75011654/225856838-8ddf29e5-5c71-4b1b-83af-8809404df4e5.png)

实践小结：

	SIFT算法对于双目图像匹配问题，目标检测问题有着比较好的实现效果，相比起传统的二值化findcounters方法有着更高的鲁棒性，实践证明，算法对于光线，旋转，尺度缩放，视角变化均有较好的不变性。识别检测特征点较多，匹配精度比较高。
  
	当然SIFT算法也存在缺点：相比起传统图像处理方法，对于大分辨率图像实时性不高，这个需要优化sift匹配算法提高效率。
