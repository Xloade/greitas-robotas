from controller import Robot
from robot_Devices import Robot_Devices
import time

def current_milli_time():
    return round(time.time() * 1000)

def changeSpeed(left_Motor, right_Motor,left_Speed, right_Speed, history, time_step, steps_Passed):
    if history is not None:
        history.append((left_Speed, right_Speed, time_step*steps_Passed))
    left_Motor.setVelocity(left_Speed)
    right_Motor.setVelocity(right_Speed)

def changeToRelitiveTime(history):
    rez = list()
    for i in range(len(history)):
        if(i < len(history)-1):
            rez.append((history[i][0], history[i][1], (history[i+1][2]-history[i][2])))
        else:
            rez.append((history[i][0], history[i][1], 0))
    return rez

def fallowLine(time_step, max_speed,robot, devices, first_Time):
    

    steps_Passed = 0
    history = list()
    #Step simulation
    while robot.step(time_step) != -1:
        steps_Passed += 1
        #read IR sensors
        center_ir_value = devices.center_ir.getValue()
        l1_ir_value = devices.l1_ir.getValue()
        l2_ir_value = devices.l2_ir.getValue()
        l3_ir_value = devices.l3_ir.getValue()
        r1_ir_value = devices.r1_ir.getValue()
        r2_ir_value = devices.r2_ir.getValue()
        r3_ir_value = devices.r3_ir.getValue()
        
        wallSensorValue = devices.rightWallSensor.getValue()
        # print("center: {} left3: {} right3 : {} wall: {}".format(center_ir_value, l3_ir_value,r3_ir_value, wallSensorValue))
        
        left_speed = max_speed
        right_speed = max_speed
        #stop
        if(wallSensorValue > 80 and (steps_Passed>1000 or first_Time)):
            changeSpeed(devices.left_motor, devices.right_motor,0,0,history, time_step, steps_Passed)
            break
        
        if(center_ir_value == 1000):
            left_speed = 0
            right_speed = 0
        # elif(40 < l1_ir_value < 600):
            # left_speed = -max_speed*0.1
        # elif(40 < r1_ir_value < 600):
            # right_speed = -max_speed*0.1
        # elif(40 < l2_ir_value < 600):
            # left_speed = -max_speed*0.5
        # elif(40 < r2_ir_value < 600):
            # right_speed = -max_speed*0.5
        # elif(40 < l3_ir_value < 600):
            # left_speed = -max_speed
        # elif(40 < r3_ir_value < 600):
            # right_speed = -max_speed
            
        elif(40 < l1_ir_value < 600):
            left_speed = max_speed*0.3
        elif(40 < l2_ir_value < 600):
            left_speed = -max_speed*0.5
        elif(40 < l3_ir_value < 600):
            left_speed = -max_speed
        if(40 < r1_ir_value < 600):
            right_speed = max_speed*0.3
        elif(40 < r2_ir_value < 600):
            right_speed = -max_speed*0.5
        elif(40 < r3_ir_value < 600):
            right_speed = -max_speed
        
        changeSpeed(devices.left_motor, devices.right_motor, left_speed, right_speed,history, time_step, steps_Passed)
    return history
def history_average(history, average_range):
    rez = list()
    for i in range(0,len(history)-average_range+1,average_range):
        new_left_speed = 0
        new_right_speed = 0
        for k in range(average_range):
            new_left_speed += history[i+k][0]
            new_right_speed += history[i+k][1]
        new_left_speed = new_left_speed/average_range
        new_right_speed = new_right_speed/average_range
        
        rez.append((new_left_speed,new_right_speed,history[i][2]*average_range))
    return rez
def repeat(history,robot, devices, speed_up):
    steps_Passed = 0
    #Step simulation
    while steps_Passed < len(history) and robot.step(int(history[steps_Passed][2]/speed_up)) != -1:
        changeSpeed(devices.left_motor, devices.right_motor, history[steps_Passed][0]*speed_up, history[steps_Passed][1]*speed_up,None, None,None)   
        steps_Passed += 1
def run_robot(robot):
    time_step = 32
    max_speed = 6.28 / 2
    devices= Robot_Devices(robot, time_step, max_speed)
    fallowLine(time_step, max_speed,robot, devices, True)
    print("-------------------------------Start-----------------------------------")
    history = fallowLine(time_step, max_speed,robot, devices, False)
    print("-------------------------------Start-----------------------------------")
    history = changeToRelitiveTime(history)
    history = history_average(history,30)
    repeat(history,robot, devices, 2)
    devices.left_motor.setVelocity(0.0)
    devices.right_motor.setVelocity(0.0)
    

if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)