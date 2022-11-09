from pilot import main

def test_main():
    assert main(["pilot.py", "5x5", "FFRFLFLF"]) == 0

def test_main_invalid_map_dimensions():
    assert main(["pilot.py", "5", "FFRFLFLF"]) == 1

def test_main_invalid_arguments():
    assert main(["pilot.py", "5x5"]) == 1

def test_main_valid_command():
    assert main(["pilot.py", "5x5", "FFRFLFLF"]) == 0

def test_main_print_valid_command(capfd):
    main(["pilot.py", "5x5", "FFRFLFLF"])
    out, err = capfd.readouterr()
    assert out == "1,4,West\n"

def test_main_print_invalid_map_dimensions(capfd):
    main(["pilot.py", "5", "FFRFLFLF"])
    out, err = capfd.readouterr()
    assert out == '''Usage: python3 pilot.py <map_dimensions> <command>
        ex: python3 pilot.py 5x5 FFRFLFLF
'''

def test_main_print_invalid_arguments(capfd):
    main(["pilot.py", "5x5"])
    out, err = capfd.readouterr()
    assert out == '''Usage: python3 pilot.py <map_dimensions> <command>
        ex: python3 pilot.py 5x5 FFRFLFLF
'''