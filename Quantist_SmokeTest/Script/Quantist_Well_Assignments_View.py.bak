import Quantist_Removing_Files
import Load_CSV_File

def Well_Assignments_View():
  
  quantist = Aliases.Quantist
  mainWindowView = Aliases.Quantist.MainWindowView
  treeView = Aliases.Quantist.MainWindowView.RunTreeView

  flag=True
  while (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files(flag)
      
  if (not treeView.HasItems):
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.WellAssignmentsFolder, "PlateRunResults_Multiplate.csv")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)

  #Click on WAs View
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Aliases.Quantist.HwndSource_MainWindowView.MainWindowView.RunTreeView.ClickItem("|[0]|[2]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    
  #Verify WAs displays two 96-Well plates
  Regions.Two_96_Well_Plates.Check(Aliases.Quantist.MainWindowView.MainView.PlatesViewScrollViewer, False, False, 46540, 17)

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
  scrollViewer = Aliases.Quantist.MainWindowView.MainView.PlatesViewScrollViewer
  scrollViewer.Keys("^a")
  Regions.Two_96_Well_Plates_HighLighted.Check(Aliases.Quantist.MainWindowView.MainView.PlatesViewScrollViewer, False, False, 46540, 17)

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
  treeView.TreeViewItem.DeleteButton.ClickButton()
  
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  mainWindowView.MaxButtonOk.ClickButton()
