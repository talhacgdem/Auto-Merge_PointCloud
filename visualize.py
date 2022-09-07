import open3d as o3d
import numpy as np

arr = np.random.randn(500, 3)
print(arr)

pcl = o3d.geometry.PointCloud()
pcl.points = o3d.utility.Vector3dVector(arr)
o3d.visualization.draw_geometries([pcl], window_name="Arhas", width=1280, height=720)

