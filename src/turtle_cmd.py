import rospy
import numpy as np
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class turtleSubscriber():
    def __init__(self):
        self.sub = rospy.Subscriber("my_turtle_pose", Pose, self.Callback)
        self.triggered = False

    def Callback(self, data):
        self.triggered = True
        self.x = data.x
        self.y = data.y
        self.theta = data.theta
        self.linear_velocity = data.linear_velocity
        self.angular_velocity = data.angular_velocity


def angularVelocity(direct):
    data = Twist()
    data.angular.z = direct*2 # gain
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=1)
    pub.publish(data)

def main():
    comp = 1
    diff_theta = 0
    turtle = turtleSubscriber()
    while not turtle.triggered: pass
    while 1:
        init_theta = turtle.theta
        print(init_theta)
        print('enter goal theta')
        goal_theta = float(input())
    
        while abs(goal_theta-turtle.theta) > 0.01:

            if abs(goal_theta-turtle.theta) > np.pi:
                if goal_theta-turtle.theta < 0:
                    diff_theta = goal_theta-turtle.theta + 2*np.pi
                else:
                    diff_theta = goal_theta-turtle.theta - 2*np.pi
            else:
                diff_theta = goal_theta - turtle.theta*comp
                # print(diff_theta)
            angularVelocity(diff_theta)
        
        angularVelocity(0)
        print('reach')
    
    
if __name__ == "__main__":
    rospy.init_node('turtle_cmd_node')
    main()