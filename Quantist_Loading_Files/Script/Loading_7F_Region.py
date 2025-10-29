import Load_CSV_File 
import Quantist_Removing_Files

def loading_7F_region():
  main = Aliases.Quantist.MainWindowView
  treeView = main.RunTreeView
  
  #flag = True
  while (treeView.HasItems):
     treeView.TreeViewItem.DeleteButton.ClickButton()
     
  if (not treeView.HasItems):
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.SampleInvalidCSVFolder, "7F_Region.csv")
      
  aqUtils.Delay(ProjectSuite.Variables.Long_Delay)    

  Regions.Region_7F_csvFile.Check(Aliases.Quantist.MainWindowView.RunTreeView)

  main = Aliases.Quantist.MainWindowView
  main.RunTreeView.ClickItem("|[0]|[4]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)    
  Regions.Region_7F_SystemFileInformation.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel.ExpanderSystemFileInformation)
  
  scrollViewer = main.MainView.CurvePanel
  scrollViewer.ExpanderSystemFileInformation.Collapse()
  Regions.Region_7F_WarningErrors.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel.ExpanderWarningErrors)

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  scrollViewer.ExpanderWarningErrors.Collapse()
  expander = scrollViewer.ExpanderAssayLotInformation
  expander.Expand()
  Regions.Region_7F_AssayLotInformation.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel.ExpanderAssayLotInformation)

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  expander.Collapse()
  expander = scrollViewer.ExpanderCalibrationInformation
  expander.Expand()
  Regions.Region_7F_CalibrationInformation.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel.ExpanderCalibrationInformation)
  
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)      
  expander.Collapse()
  scrollViewer.ExpanderBatchInformation.Expand()
  Regions.Region_7F_BatchInformation.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel.ExpanderBatchInformation)
