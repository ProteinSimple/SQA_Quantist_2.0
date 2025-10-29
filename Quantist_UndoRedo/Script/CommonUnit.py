
#***************************************#
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
  
#***************************************#
def Import_Data_File(varDir, varFileName):
  
  try:
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)

    quantist = Aliases.Quantist
    quantist.MainWindowView.LoadButton.ClickButton()
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)    
    file = varDir + varFileName 
    
    dlgOpen = quantist.dlgOpen
    quantist.dlgOpen.OpenFile(file, "Supported Files (*csv;*.quantist)")

  except ValueError as Error:
    Log.Warning("Can not load run file to Run Control View {Error}")
        
  except OSError as err:
    print("OS error: {0}".format(err))
    
  except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise

    
#***************************************#    
def Loading_File():
  try:
    quantist = Aliases.Quantist
    mainWindowView = quantist.MainWindowView
    gridSplitter = mainWindowView.GridSplitter
    mainWindowView.Button.ClickButton()
    quantist.dlgOpen.OpenFile(ProjectSuite.Variables.SampleDataFolder + ProjectSuite.Variables.sample_csv_pm8800, "Supported Files (*csv;*.quantist)")
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    
    #f = open('myfile.txt')
    #s = f.readline()
    #i = int(s.strip())
  except OSError as err:
      print("OS error: {0}".format(err))
  #except ValueError:
  #    print("Could not convert data to an integer.")
  except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
    

#***************************************#    
def Removing_CSV_Files(flag):

  main = Aliases.Quantist.MainWindowView
  treeViewItem = Aliases.Quantist.MainWindowView.RunTreeView.TreeViewItem
  Xbutton = treeViewItem.DeleteButton

  unsaved_diag = Aliases.Quantist.MainWindowView.MainViewRunCtr.UserMessageBox
  
  if (Aliases.Quantist.MainWindowView.RunTreeView.HasItems):
    i = Aliases.Quantist.MainWindowView.RunTreeView.TreeViewItem.WPFControlOrdinalNo

  while (i != 0): 
    try:
        if (Aliases.Quantist.MainWindowView.RunTreeView.HasItems):
           Log.Message("Total Number of loading items: " + aqConvert.VartoStr(i))
    
        if (Xbutton.Exists):
           Xbutton.ClickButton()
           aqUtils.Delay(ProjectSuite.Variables.Short_Delay)       
    
        if (flag == True):
           if (Aliases.Quantist.MainWindowView.MainViewRunCtr.UserMessageBox.Visible):
              main.MaxButtonOk.ClickButton()
        i -= 1
        
    except:
        Log.Message("Can not remove run file from Run Control View")
        break
        
   #finally:
   #  break
   
  Log.Message("No more run file from Run Control View")