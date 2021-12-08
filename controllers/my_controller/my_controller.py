from controller import Robot

def run_robot(robot):

    time_step = 32
    max_speed = 6.28

    #Motors
    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)
    
    #Enable IR sensors    
    center_ir = robot.getDevice("center_ir")
    center_ir.enable(time_step);
    l1_ir = robot.getDevice("l1_ir")
    l1_ir.enable(time_step);
    l2_ir = robot.getDevice("l2_ir")
    l2_ir.enable(time_step);
    l3_ir = robot.getDevice("l3_ir")
    l3_ir.enable(time_step);
    r1_ir = robot.getDevice("r1_ir")
    r1_ir.enable(time_step);
    r2_ir = robot.getDevice("r2_ir")
    r2_ir.enable(time_step);
    r3_ir = robot.getDevice("r3_ir")
    r3_ir.enable(time_step);
    
    rightWallSensor = robot.getDevice("ps2")
    rightWallSensor.enable(time_step);
   

    #Step simulation
    while robot.step(time_step) != -1:
        #read IR sensors
        center_ir_value = center_ir.getValue();
        l1_ir_value = l1_ir.getValue();
        l2_ir_value = l2_ir.getValue();
        l3_ir_value = l3_ir.getValue();
        r1_ir_value = r1_ir.getValue();
        r2_ir_value = r2_ir.getValue();
        r3_ir_value = r3_ir.getValue();
        
        wallSensorValue = rightWallSensor.getValue();
        print("center: {} left3: {} right3 : {} wall: {}".format(center_ir_value, l3_ir_value,r3_ir_value, wallSensorValue))


        
        left_speed = max_speed
        right_speed = max_speed
        
        #stop
        if(wallSensorValue > 80):
            left_speed = 0
            right_speed = 0
        
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
        
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)

if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)