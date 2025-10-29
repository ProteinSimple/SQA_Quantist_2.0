import Load_CSV_File 
import Quantist_Removing_Files

def Analytes_Not_Included():
  quantist = Aliases.Quantist
  mainWindowView = Aliases.Quantist.HwndSource_MainWindowView.MainWindowView  

  treeView = Aliases.Quantist.MainWindowView.RunTreeView
  Xbutton = treeView.TreeViewItem.Button

  flag = True
  if (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files(flag)
  
  if (not treeView.HasItems):
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.SampleDataFolder, "PM8800.csv")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)

  #Click on Analyte Panel View
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Aliases.Quantist.HwndSource_MainWindowView.MainWindowView.RunTreeView.ClickItem("|[0]|[3]")
        
  mainWindowView.Click(788, 77) # Include check/uncheck first row 
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  mainWindowView.Click(788, 97) # Include check/uncheck second row
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  mainWindowView.Click(788, 117) # Include check/uncheck third row
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  mainWindowView.Click(788, 137) # Include check/uncheck fourth row
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  mainWindowView.Click(788, 157) # Include check/uncheck fifth row

  #Verify uncheck Included
  Regions.Uncheck_Included.Check(Aliases.Quantist.HwndSource_MainWindowView.MainWindowView)

  #Click on Well Assignments View
  treeView.ClickItem("|[0]|[2]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    
  extendedDataGrid = Aliases.Quantist.MainWindowView.MainView.WA_dataGrid2

  # Verify that the NOT INCLUDED analytes will not be listed in Well Assignments View
  Regions.WA_data_grid_analytes_notIncluded_1.Check(Aliases.Quantist.MainWindowView.MainView.WA_dataGrid2)

  extendedDataGrid.Drag(54, 891, 106, -1)
  Regions.WA_data_grid_analytes_notIncluded_2.Check(Aliases.Quantist.MainWindowView.MainView.WA_dataGrid2)

  extendedDataGrid.Drag(151, 892, 94, -1)
  Regions.WA_data_grid_analytes_notIncluded_3.Check(Aliases.Quantist.MainWindowView.MainView.WA_dataGrid2)

  extendedDataGrid.Drag(261, 893, 107, -7)
  Regions.WA_data_grid_analytes_notIncluded_4.Check(Aliases.Quantist.MainWindowView.MainView.WA_dataGrid2)

  extendedDataGrid.Drag(354, 895, 106, -38)
  Regions.WA_data_grid_analytes_notIncluded_5.Check(Aliases.Quantist.MainWindowView.MainView.WA_dataGrid2)

  extendedDataGrid.Drag(477, 893, 48, -1)
  Regions.WA_data_grid_analytes_notIncluded_6.Check(Aliases.Quantist.MainWindowView.MainView.WA_dataGrid2)
  
