from os import listdir
from os.path import isfile, join
from os import walk  

#==============================================================================
def List_Installation_Files():

  #"C:\\Quantist\\SQA-Quantist\\Test_Data\\Output\\Quantist_Installation_Files.txt"
  oFile = aqFile.OpenTextFile(Project.Variables.QuantistInstallationFiles, aqFile.faWrite, aqFile.ctANSI, True)
  
  installDir = ProjectSuite.Variables.Quantist_Installation_Dir
  licenseDir = ProjectSuite.Variables.Quantist_License_Dir
  
  #=================================================
  licFile = []
  licDir  = []

  #oFile.Write("License Directory: " + licenseDir)
  Log.Message("This Test runs on Machine: " + Sys.HostName)
  Log.Message("Golden File Location: " + Project.Variables.QuantistInstallationFiles)
  Log.Message("License Directory: " + licenseDir)
  
  for (licDir, dirnames, filenames) in walk(licenseDir):
    licFile.extend(filenames)
    break

  count=1

  #oFile.Write("License File: ")
  for file in licFile:
     Log.Message("  " + str(count) +": " + licenseDir + file)
     #oFile.Write("  " + str(count) +": " + licenseDir + file)
     #count +=  1
  #=================================================
  
  files = []
  dirs  = []

  #=================================================  
  for (installDir, dirnames, filenames) in walk(installDir):
     files.extend(filenames)
     dirs.extend(dirnames)
     break
     
  oFile.Write("Installation Directory: " + installDir)
  oFile.Write("\n")
  oFile.Write("\nList of sub directories: ")
  
  for dir in dirs:
     subdir = installDir + dir
     subfile = []
     for (subdir,dirnames,subfiles) in walk(subdir):
         subfile.extend(subfiles)
     
     oFile.Write("\n")   
     oFile.Write(subdir)
     
     count=1
     for file in subfile:

         oFile.Write("\n")
         oFile.Write("    "+ str(count) +": " + subdir + "\\" + file)
         
         VerInfo = aqFileSystem.GetFileInfo(subdir + "\\" + file).VersionInfo
         if file != None and "User Guide" not in file:
            oFile.Write("- Version: " + str(VerInfo.FileMajorVersion) + "." + str(VerInfo.FileMinorVersion) + "." + str(VerInfo.FileBuildVersion) + "." + str(VerInfo.FileRevisionVersion))
            #edit.Keys(" Company: " + str(VerInfo.CompanyName[0]))
         count +=  1     

     oFile.Write("\n")
  
  #=================================================
  count=0

  for file in files:
     oFile.Write("\n")
     oFile.Write(str(count+1) +": " + installDir + file)
     oFile.Write("- Version: " + str(VerInfo.FileMajorVersion) + "." + str(VerInfo.FileMinorVersion) + "." + str(VerInfo.FileBuildVersion) + "." + str(VerInfo.FileRevisionVersion))

     count +=  1

  oFile.Close()  

  Log.Message("Installation Directory: " + installDir)
  Log.Message("Expected Number of Files from Installation Directory: " + str(Project.Variables.expectedNumOfFiles))
  Log.Message("Actual total number of files: " + str(count))
  
  if count == Project.Variables.expectedNumOfFiles:
     Log.Message("Actual total number of files matches: Passed")
  else:
     Log.Message("Actual total number of files do not match: Failed")
    
  Files.Quantist_Installation_Files.Check(Project.Variables.QuantistInstallationFiles) 
  
def FileVersion(file):
  Log.Message(file)
  VerInfo = aqFileSystem.GetFileInfo(file).VersionInfo
  edit.Keys("File version: " + str(VerInfo.FileMajorVersion) + "." + str(VerInfo.FileMinorVersion) + "." + str(VerInfo.FileBuildVersion) + "." + str(VerInfo.FileRevisionVersion))
  Log.Message("File version: " + str(VerInfo.FileMajorVersion) + "." + str(VerInfo.FileMinorVersion) + "." + str(VerInfo.FileBuildVersion) + "." + str(VerInfo.FileRevisionVersion))
  Log.Message("Description: " + str(VerInfo.FileDescription[0]))
  Log.Message("Product: " + str(VerInfo.ProductName[0]))
  Log.Message("Company: " + str(VerInfo.CompanyName[0]))

    
#==============================================================================
def SubFoldersFinder():
  # Specifies the path to the desired folder 
  installDir = Project.Variables.Quantist_Installation_Dir
  #sPath = "C:\\MyFolder"
  # Obtains information about the folder 
  FolInfo = aqFileSystem.GetFolderInfo(installDir)
  # Obtains the collection of subfolders 
  colSubFolders = FolInfo.SubFolders
  # Checks whether the collection is not empty 
  if colSubFolders != None:
    # Posts the names of the folder's subfolders to the test log 
    Log.AppendFolder("The " + installDir + " folder contains the following subfolders:")
    while colSubFolders.HasNext():
      # Obtains the current subfolder 
      FolItem = colSubFolders.Next()
      # Posts the subfolder's name to the test log 
      Log.Message(FolItem.Name)
    Log.PopLogFolder()
  else:
    Log.Message("The specified folder does not contain any subfolders.")

#==============================================================================
def get_version_number (filename):
    try:
        info = GetFileVersionInfo (filename, "\\")
        Log.Message(info)
        ms = info['FileVersionMS']
        ls = info['FileVersionLS']
        return HIWORD (ms), LOWORD (ms), HIWORD (ls), LOWORD (ls)
    except:
        return 0,0,0,0

#if __name__ == '__main__':
#  import os
#  filename = os.environ["COMSPEC"]
#  Log.Message(".".join ([str (i) for i in get_version_number (filename)]))

#==============================================================================
def getFileProperties(fname):
#==============================================================================
    """
    Read all properties of the given file return them as a dictionary.
    """
    propNames = ('Comments', 'InternalName', 'ProductName',
        'CompanyName', 'LegalCopyright', 'ProductVersion',
        'FileDescription', 'LegalTrademarks', 'PrivateBuild',
        'FileVersion', 'OriginalFilename', 'SpecialBuild')

    props = {'FixedFileInfo': None, 'StringFileInfo': None, 'FileVersion': None}

    try:
        # backslash as parm returns dictionary of numeric info corresponding to VS_FIXEDFILEINFO struc
        fixedInfo = win32api.GetFileVersionInfo(fname, '\\')
        props['FixedFileInfo'] = fixedInfo
        props['FileVersion'] = "%d.%d.%d.%d" % (fixedInfo['FileVersionMS'] / 65536,
                fixedInfo['FileVersionMS'] % 65536, fixedInfo['FileVersionLS'] / 65536,
                fixedInfo['FileVersionLS'] % 65536)

        # \VarFileInfo\Translation returns list of available (language, codepage)
        # pairs that can be used to retreive string info. We are using only the first pair.
        lang, codepage = win32api.GetFileVersionInfo(fname, '\\VarFileInfo\\Translation')[0]

        # any other must be of the form \StringfileInfo\%04X%04X\parm_name, middle
        # two are language/codepage pair returned from above

        strInfo = {}
        for propName in propNames:
            strInfoPath = u'\\StringFileInfo\\%04X%04X\\%s' % (lang, codepage, propName)
            ## print str_info
            strInfo[propName] = win32api.GetFileVersionInfo(fname, strInfoPath)

        props['StringFileInfo'] = strInfo
    except:
        pass

    return props


#==============================================================================
#from os import path
def calling_another():
  dir = Project.Variables.Quantist_Installation_Dir
  another_listDir(dir)

def another_listDir(dir):
    for filename in os.listdir(dir):
        if (os.path.isfile(os.path.join(dir, filename))):
           Log.Message((os.path.join(dir, filename)))
        if (os.path.isdir(os.path.join(dir))):
           Log.Message(os.path)

#==============================================================================
def List_Installation_Files2():

  dir = Project.Variables.Quantist_Installation_Dir
  files  = [f for f in listdir(dir) if isfile(join(dir, f))]
  subdir = [d for d in listdir(dir) if isdir(join(dir, d))]
  
  count=1
  for dirname in subdir:
      Log.Message(dirname)
      #count += 1

  #count=1
  for file in files:
      Log.Message(str(count)+": "+file)
      count += 1

     #getFileProperties(i)
     #fullPathToFile=os.path.join(dir,file)
     #major,minor,subminor,revision=filever.get_version_number(fullPathToFile)
     #Log.Message("Filename: %s \t Version: %s.%s.%s.%s" % (file,major,minor,subminor,revision))
     #for filename in os.dir():
     #    info = os.stat(filename)
     #    Log.Message(info.st_mtime)

               
  #  for root, dirs, files in os.walk(dir):
  #    for file in files:
  #        file = file.lower() # Convert .EXE to .exe so next line works
  #        if (file.count('.exe') or file.count('.dll')): # Check only exe or dll files
  #            fullPathToFile=os.path.join(root,file)
  #            major,minor,subminor,revision=filever.get_version_number(fullPathToFile)
  #            Log.Message("Filename: %s \t Version: %s.%s.%s.%s" % (file,major,minor,subminor,revision))
      
