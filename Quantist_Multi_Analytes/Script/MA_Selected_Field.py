def MA_Selected_Field():

  quantist = Aliases.Quantist
  mainView = quantist.MainWindowView.MainView
  #quantist.MainWindowView.MainView.MA_Panel.SelectedField

  mainView.MA_Panel.SelectedField.ClickItem("Mfi")
  flag  = "Mfi"
  fnAgg = "MA_MFI_Agg.txt"
  fnRep = "MA_MFI_Rep.txt"
  pathA = "C:\\Quantist\\SQA-Quantist\\Test_Data\\Output\\MA_MFI_Agg.txt"
  pathR = "C:\\Quantist\\SQA-Quantist\\Test_Data\\Output\\MA_MFI_Rep.txt"
  MA_Selected_Field_Verify(pathA, pathR, fnAgg, fnRep, flag)

  mainView.MA_Panel.SelectedField.ClickItem("MfiCvPercent")
  flag  = "MfiCvPercent"
  fnAgg = "MA_MfiCvPercent_Agg.txt"
  fnRep = "MA_MfiCvPercent_Rep.txt"
  pathA = "C:\\Quantist\\SQA-Quantist\\Test_Data\\Output\\MA_MfiCvPercent_Agg.txt"
  pathR = "C:\\Quantist\\SQA-Quantist\\Test_Data\\Output\\MA_MfiCvPercent_Rep.txt"
  MA_Selected_Field_Verify(pathA, pathR, fnAgg, fnRep, flag)

  mainView.MA_Panel.SelectedField.ClickItem("NetMfi")  
  flag  = "NetMfi"
  fnAgg = "MA_NetMfi_Agg.txt"
  fnRep = "MA_NetMfi_Rep.txt"
  pathA = "C:\\Quantist\\SQA-Quantist\\Test_Data\\Output\\MA_NetMfi_Agg.txt"
  pathR = "C:\\Quantist\\SQA-Quantist\\Test_Data\\Output\\MA_NetMfi_Rep.txt"
  MA_Selected_Field_Verify(pathA, pathR, fnAgg, fnRep, flag)

  mainView.MA_Panel.SelectedField.ClickItem("Concentration")    
  flag = "Concentration"
  fnAgg = "MA_Concentration_Agg.txt"
  fnRep = "MA_Concentration_Rep.txt"
  pathA = "C:\\Quantist\\SQA-Quantist\\Test_Data\\Output\\MA_Concentration_Agg.txt"
  pathR = "C:\\Quantist\\SQA-Quantist\\Test_Data\\Output\\MA_Concentration_Rep.txt"
  MA_Selected_Field_Verify(pathA, pathR, fnAgg, fnRep, flag)

  mainView.MA_Panel.SelectedField.ClickItem("ConcentrationStatus")      
  #field = "ConcentrationStatus"
  flag  = "ConcStatus"
  fnAgg = "MA_ConcStatus_Agg.txt"
  fnRep = "MA_ConcStatus_Rep.txt"
  pathA = "C:\\Quantist\\SQA-Quantist\\Test_Data\\Output\\MA_ConcStatus_Agg.txt"
  pathR = "C:\\Quantist\\SQA-Quantist\\Test_Data\\Output\\MA_ConcStatus_Rep.txt"
  MA_Selected_Field_Verify(pathA, pathR, fnAgg, fnRep, flag)

  mainView.MA_Panel.SelectedField.ClickItem("ConcentrationCvPercent")        
  #field = "ConcentrationCvPercent"
  flag  = "ConcCVPct"
  fnAgg = "MA_ConcCVPct_Agg.txt"
  fnRep = "MA_ConcCVPct_Rep.txt"
  pathA = "C:\\Quantist\\SQA-Quantist\\Test_Data\\Output\\MA_ConcCVPct_Agg.txt"
  pathR = "C:\\Quantist\\SQA-Quantist\\Test_Data\\Output\\MA_ConcCVPct_Rep.txt"
  MA_Selected_Field_Verify(pathA, pathR, fnAgg, fnRep, flag)

  mainView.MA_Panel.SelectedField.ClickItem("ExpectedConcentration")        
  #field = "ExpectedConcentration"
  flag  = "ExpConc"
  fnAgg = "MA_ExpectedConc_Agg.txt"
  fnRep = "MA_ExpectedConc_Rep.txt"
  pathA = "C:\\Quantist\\SQA-Quantist\\Test_Data\\Output\\MA_ExpectedConc_Agg.txt"
  pathR = "C:\\Quantist\\SQA-Quantist\\Test_Data\\Output\\MA_ExpectedConc_Rep.txt"
  MA_Selected_Field_Verify(pathA, pathR, fnAgg, fnRep, flag)

  mainView.MA_Panel.SelectedField.ClickItem("RecoveryPercent")            
  #field = "RecoveryPercent"
  flag  = "RecoveryPct"
  fnAgg = "MA_ExpectedConc_Agg.txt"
  fnRep = "MA_ExpectedConc_Rep.txt"
  pathA = "C:\\Quantist\\SQA-Quantist\\Test_Data\\Output\\MA_RecoveryPct_Agg.txt"
  pathR = "C:\\Quantist\\SQA-Quantist\\Test_Data\\Output\\MA_RecoveryPct_Rep.txt"
  MA_Selected_Field_Verify(pathA, pathR, fnAgg, fnRep, flag)

  mainView.MA_Panel.SelectedField.ClickItem("DilutionFactor")              
  flag = "DilutionFactor"
  fnAgg = "MA_DilutionFactor_Agg.txt"
  fnRep = "MA_DilutionFactor_Rep.txt"
  pathA = "C:\\Quantist\\SQA-Quantist\\Test_Data\\Output\\MA_DilutionFactor_Agg.txt"
  pathR = "C:\\Quantist\\SQA-Quantist\\Test_Data\\Output\\MA_DilutionFactor_Rep.txt"
  MA_Selected_Field_Verify(pathA, pathR, fnAgg, fnRep, flag)

  mainView.MA_Panel.SelectedField.ClickItem("BeadCount")                
  flag = "BeadCount"
  fnAgg = "MA_BeadCount_Agg.txt"
  fnRep = "MA_BeadCount_Rep.txt"
  pathA = "C:\\Quantist\\SQA-Quantist\\Test_Data\\Output\\MA_BeadCount_Agg.txt"
  pathR = "C:\\Quantist\\SQA-Quantist\\Test_Data\\Output\\MA_BeadCount_Rep.txt"
  MA_Selected_Field_Verify(pathA, pathR, fnAgg, fnRep, flag)  


def MA_Selected_Field_Verify(pathA, pathR, fnAgg, fnRep, flag):
  # Reset all Standards data
  MA_Option = Aliases.Quantist.MainWindowView.MainView
  MA_Option.MA_Standards.ClickButton()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)

  # Aggregates button click
  MA_Option.MA_Aggregates.Click()
  
  p = Sys.WaitProcess("Notepad", 2000)
  if p.Exists:
    p.Terminate()
  else:
    TestedApps.notepad.Run(1, True)
    notepad = Aliases.notepad
    wndNotepad = notepad.wndNotepad  
    edit = wndNotepad.Edit  
    edit.Keys("^v")
    wndNotepad.MainMenu.Click("File|Save As...")
    dlgSaveAs = notepad.dlgSaveAs  
    HWNDView = dlgSaveAs.DUIViewWndClassName.Explorer_Pane
    comboBox = HWNDView.FloatNotifySink.ComboBox
    comboBox.SetText(fnAgg)
    btnSave = dlgSaveAs.btnSave
    btnSave.ClickButton()
  
    #click on Yes to overwrite
    if (Aliases.notepad.dlgConfirmSaveAs.Confirm_Save_As.CtrlNotifySink.btnYes.Exists):
       Aliases.notepad.dlgConfirmSaveAs.Confirm_Save_As.CtrlNotifySink.btnYes.ClickButton()
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)

    # Verify export file
    if (flag == "Mfi"):
      Files.Multi_Analytes_MFI_Agg.Check(pathA)
    if (flag == "MfiCvPercent"):
      Files.Multi_Analytes_MfiCvPercent_Agg.Check(pathA)
    if (flag == "NetMfi"):
      Files.Multi_Analytes_NetMfi_Agg.Check(pathA) 
    if (flag == "Concentration"):
      Files.Multi_Analytes_Concentration_Agg.Check(pathA)
    if (flag == "ConcStatus"):
      Files.Multi_Analytes_ConcStatus_Agg.Check(pathA)
    if (flag == "ConcCVPct"):
      Files.Multi_Analytes_ConcCVPct_Agg.Check(pathA)    
    if (flag == "ExpConc"):
      Files.Multi_Analytes_ExpectedConc_Agg.Check(pathA)
    if (flag == "RecoveryPct"):
      Files.Multi_Analytes_RecoveryPct_Agg.Check(pathA)
    if (flag == "DilutionFactor"):
      Files.Multi_Analytes_DilutionFactor_Agg.Check(pathA)
    if (flag == "BeadCount"):
      Files.Multi_Analytes_BeadCount_Agg.Check(pathA)

    wndNotepad.Close()
  
  if (p.Exists):
    p.Terminate()
  else:
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
    # Replicates button click
    MA_Option.MA_Replicates.Click()

    TestedApps.notepad.Run(1, True)
    notepad = Aliases.notepad
    wndNotepad = notepad.wndNotepad
    edit = wndNotepad.Edit
    edit.Keys("^v")
    wndNotepad.MainMenu.Click("File|Save As...")
    dlgSaveAs = notepad.dlgSaveAs
    HWNDView = dlgSaveAs.DUIViewWndClassName.Explorer_Pane
    comboBox = HWNDView.FloatNotifySink.ComboBox
    comboBox.SetText(fnRep)
    btnSave = dlgSaveAs.btnSave
    btnSave.ClickButton()
  
	  #click on Yes to overwrite
    if (Aliases.notepad.dlgConfirmSaveAs.Confirm_Save_As.CtrlNotifySink.btnYes.Exists):
       Aliases.notepad.dlgConfirmSaveAs.Confirm_Save_As.CtrlNotifySink.btnYes.ClickButton()
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    
    if (flag == "Mfi"):
      Files.Multi_Analytes_MFI_Rep.Check(pathR)
    if (flag == "MfiCvPercent"):
      Files.Multi_Analytes_MfiCvPercent_Rep.Check(pathR)
    if (flag == "NetMfi"):
      Files.Multi_Analytes_NetMfi_Rep.Check(pathR)
    if (flag == "Concentration"):
      Files.Multi_Analytes_Concentration_Rep.Check(pathR)
    if (flag == "ConcStatus"):
      Files.Multi_Analytes_ConcStatus_Rep.Check(pathR)
    if (flag == "ConcCVPct"):
      Files.Multi_Analytes_ConcCVPct_Rep.Check(pathR)
    if (flag == "ExpConc"):
      Files.Multi_Analytes_ExpectedConc_Rep.Check(pathR)
    if (flag == "RecoveryPct"):
      Files.Multi_Analytes_RecoveryPct_Rep.Check(pathR)
    if (flag == "DilutionFactor"):
      Files.Multi_Analytes_DilutionFactor_Rep.Check(pathR)
    if (flag == "BeadCount"):
      Files.Multi_Analytes_BeadCount_Rep.Check(pathR)      

  wndNotepad.Close()
          
def Buttons_Clicks_Coordinates():
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
  
# Func starts from here:      
def MA_Fields_backup():
  resultsView = NameMapping.Sys.Quantist_Wpf.HwndSource_MainWindowView.MainWindowView.Grid.Grid.Grid.userControl_
  
  # Reset all Standards data
  resultsView.Click(1450, 145) #Reset Standards button click
  aqUtils.Delay(ProjectSuite.Variables.Long_Delay)
  
  resultsView.Click(1520, 115) #Replicates button click
  TestedApps.notepad.Run(1, True)
  notepad = Aliases.notepad
  wndNotepad = notepad.wndNotepad
  edit = wndNotepad.Edit
  edit.Keys("^v")
  wndNotepad.MainMenu.Click("File|Save As...")
  dlgSaveAs = notepad.dlgSaveAs
  HWNDView = dlgSaveAs.DUIViewWndClassName.Explorer_Pane
  comboBox = HWNDView.FloatNotifySink.ComboBox
  comboBox.SetText("Multi_Analytes_MFI_Rep.txt")
  btnSave = dlgSaveAs.btnSave
  btnSave.ClickButton()
  
  #click on Yes to overwrite
  Aliases.notepad.dlgConfirmSaveAs.Confirm_Save_As.CtrlNotifySink.btnYes.ClickButton()
    
  Files.Multi_Analytes_MFI_Rep.Check("C:\\Quantist\\SQA-Quantist\\Test_Data\\Output\\Multi_Analytes_MFI_Rep.txt")
  wndNotepad.Close()
  
  aqUtils.Delay(ProjectSuite.Variables.Long_Delay)
  resultsView.Click(1450, 115) #Aggregates button click
  TestedApps.notepad.Run(1, True)
  edit.Keys("^v")
  wndNotepad.MainMenu.Click("File|Save As...")
  comboBox.SetText("Multi_Analytes_MFI_Agg.txt")
  btnSave.ClickButton()
  
  #click on Yes to overwrite
  Aliases.notepad.dlgConfirmSaveAs.Confirm_Save_As.CtrlNotifySink.btnYes.ClickButton()
  #notepad.dlgConfirmSaveAs.Confirm_Save_As.CtrlNotifySink.btnYes.ClickButton()
  # Verify export file
  Files.Multi_Analytes_MFI_Agg.Check("C:\\Quantist\\SQA-Quantist\\Test_Data\\Output\\Multi_Analytes_MFI_Agg.txt")
  wndNotepad.Close()
  
def ComboBox_Items():
  SF = Aliases.Quantist.MainWindowView.MainView.SelectedField
  SF.ClickItem("Mfi")
  SF.ClickItem("MfiCvPercent")
  SF.ClickItem("NetMfi")
  SF.ClickItem("Concentration")
  SF.ClickItem("ConcentrationStatus")
  SF.ClickItem("ConcentrationCvPercent")
  SF.ClickItem("ExpectedConcentration")
  SF.ClickItem("RecoveryPercent")
  SF.ClickItem("DilutionFactor")
  SF.ClickItem("BeadCount")


