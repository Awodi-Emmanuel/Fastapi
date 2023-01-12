class Logger(object):
    """A file-based message logger with the following properties
    
    Attributes:
        fil_name: a string representing the full path of the log file to which
        this logger will write its messages
    """
    
    def __init__(self, error):
        """Return a logger object whose file_name is *file_name*"""
        self.error = error
        
    def write_log(self, level, msg):
        """Write a message to the file_name for a specific logger instance"""
        with open(self.error,'a') as log_file:
            log_file.write("[{0}] {1}\n".format(level, msg))
            
    def critical(self, level, msg):
        self.write_log("CRITICAL", msg)