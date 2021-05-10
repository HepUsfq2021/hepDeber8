import FWCore.ParameterSet.Config as cms

import FWCore.Utilities.FileUtils as FileUtils

process = cms.Process("led")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )

files = FileUtils.loadListFromFile("data/CMS_Run2011A_DoubleElectron_AOD_12Oct2013-v1_20000_file_index.txt")
files.extend(FileUtils.loadListFromFile("data/CMS_Run2011A_DoubleElectron_AOD_12Oct2013-v1_20001_file_index.txt"))
files.extend(FileUtils.loadListFromFile("data/CMS_Run2011B_DoubleElectron_AOD_12Oct2013-v1_00000_file_index.txt"))
files.extend(FileUtils.loadListFromFile("data/CMS_Run2011B_DoubleElectron_AOD_12Oct2013-v1_20000_file_index.txt")) 

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
       *files
    )
)

process.led = cms.EDAnalyzer('LEDAnalysis',InputCollection = cms.InputTag("gsfElectrons")
)


process.p = cms.Path(process.led)

# Register fileservice for output file
process.ledanalysis = cms.EDAnalyzer("LEDAnalysis", isData = cms.bool(True))
process.TFileService = cms.Service(
    "TFileService", fileName=cms.string("output.root"))
