import Load_CSV_File 
import Quantist_Removing_Files

def Analytes_Panel_Edit_Analyte_Names():
  
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
  quantist = Aliases.Quantist
  mainWindowView = Aliases.Quantist.HwndSource_MainWindowView.MainWindowView  
    
  md = Aliases.Quantist.MainWindowView.MainView.Btn_MoveDown
  mu = Aliases.Quantist.MainWindowView.MainView.Btn_MoveUp
  copy = Aliases.Quantist.MainWindowView.MainView.Btn_Selected_Copy
  
  treeView = Aliases.Quantist.MainWindowView.RunTreeView
  Xbutton = treeView.TreeViewItem.Button

  flag = False
  while (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files(flag)
  
  if (not treeView.HasItems):
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.SampleDataFolder, "PM8800.csv")
    aqUtils.Delay(ProjectSuite.Variables.Long_Delay)
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.SampleDataFolder, "PM8800-Mod.csv")
    aqUtils.Delay(ProjectSuite.Variables.Long_Delay)


  #Click on Analytes Panel View - PM8800-Mod  
  treeView.ClickItem("|[1]|[3]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
          
  #Select a range of analytes (7)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
  mainWindowView.Click(400, 100)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  mainWindowView.Click(400, 222, skShift)

  #Copy selected ClickButton()
  quantist.MainWindowView.MainView.Btn_Copy_Selected.ClickButton()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
    
  #Click on Analytes Panel View - PM8800
  treeView.ClickItem("|[0]|[3]")

  #Select a range of different number of analytes (6)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
  mainWindowView.Click(400, 100)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  mainWindowView.Click(400, 200, skShift)

  #Paste selected ClickButton()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Aliases.Quantist.MainWindowView.MainViewRunCtr.Click(1755, 192)
  #quantist.MainWindowView.MainView.Btn_Paste_Selected.ClickButton()
  
  #Confirm error dialog  
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
  quantist.dlg.btnOK.ClickButton()  

  #Select a range of correct number of analytes (7)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
  mainWindowView.Click(400, 100)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  mainWindowView.Click(400, 222, skShift)

  #Paste selected ClickButton()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Aliases.Quantist.MainWindowView.MainViewRunCtr.Click(1755, 192)

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
  Aliases.Quantist.MainWindowView.RunTreeView.Click(160, 413) #Clear the highlighted
  Regions.AP_copy_paste_selected.Check(Aliases.Quantist.MainWindowView.MainViewRunCtr) #, False, False, 141659, 17)

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)

  #Click on Well Assignments View - PM8800
  treeView.ClickItem("|[0]|[2]")

  extendedDataGrid = Aliases.Quantist.MainWindowView.MainView.WA_dataGrid2
  Regions.WA_data_grid_analytes_names_changed_1.Check(Aliases.Quantist.MainWindowView.MainView.WA_dataGrid2)

  extendedDataGrid.Drag(74, 899, 98, -28)
  Regions.WA_data_grid_analytes_names_changed_2.Check(Aliases.Quantist.MainWindowView.MainView.WA_dataGrid2)

  extendedDataGrid.Drag(170, 896, 101, -4)
  Regions.WA_data_grid_analytes_names_changed_3.Check(Aliases.Quantist.MainWindowView.MainView.WA_dataGrid2)

  extendedDataGrid.Drag(288, 891, 99, -3)
  Regions.WA_data_grid_analytes_names_changed_4.Check(Aliases.Quantist.MainWindowView.MainView.WA_dataGrid2)

  extendedDataGrid.Drag(370, 892, 105, -27)
  Regions.WA_data_grid_analytes_names_changed_5.Check(Aliases.Quantist.MainWindowView.MainView.WA_dataGrid2)

  extendedDataGrid.Drag(474, 896, 92, -4)
  Regions.WA_data_grid_analytes_names_changed_6.Check(Aliases.Quantist.MainWindowView.MainView.WA_dataGrid2)
    
  #Click on Multi Analytes View - PM8800
  treeView.ClickItem("|[0]|[1]")
  treeListView = Aliases.Quantist.MainWindowView.MainView.CurveData.MA_dataGrid
  aqUtils.Delay(ProjectSuite.Variables.Long_Delay)
  
  #TestObj.WaitProperty(PropertyName, PropertyValue, WaitTime)
  #grid = NameMapping.Sys.Quantist.HwndSource_MainWindowView.MainWindowView.Grid.Grid.Grid.Border.ztreeListControl1.ztreeListView1
  
  grid = Aliases.Quantist.MA_GridView
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  if (grid.WaitProperty("Visible", True, 5)):
    Regions.MA_data_grid_analytes_names_changed_1.Check(Aliases.Quantist.MA_GridView)
    treeListView.Drag(50, 948, 258, 3)
    Regions.MA_data_grid_analytes_names_changed_2.Check(Aliases.Quantist.MA_GridView)
    treeListView.Drag(367, 948, 267, -2)
    Regions.MA_data_grid_analytes_names_changed_3.Check(Aliases.Quantist.MA_GridView)
    treeListView.Drag(600, 951, 265, 8)
    Regions.MA_data_grid_analytes_names_changed_4.Check(Aliases.Quantist.MA_GridView)
    treeListView.Drag(915, 951, 206, -19)
    Regions.MA_data_grid_analytes_names_changed_5.Check(Aliases.Quantist.MA_GridView)
  
  aqUtils.Delay(ProjectSuite.Variables.Long_Delay)
  treeView.ClickItem("|[1]|[3]")
  aqUtils.Delay(ProjectSuite.Variables.Long_Delay)
  
  hwndSource = Aliases.Quantist.MainWindowView
  treeListView = hwndSource.MainView.CurveData.MA_dataGrid
  inplaceBaseEdit = treeListView.InplaceBaseEdit
  inplaceBaseEdit.Click(49, 13)
  inplaceBaseEdit2 = treeListView.InplaceBaseEdit2
  inplaceBaseEdit2.Click(46, 11, skShift)
  #Shift-Ctrl-c
  inplaceBaseEdit2.Keys("^c")
  hwndSource.RunTreeView.ClickItem("|[0]|[3]")
  aqUtils.Delay(ProjectSuite.Variables.Long_Delay)
  
  #Shift-Ctrl-v
  treeListView.InplaceBaseEdit.Click(36, 12)
  inplaceBaseEdit = treeListView.InplaceBaseEdit2
  inplaceBaseEdit.Click(40, 16, skShift)
  inplaceBaseEdit.Keys("^v")
  
  Log.Message("Confirm Row Operation: Copy-Paste using Ctrl-c and Ctrl-v are disabled")
  Regions.PM8800_CopyPaste_Ctrlc_Ctrlv_Confirm_Disabled.Check(Aliases.Quantist.MainWindowView.MainView)

  treeListControl = quantist.MainWindowView.MainView.CurveData
  inplaceBaseEdit = treeListControl.InplaceBaseEdit12
  inplaceBaseEdit.Click(81, 12)
  inplaceBaseEdit.Drag(57, 8, -74, 0)
  inplaceBaseEdit.TextEdit.ClickR(9, 12)
  editorContextMenu = quantist.HwndSource_PopupRoot.PopupRoot.EditorContextMenu
  editorContextMenu.ClickItem("Copy")
  inplaceBaseEdit = treeListControl.InplaceBaseEdit
  inplaceBaseEdit.Click(50, 10)
  inplaceBaseEdit.Click(50, 10)
  textEdit = inplaceBaseEdit.TextEdit
  textEdit.Drag(50, 10, -57, -1)
  textEdit.ClickR(25, 12)
  editorContextMenu.ClickItem("Paste")
  inplaceBaseEdit = treeListControl.InplaceBaseEdit9
  inplaceBaseEdit.Click(40, 13)
  inplaceBaseEdit.Click(41, 9)
  comboBoxEdit = inplaceBaseEdit.ComboBoxEdit
  comboBoxEdit.Drag(41, 9, -53, -3)
  comboBoxEdit.ClickR(18, 8)
  editorContextMenu.ClickItem("Copy")
  treeListView = treeListControl.MA_dataGrid
  inplaceBaseEdit = treeListView.InplaceBaseEdit
  inplaceBaseEdit.Click(33, 10)
  inplaceBaseEdit.Click(33, 10)
  inplaceBaseEdit.ComboBoxEdit.ClickR(33, 10)
  editorContextMenu.ClickItem("Paste")
  inplaceBaseEdit = treeListView.InplaceBaseEdit12
  inplaceBaseEdit.Click(24, 15)
  inplaceBaseEdit.Click(24, 15)
  inplaceBaseEdit.ComboBoxEdit.ClickR(24, 15)
  editorContextMenu.ClickItem("Paste")
  inplaceBaseEdit = treeListView.InplaceBaseEdit2
  inplaceBaseEdit.Click(30, 15)
  inplaceBaseEdit.ClickR(30, 14)

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Log.Message("Confirm Row Operation: Copy-Paste using Mouse clicks")  
  Regions.PM8800_CopyPaste_Mouse_operation.Check(Aliases.Quantist.MainWindowView.MainView.CurveData)

  treeListControl = Aliases.Quantist.MainWindowView.MainView.CurveData
  inplaceBaseEdit = treeListControl.InplaceBaseEdit12
  inplaceBaseEdit.Click(78, 9)
  inplaceBaseEdit.Keys("[Del]")
  inplaceBaseEdit.Click(74, 8)
  textEdit = inplaceBaseEdit.TextEdit
  textEdit.Keys("[BS][BS][BS][BS][BS]")
  rowControl = NameMapping.Sys.Quantist.HwndSource_MainWindowView.MainWindowView.Grid.Grid.Grid.Border.ztreeListControl1
  rowControl.RowControl5.Click(508, 10)
  textEdit.Keys("^c")
  rowControl.RowControl4.Click(522, 12)
  treeListControl.InplaceBaseEdit.Keys("^v")
  
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Log.Message("Confirm blank cell Copy-Paste using Ctrlc-Ctrlv")    
  Regions.PM8800_CopyPaste_Ctrlc_Ctrlv_EmptyCell_bugfixed.Check(Aliases.Quantist.MainWindowView.MainView)
