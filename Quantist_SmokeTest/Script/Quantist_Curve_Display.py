import Quantist_Removing_Files

def Curve_Analytes():
  pass

def Curve_Analytes_BK(): 
  
  treeView = Aliases.Quantist.MainWindowView.RunTreeView
  if not (treeView.HasItems): 
    quantist = Aliases.Quantist
    quantist.MainWindowView.LoadButton.ClickButton()
    str = ProjectSuite.Variables.SampleDataFolder + ProjectSuite.Variables.sample_csv_pm8800
    quantist.dlgOpen.OpenFile(str, "Consumable Files (*.csv;*.quantist)")
  
  i = 0
  #while (i < Aliases.Quantist.MainWindowView.MainView.AnalyteBox.wItemCount):

  while (i < 2):
     Aliases.Quantist.MainWindowView.MainView.AnalyteBox.ClickItem(i)
     #ProjectSuite.Variables.Short_Delay
     
     if (i==0): #Analyte B7_H1
       Log.Message("Analyte: B7_H1")

       Config_Current_Curve_Analyte("FivePL", "OneOverYSquared", "From60To140", "CurveData_B7_H1_5PL_1Ysq_60_140", "B7_H1_5PL_1OverYsq_60_140Pct")
       Config_Current_Curve_Analyte("FivePL", "OneOverYSquared", "From70To130", "CurveData_B7_H1_5PL_1Ysq_70_130", "B7_H1_5PL_1OverYsq_70_130Pct")
       Config_Current_Curve_Analyte("FivePL", "OneOverYSquared", "From80To120", "CurveData_B7_H1_5PL_1Ysq_80_120", "B7_H1_5PL_1OverYsq_80_120Pct")
       Config_Current_Curve_Analyte("FivePL", "OneOverYSquared", "From90To110", "CurveData_B7_H1_5PL_1Ysq_90_110", "B7_H1_5PL_1OverYsq_90_110Pct")  
       
       Config_Current_Curve_Analyte("FivePL", "None", "From60To140", "CurveData_B7_H1_5PL_None_60_140", "B7_H1_5PL_None_60_140Pct")
       Config_Current_Curve_Analyte("FivePL", "None", "From70To130", "CurveData_B7_H1_5PL_None_70_130", "B7_H1_5PL_None_70_130Pct")
       Config_Current_Curve_Analyte("FivePL", "None", "From80To120", "CurveData_B7_H1_5PL_None_80_120", "B7_H1_5PL_None_80_120Pct")
       Config_Current_Curve_Analyte("FivePL", "None", "From90To110", "CurveData_B7_H1_5PL_None_90_110", "B7_H1_5PL_None_90_110Pct")

       Config_Current_Curve_Analyte("FivePL", "OneOverY", "From60To140", "CurveData_B7_H1_5PL_1Y_60_140", "B7_H1_5PL_1OverY_60_140Pct")
       Config_Current_Curve_Analyte("FivePL", "OneOverY", "From70To130", "CurveData_B7_H1_5PL_1Y_70_130", "B7_H1_5PL_1OverY_70_130Pct")
       Config_Current_Curve_Analyte("FivePL", "OneOverY", "From80To120", "CurveData_B7_H1_5PL_1Y_80_120", "B7_H1_5PL_1OverY_80_120Pct")
       Config_Current_Curve_Analyte("FivePL", "OneOverY", "From90To110", "CurveData_B7_H1_5PL_1Y_90_110", "B7_H1_5PL_1OverY_90_110Pct")
       
     if (i==1): #Analyte CD40 Lig
       Log.Message("Analyte: CD40 Lig")

       Config_Current_Curve_Analyte("FourPL", "None", "From60To140", "CurveData_CD40_4PL_None_60_140", "CD40_4PL_None_60_140")
       Config_Current_Curve_Analyte("FourPL", "OneOverY", "From70To130", "CurveData_CD40_4PL_1Y_70_130", "CD40_4PL_1Y_70_130")
       Config_Current_Curve_Analyte("FourPL", "None", "From80To120", "CurveData_CD40_4PL_None_80_120", "CD40_4PL_None_80_120")
       Config_Current_Curve_Analyte("FourPL", "OneOverYSquared", "From90To110", "CurveData_CD40_4PL_1Ysq_90_110", "CD40_4PL_1Ysq_90_110")
       
     i += 1
  Quantist_Removing_Files.Removing_CSV_Files()

  
      
def Config_Current_Curve_Analyte(CurveFit, CurveWeight, RecoveryRange, CurveData, CurveImage):
  
  ProjectSuite.Variables.Short_Delay
  Aliases.Quantist.MainWindowView.MainView.CurveFitBox.ClickItem(CurveFit)
  Aliases.Quantist.MainWindowView.MainView.CurveWeightingBox.ClickItem(CurveWeight)
  Aliases.Quantist.MainWindowView.MainView.RecoveryRangeBox.ClickItem(RecoveryRange)  

  ## Compare Graph Images
  curve_filename = ProjectSuite.Variables.OUTPUT_DIRECTORY + CurveImage + ProjectSuite.Variables.IMAGE_EXTENSION
  graph_canvas = Aliases.Quantist.MainWindowView.MainView.zchart# The Graph object mapped name
  Aliases.Quantist.MainWindowView.RunTreeView.HoverMouse()   # Move mouse over TreeViewPanel - out of the Graph area
  
  graph_picture = graph_canvas.Picture()                    # grab the Graph chart picture
  graph_picture.SaveToFile(curve_filename)                  # Save Graph image file to OUTPUT folder

  Image_Comparison(CurveImage, "")                          # Compare images

  ## Compare Curve Data Images
  curve_data_filename = ProjectSuite.Variables.OUTPUT_DIRECTORY + CurveData + ProjectSuite.Variables.IMAGE_EXTENSION
  graph_canvas2 = Aliases.Quantist.MainWindowView.MainView.CurrentCurveData # The CurveData object 
  Aliases.Quantist.MainWindowView.RunTreeView.HoverMouse()  # Move mouse over TreeViewPanel - out of the Curve Data area
  
  curve_data_picture = graph_canvas2.Picture()              # grab the Curve Data picture
  curve_data_picture.SaveToFile(curve_data_filename)        # Save Curve Data image file to OUTPUT folder

  Image_Comparison(CurveData, "")                          # Compare images


def Image_Comparison(file_name, file_type):
# Compare image from Graph & Lane tab views to a previous version (v4.1) from Regions
#  Parameters :  file_name : string = the name of the file to save
#                file_type : string = Graph | Lane - the type of image that is being saved

    if file_type:
       expected_picture_name = "%s_%s" % (file_name, file_type)
    else:
       expected_picture_name = "%s" % (file_name)
    
    Log.AppendFolder("Image_Comparison : %s vs %s " % (file_name, expected_picture_name))

    if file_type:
       full_file_name = "%s%s_%s%s" % (ProjectSuite.Variables.OUTPUT_DIRECTORY, file_name, file_type, ProjectSuite.Variables.IMAGE_EXTENSION)     # add constant Output DIR to file_name
    else:
       full_file_name = "%s%s%s" % (ProjectSuite.Variables.OUTPUT_DIRECTORY, file_name, ProjectSuite.Variables.IMAGE_EXTENSION)     # add constant Output DIR to file_name
    
    graph_picture = Utils.Picture
    graph_picture.LoadFromFile(full_file_name)                                 # load image from disk 

    if graph_picture.Size.Height == 0:                                         # check to see if the source image was found - error on fail
       Log.Error("Source Image NOT found : %s" % (full_file_name))
       Log.PopLogFolder()
       return
       
    expected_picture = Regions.GetPicture(expected_picture_name)               # get the expected image from Regions

    if expected_picture is None:                                               # check to see if the reference image was found - error on fail
       Log.Error("Regions Reference Image NOT found : %s" % (expected_picture_name))
       Log.PopLogFolder()
       return
    
    Log.Picture(expected_picture, "Expected image : %s_%s" % (file_name, file_type))        # Add Expected image in the log report
    Log.Picture(graph_picture,"Actual image : %s" % file_name)              # Add Actual image in the log report.
        
    #if file_type:
    #   mask_image = Regions.GetPicture("Mask_%s" % (file_type))                   # get the Mask (white) image from Regions
    #else:
    #   mask_image = Regions.GetPicture("Mask_Plain")                              # plain Mask White from Regions
       
    pixcel_tolerance = ProjectSuite.Variables.PIXEL_TOLERANCE
    color_tolerance = ProjectSuite.Variables.COLOR_TOLERANCE

    # Comparing the images using the Difference method
    # PictureObj.Difference(Picture, Transparent, PixelTolerance, Mouse, ColorTolerance, Mask)
    #ResultImage = expected_picture.Difference(graph_picture, False, pixcel_tolerance, False, color_tolerance, mask_image)
    ResultImage = expected_picture.Difference(graph_picture, False, pixcel_tolerance, False, color_tolerance)

    if ResultImage == None:
       Log_Bold_Message("%s : The images are identical" % file_type)
    else:
       bold_attrib = Log.CreateNewAttributes()
       bold_attrib.Bold = True
       Log.Error("%s : IMAGE MISMATCH @ %s : %s    Ref Image : %s" % (file_type, pixcel_tolerance, color_tolerance, expected_picture_name), "", pmHigher, bold_attrib, ResultImage, -1)

    Log.PopLogFolder()
    
    
def Log_Bold_Message(error_message):
## Create a log message with BOLD font attributes
## Parameters : error_message : string = the string to send to test log
 
   MsgAttr = Log.CreateNewAttributes()                                         # set Message to Bold
   MsgAttr.Bold = True

   Log.Message(error_message, "", pmHigher, MsgAttr)    


