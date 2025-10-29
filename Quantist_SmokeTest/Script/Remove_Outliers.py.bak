import Load_CSV_File 
import Quantist_Removing_Files

def Remove_Outliers():
  quantist = Aliases.Quantist
  treeView = Aliases.Quantist.MainWindowView.RunTreeView
  
  flag=True
  while (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files(flag)
  
  if (not treeView.HasItems):
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.SampleDataFolder, "TestData.csv")

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  aqUtils.Delay(ProjectSuite.Variables.Long_Delay)
  Regions.TestData_main_before.Check(Aliases.Quantist.MainWindowView.MainViewRunCtr) #, False, False, ProjectSuite.Variables.PIXEL_TOLERANCE, ProjectSuite.Variables.COLOR_TOLERANCE)
    
  # DataPoints -"Current Curve Remove Outliers" for config at "Recovery Range 90-110%" 
  main = Aliases.Quantist.MainWindowView.MainViewRunCtr
  analyte = quantist.MainWindowView.MainView.CurvePanel.AnalyteBox
  curvePanel = Aliases.Quantist.MainWindowView.MainView.CurvePanel
    
  configCurve = Aliases.Quantist.MainWindowView.MainView.CurvePanel.ConfigureCurve
  tblOption = Aliases.Quantist.MainWindowView.MainView.CurvePanel.GroupboxTableOptions

  #Select Recovery Range 90-110%
  configCurve.RecoverRangeBox.ClickItem("From90To110")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)

  #Remove Outliers for current curve
  configCurve.ButtonForCurrentCurveOnly.ClickButton()

  #Verify that the outliers have been removed from calculation + curve plot
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Aliases.Quantist.MainWindowView.MainView.CurvePanel.LabelUnits.Click() #move mouse away from RemoveOutliers button so that highlight button can be turned off
  Regions.TestData_main_after_removeOutliers.Check(Aliases.Quantist.MainWindowView.MainViewRunCtr)

  #Reset Include Standards + config at "Recovery Range 80-120%" should bring back DataPoints as they were initially loaded  
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    
  if (tblOption.ButtonStandards.IsEnabled):
    tblOption.ButtonStandards.ClickButton()
    configCurve.RecoverRangeBox.ClickItem("From80To120")
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    Aliases.Quantist.MainWindowView.MainView.CurvePanel.LabelUnits.Click()
    #Regions.TestData_main_before.Check(Aliases.Quantist.MainWindowView.MainViewRunCtr)

  #Verify MIP_3alpha analyte before applying removing outliers 
  analyte.ClickItem(4)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Regions.CurveView_MIP_3alpha_before.Check(Aliases.Quantist.MainWindowView.MainViewRunCtr)

  #Verify MDC analyte
  analyte.ClickItem(5)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Regions.CurveView_MDC_before.Check(Aliases.Quantist.MainWindowView.MainViewRunCtr)

  #Verify MIP_1alpha analyte
  analyte.ClickItem(6)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
  Regions.CurveView_MIP_1alpha_before.Check(Aliases.Quantist.MainWindowView.MainViewRunCtr)

  #Apply Remove Outliers for ALL- Recovery Range of 80-120%
  curvePanel.ConfigureCurve.ButtonForAll.ClickButton()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)

  #Verify MIP_3alpha analyte after applying removing outliers
  analyte.ClickItem(4)
  aqUtils.Delay(ProjectSuite.Variables.Long_Delay)
  Regions.CurveView_MIP_3alpha_after.Check(Aliases.Quantist.MainWindowView.MainViewRunCtr)
  
  #Verify MDC analyte after applying removing outliers
  analyte.ClickItem(5)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Regions.CurveView_MDC_after.Check(Aliases.Quantist.MainWindowView.MainViewRunCtr)
  
  #Verify MIP_1alpha analyte after applying removing outliers
  analyte.ClickItem(6)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
  Regions.CurveView_MIP_1alpha_after.Check(Aliases.Quantist.MainWindowView.MainViewRunCtr)

  #Reset Included Standards
  #curvePanel.GroupboxTableOptions.ButtonStandards.ClickButton()
      
      
def table_Options():
  tblOption = Aliases.Quantist.MainWindowView.MainView.ScrollViewer.GroupboxTableOptions
  tblOption.ButtonStandards.ClickButton()
  tblOption.ButtonUnksCtrls.ClickButton()
  tblOption.ButtonAggregates.ClickButton()
  tblOption.ButtonReplicates.ClickButton()
  tblOption.ButtonExpandAll.ClickButton()
  tblOption.ButtonCollapseAll.ClickButton()

