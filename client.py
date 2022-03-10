#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from ur5_pruning_trails.srv import position
from std_srvs.srv import Empty


rospy.init_node('use_service')

#wait the service to be advertised, otherwise the service use will fail
# rospy.wait_for_service('move_linear')

#setup a local proxy for the service
srv_move=rospy.ServiceProxy('Move_linear',position)
srv_home=rospy.ServiceProxy('Home_linear',Empty)
srv_stop=rospy.ServiceProxy('Stop_linear',Empty)

#use the service and send it a value. In this case, I can send 1 or 0
srv_home()
# srv_move(200)
# srv_stop()
