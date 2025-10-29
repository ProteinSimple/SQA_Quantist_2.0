import Load_CSV_File 
import Quantist_Removing_Files

def MA_Remove_Outliers():
  
  q = Sys.WaitProcess("Quantist", 2000)
  if q.Exists:
    q.Terminate()

  try:
    TestedApps.Quantist.Run(1, True)
  
  except ValueError as Error:
    Log.Warning("Can not Launch Quantist {Error}")
        
  except OSError as err:
    print("OS error: {0}".format(err))
    
  except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise

    
  mainWindowView = Aliases.Quantist.MainWindowView  
  treeView = Aliases.Quantist.MainWindowView.RunTreeView
  Xbutton = treeView.TreeViewItem.Button
  
  if (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files()
  
  if (not treeView.HasItems):
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.SampleDataFolder, "PM8800.csv")

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)

  # Select Recovery Range: 90-110%
  # Click on Remove Outliers first time (Only B1 %Recovery Range=123.12 is out of range, B1 Conc=57459.38 > ULOQ=15556.67) at this point
  configCurve = Aliases.Quantist.MainWindowView.MainView.CurvePanel.ConfigureCurve
  configCurve.RecoverRangeBox.ClickItem("From90To110")
  configCurve.Btn_ForCurrent_RemoveOutliers.ClickButton()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)

  # After recalculating, B2 is now: Conc: 54904.40, %Recovery Range=117.64 > ULOQ) 
  # Click on Remove Outliers second time (note: Standard1 B2 is still out of range at this point)
  configCurve.Btn_ForCurrent_RemoveOutliers.ClickButton()
  #Aliases.Quantist.MainWindowView.ButtonForCurrentCurveOnly.ClickButton()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    
  # Both B1 and B2 are now NOT included in the calculation.
  # Switch to Multi-Analyte
  # Confirm that both B1 and B2 should not be included.
  mainWindowView.RunTreeView.ClickItem("|[0]|[1]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  

  #Expand Standard1 to Standard7 rows for verification. 
  #Standard1 should be excluded. 
  rows = Aliases.Quantist.MainWindowView.MainView.CurveData
  rows.RowMarginControl2.Click()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  rows.RowMarginControl3.Click()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  rows.RowMarginControl4.Click() #(9, 9)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  rows.RowMarginControl5.Click()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  rows.RowMarginControl6.Click()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  rows.RowMarginControl7.Click()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  rows.RowMarginControl8.Click()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
  Regions.Border.Check(Aliases.Quantist.MainWindowView.MainView, False, False, 103373, 17)

  # Copy Replicates data to notepad for verification
  Aliases.Quantist.MainWindowView.MainView.MA_Replicates.ClickButton()
  aqUtils.Delay(ProjectSuite.Variables.Long_Delay)
  
  TestedApps.notepad.Run(1, True)
  notepad = Aliases.notepad
  wndNotepad = notepad.wndNotepad
  wndNotepad.Edit.Keys("^v")
  wndNotepad.MainMenu.Click("File|Save As...")
  dlgSaveAs = notepad.dlgSaveAs
  comboBox = dlgSaveAs.DUIViewWndClassName.Explorer_Pane.FloatNotifySink.ComboBox
  comboBox.SetText("MA_Conc_remove_outliers_Rep.txt")
  dlgSaveAs.btnSave.ClickButton()

  if (Aliases.notepad.dlgConfirmSaveAs.Confirm_Save_As.CtrlNotifySink.btnYes.Exists):
     Aliases.notepad.dlgConfirmSaveAs.Confirm_Save_As.CtrlNotifySink.btnYes.ClickButton()

  Files.Multi_Analytes_Conc_Remove_outliers_Rep.Check("C:\\Quantist\\SQA-Quantist\\Test_Data\\Output\\MA_Conc_remove_outliers_Rep.txt")
  notepad.Close()

def Coordinates():
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  resultsView = NameMapping.Sys.Quantist_Wpf.HwndSource_MainWindowView.MainWindowView.Grid.Grid.Grid.userControl_
  resultsView.Click(1450, 87) #Expand All
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  resultsView.Click(1520, 87) #Colapse All
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  resultsView.Click(1450, 115) #Aggregates 
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  resultsView.Click(1520, 115) #Replicates
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  resultsView.Click(1450, 145) #Standards
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  resultsView.Click(1520, 145) #Unks/Controls

def Terminate_Quantist():
  q = Sys.WaitProcess("Quantist", 2000)
  if q.Exists:
    q.Terminate()
