import Load_CSV_File 
import Quantist_Removing_Files

def Loading_Single_Analyte():
  main = Aliases.Quantist.MainWindowView
  treeView = main.RunTreeView
  
  #flag = True
  while (treeView.HasItems):
     treeView.TreeViewItem.DeleteButton.ClickButton()
     
  if (not treeView.HasItems):
    quantist = Aliases.Quantist
    quantist.MainWindowView.LoadButton.ClickButton()
    sampleFoder = ProjectSuite.Variables.SampleSingleAnalyteFolder
    file = ProjectSuite.Variables.sample_csv_single_analyte
    quantist.dlgOpen.OpenFile(sampleFoder + file, "Supported Files (*csv;*.quantist)")
   
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)

  #Select 5PL CurveFit from the dropdown list
  Aliases.Quantist.MainWindowView.MainView.CurvePanel.ConfigureCurve.CurveFitBox.ClickItem("FivePL")
    
  Regions.SingleAnalyte_CurvePlot.Check(Aliases.Quantist.MainWindowView.MainView.Pane)
  #Regions.SingleAnalyte_CurveData.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel)
  Regions.SingleAnalyte_DataGrid_top.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.ztreeListView1)
  Aliases.Quantist.MainWindowView.MainView.CurveData.ztreeListView1.Drag(1225, 48, 6, 201)
  Regions.SingleAnalyte_DataGrid_bottom.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.ztreeListView1)

  treeView.ClickItem("|[0]|[2]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  
  treeView.ClickItem("|[0]|[0]")
  Regions.SingleAnalyte_CurvePlot.Check(Aliases.Quantist.MainWindowView.MainView.Pane)  
  Regions.SingleAnalyte_CurveData.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel)
  #Regions.SingleAnalyte_DataGrid_top.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.ztreeListView1)
  Aliases.Quantist.MainWindowView.MainView.CurveData.ztreeListView1.Drag(1225, 48, 6, 201)  
  #Regions.SingleAnalyte_DataGrid_bottom.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.ztreeListView1)
 