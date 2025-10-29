import Load_CSV_File 
import Quantist_Removing_Files

def Wells_Layout():

  main = Aliases.Quantist.MainWindowView  
  treeView = main.RunTreeView
  
  flag = False
  while (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files(flag)
  
  if (not treeView.HasItems):
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.WellAssignmentsFolder, "Approved.csv")
   
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)

  border = main.MainView
  scrollViewer = border.CurvePanel
  scrollViewer.CheckboxShowUnknowns.ClickButton(cbChecked)
  scrollViewer.CheckboxShowControls.ClickButton(cbChecked)
  Regions.BAFF_CurvePlot.Check(Aliases.Quantist.MainWindowView.MainView.Pane, False, False, 50008, 17)
  
  #Click on Well Assignments View
  main.RunTreeView.ClickItem("|[0]|[2]")
  aqUtils.Delay(ProjectSuite.Variables.Long_Delay)
  
  Regions.WA_buttons.Check(Aliases.Quantist.MainWindowView.MainView.Border)
  Regions.WA_Buttons_Bar.Check(Aliases.Quantist.MainWindowView.MainView.Border, False, False, 3016, 17)
  Regions.WA_PlatesView.Check(Aliases.Quantist.MainWindowView.MainView.PlatesViewScrollViewer, False, False, 46540, 17)
  Regions.WA_PlateAssignmentGroupsDataGrid.Check(Aliases.Quantist.MainWindowView.MainView.PlateAssignmentGroupsDataGrid, False, False, 12313, 17)
  Regions.WA_EditableDataGrid.Check(Aliases.Quantist.MainWindowView.MainView.EditableDataGrid, False, False, 37578, 17)
  
#  extendedDataGrid = border.EditableDataGrid2
#  extendedDataGrid.Drag(76, 940, 105, -32)
#  Regions.WA_EditableDataGrid2.Check(Aliases.Quantist.MainWindowView.MainView.EditableDataGrid)
#  extendedDataGrid.Drag(182, 945, 103, -27)
#  Regions.WA_EditableDataGrid3.Check(Aliases.Quantist.MainWindowView.MainView.EditableDataGrid)
#  extendedDataGrid.Drag(271, 943, 97, 11)
#  Regions.WA_EditableDataGrid4.Check(Aliases.Quantist.MainWindowView.MainView.EditableDataGrid)
#  extendedDataGrid.Drag(349, 945, 103, 1)
#  Regions.WA_EditableDataGrid5.Check(Aliases.Quantist.MainWindowView.MainView.EditableDataGrid)
#  extendedDataGrid.Drag(464, 950, 82, -2)
#  Regions.WA_EditableDataGrid6.Check(Aliases.Quantist.MainWindowView.MainView.EditableDataGrid)


  extendedDataGrid = Aliases.Quantist.MainWindowView.MainView.EditableDataGrid
  extendedDataGrid.Drag(70, 898, 104, 7)
  Regions.EditableDataGrid_n2.Check(Aliases.Quantist.MainWindowView.MainView.EditableDataGrid2)
  extendedDataGrid.Drag(170, 903, 103, -17)
  Regions.EditableDataGrid_n3.Check(Aliases.Quantist.MainWindowView.MainView.EditableDataGrid2)
  extendedDataGrid.Drag(296, 899, 99, -27)
  Regions.EditableDataGrid_n4.Check(Aliases.Quantist.MainWindowView.MainView.EditableDataGrid2)
  extendedDataGrid.Drag(370, 895, 104, -19)
  Regions.EditableDataGrid_n5.Check(Aliases.Quantist.MainWindowView.MainView.EditableDataGrid2)
  extendedDataGrid.Drag(475, 898, 111, 1)
  Regions.EditableDataGrid_n6.Check(Aliases.Quantist.MainWindowView.MainView.EditableDataGrid2)

def Test1():
  Regions.WA_buttons.Check(Aliases.Quantist.MainWindowView.MainView.Border)
