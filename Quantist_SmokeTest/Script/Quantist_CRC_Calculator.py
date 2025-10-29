import Quantist_Removing_Files
import Load_CSV_File

def CRC_Calculator():
  quantist = Aliases.Quantist
  mainWindowView = Aliases.Quantist.MainWindowView

  treeView = Aliases.Quantist.MainWindowView.RunTreeView
  Xbutton = treeView.TreeViewItem.Button
  
  flag = True
  while (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files(flag)
  
  if (not treeView.HasItems):
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.SampleDataFolder, "PM8800.csv")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)

  crcStr = "CRC32:"
  with open(ProjectSuite.Variables.SampleDataFolder + '/PM8800.csv') as f:
    line = f.readline()
    while line:
        line = f.readline()
        if (crcStr in line):
           crcValue = line[7:14]        
           Log.Message("CRC string found from CSV file: " + line)

    if (not crcStr):
       Log.Message("No CRC32 string found from current loading file!")
    f.close()
    
#  Aliases.Quantist.MainWindowView.RunTreeView.ClickItem("|[0]|[4]")
#  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
#  #Regions.PM8800_FileCRC.Check(Regions.CreateRegionInfo(Aliases.Quantist.MainWindowView.MainView, 5, 5, 182, 85, False))
#  Regions.PM8800_FileCRC.Check(Regions.CreateRegionInfo(Aliases.Quantist.MainWindowView.MainView, 2, 4, 199, 85, False))

  #aqObject.CheckProperty(Aliases.Quantist.MainWindowView.MainView.Textblock_File_CRC, "Text", cmpEqual, "FileCRC: ")
  #aqObject.CheckProperty(Aliases.Quantist.MainWindowView.MainView.Value_File_CRC, "Text", cmpEqual, crcValue)

  #aqObject.CheckProperty(Aliases.Quantist.MainWindowView.MainView.Textblock_Calculated_CRC, "Text", cmpEqual, "Calculated CRC: ")
  #aqObject.CheckProperty(Aliases.Quantist.MainWindowView.MainView.Value_Calculated_CRC, "Text", cmpEqual, crcValue)
  
#  if (crcValue in tem):
#     Log.Message("CRC value verified: pass!")
#  
  mainWindowView.RunTreeView.ClickItem("|[0]|[4]")
  Regions.SystemFileInfo.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel.ExpanderSystemFileInformation, False, False, 35813, 17)
  scrollViewer = mainWindowView.MainView.CurvePanel
  expander = scrollViewer.ExpanderBatchInformation
  expander.Expand()
  scrollViewer.ExpanderSystemFileInformation.Collapse()
  expander.Expand()
  Regions.BatchInfo.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel.ExpanderBatchInformation, False, False, 71626, 17)
  expander.Collapse()
  expander = scrollViewer.ExpanderCalibrationInformation
  expander.Expand()
  #Regions.CalibrationInfo.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel.ExpanderCalibrationInformation, False, False, 25280, 17)
  Regions.CalibrationInfo.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel.ExpanderCalibrationInformation)

  expander.Collapse()
  expander = scrollViewer.ExpanderAssayLotInformation

  expander.Expand()
  Regions.AssayLotInfo.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel.ExpanderAssayLotInformation, False, False, 25280, 17)

  expander.Collapse()
  Regions.notesView.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel.znotesView1, False, False, 14746, 17)

  scrollViewer.znotesView1.Collapse()
  scrollViewer.ExpanderWarningErrors.Expand()
  Regions.WarningErrors.Check(Aliases.Quantist.MainWindowView.MainView.CurvePanel.ExpanderWarningErrors, False, False, 25280, 17)

