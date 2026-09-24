from helper import debug_log
from robot import Robot
from movement import Movement
from pybricks.tools import wait, StopWatch

rightSpeed: int = 400
leftSpeed: int = 600

def yellow_run(robot: Robot, mv: Movement):
    debug_log("Starting Yellow Run")

    return