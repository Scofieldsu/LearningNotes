## 热力图总结

**我们的需求：平面图、定位坐标作为输入，输出图片格式的热力图。**

关于热力图的实现有几种应用方式：

1. 基于地图的热力图，输入一组经纬度定位坐标，结合一些第三方的地图资源（高德，百度，谷歌，阿里云地图）最后在地图上绘制热力。




2. 对于网页浏览记录的热力，记录用户的鼠标移动或者点击位置，结合热力相关的js库，最后对该网页的热点浏览区域进行绘制热力图。





1.heatmap.js
github: https://github.com/pa7/heatmap.js
官网：https://www.patrick-wied.at/static/heatmapjs/

Uncaught DOMException: Failed to execute 'getImageData' on 'CanvasRenderingContext2D': The source height is 0.

sharpmap

openlayer

arcgis

高德

leaflet-heat

jHeatChart




R语言的ggplot2 ，python的pyheatmap
BDP网站，基于经纬度坐标实现地图热力，企业用户收费。
