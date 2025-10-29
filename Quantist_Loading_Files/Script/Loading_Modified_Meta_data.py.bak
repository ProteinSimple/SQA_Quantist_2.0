import Load_CSV_File 
import Quantist_Removing_Files

def mod_metadata():
  
  main = Aliases.Quantist.MainWindowView
  treeView = main.RunTreeView
  
  while (treeView.HasItems):
     treeView.TreeViewItem.DeleteButton.ClickButton()
     
  if (not treeView.HasItems):
    quantist = Aliases.Quantist
    quantist.MainWindowView.LoadButton.ClickButton()
    sampleFoder = ProjectSuite.Variables.SampleInvalidCSVFolder
    file = ProjectSuite.Variables.sample_csv_mod_metadata
    quantist.dlgOpen.OpenFile(sampleFoder + file, "Supported Files (*csv;*.quantist)")

  aqUtils.Delay(ProjectSuite.Variables.Long_Delay)
  treeView.ClickItem("|[0]|[4]")
  Regions.Mod_metadata_warningErrors.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel.ExpanderWarningErrors.Border)
  scrollViewer = main.MainView.CurvePanel
  scrollViewer.ExpanderWarningErrors.Collapse()

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  expander = scrollViewer.ExpanderAssayLotInformation
  expander.Expand()
  Regions.Mod_metadata_ExpanderAssayLotInformation.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel.ExpanderAssayLotInformation)

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  expander.Collapse()
  expander = scrollViewer.ExpanderCalibrationInformation
  expander.Expand()
  Regions.Mod_metadata_ExpanderCalibrationInformation.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel.ExpanderCalibrationInformation)
  
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  expander.Collapse()
  expander = scrollViewer.ExpanderBatchInformation
  expander.Expand()
  #Regions.Mod_metadata_ExpanderBatchInformation.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel.ExpanderBatchInformation)
  #scrollViewer.VScroll.Pos = 0
  
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  expander.Collapse()
  Regions.Mod_metadata_ExpanderSystemFileInformation.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel.ExpanderSystemFileInformation)
