import configparser
"""This is a template of the configurations needed for the server object. 
Update the updated sections (last argument) with your local settings.
Code from: https://www.c-sharpcorner.com/article/configuration-files-in-python/#:~:text=Python%20can%20have%20config%20files,then%20print%20on%20the%20console.

"""

config_file = configparser.ConfigParser()

#SQL Server settings
config_file.add_section("SQLServerSettings")
# UPDATE THIS
config_file.set("SQLServerSettings", "host_name", "localhost")
config_file.set("SQLServerSettings", "user_name", "root")
config_file.set("SQLServerSettings", "user_password", "pw")


"""
config_file["Logger"]={
        "LogFilePath":"<Path to log file>",
        "LogFileName" : "<Name of log file>",
        "LogLevel" : "Info"
        }
        """

# SAVE CONFIG FILE
with open(r"configurations.ini", 'w') as configfileObj:
    config_file.write(configfileObj)
    configfileObj.flush()
    configfileObj.close()

print("Config file 'configurations.ini' created")

# PRINT FILE CONTENT
read_file = open("configurations.ini", "r")
content = read_file.read()
print("\n---Contents of the config file---")
print(content)
read_file.flush()
read_file.close()