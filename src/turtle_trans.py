import rospy
from geometry_msgs.msg import Vector3
from turtlesim.msg import Pose


def callback(data):
    pub = rospy.Publisher('my_turtle_pose', Pose, queue_size=1)
    pub.publish(data)

def main():
    rospy.Subscriber("/turtle1/pose", Pose, callback)
    rospy.spin()
    

if __name__ == "__main__":
    rospy.init_node('turtle_trans_node')
    main()