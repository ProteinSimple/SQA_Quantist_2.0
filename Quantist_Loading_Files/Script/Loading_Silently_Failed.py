import Load_CSV_File 
import Quantist_Removing_Files

def silently_failed():
  
  main = Aliases.Quantist.MainWindowView
  treeView = main.RunTreeView
  
  flag = True
  while (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files(flag)
     
  if (not treeView.HasItems):
    quantist = Aliases.Quantist
    quantist.MainWindowView.LoadButton.ClickButton()
    sampleFoder = ProjectSuite.Variables.SampleInvalidCSVFolder
    file = ProjectSuite.Variables.sample_csv_silent_failed
    quantist.dlgOpen.OpenFile(sampleFoder + file, "Supported Files (*csv;*.quantist)")

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)    
  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.MainViewRunCtr.UserMessageBox, "Enabled", cmpEqual, True)
  Aliases.Quantist.MainWindowView.MaxButtonOk.ClickButton()

  #Look for error file
  FileExists()
  
def FileExists():
  sPath = ProjectSuite.Variables.ErrorFileFolder
  if aqFileSystem.Exists(sPath):
    foundFiles = aqFileSystem.FindFiles(sPath, "error*")

    if foundFiles != None:
       while foundFiles.HasNext():
             aFile = foundFiles.Next()
             Log.Message("Quantist Error file is found from C:\\User\\...\\AppData\\Local\\biotechne\\quantist\\applog\\ folder: " + aFile.Name)
    else:
       Log.Message("No files were found.")    
    
def FileFinder():
  foundFiles = aqFileSystem.FindFiles("C:\\Work\\", "*.exe")
  if foundFiles != None:
    while foundFiles.HasNext():
      aFile = foundFiles.Next()
      Log.Message(aFile.Name)
  else:
    Log.Message("No files were found.")    
