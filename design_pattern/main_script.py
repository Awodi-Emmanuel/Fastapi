import logger 

for i in range(4):
    print(i)
    logger.log_message("log message {}".format(i))