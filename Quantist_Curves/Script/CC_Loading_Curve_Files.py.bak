import Load_CSV_File 
import Quantist_Removing_Files

def Launch():
  
  q = Sys.WaitProcess("Quantist", 2000)
  if q.Exists:
    q.Terminate()

  try:
    #BuiltIn.ShowMessage("Launching Quantist successful!")
    TestedApps.Quantist.Run(1, True)
  
  except ValueError as Error:
    Log.Warning("Can not Launch Quantist {Error}")
        
  except OSError as err:
    print("OS error: {0}".format(err))
    
  except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
  

  mainWindowView = Aliases.Quantist.MainWindowView  
  treeView = Aliases.Quantist.MainWindowView.RunTreeView
  Xbutton = treeView.TreeViewItem.Button
  
  if (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files()
  
  if (not treeView.HasItems):
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.SampleDataFolder, "PM8800.csv")

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
  
#  treeView = Aliases.Quantist.MainWindowView.RunTreeView
#  tv = Aliases.Quantist.MainWindowView.RunTreeView.TreeViewItem.Exists
#  
#  if not (treeView.HasItems): 
#    quantist = Aliases.Quantist
#    quantist.MainWindowView.LoadButton.ClickButton()
#    str = ProjectSuite.Variables.SampleDataFolder + ProjectSuite.Variables.sample_csv_pm8800
#    quantist.dlgOpen.OpenFile(str, "Consumable Files (*.csv;*.quantist)")



