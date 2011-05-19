import FWCore.ParameterSet.Config as cms

susyNtuplizer = cms.EDAnalyzer('SusyNtuplizer',
                               lumiSummaryTag = cms.InputTag("lumiProducer"),
                               l1GTReadoutTag = cms.InputTag("gtDigis"),
                               l1GTObjectMapTag = cms.InputTag("hltL1GtObjectMap"),
                               hltCollectionTag = cms.InputTag("TriggerResults::HLT"),
                               vtxCollectionTag = cms.InputTag("offlinePrimaryVertices"),
                               trackCollectionTag = cms.InputTag("generalTracks"),
                               muonCollectionTag = cms.InputTag("muons"),
                               muonIDCollectionTags = cms.vstring("muidAllArbitrated",
                                                                  "muidGMStaChiCompatibility",
                                                                  "muidGMTkChiCompatibility",
                                                                  "muidGMTkKinkTight",
                                                                  "muidGlobalMuonPromptTight",
                                                                  "muidTM2DCompatibilityLoose",
                                                                  "muidTM2DCompatibilityTight",
                                                                  "muidTMLastStationAngLoose",
                                                                  "muidTMLastStationAngTight",
                                                                  "muidTMLastStationLoose",
                                                                  "muidTMLastStationOptimizedLowPtLoose",
                                                                  "muidTMLastStationOptimizedLowPtTight",
                                                                  "muidTMLastStationTight",
                                                                  "muidTMOneStationAngLoose",
                                                                  "muidTMOneStationAngTight",
                                                                  "muidTMOneStationLoose",
                                                                  "muidTMOneStationTight",
                                                                  "muidTrackerMuonArbitrated"),
                               electronCollectionTags = cms.vstring("gsfElectrons","pfElectronTranslator:pf"),
                               electronIDCollectionTags = cms.vstring("eidLoose",
                                                                      "eidRobustHighEnergy",
                                                                      "eidRobustLoose",
                                                                      "eidRobustTight",
                                                                      "eidTight"),
                               photonCollectionTags = cms.vstring("photons","pfPhotonTranslator:pfphot"),
                               photonIDCollectionTags = cms.vstring("PhotonCutBasedIDLoose",
                                                                    "PhotonCutBasedIDLooseEM",
                                                                    "PhotonCutBasedIDTight"),
                               genCollectionTag = cms.InputTag("genParticles"),
                               simVertexCollectionTag = cms.InputTag("g4SimHits"),
                               caloJetCollectionTags = cms.vstring("ak5CaloJets",
                                                                   "ak7CaloJets",
                                                                   "kt4CaloJets",
                                                                   "kt6CaloJets"),
                               pfJetCollectionTags = cms.vstring("ak5PFJets",
                                                                 "ak7PFJets",
                                                                 "kt4PFJets",
                                                                 "kt6PFJets"),
                               jptJetCollectionTags = cms.vstring("JetPlusTrackZSPCorJetAntiKt5",
                                                                  "TCTauJetPlusTrackZSPCorJetAntiKt5"),
                               metCollectionTags = cms.vstring("tcMet",
                                                               "corMetGlobalMuons",
                                                               "met",
                                                               "pfMet"),
                               pfCandidateCollectionTags = cms.vstring("particleFlow","particleFlow:electrons"),
                               muonThreshold = cms.double(10.0),
                               electronThreshold = cms.double(10.0),
                               photonThreshold = cms.double(10.0),
                               jetThreshold = cms.double(10.0),
                               pfParticleThreshold = cms.double(1.0),
                               debugLevel = cms.int32(0),
                               storeGenInfos = cms.bool(True),
                               storeGeneralTracks = cms.bool(False),
                               recoMode = cms.bool(False),
                               outputFileName = cms.string("susyEvent.root")                               
)
