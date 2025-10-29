import Load_CSV_File 
import Quantist_Removing_Files

def Wells_Multi_Plates_Layout():
  main = Aliases.Quantist.MainWindowView  
  treeView = main.RunTreeView
  
  flag = False
  while (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files(flag)
  
  if (not treeView.HasItems):
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.WellAssignmentsFolder, "Two_plates_with_one_std_code.csv")
   
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)

  border = main.MainView
  border.CurvePanel.CheckboxShowUnknowns.ClickButton(cbChecked)
  Regions.WA_2Plates_CurvePlot.Check(Aliases.Quantist.MainWindowView.MainView.Pane, False, False, 50008, 17)

  treeView = main.RunTreeView
  treeView.ClickItem("|[0]|[2]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  border.ZoomSlider.wPosition = 0.94999999999999996
  Regions.WA_2_PlatesViewScrollViewer.Check(Aliases.Quantist.MainWindowView.MainView.PlatesViewScrollViewer, False, False, 46540, 17)
  Regions.WA_2_PlateAssignmentGroupsDataGrid.Check(Aliases.Quantist.MainWindowView.MainView.PlateAssignmentGroupsDataGrid, False, False, 12313, 17)
  Regions.WA_2_EditableDataGrid.Check(Aliases.Quantist.MainWindowView.MainView.EditableDataGrid, False, False, 37578, 17)

  extendedDataGrid = border.EditableDataGrid
  extendedDataGrid.Drag(76, 946, 224, 4)
  Regions.WA_2_EditableDataGrid2.Check(Aliases.Quantist.MainWindowView.MainView.EditableDataGrid, False, False, 37578, 17)
  extendedDataGrid.Drag(575, 157, 15, 599)
  Regions.WA_2_PlateAssignmentGroupsDataGrid2.Check(Aliases.Quantist.MainWindowView.MainView.PlateAssignmentGroupsDataGrid, False, False, 12313, 17)

  treeView.ClickItem("|[0]|[1]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Regions.MA_2Plates_Conc_GridData.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData, False, False, 79168, 17)

  ma_selectedField = border.MA_Panel.SelectedField
  ma_selectedField.ClickItem("NetMfi")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Regions.MA_2Plates_NetMFI_GridData.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData, False, False, 79168, 17)
  
  ma_selectedField.ClickItem("ExpectedConcentration")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Regions.MA_2Plates_ExpConc_GridData.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData, False, False, 79168, 17)
  
  ma_selectedField.ClickItem("BeadCount")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  #hwndSource.MainViewRunCtr.Click(1084, 33)
  Regions.MA_2Plates_BeadCount_GridData.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData, False, False, 79168, 17)
