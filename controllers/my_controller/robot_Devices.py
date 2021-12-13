from controller import Robot

class Robot_Devices:
  def __init__(self, robot, time_step, max_speed):
    #Motors
    self.left_motor = robot.getDevice('left wheel motor')
    self.right_motor = robot.getDevice('right wheel motor')
    self.left_motor.setPosition(float('inf'))
    self.right_motor.setPosition(float('inf'))
    self.left_motor.setVelocity(0.0)
    self.right_motor.setVelocity(0.0)
    
    #Enable IR sensors    
    self.center_ir = robot.getDevice("center_ir")
    self.center_ir.enable(time_step)
    self.l1_ir = robot.getDevice("l1_ir")
    self.l1_ir.enable(time_step)
    self.l2_ir = robot.getDevice("l2_ir")
    self.l2_ir.enable(time_step)
    self.l3_ir = robot.getDevice("l3_ir")
    self.l3_ir.enable(time_step)
    self.r1_ir = robot.getDevice("r1_ir")
    self.r1_ir.enable(time_step)
    self.r2_ir = robot.getDevice("r2_ir")
    self.r2_ir.enable(time_step)
    self.r3_ir = robot.getDevice("r3_ir")
    self.r3_ir.enable(time_step)
    
    self.rightWallSensor = robot.getDevice("ps2")
    self.rightWallSensor.enable(time_step)