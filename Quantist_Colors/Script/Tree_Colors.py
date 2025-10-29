import Load_CSV_File 
import Quantist_Removing_Files

def Tree_Colors():
  
# Requirement 1963
# Goal for icons and sample types colors is to be comply with Bio-Techne colors.
#
# Bio-techne logo on top left of the application
#
# Icons for .quantist file and .csv file are different. 
# Selected run files icons are light green in color and unselected run files are greyed out. 
# Different icons are displayed for different views for each run file. 
# Unselected views icons are greyed out selected view is darker. 
    
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
  
  flag = False
  if (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files(flag)
  
  if (not treeView.HasItems):
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.SampleDataFolder, ProjectSuite.Variables.sample_csv_pm8800)
    aqUtils.Delay(ProjectSuite.Variables.Long_Delay)
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.SampleDataFolder, ProjectSuite.Variables.sample_csv_unknown_control)
    aqUtils.Delay(ProjectSuite.Variables.Long_Delay)
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.SampleQuantistFolder, ProjectSuite.Variables.sample_quantist_pm8800)

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  

  mainWindowView.CollapseButton.ClickButton()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
  Regions.Colors_RunTreeView_1.Check(Aliases.Quantist.MainWindowView.RunTreeView)

  mainWindowView.ExpandingButton.ClickButton()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Regions.Colors_RunTreeView_2.Check(Aliases.Quantist.MainWindowView.RunTreeView)
  #Regions.Colors_RunTreeView_quantist_icon_active.Check(Regions.CreateRegionInfo(Aliases.Quantist.MainWindowView.RunTreeView, 3, 328, 55, 32, False))
  Regions.Colors_RunTreeView_quantist_icon_active.Check(Regions.CreateRegionInfo(Aliases.Quantist.MainWindowView.RunTreeView, 3, 324, 55, 35, False))

  treeView = mainWindowView.RunTreeView
  treeView.ClickItem("|[1]|[0]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
  
  Regions.Colors_RunTreeView_csv_icon_active.Check(Regions.CreateRegionInfo(Aliases.Quantist.MainWindowView.RunTreeView, 0, 165, 59, 36, False))
  Regions.Colors_RunTreeView_csv_icon_inactive.Check(Regions.CreateRegionInfo(Aliases.Quantist.MainWindowView.RunTreeView, 7, 10, 52, 31, False))
  #Regions.Colors_RunTreeView_quantist_icon_inactive.Check(Regions.CreateRegionInfo(Aliases.Quantist.MainWindowView.RunTreeView, 3, 322, 54, 39, False))
  Regions.Colors_RunTreeView_quantist_icon_inactive.Check(Regions.CreateRegionInfo(Aliases.Quantist.MainWindowView.RunTreeView, 1, 322, 57, 38, False))
  Regions.Colors_RunTreeView_SingleAnalyteView_active.Check(Regions.CreateRegionInfo(Aliases.Quantist.MainWindowView.RunTreeView, 2, 164, 273, 159, False))

  treeView.ClickItem("|[1]|[1]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
  Regions.Colors_RunTreeView_MultiAnalyteView_active.Check(Regions.CreateRegionInfo(Aliases.Quantist.MainWindowView.RunTreeView, 5, 165, 277, 158, False))

  treeView.ClickItem("|[1]|[2]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Regions.Colors_RunTreeView_WellAssignmentsView_active.Check(Regions.CreateRegionInfo(Aliases.Quantist.MainWindowView.RunTreeView, 0, 162, 281, 162, False))

  treeView.ClickItem("|[1]|[3]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Regions.Colors_RunTreeView_AnalytesPanelView_active.Check(Regions.CreateRegionInfo(Aliases.Quantist.MainWindowView.RunTreeView, 3, 165, 275, 156, False))

  treeView.ClickItem("|[1]|[4]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Regions.Colors_RunTreeView_RunInformationView_active.Check(Regions.CreateRegionInfo(Aliases.Quantist.MainWindowView.RunTreeView, 9, 169, 264, 158, False))  
  
# Verify Bio-Techne logo displayed on Menu bar
  Regions.Quantist_Bio_Techne_logo_menubar.Check(Regions.CreateRegionInfo(Aliases.Quantist.MainWindowView.MainViewRunCtr, 1771, 5, 144, 31, False))
  
def CorrectRGBComponent(component):
  component = aqConvert.VarToInt(component)
  if component < 0:
    component = 0
  else:
    if component > 255:
      component = 255
  return component

def RGB(r, g, b):
  r = CorrectRGBComponent(r)
  g = CorrectRGBComponent(g)
  b = CorrectRGBComponent(b)
  return r | (g << 8) | (b << 16)

def Test():
  Orange = RGB(255, 165, 0)
