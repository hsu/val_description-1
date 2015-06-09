
# Recursive find/replace command for quickly changing names:
find . -type f -print0 | xargs -0 sed -i 's/NJ2_Origin_X/NeckYawOrigin_X/g'

@TODO
# Make sure this stuff is on your ROS_PACKAGE_PATH

# Generate URDF
cd V1_description/V1/models/V1
rosrun xacro xacro.py xacro/V1.xacro -o V1.urdf

# Generate SDF
source urdf2sdf.sh
