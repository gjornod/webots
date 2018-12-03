# Copyright 1996-2018 Cyberbotics Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""enable_all_lidars controller."""

from controller import Node, Robot
import sys

robot = Robot()
timestep = int(robot.getBasicTimeStep())
lidars = []

for i in range(robot.getNumberOfDevices()):
    device = robot.getDeviceByIndex(i)
    if (device.getNodeType() == Node.LIDAR):
        lidars.append(device)
        device.enable(timestep)
        device.enablePointCloud()

if len(lidars) == 0:
    sys.exit("This vehicle has no 'Lidar' node.")

while robot.step(timestep) != -1:
    for lidar in lidars:
        lidar.getPointCloud()