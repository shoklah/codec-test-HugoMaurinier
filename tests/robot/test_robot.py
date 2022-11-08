from robot.robot import robot

def test_turn_left():
    robot1 = robot(5, 5)
    assert robot1.move("L") == (1, 1, "West")

def test_turn_right():
    robot1 = robot(5, 5)
    assert robot1.move("R") == (1, 1, "East")

def test_move_forward():
    robot1 = robot(5, 5)
    assert robot1.move("F") == (1, 2, "North")

def test_move_forward_twice():
    robot1 = robot(5, 5)
    assert robot1.move("FF") == (1, 3, "North")

def test_move_out_of_map():
    robot1 = robot(1, 1)
    assert robot1.move("F") == (1, 1, "North")

def test_move_out_of_map_blocking():
    robot1 = robot(1, 1)
    assert robot1.move("FR") == (1, 1, "East")

def test_basic_command():
    robot1 = robot(5, 5)
    assert robot1.move("RF") == (2, 1, "East")

def test_medium_command():
    robot1 = robot(5, 5)
    assert robot1.move("FFRFLFLF") == (1, 4, "West")

def test_huge_command():
    robot1 = robot(5, 5)
    assert robot1.move("FFRFLFLFRFFLFFRL" * 100) == (5, 4, "North")

def test_huge_map():
    robot1 = robot(10000000000000000, 10000000000000000)
    assert robot1.move("FFRFLFLF") == (1, 4, "West")
