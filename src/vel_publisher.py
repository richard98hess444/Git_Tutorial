import rospy
from std_msgs.msg import Float32

def talker(vel):
    if vel == 0:
        dt = 0
    elif vel > 0:
        dt = -50/0.095*vel + 150
    elif vel < 0:
        vel = -vel
        dt = -(-50/0.095*vel + 150)
    pub = rospy.Publisher('cmd_linvel', Float32, queue_size=2)
    pub.publish(dt)

def velocity_filter(vel):
    if abs(vel) > 0.25:
        vel = 0
    return vel

if __name__ == '__main__':
    rospy.init_node('vel_publisher', anonymous=True)
    talker(0)
    try:
        while not rospy.is_shutdown():
            print('Enter -0.25 to 0.25: ')
            x = float(input())
            vel_filter = velocity_filter(x)
            talker(vel_filter)
    except rospy.ROSInterruptException:
        pass