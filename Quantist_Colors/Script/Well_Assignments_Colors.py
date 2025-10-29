import Load_CSV_File 
import Quantist_Removing_Files

def WA_Colors_Shapes():
  mainWindowView = Aliases.Quantist.MainWindowView  
  treeView = Aliases.Quantist.MainWindowView.RunTreeView
  Xbutton = treeView.TreeViewItem.Button
  
  flag = True
  if (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files(flag)
  
  if (not treeView.HasItems):
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.SampleDataFolder, ProjectSuite.Variables.sample_csv_pm8800)

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  

  hwndSource = Aliases.Quantist.MainWindowView
  hwndSource.RunTreeView.ClickItem("|[0]|[2]")
  border = hwndSource.MainView
  slider = border.ZoomSlider
  slider.wPosition = 0.84999999999999998
  plate96WellView = border.ItemsControl.Plate96WellView
  plate96WellView.Drag(645, 17, 46, 109)
  textBox = border.TextboxReplicateCount
  textBox.Click(32, 13)
  textBox.SetText("1")
  border.ButtonControl.ClickButton()
  listView = plate96WellView.wellplate

  listView.ListViewItem.Drag(579, 3, 48, 109)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  border.ButtonBlank.ClickButton()
  
  listView.ListViewItem2.Drag(585, 54, 98, 111)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  border.ButtonUnknown.ClickButton()
  
  plate96WellView.Drag(590, 246, 93, 110)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
  
  border.ButtonStandard.ClickButton()
  Regions.WA_Colors_Shapes_PlatesView_1.Check(Aliases.Quantist.MainWindowView.MainView.PlatesViewScrollViewer)
  #Regions.WA_Colors_Buttons.Check(Aliases.Quantist.MainWindowView.MainView.Border)
  Aliases.Quantist.MainWindowView.RunTreeView.Click(189, 351)
  Regions.WA_Colors_Buttons.Check(Aliases.Quantist.MainWindowView.MainView.Border)
  
#  slider.wPosition = 3
#  scrollViewer = border.PlatesViewScrollViewer
#  scrollViewer.VScroll.Pos = 0
#  scrollViewer.HScroll.Pos = 0
#  Regions.WA_Blank_Color_Shape.Check(Regions.CreateRegionInfo(Aliases.Quantist.MainWindowView.MainView.PlatesViewScrollViewer.ItemsControl.Grid, 23, 68, 420, 206, False))
#  Regions.WA_Standard_Color_Shape.Check(Regions.CreateRegionInfo(Aliases.Quantist.MainWindowView.MainView.PlatesViewScrollViewer.ItemsControl.Grid.wellplate, 5, 191, 410, 198, False))
#  Regions.WA_Unknown_Color_Shape.Check(Regions.CreateRegionInfo(Aliases.Quantist.MainWindowView.MainView.PlatesViewScrollViewer.ItemsControl.Grid.wellplate, 425, 8, 188, 380, False))
#
#  scrollViewer.HScroll.Pos = 1795.0833333333333
#  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
#    
#  Regions.WA_Blank_Color_Shape_2.Check(Regions.CreateRegionInfo(Aliases.Quantist.MainWindowView.MainView.PlatesViewScrollViewer.ItemsControl.Grid.wellplate, 2041, 4, 181, 382, False))
#  Regions.WA_Control_Color_Shape.Check(Regions.CreateRegionInfo(Aliases.Quantist.MainWindowView.MainView.PlatesViewScrollViewer.ItemsControl.Grid.wellplate, 2240, 7, 178, 377, False))
#  Regions.WA_Standard_Color_Shape_2.Check(Regions.CreateRegionInfo(NameMapping.Sys.Quantist.HwndSource_MainWindowView.MainWindowView.Grid.Grid.Grid.Border.Grid2.Grid.Grid.PlatesViewScrollViewer.ItemsControl.Border, 2048, 472, 396, 194, False))

  main = Aliases.Quantist.MainWindowView.MainView
  button = border.Button
  button.ClickButton()
  slider = border.ZoomSlider
  slider.wPosition = 0.94999999999999996
  button.ClickButton()
  slider.wPosition = 1.05
  button.ClickButton()
  slider.wPosition = 1.1500000000000001
  button.ClickButton()
  slider.wPosition = 1.25
  button.ClickButton()
  main.PlatesViewScrollViewer.HScroll.Pos = 285.33333333333326
  Regions.Blank_update.Check(Regions.CreateRegionInfo(NameMapping.Sys.Quantist.HwndSource_MainWindowView.MainWindowView.Grid.Grid.Grid.Border.Grid2.Grid.Grid.PlatesViewScrollViewer.ItemsControl.Border, 853, 29, 80, 164, False))
  Regions.Control_update.Check(Regions.CreateRegionInfo(NameMapping.Sys.Quantist.HwndSource_MainWindowView.MainWindowView.Grid.Grid.Grid.Border.Grid2.Grid.Grid.PlatesViewScrollViewer.ItemsControl.Border, 933, 28, 84, 165, False))
  Regions.Unknown_update.Check(Regions.CreateRegionInfo(Aliases.Quantist.MainWindowView.MainView.ItemsControl.Plate96WellView.wellplate, 849, 164, 160, 163, False))
  Regions.Standard_update.Check(Regions.CreateRegionInfo(NameMapping.Sys.Quantist.HwndSource_MainWindowView.MainWindowView.Grid.Grid.Grid.Border.Grid2.Grid.Grid.PlatesViewScrollViewer.ItemsControl.Border, 857, 362, 164, 166, False))

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Aliases.Quantist.MainWindowView.MainView.PlatesViewScrollViewer.HScroll.Pos = 0
  Regions.Blank_org.Check(Regions.CreateRegionInfo(NameMapping.Sys.Quantist.HwndSource_MainWindowView.MainWindowView.Grid.Grid.Grid.Border.Grid2.Grid.Grid.PlatesViewScrollViewer.ItemsControl.Border, 13, 32, 168, 84, False))
  Regions.Standard_org.Check(Regions.CreateRegionInfo(Aliases.Quantist.MainWindowView.MainView.ItemsControl.Plate96WellView.wellplate, 5, 80, 169, 580, False))
  Regions.Unknown_org.Check(Regions.CreateRegionInfo(NameMapping.Sys.Quantist.HwndSource_MainWindowView.MainWindowView.Grid.Grid.Grid.Border.Grid2.Grid.Grid.PlatesViewScrollViewer.ItemsControl.Border, 186, 22, 330, 671, False))
