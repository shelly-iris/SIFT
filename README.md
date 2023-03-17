## Running the tests

python main.py <REF_path> <QRY_path> <name_of_query_image>

Ex : python main.py ../data/input.jpg ../data/query.jpg query

Result will be saved in the folder where is code

## 简介：

基于BFmatcher的SIFT实现过程：

BFmatcher（Brute-Force Matching）暴力匹配，应用BFMatcher.knnMatch( )函数来进行核心的匹配，knnMatch（k-nearest neighbor classification）k近邻分类算法。

## 效果演示：

eg1：首先测试的一组图像是之前在实验室调低曝光后的免驱相机拍摄的角点发光收集框，模拟的是双目相机看到的效果（从不同角度）。

原图：

![image](https://user-images.githubusercontent.com/75011654/225864235-44412c33-e99b-405f-81dd-d439045abfeb.png)
![image](https://user-images.githubusercontent.com/75011654/225864262-839842ed-f303-4734-87ec-a903e2f6da18.png)

算法处理效果：

![image](https://user-images.githubusercontent.com/75011654/225864313-981dd96d-d691-4ea4-b9d7-82b6eb565f33.png)

eg2:第二组图片选取一组目标物体呈90角且视角偏移光线不同的图像（用手机拍摄自己的鼠标）

原图：

![image](https://user-images.githubusercontent.com/75011654/225864524-99d6560c-48c3-4ffc-98a1-9d8261ab675f.png)
![image](https://user-images.githubusercontent.com/75011654/225864549-0a028142-f618-4f18-ace2-a5f37b96fcfe.png)

算法处理效果：

![image](https://user-images.githubusercontent.com/75011654/225864575-81c8dc11-a4b6-4154-b6b0-c152ccccf48e.png)

eg3:第三组图像选择的是目标物体特写以及目标物体在复杂环境中的两张图片，也就是检测SIFT算法在目标检测中的应用效果：

原图：

![image](https://user-images.githubusercontent.com/75011654/225864729-82b38e51-d3f5-40cc-ad6c-17f1f055f0d6.png)
![image](https://user-images.githubusercontent.com/75011654/225864749-537a23fc-52cf-47ab-879d-0e8b103a8a7c.png)

算法处理效果：

![image](https://user-images.githubusercontent.com/75011654/225864796-70b92788-27d3-46ba-9297-f4a0726bca4f.png)

## 实践总结：

	SIFT算法对于双目图像匹配问题，目标检测问题有着比较好的实现效果，相比起传统的二值化findcounters方法有着更高的鲁棒性，实践证明，算法对于光线，旋转，尺度缩放，视角变化均有较好的不变性。识别检测特征点较多，匹配精度比较高。
  
	当然SIFT算法也存在缺点：相比起传统图像处理方法，对于大分辨率图像实时性不高，这个需要优化sift匹配算法提高效率。
