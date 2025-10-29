def Sorting_Region():
  region  = Aliases.Quantist.MainWindowView.MainView.CurveData.RegionHeader
  
  region.Click()
  Regions.AP_Sorting_Region.Check(Aliases.Quantist.MainWindowView.MainViewRunCtr, False, False, 141659, 17)

  
  
def Sorting_AnalyteNames():
  analyte = Aliases.Quantist.MainWindowView.MainView.CurveData.AnalyteHeader
  
  analyte.Click()
  Regions.AP_Sorting_Analyte_Names_1.Check(Aliases.Quantist.MainWindowView.MainViewRunCtr, False, False, 141659, 17)
  
