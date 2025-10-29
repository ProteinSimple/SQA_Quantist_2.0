def Import_Data_File(varDir, varFileName):
  
  try:
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)

    quantist = Aliases.Quantist
    quantist.MainWindowView.LoadButton.ClickButton()
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)    
    file = varDir + varFileName 
    
    dlgOpen = quantist.dlgOpen
    quantist.dlgOpen.OpenFile(file, "Supported Files (*csv;*.quantist)")

  except ValueError as Error:
    Log.Warning("Can not load run file to Run Control View {Error}")
        
  except OSError as err:
    print("OS error: {0}".format(err))
    
  except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise

def Loading_File():
  try:
    quantist = Aliases.Quantist
    mainWindowView = quantist.MainWindowView
    gridSplitter = mainWindowView.GridSplitter
    mainWindowView.Button.ClickButton()
    quantist.dlgOpen.OpenFile(ProjectSuite.Variables.SampleDataFolder + ProjectSuite.Variables.sample_csv_pm8800, "Supported Files (*csv;*.quantist)")
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    
    #f = open('myfile.txt')
    #s = f.readline()
    #i = int(s.strip())
  except OSError as err:
      print("OS error: {0}".format(err))
  #except ValueError:
  #    print("Could not convert data to an integer.")
  except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
