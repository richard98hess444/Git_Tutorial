import rospy
from std_msgs.msg import Int32MultiArray


def talker():
    pub = rospy.Publisher('cmd_servo', Int32MultiArray)
    rospy.init_node('cmd_servo_talker', anonymous=True)
    while not rospy.is_shutdown():
        id = [1801, 500, 1400, 2500, 1000]
        pub.publish(Int32MultiArray(data = id))

if __name__ == '__main__':

    try:
        talker()
    except rospy.ROSInterruptException:
        pass
