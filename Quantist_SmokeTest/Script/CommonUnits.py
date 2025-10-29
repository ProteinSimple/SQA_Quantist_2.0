def OSInfo():
  OSInfo = Sys.OSInfo
  
  # Obtains information on the running operating system
  # Sys.OSInfo.FullName
  Info = "Name: " + OSInfo.Name + " " 
  
  
  if OSInfo.Windows64bit:
    Info = Info + "64-bit version" + "\r\n"
  else:
    Info = Info + "32-bit version" + "\r\n"
  
  Info = Info + "Edition: " + OSInfo.Edition + "\r\n" +\
    "Service Pack Version: " + OSInfo.ServicePackVersion + "\r\n" +\
    "Version: " + OSInfo.Version
  
  # Posts the information to the test log
  Log.Message("Operating system information:", Info)
  Log.Message("Host Name: " + Sys.HostName)