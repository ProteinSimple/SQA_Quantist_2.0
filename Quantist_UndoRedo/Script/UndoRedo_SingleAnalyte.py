import CommonUnit

def Loading_CSV_File():
  analyte = Aliases.Quantist.MainWindowView.MainView.CurvePanel.AnalyteBox

  #CommonUnit.Import_Data_File(Project.Variables.SampleQuantistFiles, "MAGPIX data.csv")

  i = 0
  analyteCount = Aliases.Quantist.MainWindowView.MainView.CurvePanel.AnalyteBox.wItemCount
      
  while (i < analyteCount):
      
    Aliases.Quantist.MainWindowView.MainView.CurvePanel.AnalyteBox.ClickItem(i)
    analyte = Aliases.Quantist.MainWindowView.MainView.CurvePanel.AnalyteBox.wText

    aqUtils.Delay(Project.Variables.ShortDelay)
    Log.Message(" ")
    Log.Message("Analyte: " + analyte)
    i = i+1
