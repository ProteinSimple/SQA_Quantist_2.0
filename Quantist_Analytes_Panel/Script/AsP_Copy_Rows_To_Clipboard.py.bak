import Load_CSV_File 
import Quantist_Removing_Files

def Analytes_Panel_Copy_Rows():
  
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
    
  quantist = Aliases.Quantist
  mainWindowView = Aliases.Quantist.HwndSource_MainWindowView.MainWindowView  

  treeView = Aliases.Quantist.MainWindowView.RunTreeView
  Xbutton = treeView.TreeViewItem.Button

  if (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files()
  
  if (not treeView.HasItems):
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.SampleDataFolder, "PM8800.csv")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)

  #Click on Analyte Panel View
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Aliases.Quantist.HwndSource_MainWindowView.MainWindowView.RunTreeView.ClickItem("|[0]|[3]")
      
  Aliases.Quantist.MainWindowView.MainView.Btn_Copy_All.ClickButton()
    
  NotePad_SaveToFile("AP_Copy_All.txt")
  Files.AP_Copy_All.Check(Project.Variables.OutputFolder + "AP_Copy_All.txt")
    
  #Click on Copy to Clipboard - Selected option
  SelectRows()
  
  Aliases.Quantist.MainWindowView.MainView.Btn_Copy_Selected.ClickButton() 
    
  NotePad_SaveToFile("AP_Copy_Selected")
  
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Files.AP_Copy_Selected.Check(Project.Variables.OutputFolder + "AP_Copy_Selected.txt")
    

def NotePad_SaveToFile(fileName):

    TestedApps.notepad.Run(1, True)
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    
    notepad = Aliases.notepad
    wndNotepad = notepad.wndNotepad
  
    richEditD2DPT = wndNotepad.NotepadTextBox.RichEditD2DPT
    richEditD2DPT.Keys("^v")

    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    richEditD2DPT.Keys("^s")
        
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)

    dlgSaveAs = notepad.dlgSaveAs
    dlgSaveAs.DUIViewWndClassName.Explorer_Pane.FloatNotifySink.ComboBox.SetText(Project.Variables.OutputFolder + fileName)

    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    dlgSaveAs.btnSave.ClickButton()
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
    notepad.dlgConfirmSaveAs.Confirm_Save_As.CtrlNotifySink.btnYes.ClickButton()

    notepad.Close()
  

def SelectRows():
  border = Aliases.Quantist.MainWindowView.MainView
  treeListView = border.CurveData.MA_dataGrid
  OCR.Recognize(treeListView.InplaceBaseEdit13).BlockByText("10").Click()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)

  OCR.Recognize(treeListView.InplaceBaseEdit14).BlockByText("57").Click(-1, -1, skShift)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  border.Btn_Copy_Selected.ClickButton()

  
def Analyte_Panel_Table_Options_Coordinators():
  mainWindowView = Aliases.Quantist.HwndSource_MainWindowView.MainWindowView
  mainWindowView.Click(1775, 87) #Down button coordinate
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  mainWindowView.Click(1825, 87) #Up button coordinate
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  mainWindowView.Click(1825, 117) #Selected button coordinate
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  mainWindowView.Click(1775, 147) #Reset button coordinate
    
def test2():
  NotePad_SaveToFile("Test")
