import Load_CSV_File 
import Quantist_Removing_Files

def Rsquared_value():
  
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
  
  while (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files()
  
  if (not treeView.HasItems):
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.SampleInvalidCSVFolder, "SS_Spiked_Linearity_HEP-EDTA.csv")

  aqUtils.Delay(3000)
  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.MainView.CurvePanel.Textblock0999594, "Enabled", cmpEqual, True)
  
  Rsq = Aliases.Quantist.MainWindowView.MainView.CurvePanel.Rsquared.WPFControlText
  analyte = Aliases.Quantist.MainWindowView.MainView.CurvePanel.AnalyteBox
  
  i=0
  while (i < 50):
     analyte.ClickItem(i)
     if (Rsq == "1"):
        Log.Message("Analyte: " + analyte.wText)
        Log.Message("   R squared = 1!")
        Log.Message("   Failed !!")
     elif(Rsq != "1"):
        Log.Message("Analyte: " + analyte.wText)
        Log.Message("   R squared: " + Rsq)
     i += 1
