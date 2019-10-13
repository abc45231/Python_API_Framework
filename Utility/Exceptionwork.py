from ConfigParser import ConfigParser

config = ConfigParser()

#To read data from config file

config.read("../InputFiles/Config.cfg")

print(config.get("Section1","username"))
print(config.get("Section1","password"))


