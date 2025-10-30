import Load_CSV_File 
import Quantist_Removing_Files

def Analytes_Panel_Edit_Units():
  
  quantist = Aliases.Quantist    
  main = Aliases.Quantist.MainWindowView  
  treeView = main.RunTreeView
  Xbutton = treeView.TreeViewItem.Button
  border = main.MainView
  
  flag = True
  if (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files(flag)
  
  if (not treeView.HasItems):
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.SampleDataFolder, "PM8800.csv")

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  treeView.ClickItem("|[0]|[3]")
    
  treeListControl = Aliases.Quantist.MainWindowView.MainView.CurveData
  treeListControl.InplaceBaseEdit12.Click(98, 8)
  treeListView = treeListControl.MA_dataGrid
  treeListView.InplaceBaseEdit3.Click(117, 2, skShift)
  Regions.PM8800_Selected_Rows_1.Check(Aliases.Quantist.MA_GridView)
  
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    
  treeListControl.InplaceBaseEdit10.Click(30, 9)
  treeListControl.InplaceBaseEdit13.Click(44, 9)
  inplaceBaseEdit = treeListView.InplaceBaseEdit5
  inplaceBaseEdit.Click(37, 10, skShift)
  Regions.PM8800_Selected_Rows_2.Check(Aliases.Quantist.MA_GridView)
    
  treeListControl.InplaceBaseEdit13.Click(29, 12)
  inplaceBaseEdit = treeListControl.MA_dataGrid.InplaceBaseEdit4
  inplaceBaseEdit.Click(36, 4, skShift)
  inplaceBaseEdit.Keys("pg/mL")
  #inplaceBaseEdit.ComboBoxEdit.Keys("g/mL")
  
  Regions.PM8800_Selected_Rows_3.Check(Aliases.Quantist.MA_GridView)  
 
  button = border.Btn_MoveDown
  for i in range(5):
    button.ClickButton()
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    i += 1

  Aliases.Quantist.MainWindowView.MainView.CurveData.InplaceBaseEdit12.Click(86, 13)

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Regions.PM8800_Selected_Rows_4.Check(Aliases.Quantist.MA_GridView)
        
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Aliases.Quantist.MainWindowView.MainView.Btn_Reset.ClickButton()
  Regions.PM8800_Selected_Rows_5.Check(Aliases.Quantist.MA_GridView)

  treeListControl.InplaceBaseEdit13.Click(37, 12)
  inplaceBaseEdit = treeListControl.MA_dataGrid.InplaceBaseEdit4
  inplaceBaseEdit.Click(55, 6, skShift)
  inplaceBaseEdit.Keys("test/mL")
  #inplaceBaseEdit.ComboBoxEdit.Keys("est/mL")
  Regions.PM8800_Selected_Rows_6.Check(Aliases.Quantist.MA_GridView)


  
  
def Analytes_bk():
  quantist = Aliases.Quantist    
  main = Aliases.Quantist.MainWindowView  
  treeView = main.RunTreeView
  Xbutton = treeView.TreeViewItem.Button
  
  flag = True
  if (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files(flag)
  
  if (not treeView.HasItems):
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.SampleDataFolder, "PM8800.csv")

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  treeView.ClickItem("|[0]|[3]")

  border = main.MainView
  treeListControl = border.CurveData
  inplaceBaseEdit = treeListControl.InplaceBaseEdit12
  
  inplaceBaseEdit.Click()
  treeListView = treeListControl.MA_dataGrid
  treeListView.InplaceBaseEdit.Click(95, 17, skShift)

  Regions.PM8800_Selected_Rows_1.Check(Aliases.Quantist.MA_GridView)
  treeListControl.InplaceBaseEdit10.Click()
  Aliases.Quantist.MainWindowView.RunTreeView.Click()
  Regions.PM8800_Selected_Rows_2.Check(Aliases.Quantist.MA_GridView)
  
  treeListControl.InplaceBaseEdit13.Click()
  inplaceBaseEdit2 = treeListView.InplaceBaseEdit2
  inplaceBaseEdit2.Click(47, 8, skShift)
  inplaceBaseEdit2.Click(10, 10)
  Aliases.Quantist.MainWindowView.MainView.CurveData.MA_dataGrid.InplaceBaseEdit2.ComboBoxEdit.Keys("pg/mL")  

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)    
  Regions.PM8800_Selected_Rows_3.Check(Aliases.Quantist.MA_GridView)

  button = border.Btn_MoveDown
  for i in range(5):
    button.ClickButton()
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    i += 1
  
  inplaceBaseEdit.Click()
  
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Regions.PM8800_Selected_Rows_4.Check(Aliases.Quantist.MA_GridView)    

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Aliases.Quantist.MainWindowView.MainView.Btn_Reset.ClickButton()
  Regions.PM8800_Selected_Rows_5.Check(Aliases.Quantist.MA_GridView)

  treeListView = Aliases.Quantist.MainWindowView.MainView.CurveData.MA_dataGrid
  treeListView.InplaceBaseEdit3.Click(29, 5)
  inplaceBaseEdit = treeListView.InplaceBaseEdit7
  inplaceBaseEdit.Click(61, 12, skShift)
  inplaceBaseEdit.Keys("n")
  inplaceBaseEdit.ComboBoxEdit.Keys("g/mL[Enter]")
  inplaceBaseEdit = treeListView.InplaceBaseEdit9
  inplaceBaseEdit.Click(44, 15, skShift)
  inplaceBaseEdit.Keys("U")
  inplaceBaseEdit.ComboBoxEdit.Keys("nits/mL[Enter]")  

  Regions.Analytes_units.Check(Aliases.Quantist.MA_GridView)
  #Files.Analytes_Units.Check("C:\\Quantist\\SQA-Quantist\\Test_Data\\OutTest1put\\Analytes_Units.txt")
  
  