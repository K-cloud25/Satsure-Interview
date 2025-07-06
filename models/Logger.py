from datetime import datetime
class Logger:
    
    FILEPATH = "log.txt"
    
    def log( stmt:str, log_level="INFO") -> None:
        d = datetime.now()
        with open( Logger.FILEPATH, "+a") as log_file:
            log_file.writelines( "[" +d.strftime("%Y-%m-%d %H:%M:%S" + "]") + " : " + log_level + " : " + stmt)
            log_file.writelines("\n")   
        