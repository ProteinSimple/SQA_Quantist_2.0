import Load_CSV_File 
import Quantist_Removing_Files

def CC_Remove_Outliers_Current():
  treeView = Aliases.Quantist.MainWindowView.RunTreeView
  Xbutton = treeView.TreeViewItem.Button

  flag = True  
  if (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files(flag)

  if (not treeView.HasItems):
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.SampleDataFolder, "TestData.csv")

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  #Regions.TestData_B7_H1_80_120_GridData.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData)
  Regions.TestData_B7_H1_5PL_1Y2_80_120_CurvePlot.Check(Aliases.Quantist.MainWindowView.MainView.Pane, False, False, 21869, 17)
  Regions.TestData_B7_H1_5PL_1Y2_80_120_GridData.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData)

  # Verify that Standard 7 is out of range because of the Conc CV > 20%
  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.MainView.CurveData.InplaceBaseEdit25, "DisplayText", cmpEqual, "22.57")
    
  # DataPoints - Clicked on current Curve Remove Outliers Recovery Range 90-110%
  configCurve = Aliases.Quantist.MainWindowView.MainView.CurvePanel
  configCurve.RecoverRangeBox.ClickItem("From90To110")
  configCurve.Btn_ForCurrentCurveOnly.ClickButton()
  
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)    
  # Verify that Standard 7 is not included (unchecked)
  Regions.TestData_B7_H1_5PL_1Y2_90_110_CurvePlot_No_Std7.Check(Aliases.Quantist.MainWindowView.MainView.Pane)
  Regions.TestData_B7_H1_5PL_1Y2_90_110_GridData_No_Std7.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData)  
  # Regions.TestData_B7_H1_90_110_RemoveOutliers_GridData.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData)
    
  # Reset Include Standard button should bring back DataPoints as before Remove Outliers
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  configCurve.RecoverRangeBox.ClickItem("From80To120")
  configCurve.GroupboxTableOptions.ButtonStandards.ClickButton()
        
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Regions.TestData_B7_H1_5PL_1Y2_80_120_GridData.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData)
  Regions.TestData_B7_H1_5PL_1Y2_80_120_CurvePlot.Check(Aliases.Quantist.MainWindowView.MainView.Pane)  
    
def CC_Remove_Outliers_All():

  treeView = Aliases.Quantist.MainWindowView.RunTreeView
  Xbutton = treeView.TreeViewItem.Button
  
  flag = True
  if (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files(flag)
  
  if (not treeView.HasItems):
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.SampleDataFolder, "PM8800.csv")
        
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)

  main = Aliases.Quantist.MainWindowView.MainView
  configCurve = main.CurvePanel
  treeview = Aliases.Quantist.MainWindowView.RunTreeView #List of files
  ma_listControl = Aliases.Quantist.MainWindowView.MainView.CurveData #Multi Analytes List
  
  configCurve.CurveFitBox.ClickItem("FivePL")
  configCurve.CurveWeightingBox.ClickItem("OneOverYSquared")
  configCurve.RecoverRangeBox.ClickItem("From90To110")
  configCurve.Btn_CopyToAll_RecoveryRange.ClickButton()  

  # Verify  B7_H1 Curve Plot and Grid data before applying Remove Outliers for All
  Regions.PM8800_B7_H1_5PL_1Y2_90_110_GridData.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData)
  Regions.PM8800_B7_H1_5PL_1Y2_90_110_CurvePlot.Check(Aliases.Quantist.MainWindowView.MainView.Pane)

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  analyte = configCurve.AnalyteBox
  analyte.ClickItem(2)   # Select EGF analyte, then
  # Verify EGF Curve Plot and Grid data before applying Remove Outliers for All  
  Regions.PM8800_EGF_5PL_1Y2_90_110_GridData.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData)
  Regions.PM8800_EGF_5PL_1Y2_90_110_CurvePlot.Check(Aliases.Quantist.MainWindowView.MainView.Pane)

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  analyte.ClickItem(11)   # Select GRO Alpha analyte, then    
  # Verify FGF basis Curve Data and Grid data before applying Remove Outliers for All                                                                                                                                                           
  Regions.PM8800_GRO_Alpha_5PL_1Y2_90_110_CurvePlot.Check(Aliases.Quantist.MainWindowView.MainView.Pane)
  Regions.PM8800_GRO_Alpha_5PL_1Y2_90_110_GridData.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData)  

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
  # Apply Remove Outliers for All analytes
  configCurve.Btn_ForAll_RemoveOutliers.ClickButton()

  Regions.PM8800_GRO_Alpha_5PL_1Y2_90_110_CurvePlot_RemoveOutliers.Check(Aliases.Quantist.MainWindowView.MainView.Pane)
  Regions.PM8800_GRO_Alpha_5PL_1Y2_90_110_GridData_RemoveOutliers.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData)

  aqUtils.Delay(ProjectSuite.Variables.Long_Delay)
  analyte.ClickItem(2)   # Select EGF analyte, then   
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
  # Verify EGF Curve Plot and Grid data after applying Remove Outliers for All
  
  #Check again for build 0.12.0.0
  #Regions.PM8800_EGF_5PL_1Y2_90_110_CurvePlot_RemoveOutliers.Check(Aliases.Quantist.MainWindowView.MainView.Pane)
  #Regions.PM8800_EGF_5PL_1Y2_90_110_GridData_RemoveOutliers.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData)

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)    
  analyte.ClickItem(0)  # Select B7_H1 analyte, then
  Regions.PM8800_B7_H1_5PL_1Y2_90_110_GridData.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData)
  Regions.PM8800_B7_H1_5PL_1Y2_90_110_CurvePlot.Check(Aliases.Quantist.MainWindowView.MainView.Pane, False, False, 21869, 17)
  # Verify B7_H1 Curve Data and Grid data after applying Remove Outliers for All

  # Switch to Multi Analytes View
  treeView.ClickItem("|[0]|[1]")

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)    
  #Expand Standard1 - Standard2
  ma_listControl.RowMarginControl2.Click()
  ma_listControl.RowMarginControl3.Click()
  ma_listControl.RowMarginControl4.Click()
  ma_listControl.RowMarginControl5.Click()
  ma_listControl.RowMarginControl6.Click()
  ma_listControl.RowMarginControl7.Click()
  ma_listControl.RowMarginControl8.Click()
  
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)      
  main.MA_Replicates.ClickButton()
  
  TestedApps.notepad.Run(1, True)
  notepad = Aliases.notepad
  wndNotepad = notepad.wndNotepad
  wndNotepad.Edit.Keys("^v")
  wndNotepad.MainMenu.Click("File|Save As...")
  dlgSaveAs = notepad.dlgSaveAs
  dlgSaveAs.DUIViewWndClassName.Explorer_Pane.FloatNotifySink.ComboBox.SetText("RemoveOutliers_All_Replicates.txt")
  dlgSaveAs.btnSave.ClickButton()
  Aliases.notepad.dlgConfirmSaveAs.Confirm_Save_As.CtrlNotifySink.btnYes.ClickButton()
  Files.RemoveOutliers_All_Replicates.Check("C:\\Quantist\\SQA-Quantist\\Test_Data\\Output\\RemoveOutliers_All_Replicates.txt")
  wndNotepad.Close()
  main.MA_Standards.ClickButton()
  treeView.ClickItem("|[0]|[0]")
   

def Test1():
  Files.RemoveOutliers_All_Replicates_txt1.Check("C:\\Quantist\\SQA-Quantist\\Test_Data\\Output\\RemoveOutliers_All_Replicates.txt")
