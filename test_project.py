
import os
from project import validate_date, log_event, view_log


def test_validate_date():
    assert validate_date("banana") is None
    assert validate_date("2026-08-26").year == 2026
    
    
def test_log_event():
    log_event("feed", "test_log.csv")
    
    with open("test_log.csv") as file:
        contents = file.read()
        
    assert "feed" in contents
    os.remove("test_log.csv")
    
def test_view_log(capsys):
    log_event("feed", "test_log.csv")     
    view_log("test_log.csv")             
    
    output = capsys.readouterr().out 
    assert "feed" in output
    os.remove("test_log.csv")