def Curve_View():
  pass

def Curve_View_BK():
  
  #try to reuse Load_CSV_Files from CSV_Files project
  quantist = Aliases.Quantist
  mainWindowView = quantist.MainWindowView
  gridSplitter = mainWindowView.GridSplitter
  mainWindowView.Button.ClickButton()
  quantist.dlgOpen.OpenFile(ProjectSuite.Variables.SampleDataFolder + ProjectSuite.Variables.sample_csv_pm8800)
  aqUtils.Delay(ProjectSuite.Variables.Long_Delay)
  ##
  Regions.PM8800_Tree.Check(Aliases.Quantist.MainWindowView.RunTreeView.TreeViewItem)
  Regions.PM8800_Chart.Check(Aliases.Quantist.MainWindowView.MainView.zchart)
  Regions.PM8800_Options.Check(Regions.CreateRegionInfo(Aliases.Quantist.MainWindowView.MainView, 1257, 5, 324, 873, False))
  #Regions.PM8800_GridCurveData.Check(Regions.CreateRegionInfo(Aliases.Quantist.MainWindowView.MainView.Grid, 2, 686, 1219, 276, False))
  Regions.PM8800_main.Check(Aliases.Quantist.MainWindowView.MainView)    


def Test1():
  Regions.PM8800_main.Check(Aliases.Quantist.MainWindowView.MainView)
