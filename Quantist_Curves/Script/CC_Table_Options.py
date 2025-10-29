import Load_CSV_File 
import Quantist_Removing_Files
#import pyperclip

def SingleAnalyte_Table_operations():
  quantist = Aliases.Quantist
  main = Aliases.Quantist.MainWindowView.MainView
  treeView = Aliases.Quantist.MainWindowView.RunTreeView

  flag = False
  if (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files(flag)
        
  if not (treeView.HasItems): 
    quantist = Aliases.Quantist
    quantist.MainWindowView.LoadButton.ClickButton()
    
    sampleFoder = ProjectSuite.Variables.SampleDataFolder
    file = ProjectSuite.Variables.sample_csv_pm8800
    quantist.dlgOpen.OpenFile(sampleFoder + file, "Supported Files (*csv;*.quantist)")
        
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)    

  border = Aliases.Quantist.MainWindowView.MainView
  border.GridSplitter2.Drag(709, 1, -3, -386)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    
  groupBox = border.CurvePanel.GroupboxTableOptions
  Aliases.Quantist.MainWindowView.RunTreeView.Click()
  groupBox.ButtonExpandAll.ClickButton()
  Regions.PM8800_SingleAnalyte_TableOption_RowExpand.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData)

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  border.CurveData.GridData.Drag(1224, 142, 12, 421)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  
  Regions.PM8800_SingleAnalyte_TableOption_RowExpand_bottom.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData)
  groupBox.ButtonCollapseAll.ClickButton()
  Regions.PM8800_SingleAnalyte_TableOption_RowCollapse.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData)
    
def Row_Operations_Expand_All():
  Log.Message("Refer to SingleAnalyte_Table_operations test case")  
  pass  

def Row_Operations_Collapse_All():
  Log.Message("Refer to SingleAnalyte_Table_operations test case")
  pass

  
def Copy_Rows_To_Clipboard_Agg():
  quantist = Aliases.Quantist
  main = Aliases.Quantist.MainWindowView.MainView
  treeView = Aliases.Quantist.MainWindowView.RunTreeView
      
  flag = True
  if (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files(flag)
        
  if not (treeView.HasItems): 
    quantist = Aliases.Quantist
    quantist.MainWindowView.LoadButton.ClickButton()
    
    sampleFoder = ProjectSuite.Variables.SampleDataFolder
    file = ProjectSuite.Variables.sample_csv_pm8800
    quantist.dlgOpen.OpenFile(sampleFoder + file, "Supported Files (*csv;*.quantist)")

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)    
  tblOption = Aliases.Quantist.MainWindowView.MainView.CurvePanel.GroupboxTableOptions
  tblOption.ButtonAggregates.ClickButton()

  TestedApps.notepad.Run(1, True)
  notepad = Aliases.notepad
  wndNotepad = notepad.wndNotepad

  edit = wndNotepad.Edit
  edit.Keys("^v")

  wndNotepad.MainMenu.Click("File|Save As...")
  dlgSaveAs = notepad.dlgSaveAs
  dlgSaveAs.DUIViewWndClassName.Explorer_Pane.FloatNotifySink.ComboBox.SetText("PM8800-Agg.txt")
  dlgSaveAs.btnSave.ClickButton()

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  if (notepad.dlgConfirmSaveAs.Confirm_Save_As.CtrlNotifySink.btnYes.Exists):
     notepad.dlgConfirmSaveAs.Confirm_Save_As.CtrlNotifySink.btnYes.ClickButton()
  
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)   
  Files.PM8800_Aggregates.Check("C:\\Quantist\\SQA-Quantist\\Test_Data\\Output\\PM8800-Agg.txt")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
  wndNotepad.Close()   

        
def Copy_Rows_To_Clipboard_Replicates():
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)    

  tblOption = Aliases.Quantist.MainWindowView.MainView.CurvePanel.GroupboxTableOptions
  tblOption.ButtonReplicates.ClickButton()

  TestedApps.notepad.Run(1, True)
  notepad = Aliases.notepad
  wndNotepad = notepad.wndNotepad
  
  edit = wndNotepad.Edit
  edit.Keys("^v")
  
  wndNotepad.MainMenu.Click("File|Save As...")  
  dlgSaveAs = notepad.dlgSaveAs
  dlgSaveAs.DUIViewWndClassName.Explorer_Pane.FloatNotifySink.ComboBox.SetText("PM8800-Rep.txt")
  dlgSaveAs.btnSave.ClickButton()
  
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  if (notepad.dlgConfirmSaveAs.Confirm_Save_As.CtrlNotifySink.btnYes.Exists):
     notepad.dlgConfirmSaveAs.Confirm_Save_As.CtrlNotifySink.btnYes.ClickButton()
    
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)     
  Files.PM8800_Replicates.Check("C:\\Quantist\\SQA-Quantist\\Test_Data\\Output\\PM8800-Rep.txt")
  wndNotepad.Close() 
  

def Reset_Included_Standards():

  main = Aliases.Quantist.MainWindowView.MainView
  curvePanel = main.CurvePanel
  treeView = Aliases.Quantist.MainWindowView.RunTreeView #List of files
  analyte = curvePanel.AnalyteBox

  flag = True
  if (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files(flag)
    
  if not (treeView.HasItems): 
    quantist = Aliases.Quantist
    quantist.MainWindowView.LoadButton.ClickButton()
    
    sampleFoder = ProjectSuite.Variables.SampleDataFolder
    file = ProjectSuite.Variables.sample_csv_unknown_control
    quantist.dlgOpen.OpenFile(sampleFoder + file, "Supported Files (*csv;*.quantist)")
  
  hwndSource = Aliases.Quantist.MainWindowView
  border = hwndSource.MainView
  treeListControl = border.CurveData
  treeListControl.InplaceBaseEdit26.Click()
  treeListControl.InplaceBaseEdit27.Click()
  treeListControl.InplaceBaseEdit28.Click()
  treeListControl.InplaceBaseEdit29.Click()
  scrollViewer = border.CurvePanel
  scrollViewer.CheckboxShowUnknowns.ClickButton(cbChecked)
  scrollViewer.CheckboxShowControls.ClickButton(cbChecked)
  hwndSource.RunTreeView.Click() #Clear highlighted
  
  Regions.BAFF_Standard1_4_Not_Included.Check(Aliases.Quantist.MainWindowView.MainView.CurveChart)
  Regions.BAFF_Standard1_4_GrdiData_Not_Included.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData)
  groupBox = scrollViewer.GroupboxTableOptions
  groupBox.ButtonStandards.ClickButton()
  Regions.BAFF_Standards_All_Included.Check(Aliases.Quantist.MainWindowView.MainView.CurveChart)
  treeListControl.InplaceBaseEdit30.Click()
  treeListControl.InplaceBaseEdit12.Click()
  Regions.BAFF_Control1_2_Plot_Not_Included.Check(Aliases.Quantist.MainWindowView.MainView.CurveChart)

  hwndSource.RunTreeView.Click() #Clear highlighted
  Regions.BAFF_Control1_2_GridData_Not_Included.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData)
  button = groupBox.ButtonUnksCtrls
  button.ClickButton()
  
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Regions.BAFF_Control1_2_Plot_All_Included.Check(Aliases.Quantist.MainWindowView.MainView.CurveChart)
  Regions.BAFF_Control1_2_GridData_All_Included.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData)
  treeListView = treeListControl.GridData
  treeListView.InplaceBaseEdit9.Click()
  treeListControl.InplaceBaseEdit11.Click()
  treeListView.InplaceBaseEdit10.Click()
  Regions.BAFF_Unknown1_3_Plot_Not_Included.Check(Aliases.Quantist.MainWindowView.MainView.CurveChart)
  Regions.BAFF_Unknown1_3_GridData_Not_Included.Check(Aliases.Quantist.MainWindowView.MainView.CurveData.GridData)
  button.ClickButton()
  Regions.BAFF_Unknown1_3_Plot_All_Included.Check(Aliases.Quantist.MainWindowView.MainView.CurveChart)

def Reset_Included_Unknowns_Ctrls():
  Log.Message("Refer to Reset_Included_Standards test case")
  pass

#def Export_Clipboard_Content_to_TextFile(Files)
#  
#  # Get clipboard content
#  clipboard_content = pyperclip.paste()
#
#  # Define the output file path
#  output_file = "clipboard_output.txt"
#
#  # Write to the file
#  with open(output_file, "w", encoding="utf-8") as file:
#      file.write(clipboard_content)
#
#  print(f"Clipboard content saved to {output_file}")


