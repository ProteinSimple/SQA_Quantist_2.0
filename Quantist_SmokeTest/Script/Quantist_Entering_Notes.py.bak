import Quantist_Removing_Files
import Load_CSV_File
from datetime import datetime

def Entering_Notes():
  
  q = Sys.WaitProcess("Quantist", 2000)
  if q.Exists:
    q.Terminate()

  try:
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
  
  while (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files()
  
  if (not treeView.HasItems):
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.SampleInvalidCSVFolder, "MetaData-Mod.csv")
  
  main = Aliases.Quantist.MainWindowView

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  treeView = main.RunTreeView
  treeViewItem = treeView.TreeViewItem
  
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  treeView.ClickItem("|[0]|[4]")
  aqUtils.Delay(ProjectSuite.Variables.Long_Delay)  
  textBox = main.MainView.CurvePanel.znotesView1.ztextBox1
  
  now = datetime.now() # current date and time
  date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
  year = now.strftime("%Y")
  month = now.strftime("%m")
  day = now.strftime("%d")
  time1 = now.strftime("%H_%M_%S")
  time2 = now.strftime("%H:%M:%S")  
  
  textBox.Keys("MetaData-Mod - new notes\r")
  textBox.Keys(date_time)

  filename = "MetaData-Mod_"+year+"_"+month+"_"+day+"_"+time1
  savedDir = ProjectSuite.Variables.SavedChangesFolder

  save_file(savedDir, filename)
  
  verify_saved(savedDir, filename, date_time)
  
def save_file(savedDir, filename):
  
  quantist = Aliases.Quantist
  menu = quantist.MainWindowView.Menu
  
  if (Aliases.Quantist.MainWindowView.Menu.MenuitemFile.Enabled == True):
     menu.WPFMenu.Click("File")

  if (quantist.HwndSource_PopupRoot.PopupRoot.MenuitemSaveMetadataMod.Enabled == True):
     menu.WPFMenu.Click("File|Save 'metadata-mod'")


  dlgSaveMetaDataModAs = Aliases.Quantist.dlg
  HWNDView = dlgSaveMetaDataModAs.DUIViewWndClassName.Explorer_Pane
  comboBox = HWNDView.FloatNotifySink.ComboBox
  comboBox.SetText(Project.Variables.SavedChangesFolder + filename)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  dlgSaveMetaDataModAs.btnSave.ClickButton()  
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  
#  Quantist 1.0.0.1     
#  dlgSavemetadatamodAs = quantist.dlg
#  hwn = dlgSavemetadatamodAs.DUIViewWndClassName.Explorer_Pane
#  tvNamespaceTreeControl = hwn.CtrlNotifySink.NamespaceTreeControl.tvNamespaceTreeControl
#  tvNamespaceTreeControl.ExpandItem("|Desktop|This PC|Local Disk (C:)")
#  tvNamespaceTreeControl.ExpandItem("|Desktop|This PC|Local Disk (C:)|Quantist")
#  tvNamespaceTreeControl.ExpandItem("|Desktop|This PC|Local Disk (C:)|Quantist|SQA-Quantist")
#  tvNamespaceTreeControl.ExpandItem("|Desktop|This PC|Local Disk (C:)|Quantist|SQA-Quantist|Test_Data")
#  tvNamespaceTreeControl.ClickItem("|Desktop|This PC|Local Disk (C:)|Quantist|SQA-Quantist|Test_Data|SampleQuantistFiles|Saved_Changes")

  
def verify_saved(savedDir, filename, date_time):
  q = Sys.WaitProcess("Quantist", 2000)
  if q.Exists:
    q.Terminate()

  try:
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
  
  while (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files()
  
  if (not treeView.HasItems):
    Load_CSV_File.Import_Data_File(savedDir, filename)
    
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)    
  main = Aliases.Quantist.MainWindowView
  main.RunTreeView.ClickItem("|[0]|[4]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
  aqObject.CheckProperty(main.MainView.CurvePanel.znotesView1.ztextBox1, "Text", cmpEqual, "MetaData-Mod - new notes\r\n"+date_time)
