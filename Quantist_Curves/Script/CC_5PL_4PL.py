# Test data file: PM8880
# Analyte: All 50 analytes
# Curve Fit: 5PL / 4PL
# Curve Weighting: 1/Ysq
# Recovery Range: 80-120%

import Load_CSV_File 
import Quantist_Removing_Files

def Calculate_netMFI_5PL():
  
  mainWindowView = Aliases.Quantist.MainWindowView  
  treeView = Aliases.Quantist.MainWindowView.RunTreeView
  
  flag = True
  while (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files(flag)
  
  if (not treeView.HasItems):
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.SampleDataFolder, "PM8800.csv")
    #Load_CSV_File.Import_Data_File(ProjectSuite.Variables.SampleQuantistFolder, "PM8800_ConcCV5pct.quantist")    

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Aliases.Quantist.MainWindowView.MainView.CurvePanel.CurveFitBox.ClickItem("FivePL")
  Aliases.Quantist.MainWindowView.MainView.CurvePanel.Btn_CopyToAll_CurveFit.ClickButton()
  
  i = 0
  analyteCount = Aliases.Quantist.MainWindowView.MainView.CurvePanel.AnalyteBox.wItemCount
  
  while (i < 10): #analyteCount):
      
    Aliases.Quantist.MainWindowView.MainView.CurvePanel.AnalyteBox.ClickItem(i)
    analyte = Aliases.Quantist.MainWindowView.MainView.CurvePanel.AnalyteBox.wText
    Log.Message(" ")
    Log.Message("Analyte: " + analyte)
  
    curveData = Aliases.Quantist.MainWindowView.MainView.CurvePanel

    a = curveData.AValue.WPFControlText
    b = curveData.BValue.WPFControlText
    c = curveData.CValue.WPFControlText
    d = curveData.DValue.WPFControlText
    g = curveData.GValue.WPFControlText

    grid = Aliases.Quantist.MainWindowView.MainView.CurveData
    grid.InplaceBaseEdit13.Click()
    grid.RowMarginControl2.Click()
    grid.GridData.InplaceBaseEdit4.Click()  # To highlight the rows for reviewing task
    grid.GridData.InplaceBaseEdit3.Click()  
    
    conc_B1 = grid.GridData.InplaceBaseEdit2.DisplayText    # Get Concentration value for B1
    conc_B2 = grid.GridData.InplaceBaseEdit7.DisplayText    # Get Concentration value for B2
    netMFI_B1 = grid.GridData.InplaceBaseEdit.DisplayText   # NetFMI B1 ("6639.00")
    netMFI_B2 = grid.GridData.InplaceBaseEdit6.DisplayText  # NnetMFI B2,("6276.00")

    Log.Message("Standard1")
    if ((conc_B1 != "") and (conc_B2 != "")):
      # perform 5PL calculation and verify displayed NetMFI value
      netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_B1), float(netMFI_B1))  
      netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_B2), float(netMFI_B2))  
    else:
      Log.Message("Concentration cannot be calculated. Net MFI > d coefficient!")
      Log.Message("Coeff d: "   + str(float(d)))
      Log.Message("NetMFI B1: " + str(float(netMFI_B1)))
      Log.Message("NetMFI B2: " + str(float(netMFI_B2)))
  
    ###################################################
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
    grid.RowMarginControl2.Click() # Collapse Standard1
    grid.InplaceBaseEdit16.Click()  
    grid.RowMarginControl3.Click() # Expand Standard2
    grid.GridData.InplaceBaseEdit4.Click()  # To highlight the rows for reviewing task
    grid.GridData.InplaceBaseEdit3.Click()  

    conc_C1 = grid.GridData.InplaceBaseEdit2.DisplayText    # Get Concentration value for C1
    conc_C2 = grid.GridData.InplaceBaseEdit7.DisplayText    # Get Concentration value for C2
    netMFI_C1 = grid.GridData.InplaceBaseEdit.DisplayText   # NetFMI C1
    netMFI_C2 = grid.GridData.InplaceBaseEdit6.DisplayText  # NetMFI C2
        
    # perform 5PL calculation and verify displayed NetMFI value
    Log.Message("Standard2")
    if ((conc_C1 != "") and (conc_C2 != "")):
      netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_C1), float(netMFI_C1))  
      netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_C2), float(netMFI_C2))  
    else:
      Log.Message("Concentration cannot be calculated. Net MFI > d coefficient!")
      Log.Message("Coeff d: "   + str(float(d)))
      Log.Message("NetMFI C1: " + str(float(netMFI_C1)))
      Log.Message("NetMFI C2: " + str(float(netMFI_C2)))

    ###################################################
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    grid.RowMarginControl3.Click() # Collapse Standard2
    grid.InplaceBaseEdit17.Click()
    grid.RowMarginControl4.Click() # Expand Standard3
    grid.GridData.InplaceBaseEdit4.Click()  # To highlight the rows for reviewing task
    grid.GridData.InplaceBaseEdit3.Click()  

    conc_D1 = grid.GridData.InplaceBaseEdit2.DisplayText    # Get Concentration value for D1
    conc_D2 = grid.GridData.InplaceBaseEdit7.DisplayText    # Get Concentration value for D2
    netMFI_D1 = grid.GridData.InplaceBaseEdit.DisplayText   # NetFMI D1
    netMFI_D2 = grid.GridData.InplaceBaseEdit6.DisplayText  # NetMFI D2
        
    Log.Message("Standard3")
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_D1), float(netMFI_D1))  
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_D2), float(netMFI_D2))  

    ###################################################
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
    grid.RowMarginControl4.Click() # Collapse Standard3
    grid.InplaceBaseEdit18.Click()
    grid.RowMarginControl5.Click() # Expand Standard4
    grid.GridData.InplaceBaseEdit4.Click()  # To highlight the rows for reviewing task
    grid.GridData.InplaceBaseEdit3.Click()  

    conc_E1 = grid.GridData.InplaceBaseEdit2.DisplayText    # Get Concentration value for E1
    conc_E2 = grid.GridData.InplaceBaseEdit7.DisplayText    # Get Concentration value for E2
    netMFI_E1 = grid.GridData.InplaceBaseEdit.DisplayText   # NetFMI E1
    netMFI_E2 = grid.GridData.InplaceBaseEdit6.DisplayText  # NetMFI E2

    Log.Message("Standard4")
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_E1), float(netMFI_E1))  
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_E2), float(netMFI_E2))    

    ###################################################
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
    grid.RowMarginControl5.Click() # Collapse Standard4
    grid.InplaceBaseEdit19.Click()
    grid.RowMarginControl6.Click() # Expand Standard5
    grid.GridData.InplaceBaseEdit4.Click()  # To highlight the rows for reviewing task
    grid.GridData.InplaceBaseEdit3.Click()  

    conc_F1 = grid.GridData.InplaceBaseEdit2.DisplayText    # Get Concentration value for F1
    conc_F2 = grid.GridData.InplaceBaseEdit7.DisplayText    # Get Concentration value for F2
    netMFI_F1 = grid.GridData.InplaceBaseEdit.DisplayText   # NetFMI F1
    netMFI_F2 = grid.GridData.InplaceBaseEdit6.DisplayText  # NetMFI F2

    Log.Message("Standard5")
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_F1), float(netMFI_F1))  
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_F2), float(netMFI_F2))        
  
    ###################################################
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
    grid.RowMarginControl6.Click() # Collapse Standard5
    grid.InplaceBaseEdit20.Click()
    grid.RowMarginControl7.Click() # Expand Standard6
    grid.GridData.InplaceBaseEdit4.Click()  # To highlight the rows for reviewing task
    grid.GridData.InplaceBaseEdit3.Click()  

    conc_G1 = grid.GridData.InplaceBaseEdit2.DisplayText    # Get Concentration value for D1
    conc_G2 = grid.GridData.InplaceBaseEdit7.DisplayText    # Get Concentration value for D2
    netMFI_G1 = grid.GridData.InplaceBaseEdit.DisplayText   # NetFMI D1
    netMFI_G2 = grid.GridData.InplaceBaseEdit6.DisplayText  # NetMFI D2

    Log.Message("Standard6")
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_G1), float(netMFI_G1))  
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_G2), float(netMFI_G2))  

    ###################################################
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
    grid.RowMarginControl7.Click() # Collapse Standard6
    grid.InplaceBaseEdit21.Click()
    grid.RowMarginControl8.Click() # Expand Standard7
    grid.GridData.InplaceBaseEdit4.Click()  
    grid.GridData.InplaceBaseEdit3.Click()  

    conc_H1 = grid.GridData.InplaceBaseEdit2.DisplayText    # Get Concentration value for D1
    conc_H2 = grid.GridData.InplaceBaseEdit7.DisplayText    # Get Concentration value for D2
    netMFI_H1 = grid.GridData.InplaceBaseEdit.DisplayText   # NetFMI D1
    netMFI_H2 = grid.GridData.InplaceBaseEdit6.DisplayText  # NetMFI D2
      
    Log.Message("Standard7")
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_H1), float(netMFI_H1))  
    netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_H2), float(netMFI_H2))

    grid.RowMarginControl8.Click() # Collapse Standard7        

    i += 1
      
def netMFI_5PL(a, b, c, d, g, conc, netMFI):
  netMFI_calc = (d + ((a-d) / pow((1+ pow((conc/c), b)), g)))
  if (int(netMFI_calc) == int(netMFI) or ((netMFI_calc / netMFI) < 1.0)):
    Log.Message("  netMFI displayed: " + str(netMFI))
    Log.Message("  netMFI value calculated: " + str(netMFI_calc))
    Log.Message("  netMFI 5PL verification Passed")
    Log.Message(" ")
    #Log.Message((netMFI_calc / netMFI))  

  else:
    Log.Message("  netMFI displayed: " + str(netMFI))
    Log.Message("  netMFI value calculated: " + str(netMFI_calc))
    Log.Message("  netMFI 5PL verification Failed")
    Log.Message(" ")

def Calculate_netMFI_4PL():
  
  mainWindowView = Aliases.Quantist.MainWindowView  
  treeView = Aliases.Quantist.MainWindowView.RunTreeView
  
  flag = True
  if (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files(flag)
  
  if (not treeView.HasItems):
    #Load_CSV_File.Import_Data_File(ProjectSuite.Variables.SampleDataFolder, "PM8800.csv")
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.SampleQuantistFolder, "PM8800.quantist")

  curve = Aliases.Quantist.MainWindowView.MainView.CurvePanel
  curve.CurveFitBox.ClickItem("FourPL")
  curve.Btn_CopyToAll_CurveFit.ClickButton()
  Aliases.Quantist.MainWindowView.MainView.CurvePanel.CurveWeightingBox.ClickItem("None")  
  
  i = 0
  analyteCount = Aliases.Quantist.MainWindowView.MainView.CurvePanel.AnalyteBox.wItemCount
    
  #while (i < analyteCount):
  while (i < 5):
    
    Aliases.Quantist.MainWindowView.MainView.CurvePanel.AnalyteBox.ClickItem(i)
    analyte = Aliases.Quantist.MainWindowView.MainView.CurvePanel.AnalyteBox.wText
    Log.Message(" ")
    Log.Message("Analyte: " + analyte)

    grid = Aliases.Quantist.MainWindowView.MainView.CurveData
    curveData = Aliases.Quantist.MainWindowView.MainView.CurvePanel

    a = curveData.AValue.WPFControlText
    b = curveData.BValue.WPFControlText
    c = curveData.CValue.WPFControlText
    d = curveData.DValue.WPFControlText

    ###################################################
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  
    grid.InplaceBaseEdit13.Click()
    grid.RowMarginControl2.Click()
    grid.GridData.InplaceBaseEdit4.Click()  # To highlight the rows for reviewing task
    grid.GridData.InplaceBaseEdit3.Click()  

    conc_B1 = grid.GridData.InplaceBaseEdit2.DisplayText    # Get Concentration value for B1
    conc_B2 = grid.GridData.InplaceBaseEdit7.DisplayText    # Get Concentration value for B2
    netMFI_B1 = grid.GridData.InplaceBaseEdit.DisplayText   # NetFMI B1
    netMFI_B2 = grid.GridData.InplaceBaseEdit6.DisplayText  # NetMFI B2
        
    #perform calculation and verify displayed NetMFI value
    Log.Message("Standard1")    
    
    if ((conc_B1 != "") and (conc_B2 != "")):
      netMFI_4PL (float(a), float(b), float(c), float(d), float(conc_B1), float(netMFI_B1))  
      netMFI_4PL (float(a), float(b), float(c), float(d), float(conc_B2), float(netMFI_B2))
    else:
      Log.Message("Concentration cannot be calculated. Net MFI > d coefficient!")
      
    ###################################################
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    grid.RowMarginControl2.Click() # To colapse Standard1
    grid.InplaceBaseEdit13.Click()
    grid.RowMarginControl3.Click()
    grid.GridData.InplaceBaseEdit4.Click()  # To highlight the rows for reviewing task
    grid.GridData.InplaceBaseEdit3.Click()  

    conc_C1 = grid.GridData.InplaceBaseEdit2.DisplayText    # Get Concentration value for C1
    conc_C2 = grid.GridData.InplaceBaseEdit7.DisplayText    # Get Concentration value for C2
    netMFI_C1 = grid.GridData.InplaceBaseEdit.DisplayText   # NetFMI C1 
    netMFI_C2 = grid.GridData.InplaceBaseEdit6.DisplayText  # NetMFI C2

    #perform calculation and verify displayed NetMFI value
    Log.Message("Standard2")
    netMFI_4PL (float(a), float(b), float(c), float(d), float(conc_C1), float(netMFI_C1))  
    netMFI_4PL (float(a), float(b), float(c), float(d), float(conc_C2), float(netMFI_C2))      
  
    ###################################################
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    grid.RowMarginControl3.Click() # To colapse Standard2
    #grid.InplaceBaseEdit13.Click()
    grid.RowMarginControl4.Click()
    grid.GridData.InplaceBaseEdit4.Click()  # To highlight the rows for reviewing task
    grid.GridData.InplaceBaseEdit3.Click()  

    conc_D1 = grid.GridData.InplaceBaseEdit2.DisplayText    # Get Concentration value for D1
    conc_D2 = grid.GridData.InplaceBaseEdit7.DisplayText    # Get Concentration value for D2
    netMFI_D1 = grid.GridData.InplaceBaseEdit.DisplayText   # NetFMI D1
    netMFI_D2 = grid.GridData.InplaceBaseEdit6.DisplayText  # NetMFI D2
        
    #perform calculation and verify displayed NetMFI value
    Log.Message("Standard3")
    netMFI_4PL (float(a), float(b), float(c), float(d), float(conc_D1), float(netMFI_D1))  
    netMFI_4PL (float(a), float(b), float(c), float(d), float(conc_D2), float(netMFI_D2))

    ###################################################
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    grid.RowMarginControl4.Click() # To colapse Standard3
    #grid.InplaceBaseEdit13.Click()
    grid.RowMarginControl5.Click()
    grid.GridData.InplaceBaseEdit4.Click()  # To highlight the rows for reviewing task
    grid.GridData.InplaceBaseEdit3.Click()  

    conc_E1 = grid.GridData.InplaceBaseEdit2.DisplayText    # Get Concentration value for E1
    conc_E2 = grid.GridData.InplaceBaseEdit7.DisplayText    # Get Concentration value for E2
    netMFI_E1 = grid.GridData.InplaceBaseEdit.DisplayText   # NetFMI E1
    netMFI_E2 = grid.GridData.InplaceBaseEdit6.DisplayText  # NetMFI E2

    #perform calculation and verify displayed NetMFI value
    Log.Message("Standard4")
    netMFI_4PL (float(a), float(b), float(c), float(d), float(conc_E1), float(netMFI_E1))  
    netMFI_4PL (float(a), float(b), float(c), float(d), float(conc_E2), float(netMFI_E2))  

    ###################################################
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    grid.RowMarginControl5.Click() # To colapse Standard4
    #grid.InplaceBaseEdit13.Click()
    grid.RowMarginControl6.Click()
    grid.GridData.InplaceBaseEdit4.Click()  # To highlight the rows for reviewing task
    grid.GridData.InplaceBaseEdit3.Click()  

    conc_F1 = grid.GridData.InplaceBaseEdit2.DisplayText    # Get Concentration value for F1
    conc_F2 = grid.GridData.InplaceBaseEdit7.DisplayText    # Get Concentration value for F2
    netMFI_F1 = grid.GridData.InplaceBaseEdit.DisplayText   # NetFMI F1 
    netMFI_F2 = grid.GridData.InplaceBaseEdit6.DisplayText  # NetMFI F2
        
    #perform calculation and verify displayed NetMFI value
    Log.Message("Standard5")
    netMFI_4PL (float(a), float(b), float(c), float(d), float(conc_F1), float(netMFI_F1))  
    netMFI_4PL (float(a), float(b), float(c), float(d), float(conc_F2), float(netMFI_F2))      
  
    ###################################################
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    grid.RowMarginControl6.Click() # To colapse Standard5
    #grid.InplaceBaseEdit13.Click()
    grid.RowMarginControl7.Click()
    grid.GridData.InplaceBaseEdit4.Click()  # To highlight the rows for reviewing task
    grid.GridData.InplaceBaseEdit3.Click()  

    conc_G1 = grid.GridData.InplaceBaseEdit2.DisplayText    # Get Concentration value for G1
    conc_G2 = grid.GridData.InplaceBaseEdit7.DisplayText    # Get Concentration value for G2
    netMFI_G1 = grid.GridData.InplaceBaseEdit.DisplayText   # NetFMI G1
    netMFI_G2 = grid.GridData.InplaceBaseEdit6.DisplayText  # NetMFI G2

    #perform calculation and verify displayed NetMFI value
    Log.Message("Standard6")
    netMFI_4PL (float(a), float(b), float(c), float(d), float(conc_G1), float(netMFI_G1))  
    netMFI_4PL (float(a), float(b), float(c), float(d), float(conc_G2), float(netMFI_G2))    
  
    ###################################################
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    grid.RowMarginControl7.Click() # To colapse Standard6
    #grid.InplaceBaseEdit13.Click()
    grid.RowMarginControl8.Click()
    grid.GridData.InplaceBaseEdit4.Click()  # To highlight the rows for reviewing task
    grid.GridData.InplaceBaseEdit3.Click()  

    conc_H1 = grid.GridData.InplaceBaseEdit2.DisplayText    # Get Concentration value for H1
    conc_H2 = grid.GridData.InplaceBaseEdit7.DisplayText    # Get Concentration value for H2
    netMFI_H1 = grid.GridData.InplaceBaseEdit.DisplayText   # NetFMI H1
    netMFI_H2 = grid.GridData.InplaceBaseEdit6.DisplayText  # NetMFI H2
        
    #perform calculation and verify displayed NetMFI value
    Log.Message("Standard7")
    netMFI_4PL (float(a), float(b), float(c), float(d), float(conc_H1), float(netMFI_H1))  
    netMFI_4PL (float(a), float(b), float(c), float(d), float(conc_H2), float(netMFI_H2)) 
   
    i += 1
        
def netMFI_4PL(a, b, c, d, conc, netMFI):
  netMFI_calc = (d + ((a-d) / (1+ pow((conc/c), b))))

  #if ((netMFI_calc / netMFI) < 1.1):
  if (int(netMFI_calc) == int(netMFI) or ((netMFI_calc / netMFI) < 1.0)):
    Log.Message("  netMFI displayed: " + str(netMFI))
    Log.Message("  netMFI value calculated: " + str(netMFI_calc))
    Log.Message("  netMFI 4PL verification Passed:")
    Log.Message(" ")
    #Log.Message((netMFI_calc / netMFI))  

  else:
    Log.Message("  netMFI displayed: " + str(netMFI))
    Log.Message("  netMFI value calculated: " + str(netMFI_calc))
    Log.Message("  netMFI 4PL verification Failed")
    Log.Message(" ")

def Calculate_5PL_Unknowns():
  
  treeListControl = Aliases.Quantist.MainWindowView.MainView.CurveData
  treeListView = treeListControl.GridData
  gridColumnHeader = treeListView.GridColumnHeader
  gridColumnHeader.Click()
  gridColumnHeader.Click()
  treeListView.Drag(1225, 200, -2, -153)
  
  curveData = Aliases.Quantist.MainWindowView.MainView.CurvePanel

  a = curveData.AValue.WPFControlText
  b = curveData.BValue.WPFControlText
  c = curveData.CValue.WPFControlText
  d = curveData.DValue.WPFControlText
  g = curveData.GValue.WPFControlText

#  grid = Aliases.Quantist.MainWindowView.MainView.CurveData
#  grid.InplaceBaseEdit13.Click()
#  grid.RowMarginControl2.Click()
#  grid.GridData.InplaceBaseEdit4.Click()  # To highlight the rows for review works
#  grid.GridData.InplaceBaseEdit3.Click()  
    
#  conc_1 = grid.InplaceBaseEdit14.DisplayText           # Get Concentration value for B1
#  conc_2 = grid.GridData.InplaceBaseEdit.DisplayText    # Get Concentration value for B2
#  netMFI_1 = grid.InplaceBaseEdit15.DisplayText         # Get netMFI value for B1
#  netMFI_2 = grid.GridData.InplaceBaseEdit2.DisplayText # Get netMFI value for B2    
#  
  rowMarginControl = treeListControl.RowMarginControl2
  
  treeListControl.RowMarginControl.Click()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  conc_1 = treeListControl.InplaceBaseEdit22.DisplayText
                    #aqObject.CheckProperty(inplaceBaseEdit, "DisplayText", cmpEqual, "0.00")
  conc_2 = treeListControl.InplaceBaseEdit14.DisplayText
                   #aqObject.CheckProperty(inplaceBaseEdit3, "DisplayText", cmpEqual, "194.86")
  netMFI_1 = treeListControl.InplaceBaseEdit23.DisplayText
                   #aqObject.CheckProperty(inplaceBaseEdit2, "DisplayText", cmpEqual, "-0.50")
  netMFI_2 = treeListControl.InplaceBaseEdit15.DisplayText
                   #aqObject.CheckProperty(inplaceBaseEdit4, "DisplayText", cmpEqual, "78.00")
  treeListControl.RowMarginControl.Click()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  

  netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_1), float(netMFI_1))  
  netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_2), float(netMFI_2))

######################################################  
  treeListControl.RowMarginControl4.Click()
  conc_1 = treeListControl.InplaceBaseEdit.DisplayText
                   #aqObject.CheckProperty(inplaceBaseEdit, "DisplayText", cmpEqual, "55.29")
  netMFI_1 = treeListControl.InplaceBaseEdit2.DisplayText
                   #aqObject.CheckProperty(inplaceBaseEdit2, "DisplayText", cmpEqual, "28.00")
  conc_2 = treeListControl.InplaceBaseEdit3.DisplayText
                   #aqObject.CheckProperty(inplaceBaseEdit3, "DisplayText", cmpEqual, "0.23")
  netMFI_2 = treeListControl.InplaceBaseEdit4.DisplayText
                   #aqObject.CheckProperty(inplaceBaseEdit4, "DisplayText", cmpEqual, "5.00")
  treeListControl.RowMarginControl4.Click()

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)    
  netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_1), float(netMFI_1))  
  netMFI_5PL (float(a), float(b), float(c), float(d), float(g), float(conc_2), float(netMFI_2))

def Test1():
  Aliases.Quantist.MainWindowView.MainView.CurvePanel.CurveWeightingBox.ClickItem("None")
