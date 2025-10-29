
def Test1():
  quantist_Wpf = Aliases.Quantist_WPF
  mainWindowView = quantist_Wpf.HwndSource_MainWindowView.MainWindowView
  mainWindowView.Button.ClickButton()
  quantist_Wpf.dlgOpen.OpenFile("E:\\TestComplete\\Quantist\\SampleQuantistFiles\\01-10-18 MS B0 wk 28 repeat PM8800_20180110_133338.csv", "Consumable Files (*.csv;*.quantist)")
  treeView = mainWindowView.RunTreeView
  treeView.ExpandItem("|[0]")
  treeView.ClickItem("|[0]|[1]")
  Regions.MS_B0_Concentration_Curve.Check(Regions.CreateRegionInfo(Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView.Grid.zchart, 8, 5, 702, 473, False))
  mainWindowView.GridSplitter.Drag(146, 1, 26, -191)
  dataGrid = mainWindowView.zdataGrid1
  dataGrid.DatagridcolumnheaderRecovery.Drag(1, 12, 2, 8)
  dataGrid.DatagridcolumnheaderWell.Drag(1, 17, -55, 1)
  dataGrid.DatagridcolumnheaderExpConc.Drag(96, 12, 17, 0)
  Regions.MS_B0_Concentration_Data.Check(Regions.CreateRegionInfo(Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView.Border, 12, 292, 706, 325, False))
  OCR.Recognize(Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView.zdataGrid1.DatagridcolumnheaderSample).CheckText("*Sample*")
  OCR.Recognize(Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView.zdataGrid1.DatagridcolumnheaderWell).CheckText("*Well*")
  OCR.Recognize(Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView.zdataGrid1.DatagridcolumnheaderNetMfi).CheckText("*Net MFI*")
  OCR.Recognize(Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView.zdataGrid1.DatagridcolumnheaderNetMfiCv).CheckText("*Net MFI CV%*")
  OCR.Recognize(Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView.zdataGrid1.DatagridcolumnheaderBackfitConc).CheckText("*Backfit Conc*")
  OCR.Recognize(Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView.zdataGrid1.DatagridcolumnheaderExpConc).CheckText("*Exp Conc*")
  OCR.Recognize(Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView.zdataGrid1.DatagridcolumnheaderRecovery).CheckText("*% Recovery*")
  OCR.Recognize(Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView.zdataGrid1.DatagridcolumnheaderIncluded).CheckText("*Included*")
  Tables.Analyte.Check()
  aqObject.CheckProperty(Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView.Grid.ComboBox, "wItemCount", cmpEqual, 50)
  aqObject.CheckProperty(Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView.Grid.ComboBox, "wText", cmpEqual, "B7-H1")

def Curve_Analytes():
  quantist_Wpf = Aliases.Quantist_WPF
  mainWindowView = quantist_Wpf.HwndSource_MainWindowView.MainWindowView
  mainWindowView.Button.ClickButton()
  quantist_Wpf.dlgOpen.OpenFile(ProjectSuite.Variables.SampleDataFolder + "2 plates with 1 std.csv", "Consumable Files (*.csv;*.quantist)")
  treeView = mainWindowView.RunTreeView
  treeView.ExpandItem("|[0]")
  treeView.ClickItem("|[0]|[1]")
  #mainWindowView.GridSplitter.Drag(159, 1, 11, -185)
  #mainWindowView.zdataGrid1.DatagridcolumnheaderSample.Drag(170, 12, -72, -2)
  analyteBox = Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView.Grid.ComboBox
  #analyteBox = mainWindowView.Grid.ComboBox
  #aqObject.CheckProperty(grid.zchart, "Enabled", cmpEqual, True)
  #Tables.GM_CSF.Check()
  #Regions.zchart.Check(Regions.CreateRegionInfo(Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView.Grid.zchart, 12, 8, 694, 283, False))
  #comboBox = grid.ComboBox
  
  for i in range(13):
    analyteBox.ClickItem(i)
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    
  #Regions.IFNg.Check(Regions.CreateRegionInfo(Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView.Grid.zchart, 10, 6, 693, 284, False))
  #Regions.Border.Check(Regions.CreateRegionInfo(Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView.Border, 735, 465, 300, 128, False))
  #Regions.IL_10.Check(Regions.CreateRegionInfo(Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView.Grid.zchart, 13, 10, 694, 281, False))


