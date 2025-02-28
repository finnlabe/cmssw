# /dev/CMSSW_12_4_0/GRun

import FWCore.ParameterSet.Config as cms


# stream ParkingDoubleElectronLowMass0

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamParkingDoubleElectronLowMass0_datasetParkingDoubleElectronLowMass0_selector
streamParkingDoubleElectronLowMass0_datasetParkingDoubleElectronLowMass0_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamParkingDoubleElectronLowMass0_datasetParkingDoubleElectronLowMass0_selector.l1tResults = cms.InputTag('')
streamParkingDoubleElectronLowMass0_datasetParkingDoubleElectronLowMass0_selector.throw      = cms.bool(False)
streamParkingDoubleElectronLowMass0_datasetParkingDoubleElectronLowMass0_selector.triggerConditions = cms.vstring(
    'HLT_DoubleEle10_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle10_eta1p22_mMax6_v2',
    'HLT_DoubleEle4_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle4_eta1p22_mMax6_v2',
    'HLT_DoubleEle4p5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle4p5_eta1p22_mMax6_v2',
    'HLT_DoubleEle5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle5_eta1p22_mMax6_v2',
    'HLT_DoubleEle5p5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle5p5_eta1p22_mMax6_v2',
    'HLT_DoubleEle6_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle6_eta1p22_mMax6_v2',
    'HLT_DoubleEle6p5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle6p5_eta1p22_mMax6_v2',
    'HLT_DoubleEle7_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle7_eta1p22_mMax6_v2',
    'HLT_DoubleEle7p5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle7p5_eta1p22_mMax6_v2',
    'HLT_DoubleEle8_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle8_eta1p22_mMax6_v2',
    'HLT_DoubleEle8p5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle8p5_eta1p22_mMax6_v2',
    'HLT_DoubleEle9_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle9_eta1p22_mMax6_v2',
    'HLT_DoubleEle9p5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle9p5_eta1p22_mMax6_v2',
    'HLT_SingleEle8_SingleEGL1_v1',
    'HLT_SingleEle8_v1'
)

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamParkingDoubleElectronLowMass0_datasetParkingDoubleElectronLowMass1_selector
streamParkingDoubleElectronLowMass0_datasetParkingDoubleElectronLowMass1_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamParkingDoubleElectronLowMass0_datasetParkingDoubleElectronLowMass1_selector.l1tResults = cms.InputTag('')
streamParkingDoubleElectronLowMass0_datasetParkingDoubleElectronLowMass1_selector.throw      = cms.bool(False)
streamParkingDoubleElectronLowMass0_datasetParkingDoubleElectronLowMass1_selector.triggerConditions = cms.vstring(
    'HLT_DoubleEle10_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle10_eta1p22_mMax6_v2',
    'HLT_DoubleEle4_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle4_eta1p22_mMax6_v2',
    'HLT_DoubleEle4p5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle4p5_eta1p22_mMax6_v2',
    'HLT_DoubleEle5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle5_eta1p22_mMax6_v2',
    'HLT_DoubleEle5p5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle5p5_eta1p22_mMax6_v2',
    'HLT_DoubleEle6_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle6_eta1p22_mMax6_v2',
    'HLT_DoubleEle6p5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle6p5_eta1p22_mMax6_v2',
    'HLT_DoubleEle7_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle7_eta1p22_mMax6_v2',
    'HLT_DoubleEle7p5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle7p5_eta1p22_mMax6_v2',
    'HLT_DoubleEle8_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle8_eta1p22_mMax6_v2',
    'HLT_DoubleEle8p5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle8p5_eta1p22_mMax6_v2',
    'HLT_DoubleEle9_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle9_eta1p22_mMax6_v2',
    'HLT_DoubleEle9p5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle9p5_eta1p22_mMax6_v2',
    'HLT_SingleEle8_SingleEGL1_v1',
    'HLT_SingleEle8_v1'
)


# stream ParkingDoubleElectronLowMass1

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamParkingDoubleElectronLowMass1_datasetParkingDoubleElectronLowMass2_selector
streamParkingDoubleElectronLowMass1_datasetParkingDoubleElectronLowMass2_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamParkingDoubleElectronLowMass1_datasetParkingDoubleElectronLowMass2_selector.l1tResults = cms.InputTag('')
streamParkingDoubleElectronLowMass1_datasetParkingDoubleElectronLowMass2_selector.throw      = cms.bool(False)
streamParkingDoubleElectronLowMass1_datasetParkingDoubleElectronLowMass2_selector.triggerConditions = cms.vstring(
    'HLT_DoubleEle10_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle10_eta1p22_mMax6_v2',
    'HLT_DoubleEle4_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle4_eta1p22_mMax6_v2',
    'HLT_DoubleEle4p5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle4p5_eta1p22_mMax6_v2',
    'HLT_DoubleEle5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle5_eta1p22_mMax6_v2',
    'HLT_DoubleEle5p5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle5p5_eta1p22_mMax6_v2',
    'HLT_DoubleEle6_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle6_eta1p22_mMax6_v2',
    'HLT_DoubleEle6p5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle6p5_eta1p22_mMax6_v2',
    'HLT_DoubleEle7_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle7_eta1p22_mMax6_v2',
    'HLT_DoubleEle7p5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle7p5_eta1p22_mMax6_v2',
    'HLT_DoubleEle8_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle8_eta1p22_mMax6_v2',
    'HLT_DoubleEle8p5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle8p5_eta1p22_mMax6_v2',
    'HLT_DoubleEle9_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle9_eta1p22_mMax6_v2',
    'HLT_DoubleEle9p5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle9p5_eta1p22_mMax6_v2',
    'HLT_SingleEle8_SingleEGL1_v1',
    'HLT_SingleEle8_v1'
)

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamParkingDoubleElectronLowMass1_datasetParkingDoubleElectronLowMass3_selector
streamParkingDoubleElectronLowMass1_datasetParkingDoubleElectronLowMass3_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamParkingDoubleElectronLowMass1_datasetParkingDoubleElectronLowMass3_selector.l1tResults = cms.InputTag('')
streamParkingDoubleElectronLowMass1_datasetParkingDoubleElectronLowMass3_selector.throw      = cms.bool(False)
streamParkingDoubleElectronLowMass1_datasetParkingDoubleElectronLowMass3_selector.triggerConditions = cms.vstring(
    'HLT_DoubleEle10_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle10_eta1p22_mMax6_v2',
    'HLT_DoubleEle4_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle4_eta1p22_mMax6_v2',
    'HLT_DoubleEle4p5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle4p5_eta1p22_mMax6_v2',
    'HLT_DoubleEle5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle5_eta1p22_mMax6_v2',
    'HLT_DoubleEle5p5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle5p5_eta1p22_mMax6_v2',
    'HLT_DoubleEle6_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle6_eta1p22_mMax6_v2',
    'HLT_DoubleEle6p5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle6p5_eta1p22_mMax6_v2',
    'HLT_DoubleEle7_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle7_eta1p22_mMax6_v2',
    'HLT_DoubleEle7p5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle7p5_eta1p22_mMax6_v2',
    'HLT_DoubleEle8_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle8_eta1p22_mMax6_v2',
    'HLT_DoubleEle8p5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle8p5_eta1p22_mMax6_v2',
    'HLT_DoubleEle9_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle9_eta1p22_mMax6_v2',
    'HLT_DoubleEle9p5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle9p5_eta1p22_mMax6_v2',
    'HLT_SingleEle8_SingleEGL1_v1',
    'HLT_SingleEle8_v1'
)


# stream ParkingDoubleElectronLowMass2

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamParkingDoubleElectronLowMass2_datasetParkingDoubleElectronLowMass4_selector
streamParkingDoubleElectronLowMass2_datasetParkingDoubleElectronLowMass4_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamParkingDoubleElectronLowMass2_datasetParkingDoubleElectronLowMass4_selector.l1tResults = cms.InputTag('')
streamParkingDoubleElectronLowMass2_datasetParkingDoubleElectronLowMass4_selector.throw      = cms.bool(False)
streamParkingDoubleElectronLowMass2_datasetParkingDoubleElectronLowMass4_selector.triggerConditions = cms.vstring(
    'HLT_DoubleEle10_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle10_eta1p22_mMax6_v2',
    'HLT_DoubleEle4_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle4_eta1p22_mMax6_v2',
    'HLT_DoubleEle4p5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle4p5_eta1p22_mMax6_v2',
    'HLT_DoubleEle5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle5_eta1p22_mMax6_v2',
    'HLT_DoubleEle5p5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle5p5_eta1p22_mMax6_v2',
    'HLT_DoubleEle6_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle6_eta1p22_mMax6_v2',
    'HLT_DoubleEle6p5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle6p5_eta1p22_mMax6_v2',
    'HLT_DoubleEle7_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle7_eta1p22_mMax6_v2',
    'HLT_DoubleEle7p5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle7p5_eta1p22_mMax6_v2',
    'HLT_DoubleEle8_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle8_eta1p22_mMax6_v2',
    'HLT_DoubleEle8p5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle8p5_eta1p22_mMax6_v2',
    'HLT_DoubleEle9_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle9_eta1p22_mMax6_v2',
    'HLT_DoubleEle9p5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle9p5_eta1p22_mMax6_v2',
    'HLT_SingleEle8_SingleEGL1_v1',
    'HLT_SingleEle8_v1'
)

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamParkingDoubleElectronLowMass2_datasetParkingDoubleElectronLowMass5_selector
streamParkingDoubleElectronLowMass2_datasetParkingDoubleElectronLowMass5_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamParkingDoubleElectronLowMass2_datasetParkingDoubleElectronLowMass5_selector.l1tResults = cms.InputTag('')
streamParkingDoubleElectronLowMass2_datasetParkingDoubleElectronLowMass5_selector.throw      = cms.bool(False)
streamParkingDoubleElectronLowMass2_datasetParkingDoubleElectronLowMass5_selector.triggerConditions = cms.vstring(
    'HLT_DoubleEle10_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle10_eta1p22_mMax6_v2',
    'HLT_DoubleEle4_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle4_eta1p22_mMax6_v2',
    'HLT_DoubleEle4p5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle4p5_eta1p22_mMax6_v2',
    'HLT_DoubleEle5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle5_eta1p22_mMax6_v2',
    'HLT_DoubleEle5p5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle5p5_eta1p22_mMax6_v2',
    'HLT_DoubleEle6_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle6_eta1p22_mMax6_v2',
    'HLT_DoubleEle6p5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle6p5_eta1p22_mMax6_v2',
    'HLT_DoubleEle7_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle7_eta1p22_mMax6_v2',
    'HLT_DoubleEle7p5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle7p5_eta1p22_mMax6_v2',
    'HLT_DoubleEle8_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle8_eta1p22_mMax6_v2',
    'HLT_DoubleEle8p5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle8p5_eta1p22_mMax6_v2',
    'HLT_DoubleEle9_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle9_eta1p22_mMax6_v2',
    'HLT_DoubleEle9p5_eta1p22_mMax6_dz0p8_v1',
    'HLT_DoubleEle9p5_eta1p22_mMax6_v2',
    'HLT_SingleEle8_SingleEGL1_v1',
    'HLT_SingleEle8_v1'
)


# stream ParkingDoubleMuonLowMass0

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamParkingDoubleMuonLowMass0_datasetParkingDoubleMuonLowMass0_selector
streamParkingDoubleMuonLowMass0_datasetParkingDoubleMuonLowMass0_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamParkingDoubleMuonLowMass0_datasetParkingDoubleMuonLowMass0_selector.l1tResults = cms.InputTag('')
streamParkingDoubleMuonLowMass0_datasetParkingDoubleMuonLowMass0_selector.throw      = cms.bool(False)
streamParkingDoubleMuonLowMass0_datasetParkingDoubleMuonLowMass0_selector.triggerConditions = cms.vstring(
    'HLT_Dimuon0_Jpsi3p5_Muon2_v7',
    'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v9',
    'HLT_Dimuon0_Jpsi_L1_NoOS_v9',
    'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v9',
    'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v9',
    'HLT_Dimuon0_Jpsi_NoVertexing_v10',
    'HLT_Dimuon0_Jpsi_v10',
    'HLT_Dimuon0_LowMass_L1_0er1p5R_v9',
    'HLT_Dimuon0_LowMass_L1_0er1p5_v10',
    'HLT_Dimuon0_LowMass_L1_4R_v9',
    'HLT_Dimuon0_LowMass_L1_4_v10',
    'HLT_Dimuon0_LowMass_L1_TM530_v8',
    'HLT_Dimuon0_LowMass_v10',
    'HLT_Dimuon0_Upsilon_L1_4p5NoOS_v10',
    'HLT_Dimuon0_Upsilon_L1_4p5_v11',
    'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v9',
    'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v11',
    'HLT_Dimuon0_Upsilon_L1_5M_v10',
    'HLT_Dimuon0_Upsilon_L1_5_v11',
    'HLT_Dimuon0_Upsilon_Muon_L1_TM0_v8',
    'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v8',
    'HLT_Dimuon0_Upsilon_NoVertexing_v9',
    'HLT_Dimuon10_PsiPrime_Barrel_Seagulls_v9',
    'HLT_Dimuon10_Upsilon_y1p4_v3',
    'HLT_Dimuon12_Upsilon_y1p4_v4',
    'HLT_Dimuon14_Phi_Barrel_Seagulls_v9',
    'HLT_Dimuon14_PsiPrime_noCorrL1_v7',
    'HLT_Dimuon14_PsiPrime_v15',
    'HLT_Dimuon18_PsiPrime_noCorrL1_v8',
    'HLT_Dimuon18_PsiPrime_v16',
    'HLT_Dimuon20_Jpsi_Barrel_Seagulls_v9',
    'HLT_Dimuon24_Phi_noCorrL1_v8',
    'HLT_Dimuon24_Upsilon_noCorrL1_v8',
    'HLT_Dimuon25_Jpsi_noCorrL1_v8',
    'HLT_Dimuon25_Jpsi_v16',
    'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v8',
    'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v6',
    'HLT_DoubleMu3_TkMu_DsTau3Mu_v6',
    'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v8',
    'HLT_DoubleMu3_Trk_Tau3mu_v14',
    'HLT_DoubleMu4_3_Bs_v17',
    'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v2',
    'HLT_DoubleMu4_3_Jpsi_v17',
    'HLT_DoubleMu4_3_LowMass_v3',
    'HLT_DoubleMu4_3_Photon4_BsToMMG_v2',
    'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v9',
    'HLT_DoubleMu4_JpsiTrk_Bc_v2',
    'HLT_DoubleMu4_Jpsi_Displaced_v9',
    'HLT_DoubleMu4_Jpsi_NoVertexing_v9',
    'HLT_DoubleMu4_LowMass_Displaced_v3',
    'HLT_DoubleMu4_MuMuTrk_Displaced_v17',
    'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v6',
    'HLT_Mu20_TkMu0_Phi_v10',
    'HLT_Mu25_TkMu0_Onia_v10',
    'HLT_Mu25_TkMu0_Phi_v10',
    'HLT_Mu30_TkMu0_Psi_v3',
    'HLT_Mu30_TkMu0_Upsilon_v3',
    'HLT_Mu4_L1DoubleMu_v3',
    'HLT_Mu7p5_L2Mu2_Jpsi_v12',
    'HLT_Mu7p5_L2Mu2_Upsilon_v12',
    'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v6',
    'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v6',
    'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v6',
    'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v6',
    'HLT_Trimuon5_3p5_2_Upsilon_Muon_v7',
    'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v5'
)

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamParkingDoubleMuonLowMass0_datasetParkingDoubleMuonLowMass1_selector
streamParkingDoubleMuonLowMass0_datasetParkingDoubleMuonLowMass1_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamParkingDoubleMuonLowMass0_datasetParkingDoubleMuonLowMass1_selector.l1tResults = cms.InputTag('')
streamParkingDoubleMuonLowMass0_datasetParkingDoubleMuonLowMass1_selector.throw      = cms.bool(False)
streamParkingDoubleMuonLowMass0_datasetParkingDoubleMuonLowMass1_selector.triggerConditions = cms.vstring(
    'HLT_Dimuon0_Jpsi3p5_Muon2_v7',
    'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v9',
    'HLT_Dimuon0_Jpsi_L1_NoOS_v9',
    'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v9',
    'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v9',
    'HLT_Dimuon0_Jpsi_NoVertexing_v10',
    'HLT_Dimuon0_Jpsi_v10',
    'HLT_Dimuon0_LowMass_L1_0er1p5R_v9',
    'HLT_Dimuon0_LowMass_L1_0er1p5_v10',
    'HLT_Dimuon0_LowMass_L1_4R_v9',
    'HLT_Dimuon0_LowMass_L1_4_v10',
    'HLT_Dimuon0_LowMass_L1_TM530_v8',
    'HLT_Dimuon0_LowMass_v10',
    'HLT_Dimuon0_Upsilon_L1_4p5NoOS_v10',
    'HLT_Dimuon0_Upsilon_L1_4p5_v11',
    'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v9',
    'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v11',
    'HLT_Dimuon0_Upsilon_L1_5M_v10',
    'HLT_Dimuon0_Upsilon_L1_5_v11',
    'HLT_Dimuon0_Upsilon_Muon_L1_TM0_v8',
    'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v8',
    'HLT_Dimuon0_Upsilon_NoVertexing_v9',
    'HLT_Dimuon10_PsiPrime_Barrel_Seagulls_v9',
    'HLT_Dimuon10_Upsilon_y1p4_v3',
    'HLT_Dimuon12_Upsilon_y1p4_v4',
    'HLT_Dimuon14_Phi_Barrel_Seagulls_v9',
    'HLT_Dimuon14_PsiPrime_noCorrL1_v7',
    'HLT_Dimuon14_PsiPrime_v15',
    'HLT_Dimuon18_PsiPrime_noCorrL1_v8',
    'HLT_Dimuon18_PsiPrime_v16',
    'HLT_Dimuon20_Jpsi_Barrel_Seagulls_v9',
    'HLT_Dimuon24_Phi_noCorrL1_v8',
    'HLT_Dimuon24_Upsilon_noCorrL1_v8',
    'HLT_Dimuon25_Jpsi_noCorrL1_v8',
    'HLT_Dimuon25_Jpsi_v16',
    'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v8',
    'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v6',
    'HLT_DoubleMu3_TkMu_DsTau3Mu_v6',
    'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v8',
    'HLT_DoubleMu3_Trk_Tau3mu_v14',
    'HLT_DoubleMu4_3_Bs_v17',
    'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v2',
    'HLT_DoubleMu4_3_Jpsi_v17',
    'HLT_DoubleMu4_3_LowMass_v3',
    'HLT_DoubleMu4_3_Photon4_BsToMMG_v2',
    'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v9',
    'HLT_DoubleMu4_JpsiTrk_Bc_v2',
    'HLT_DoubleMu4_Jpsi_Displaced_v9',
    'HLT_DoubleMu4_Jpsi_NoVertexing_v9',
    'HLT_DoubleMu4_LowMass_Displaced_v3',
    'HLT_DoubleMu4_MuMuTrk_Displaced_v17',
    'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v6',
    'HLT_Mu20_TkMu0_Phi_v10',
    'HLT_Mu25_TkMu0_Onia_v10',
    'HLT_Mu25_TkMu0_Phi_v10',
    'HLT_Mu30_TkMu0_Psi_v3',
    'HLT_Mu30_TkMu0_Upsilon_v3',
    'HLT_Mu4_L1DoubleMu_v3',
    'HLT_Mu7p5_L2Mu2_Jpsi_v12',
    'HLT_Mu7p5_L2Mu2_Upsilon_v12',
    'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v6',
    'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v6',
    'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v6',
    'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v6',
    'HLT_Trimuon5_3p5_2_Upsilon_Muon_v7',
    'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v5'
)


# stream ParkingDoubleMuonLowMass1

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamParkingDoubleMuonLowMass1_datasetParkingDoubleMuonLowMass2_selector
streamParkingDoubleMuonLowMass1_datasetParkingDoubleMuonLowMass2_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamParkingDoubleMuonLowMass1_datasetParkingDoubleMuonLowMass2_selector.l1tResults = cms.InputTag('')
streamParkingDoubleMuonLowMass1_datasetParkingDoubleMuonLowMass2_selector.throw      = cms.bool(False)
streamParkingDoubleMuonLowMass1_datasetParkingDoubleMuonLowMass2_selector.triggerConditions = cms.vstring(
    'HLT_Dimuon0_Jpsi3p5_Muon2_v7',
    'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v9',
    'HLT_Dimuon0_Jpsi_L1_NoOS_v9',
    'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v9',
    'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v9',
    'HLT_Dimuon0_Jpsi_NoVertexing_v10',
    'HLT_Dimuon0_Jpsi_v10',
    'HLT_Dimuon0_LowMass_L1_0er1p5R_v9',
    'HLT_Dimuon0_LowMass_L1_0er1p5_v10',
    'HLT_Dimuon0_LowMass_L1_4R_v9',
    'HLT_Dimuon0_LowMass_L1_4_v10',
    'HLT_Dimuon0_LowMass_L1_TM530_v8',
    'HLT_Dimuon0_LowMass_v10',
    'HLT_Dimuon0_Upsilon_L1_4p5NoOS_v10',
    'HLT_Dimuon0_Upsilon_L1_4p5_v11',
    'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v9',
    'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v11',
    'HLT_Dimuon0_Upsilon_L1_5M_v10',
    'HLT_Dimuon0_Upsilon_L1_5_v11',
    'HLT_Dimuon0_Upsilon_Muon_L1_TM0_v8',
    'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v8',
    'HLT_Dimuon0_Upsilon_NoVertexing_v9',
    'HLT_Dimuon10_PsiPrime_Barrel_Seagulls_v9',
    'HLT_Dimuon10_Upsilon_y1p4_v3',
    'HLT_Dimuon12_Upsilon_y1p4_v4',
    'HLT_Dimuon14_Phi_Barrel_Seagulls_v9',
    'HLT_Dimuon14_PsiPrime_noCorrL1_v7',
    'HLT_Dimuon14_PsiPrime_v15',
    'HLT_Dimuon18_PsiPrime_noCorrL1_v8',
    'HLT_Dimuon18_PsiPrime_v16',
    'HLT_Dimuon20_Jpsi_Barrel_Seagulls_v9',
    'HLT_Dimuon24_Phi_noCorrL1_v8',
    'HLT_Dimuon24_Upsilon_noCorrL1_v8',
    'HLT_Dimuon25_Jpsi_noCorrL1_v8',
    'HLT_Dimuon25_Jpsi_v16',
    'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v8',
    'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v6',
    'HLT_DoubleMu3_TkMu_DsTau3Mu_v6',
    'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v8',
    'HLT_DoubleMu3_Trk_Tau3mu_v14',
    'HLT_DoubleMu4_3_Bs_v17',
    'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v2',
    'HLT_DoubleMu4_3_Jpsi_v17',
    'HLT_DoubleMu4_3_LowMass_v3',
    'HLT_DoubleMu4_3_Photon4_BsToMMG_v2',
    'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v9',
    'HLT_DoubleMu4_JpsiTrk_Bc_v2',
    'HLT_DoubleMu4_Jpsi_Displaced_v9',
    'HLT_DoubleMu4_Jpsi_NoVertexing_v9',
    'HLT_DoubleMu4_LowMass_Displaced_v3',
    'HLT_DoubleMu4_MuMuTrk_Displaced_v17',
    'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v6',
    'HLT_Mu20_TkMu0_Phi_v10',
    'HLT_Mu25_TkMu0_Onia_v10',
    'HLT_Mu25_TkMu0_Phi_v10',
    'HLT_Mu30_TkMu0_Psi_v3',
    'HLT_Mu30_TkMu0_Upsilon_v3',
    'HLT_Mu4_L1DoubleMu_v3',
    'HLT_Mu7p5_L2Mu2_Jpsi_v12',
    'HLT_Mu7p5_L2Mu2_Upsilon_v12',
    'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v6',
    'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v6',
    'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v6',
    'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v6',
    'HLT_Trimuon5_3p5_2_Upsilon_Muon_v7',
    'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v5'
)

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamParkingDoubleMuonLowMass1_datasetParkingDoubleMuonLowMass3_selector
streamParkingDoubleMuonLowMass1_datasetParkingDoubleMuonLowMass3_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamParkingDoubleMuonLowMass1_datasetParkingDoubleMuonLowMass3_selector.l1tResults = cms.InputTag('')
streamParkingDoubleMuonLowMass1_datasetParkingDoubleMuonLowMass3_selector.throw      = cms.bool(False)
streamParkingDoubleMuonLowMass1_datasetParkingDoubleMuonLowMass3_selector.triggerConditions = cms.vstring(
    'HLT_Dimuon0_Jpsi3p5_Muon2_v7',
    'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v9',
    'HLT_Dimuon0_Jpsi_L1_NoOS_v9',
    'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v9',
    'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v9',
    'HLT_Dimuon0_Jpsi_NoVertexing_v10',
    'HLT_Dimuon0_Jpsi_v10',
    'HLT_Dimuon0_LowMass_L1_0er1p5R_v9',
    'HLT_Dimuon0_LowMass_L1_0er1p5_v10',
    'HLT_Dimuon0_LowMass_L1_4R_v9',
    'HLT_Dimuon0_LowMass_L1_4_v10',
    'HLT_Dimuon0_LowMass_L1_TM530_v8',
    'HLT_Dimuon0_LowMass_v10',
    'HLT_Dimuon0_Upsilon_L1_4p5NoOS_v10',
    'HLT_Dimuon0_Upsilon_L1_4p5_v11',
    'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v9',
    'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v11',
    'HLT_Dimuon0_Upsilon_L1_5M_v10',
    'HLT_Dimuon0_Upsilon_L1_5_v11',
    'HLT_Dimuon0_Upsilon_Muon_L1_TM0_v8',
    'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v8',
    'HLT_Dimuon0_Upsilon_NoVertexing_v9',
    'HLT_Dimuon10_PsiPrime_Barrel_Seagulls_v9',
    'HLT_Dimuon10_Upsilon_y1p4_v3',
    'HLT_Dimuon12_Upsilon_y1p4_v4',
    'HLT_Dimuon14_Phi_Barrel_Seagulls_v9',
    'HLT_Dimuon14_PsiPrime_noCorrL1_v7',
    'HLT_Dimuon14_PsiPrime_v15',
    'HLT_Dimuon18_PsiPrime_noCorrL1_v8',
    'HLT_Dimuon18_PsiPrime_v16',
    'HLT_Dimuon20_Jpsi_Barrel_Seagulls_v9',
    'HLT_Dimuon24_Phi_noCorrL1_v8',
    'HLT_Dimuon24_Upsilon_noCorrL1_v8',
    'HLT_Dimuon25_Jpsi_noCorrL1_v8',
    'HLT_Dimuon25_Jpsi_v16',
    'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v8',
    'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v6',
    'HLT_DoubleMu3_TkMu_DsTau3Mu_v6',
    'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v8',
    'HLT_DoubleMu3_Trk_Tau3mu_v14',
    'HLT_DoubleMu4_3_Bs_v17',
    'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v2',
    'HLT_DoubleMu4_3_Jpsi_v17',
    'HLT_DoubleMu4_3_LowMass_v3',
    'HLT_DoubleMu4_3_Photon4_BsToMMG_v2',
    'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v9',
    'HLT_DoubleMu4_JpsiTrk_Bc_v2',
    'HLT_DoubleMu4_Jpsi_Displaced_v9',
    'HLT_DoubleMu4_Jpsi_NoVertexing_v9',
    'HLT_DoubleMu4_LowMass_Displaced_v3',
    'HLT_DoubleMu4_MuMuTrk_Displaced_v17',
    'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v6',
    'HLT_Mu20_TkMu0_Phi_v10',
    'HLT_Mu25_TkMu0_Onia_v10',
    'HLT_Mu25_TkMu0_Phi_v10',
    'HLT_Mu30_TkMu0_Psi_v3',
    'HLT_Mu30_TkMu0_Upsilon_v3',
    'HLT_Mu4_L1DoubleMu_v3',
    'HLT_Mu7p5_L2Mu2_Jpsi_v12',
    'HLT_Mu7p5_L2Mu2_Upsilon_v12',
    'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v6',
    'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v6',
    'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v6',
    'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v6',
    'HLT_Trimuon5_3p5_2_Upsilon_Muon_v7',
    'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v5'
)


# stream ParkingDoubleMuonLowMass2

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamParkingDoubleMuonLowMass2_datasetParkingDoubleMuonLowMass4_selector
streamParkingDoubleMuonLowMass2_datasetParkingDoubleMuonLowMass4_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamParkingDoubleMuonLowMass2_datasetParkingDoubleMuonLowMass4_selector.l1tResults = cms.InputTag('')
streamParkingDoubleMuonLowMass2_datasetParkingDoubleMuonLowMass4_selector.throw      = cms.bool(False)
streamParkingDoubleMuonLowMass2_datasetParkingDoubleMuonLowMass4_selector.triggerConditions = cms.vstring(
    'HLT_Dimuon0_Jpsi3p5_Muon2_v7',
    'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v9',
    'HLT_Dimuon0_Jpsi_L1_NoOS_v9',
    'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v9',
    'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v9',
    'HLT_Dimuon0_Jpsi_NoVertexing_v10',
    'HLT_Dimuon0_Jpsi_v10',
    'HLT_Dimuon0_LowMass_L1_0er1p5R_v9',
    'HLT_Dimuon0_LowMass_L1_0er1p5_v10',
    'HLT_Dimuon0_LowMass_L1_4R_v9',
    'HLT_Dimuon0_LowMass_L1_4_v10',
    'HLT_Dimuon0_LowMass_L1_TM530_v8',
    'HLT_Dimuon0_LowMass_v10',
    'HLT_Dimuon0_Upsilon_L1_4p5NoOS_v10',
    'HLT_Dimuon0_Upsilon_L1_4p5_v11',
    'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v9',
    'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v11',
    'HLT_Dimuon0_Upsilon_L1_5M_v10',
    'HLT_Dimuon0_Upsilon_L1_5_v11',
    'HLT_Dimuon0_Upsilon_Muon_L1_TM0_v8',
    'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v8',
    'HLT_Dimuon0_Upsilon_NoVertexing_v9',
    'HLT_Dimuon10_PsiPrime_Barrel_Seagulls_v9',
    'HLT_Dimuon10_Upsilon_y1p4_v3',
    'HLT_Dimuon12_Upsilon_y1p4_v4',
    'HLT_Dimuon14_Phi_Barrel_Seagulls_v9',
    'HLT_Dimuon14_PsiPrime_noCorrL1_v7',
    'HLT_Dimuon14_PsiPrime_v15',
    'HLT_Dimuon18_PsiPrime_noCorrL1_v8',
    'HLT_Dimuon18_PsiPrime_v16',
    'HLT_Dimuon20_Jpsi_Barrel_Seagulls_v9',
    'HLT_Dimuon24_Phi_noCorrL1_v8',
    'HLT_Dimuon24_Upsilon_noCorrL1_v8',
    'HLT_Dimuon25_Jpsi_noCorrL1_v8',
    'HLT_Dimuon25_Jpsi_v16',
    'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v8',
    'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v6',
    'HLT_DoubleMu3_TkMu_DsTau3Mu_v6',
    'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v8',
    'HLT_DoubleMu3_Trk_Tau3mu_v14',
    'HLT_DoubleMu4_3_Bs_v17',
    'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v2',
    'HLT_DoubleMu4_3_Jpsi_v17',
    'HLT_DoubleMu4_3_LowMass_v3',
    'HLT_DoubleMu4_3_Photon4_BsToMMG_v2',
    'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v9',
    'HLT_DoubleMu4_JpsiTrk_Bc_v2',
    'HLT_DoubleMu4_Jpsi_Displaced_v9',
    'HLT_DoubleMu4_Jpsi_NoVertexing_v9',
    'HLT_DoubleMu4_LowMass_Displaced_v3',
    'HLT_DoubleMu4_MuMuTrk_Displaced_v17',
    'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v6',
    'HLT_Mu20_TkMu0_Phi_v10',
    'HLT_Mu25_TkMu0_Onia_v10',
    'HLT_Mu25_TkMu0_Phi_v10',
    'HLT_Mu30_TkMu0_Psi_v3',
    'HLT_Mu30_TkMu0_Upsilon_v3',
    'HLT_Mu4_L1DoubleMu_v3',
    'HLT_Mu7p5_L2Mu2_Jpsi_v12',
    'HLT_Mu7p5_L2Mu2_Upsilon_v12',
    'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v6',
    'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v6',
    'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v6',
    'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v6',
    'HLT_Trimuon5_3p5_2_Upsilon_Muon_v7',
    'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v5'
)

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamParkingDoubleMuonLowMass2_datasetParkingDoubleMuonLowMass5_selector
streamParkingDoubleMuonLowMass2_datasetParkingDoubleMuonLowMass5_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamParkingDoubleMuonLowMass2_datasetParkingDoubleMuonLowMass5_selector.l1tResults = cms.InputTag('')
streamParkingDoubleMuonLowMass2_datasetParkingDoubleMuonLowMass5_selector.throw      = cms.bool(False)
streamParkingDoubleMuonLowMass2_datasetParkingDoubleMuonLowMass5_selector.triggerConditions = cms.vstring(
    'HLT_Dimuon0_Jpsi3p5_Muon2_v7',
    'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v9',
    'HLT_Dimuon0_Jpsi_L1_NoOS_v9',
    'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v9',
    'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v9',
    'HLT_Dimuon0_Jpsi_NoVertexing_v10',
    'HLT_Dimuon0_Jpsi_v10',
    'HLT_Dimuon0_LowMass_L1_0er1p5R_v9',
    'HLT_Dimuon0_LowMass_L1_0er1p5_v10',
    'HLT_Dimuon0_LowMass_L1_4R_v9',
    'HLT_Dimuon0_LowMass_L1_4_v10',
    'HLT_Dimuon0_LowMass_L1_TM530_v8',
    'HLT_Dimuon0_LowMass_v10',
    'HLT_Dimuon0_Upsilon_L1_4p5NoOS_v10',
    'HLT_Dimuon0_Upsilon_L1_4p5_v11',
    'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v9',
    'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v11',
    'HLT_Dimuon0_Upsilon_L1_5M_v10',
    'HLT_Dimuon0_Upsilon_L1_5_v11',
    'HLT_Dimuon0_Upsilon_Muon_L1_TM0_v8',
    'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v8',
    'HLT_Dimuon0_Upsilon_NoVertexing_v9',
    'HLT_Dimuon10_PsiPrime_Barrel_Seagulls_v9',
    'HLT_Dimuon10_Upsilon_y1p4_v3',
    'HLT_Dimuon12_Upsilon_y1p4_v4',
    'HLT_Dimuon14_Phi_Barrel_Seagulls_v9',
    'HLT_Dimuon14_PsiPrime_noCorrL1_v7',
    'HLT_Dimuon14_PsiPrime_v15',
    'HLT_Dimuon18_PsiPrime_noCorrL1_v8',
    'HLT_Dimuon18_PsiPrime_v16',
    'HLT_Dimuon20_Jpsi_Barrel_Seagulls_v9',
    'HLT_Dimuon24_Phi_noCorrL1_v8',
    'HLT_Dimuon24_Upsilon_noCorrL1_v8',
    'HLT_Dimuon25_Jpsi_noCorrL1_v8',
    'HLT_Dimuon25_Jpsi_v16',
    'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v8',
    'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v6',
    'HLT_DoubleMu3_TkMu_DsTau3Mu_v6',
    'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v8',
    'HLT_DoubleMu3_Trk_Tau3mu_v14',
    'HLT_DoubleMu4_3_Bs_v17',
    'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v2',
    'HLT_DoubleMu4_3_Jpsi_v17',
    'HLT_DoubleMu4_3_LowMass_v3',
    'HLT_DoubleMu4_3_Photon4_BsToMMG_v2',
    'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v9',
    'HLT_DoubleMu4_JpsiTrk_Bc_v2',
    'HLT_DoubleMu4_Jpsi_Displaced_v9',
    'HLT_DoubleMu4_Jpsi_NoVertexing_v9',
    'HLT_DoubleMu4_LowMass_Displaced_v3',
    'HLT_DoubleMu4_MuMuTrk_Displaced_v17',
    'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v6',
    'HLT_Mu20_TkMu0_Phi_v10',
    'HLT_Mu25_TkMu0_Onia_v10',
    'HLT_Mu25_TkMu0_Phi_v10',
    'HLT_Mu30_TkMu0_Psi_v3',
    'HLT_Mu30_TkMu0_Upsilon_v3',
    'HLT_Mu4_L1DoubleMu_v3',
    'HLT_Mu7p5_L2Mu2_Jpsi_v12',
    'HLT_Mu7p5_L2Mu2_Upsilon_v12',
    'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v6',
    'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v6',
    'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v6',
    'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v6',
    'HLT_Trimuon5_3p5_2_Upsilon_Muon_v7',
    'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v5'
)


# stream ParkingDoubleMuonLowMass3

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamParkingDoubleMuonLowMass3_datasetParkingDoubleMuonLowMass6_selector
streamParkingDoubleMuonLowMass3_datasetParkingDoubleMuonLowMass6_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamParkingDoubleMuonLowMass3_datasetParkingDoubleMuonLowMass6_selector.l1tResults = cms.InputTag('')
streamParkingDoubleMuonLowMass3_datasetParkingDoubleMuonLowMass6_selector.throw      = cms.bool(False)
streamParkingDoubleMuonLowMass3_datasetParkingDoubleMuonLowMass6_selector.triggerConditions = cms.vstring(
    'HLT_Dimuon0_Jpsi3p5_Muon2_v7',
    'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v9',
    'HLT_Dimuon0_Jpsi_L1_NoOS_v9',
    'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v9',
    'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v9',
    'HLT_Dimuon0_Jpsi_NoVertexing_v10',
    'HLT_Dimuon0_Jpsi_v10',
    'HLT_Dimuon0_LowMass_L1_0er1p5R_v9',
    'HLT_Dimuon0_LowMass_L1_0er1p5_v10',
    'HLT_Dimuon0_LowMass_L1_4R_v9',
    'HLT_Dimuon0_LowMass_L1_4_v10',
    'HLT_Dimuon0_LowMass_L1_TM530_v8',
    'HLT_Dimuon0_LowMass_v10',
    'HLT_Dimuon0_Upsilon_L1_4p5NoOS_v10',
    'HLT_Dimuon0_Upsilon_L1_4p5_v11',
    'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v9',
    'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v11',
    'HLT_Dimuon0_Upsilon_L1_5M_v10',
    'HLT_Dimuon0_Upsilon_L1_5_v11',
    'HLT_Dimuon0_Upsilon_Muon_L1_TM0_v8',
    'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v8',
    'HLT_Dimuon0_Upsilon_NoVertexing_v9',
    'HLT_Dimuon10_PsiPrime_Barrel_Seagulls_v9',
    'HLT_Dimuon10_Upsilon_y1p4_v3',
    'HLT_Dimuon12_Upsilon_y1p4_v4',
    'HLT_Dimuon14_Phi_Barrel_Seagulls_v9',
    'HLT_Dimuon14_PsiPrime_noCorrL1_v7',
    'HLT_Dimuon14_PsiPrime_v15',
    'HLT_Dimuon18_PsiPrime_noCorrL1_v8',
    'HLT_Dimuon18_PsiPrime_v16',
    'HLT_Dimuon20_Jpsi_Barrel_Seagulls_v9',
    'HLT_Dimuon24_Phi_noCorrL1_v8',
    'HLT_Dimuon24_Upsilon_noCorrL1_v8',
    'HLT_Dimuon25_Jpsi_noCorrL1_v8',
    'HLT_Dimuon25_Jpsi_v16',
    'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v8',
    'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v6',
    'HLT_DoubleMu3_TkMu_DsTau3Mu_v6',
    'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v8',
    'HLT_DoubleMu3_Trk_Tau3mu_v14',
    'HLT_DoubleMu4_3_Bs_v17',
    'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v2',
    'HLT_DoubleMu4_3_Jpsi_v17',
    'HLT_DoubleMu4_3_LowMass_v3',
    'HLT_DoubleMu4_3_Photon4_BsToMMG_v2',
    'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v9',
    'HLT_DoubleMu4_JpsiTrk_Bc_v2',
    'HLT_DoubleMu4_Jpsi_Displaced_v9',
    'HLT_DoubleMu4_Jpsi_NoVertexing_v9',
    'HLT_DoubleMu4_LowMass_Displaced_v3',
    'HLT_DoubleMu4_MuMuTrk_Displaced_v17',
    'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v6',
    'HLT_Mu20_TkMu0_Phi_v10',
    'HLT_Mu25_TkMu0_Onia_v10',
    'HLT_Mu25_TkMu0_Phi_v10',
    'HLT_Mu30_TkMu0_Psi_v3',
    'HLT_Mu30_TkMu0_Upsilon_v3',
    'HLT_Mu4_L1DoubleMu_v3',
    'HLT_Mu7p5_L2Mu2_Jpsi_v12',
    'HLT_Mu7p5_L2Mu2_Upsilon_v12',
    'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v6',
    'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v6',
    'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v6',
    'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v6',
    'HLT_Trimuon5_3p5_2_Upsilon_Muon_v7',
    'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v5'
)

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamParkingDoubleMuonLowMass3_datasetParkingDoubleMuonLowMass7_selector
streamParkingDoubleMuonLowMass3_datasetParkingDoubleMuonLowMass7_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamParkingDoubleMuonLowMass3_datasetParkingDoubleMuonLowMass7_selector.l1tResults = cms.InputTag('')
streamParkingDoubleMuonLowMass3_datasetParkingDoubleMuonLowMass7_selector.throw      = cms.bool(False)
streamParkingDoubleMuonLowMass3_datasetParkingDoubleMuonLowMass7_selector.triggerConditions = cms.vstring(
    'HLT_Dimuon0_Jpsi3p5_Muon2_v7',
    'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v9',
    'HLT_Dimuon0_Jpsi_L1_NoOS_v9',
    'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v9',
    'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v9',
    'HLT_Dimuon0_Jpsi_NoVertexing_v10',
    'HLT_Dimuon0_Jpsi_v10',
    'HLT_Dimuon0_LowMass_L1_0er1p5R_v9',
    'HLT_Dimuon0_LowMass_L1_0er1p5_v10',
    'HLT_Dimuon0_LowMass_L1_4R_v9',
    'HLT_Dimuon0_LowMass_L1_4_v10',
    'HLT_Dimuon0_LowMass_L1_TM530_v8',
    'HLT_Dimuon0_LowMass_v10',
    'HLT_Dimuon0_Upsilon_L1_4p5NoOS_v10',
    'HLT_Dimuon0_Upsilon_L1_4p5_v11',
    'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v9',
    'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v11',
    'HLT_Dimuon0_Upsilon_L1_5M_v10',
    'HLT_Dimuon0_Upsilon_L1_5_v11',
    'HLT_Dimuon0_Upsilon_Muon_L1_TM0_v8',
    'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v8',
    'HLT_Dimuon0_Upsilon_NoVertexing_v9',
    'HLT_Dimuon10_PsiPrime_Barrel_Seagulls_v9',
    'HLT_Dimuon10_Upsilon_y1p4_v3',
    'HLT_Dimuon12_Upsilon_y1p4_v4',
    'HLT_Dimuon14_Phi_Barrel_Seagulls_v9',
    'HLT_Dimuon14_PsiPrime_noCorrL1_v7',
    'HLT_Dimuon14_PsiPrime_v15',
    'HLT_Dimuon18_PsiPrime_noCorrL1_v8',
    'HLT_Dimuon18_PsiPrime_v16',
    'HLT_Dimuon20_Jpsi_Barrel_Seagulls_v9',
    'HLT_Dimuon24_Phi_noCorrL1_v8',
    'HLT_Dimuon24_Upsilon_noCorrL1_v8',
    'HLT_Dimuon25_Jpsi_noCorrL1_v8',
    'HLT_Dimuon25_Jpsi_v16',
    'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v8',
    'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v6',
    'HLT_DoubleMu3_TkMu_DsTau3Mu_v6',
    'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v8',
    'HLT_DoubleMu3_Trk_Tau3mu_v14',
    'HLT_DoubleMu4_3_Bs_v17',
    'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v2',
    'HLT_DoubleMu4_3_Jpsi_v17',
    'HLT_DoubleMu4_3_LowMass_v3',
    'HLT_DoubleMu4_3_Photon4_BsToMMG_v2',
    'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v9',
    'HLT_DoubleMu4_JpsiTrk_Bc_v2',
    'HLT_DoubleMu4_Jpsi_Displaced_v9',
    'HLT_DoubleMu4_Jpsi_NoVertexing_v9',
    'HLT_DoubleMu4_LowMass_Displaced_v3',
    'HLT_DoubleMu4_MuMuTrk_Displaced_v17',
    'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v6',
    'HLT_Mu20_TkMu0_Phi_v10',
    'HLT_Mu25_TkMu0_Onia_v10',
    'HLT_Mu25_TkMu0_Phi_v10',
    'HLT_Mu30_TkMu0_Psi_v3',
    'HLT_Mu30_TkMu0_Upsilon_v3',
    'HLT_Mu4_L1DoubleMu_v3',
    'HLT_Mu7p5_L2Mu2_Jpsi_v12',
    'HLT_Mu7p5_L2Mu2_Upsilon_v12',
    'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v6',
    'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v6',
    'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v6',
    'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v6',
    'HLT_Trimuon5_3p5_2_Upsilon_Muon_v7',
    'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v5'
)


# stream ParkingSingleMuon0

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamParkingSingleMuon0_datasetParkingSingleMuon0_selector
streamParkingSingleMuon0_datasetParkingSingleMuon0_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamParkingSingleMuon0_datasetParkingSingleMuon0_selector.l1tResults = cms.InputTag('')
streamParkingSingleMuon0_datasetParkingSingleMuon0_selector.throw      = cms.bool(False)
streamParkingSingleMuon0_datasetParkingSingleMuon0_selector.triggerConditions = cms.vstring('HLT_Mu12_IP6_v2')


# stream ParkingSingleMuon1

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamParkingSingleMuon1_datasetParkingSingleMuon1_selector
streamParkingSingleMuon1_datasetParkingSingleMuon1_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamParkingSingleMuon1_datasetParkingSingleMuon1_selector.l1tResults = cms.InputTag('')
streamParkingSingleMuon1_datasetParkingSingleMuon1_selector.throw      = cms.bool(False)
streamParkingSingleMuon1_datasetParkingSingleMuon1_selector.triggerConditions = cms.vstring('HLT_Mu12_IP6_v2')


# stream ParkingSingleMuon2

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamParkingSingleMuon2_datasetParkingSingleMuon2_selector
streamParkingSingleMuon2_datasetParkingSingleMuon2_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamParkingSingleMuon2_datasetParkingSingleMuon2_selector.l1tResults = cms.InputTag('')
streamParkingSingleMuon2_datasetParkingSingleMuon2_selector.throw      = cms.bool(False)
streamParkingSingleMuon2_datasetParkingSingleMuon2_selector.triggerConditions = cms.vstring('HLT_Mu12_IP6_v2')


# stream PhysicsCommissioning

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamPhysicsCommissioning_datasetCommissioning_selector
streamPhysicsCommissioning_datasetCommissioning_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamPhysicsCommissioning_datasetCommissioning_selector.l1tResults = cms.InputTag('')
streamPhysicsCommissioning_datasetCommissioning_selector.throw      = cms.bool(False)
streamPhysicsCommissioning_datasetCommissioning_selector.triggerConditions = cms.vstring(
    'HLT_IsoTrackHB_v6',
    'HLT_IsoTrackHE_v6',
    'HLT_L1_CDC_SingleMu_3_er1p2_TOP120_DPHI2p618_3p142_v3',
    'HLT_PFJet40_GPUvsCPU_v1'
)

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamPhysicsCommissioning_datasetCosmics_selector
streamPhysicsCommissioning_datasetCosmics_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamPhysicsCommissioning_datasetCosmics_selector.l1tResults = cms.InputTag('')
streamPhysicsCommissioning_datasetCosmics_selector.throw      = cms.bool(False)
streamPhysicsCommissioning_datasetCosmics_selector.triggerConditions = cms.vstring('HLT_L1SingleMuCosmics_v2')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamPhysicsCommissioning_datasetEmptyBX_selector
streamPhysicsCommissioning_datasetEmptyBX_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamPhysicsCommissioning_datasetEmptyBX_selector.l1tResults = cms.InputTag('')
streamPhysicsCommissioning_datasetEmptyBX_selector.throw      = cms.bool(False)
streamPhysicsCommissioning_datasetEmptyBX_selector.triggerConditions = cms.vstring(
    'HLT_L1NotBptxOR_v4',
    'HLT_L1UnpairedBunchBptxMinus_v3',
    'HLT_L1UnpairedBunchBptxPlus_v3'
)

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamPhysicsCommissioning_datasetHLTPhysics_selector
streamPhysicsCommissioning_datasetHLTPhysics_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamPhysicsCommissioning_datasetHLTPhysics_selector.l1tResults = cms.InputTag('')
streamPhysicsCommissioning_datasetHLTPhysics_selector.throw      = cms.bool(False)
streamPhysicsCommissioning_datasetHLTPhysics_selector.triggerConditions = cms.vstring('HLT_Physics_v8')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamPhysicsCommissioning_datasetHcalNZS_selector
streamPhysicsCommissioning_datasetHcalNZS_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamPhysicsCommissioning_datasetHcalNZS_selector.l1tResults = cms.InputTag('')
streamPhysicsCommissioning_datasetHcalNZS_selector.throw      = cms.bool(False)
streamPhysicsCommissioning_datasetHcalNZS_selector.triggerConditions = cms.vstring(
    'HLT_HcalNZS_v14',
    'HLT_HcalPhiSym_v16'
)

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamPhysicsCommissioning_datasetIsolatedBunch_selector
streamPhysicsCommissioning_datasetIsolatedBunch_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamPhysicsCommissioning_datasetIsolatedBunch_selector.l1tResults = cms.InputTag('')
streamPhysicsCommissioning_datasetIsolatedBunch_selector.throw      = cms.bool(False)
streamPhysicsCommissioning_datasetIsolatedBunch_selector.triggerConditions = cms.vstring('HLT_HcalIsolatedbunch_v6')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamPhysicsCommissioning_datasetMonteCarlo_selector
streamPhysicsCommissioning_datasetMonteCarlo_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamPhysicsCommissioning_datasetMonteCarlo_selector.l1tResults = cms.InputTag('')
streamPhysicsCommissioning_datasetMonteCarlo_selector.throw      = cms.bool(False)
streamPhysicsCommissioning_datasetMonteCarlo_selector.triggerConditions = cms.vstring(
    'MC_AK4CaloJetsFromPV_v10',
    'MC_AK4CaloJets_v11',
    'MC_AK4PFJets_v19',
    'MC_AK8CaloHT_v10',
    'MC_AK8PFHT_v18',
    'MC_AK8PFJets_v19',
    'MC_AK8TrimPFJets_v19',
    'MC_CaloBTagDeepCSV_v10',
    'MC_CaloHT_v10',
    'MC_CaloMET_JetIdCleaned_v11',
    'MC_CaloMET_v10',
    'MC_CaloMHT_v10',
    'MC_Diphoton10_10_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass10_v15',
    'MC_DoubleEle5_CaloIdL_MW_v17',
    'MC_DoubleMuNoFiltersNoVtx_v9',
    'MC_DoubleMu_TrkIsoVVL_DZ_v13',
    'MC_Ele15_Ele10_CaloIdL_TrackIdL_IsoVL_DZ_v17',
    'MC_Ele5_WPTight_Gsf_v10',
    'MC_IsoMu_v17',
    'MC_PFBTagDeepCSV_v12',
    'MC_PFBTagDeepJet_v3',
    'MC_PFHT_v18',
    'MC_PFMET_v19',
    'MC_PFMHT_v18',
    'MC_ReducedIterativeTracking_v14',
    'MC_Run3_PFScoutingPixelTracking_v17'
)

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamPhysicsCommissioning_datasetNoBPTX_selector
streamPhysicsCommissioning_datasetNoBPTX_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamPhysicsCommissioning_datasetNoBPTX_selector.l1tResults = cms.InputTag('')
streamPhysicsCommissioning_datasetNoBPTX_selector.throw      = cms.bool(False)
streamPhysicsCommissioning_datasetNoBPTX_selector.triggerConditions = cms.vstring(
    'HLT_CDC_L2cosmic_10_er1p0_v2',
    'HLT_CDC_L2cosmic_5p5_er1p0_v2',
    'HLT_L2Mu10_NoVertex_NoBPTX3BX_v6',
    'HLT_L2Mu10_NoVertex_NoBPTX_v7',
    'HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_v6',
    'HLT_L2Mu45_NoVertex_3Sta_NoBPTX3BX_v5',
    'HLT_UncorrectedJetE30_NoBPTX3BX_v7',
    'HLT_UncorrectedJetE30_NoBPTX_v7',
    'HLT_UncorrectedJetE60_NoBPTX3BX_v7',
    'HLT_UncorrectedJetE70_NoBPTX3BX_v7'
)

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamPhysicsCommissioning_datasetZeroBias_selector
streamPhysicsCommissioning_datasetZeroBias_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamPhysicsCommissioning_datasetZeroBias_selector.l1tResults = cms.InputTag('')
streamPhysicsCommissioning_datasetZeroBias_selector.throw      = cms.bool(False)
streamPhysicsCommissioning_datasetZeroBias_selector.triggerConditions = cms.vstring(
    'HLT_Random_v3',
    'HLT_ZeroBias_Alignment_v2',
    'HLT_ZeroBias_FirstBXAfterTrain_v4',
    'HLT_ZeroBias_FirstCollisionAfterAbortGap_v6',
    'HLT_ZeroBias_FirstCollisionInTrain_v5',
    'HLT_ZeroBias_IsolatedBunches_v6',
    'HLT_ZeroBias_LastCollisionInTrain_v4',
    'HLT_ZeroBias_v7'
)


# stream PhysicsDispJetBTagMuEGTau

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamPhysicsDispJetBTagMuEGTau_datasetBTagMu_selector
streamPhysicsDispJetBTagMuEGTau_datasetBTagMu_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamPhysicsDispJetBTagMuEGTau_datasetBTagMu_selector.l1tResults = cms.InputTag('')
streamPhysicsDispJetBTagMuEGTau_datasetBTagMu_selector.throw      = cms.bool(False)
streamPhysicsDispJetBTagMuEGTau_datasetBTagMu_selector.triggerConditions = cms.vstring(
    'HLT_BTagMu_AK4DiJet110_Mu5_v15',
    'HLT_BTagMu_AK4DiJet170_Mu5_v14',
    'HLT_BTagMu_AK4DiJet20_Mu5_v15',
    'HLT_BTagMu_AK4DiJet40_Mu5_v15',
    'HLT_BTagMu_AK4DiJet70_Mu5_v15',
    'HLT_BTagMu_AK4Jet300_Mu5_v14',
    'HLT_BTagMu_AK8DiJet170_Mu5_v11',
    'HLT_BTagMu_AK8Jet170_DoubleMu5_v4',
    'HLT_BTagMu_AK8Jet300_Mu5_v14'
)

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamPhysicsDispJetBTagMuEGTau_datasetDisplacedJet_selector
streamPhysicsDispJetBTagMuEGTau_datasetDisplacedJet_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamPhysicsDispJetBTagMuEGTau_datasetDisplacedJet_selector.l1tResults = cms.InputTag('')
streamPhysicsDispJetBTagMuEGTau_datasetDisplacedJet_selector.throw      = cms.bool(False)
streamPhysicsDispJetBTagMuEGTau_datasetDisplacedJet_selector.triggerConditions = cms.vstring(
    'HLT_CaloMET60_DTCluster50_v3',
    'HLT_CaloMET60_DTClusterNoMB1S50_v3',
    'HLT_CscCluster_Loose_v2',
    'HLT_CscCluster_Medium_v2',
    'HLT_CscCluster_Tight_v2',
    'HLT_HT170_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack_v2',
    'HLT_HT200_L1SingleLLPJet_DelayedJet40_DoubleDelay0p5nsTrackless_v2',
    'HLT_HT200_L1SingleLLPJet_DelayedJet40_DoubleDelay1nsInclusive_v2',
    'HLT_HT200_L1SingleLLPJet_DelayedJet40_SingleDelay1nsTrackless_v2',
    'HLT_HT200_L1SingleLLPJet_DelayedJet40_SingleDelay2nsInclusive_v2',
    'HLT_HT200_L1SingleLLPJet_DisplacedDijet30_Inclusive1PtrkShortSig5_v2',
    'HLT_HT200_L1SingleLLPJet_DisplacedDijet35_Inclusive1PtrkShortSig5_v2',
    'HLT_HT200_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack_v2',
    'HLT_HT200_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5_v2',
    'HLT_HT200_L1SingleLLPJet_DisplacedDijet60_DisplacedTrack_v2',
    'HLT_HT270_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack_v2',
    'HLT_HT320_L1SingleLLPJet_DisplacedDijet60_Inclusive_v2',
    'HLT_HT400_DisplacedDijet40_DisplacedTrack_v15',
    'HLT_HT420_L1SingleLLPJet_DisplacedDijet60_Inclusive_v2',
    'HLT_HT425_v11',
    'HLT_HT430_DelayedJet40_DoubleDelay0p5nsInclusive_v1',
    'HLT_HT430_DelayedJet40_DoubleDelay0p5nsTrackless_v3',
    'HLT_HT430_DelayedJet40_DoubleDelay1nsInclusive_v3',
    'HLT_HT430_DelayedJet40_SingleDelay0p5nsInclusive_v1',
    'HLT_HT430_DelayedJet40_SingleDelay0p5nsTrackless_v1',
    'HLT_HT430_DelayedJet40_SingleDelay1nsInclusive_v1',
    'HLT_HT430_DelayedJet40_SingleDelay1nsTrackless_v3',
    'HLT_HT430_DelayedJet40_SingleDelay1p5nsInclusive_v1',
    'HLT_HT430_DelayedJet40_SingleDelay2nsInclusive_v3',
    'HLT_HT430_DisplacedDijet30_Inclusive1PtrkShortSig5_v3',
    'HLT_HT430_DisplacedDijet35_Inclusive1PtrkShortSig5_v3',
    'HLT_HT430_DisplacedDijet40_DisplacedTrack_v15',
    'HLT_HT430_DisplacedDijet40_Inclusive1PtrkShortSig5_v3',
    'HLT_HT430_DisplacedDijet60_DisplacedTrack_v15',
    'HLT_HT500_DisplacedDijet40_DisplacedTrack_v15',
    'HLT_HT550_DisplacedDijet60_Inclusive_v15',
    'HLT_HT650_DisplacedDijet60_Inclusive_v15',
    'HLT_L1CSCShower_DTCluster50_v2',
    'HLT_L1CSCShower_DTCluster75_v2',
    'HLT_L1MET_DTCluster50_v3',
    'HLT_L1MET_DTClusterNoMB1S50_v3',
    'HLT_L1Mu6HT240_v2',
    'HLT_Mu6HT240_DisplacedDijet30_Inclusive0PtrkShortSig5_v3',
    'HLT_Mu6HT240_DisplacedDijet30_Inclusive1PtrkShortSig5_DisplacedLoose_v3',
    'HLT_Mu6HT240_DisplacedDijet35_Inclusive0PtrkShortSig5_v3',
    'HLT_Mu6HT240_DisplacedDijet35_Inclusive1PtrkShortSig5_DisplacedLoose_v3',
    'HLT_Mu6HT240_DisplacedDijet40_Inclusive0PtrkShortSig5_v3',
    'HLT_Mu6HT240_DisplacedDijet40_Inclusive1PtrkShortSig5_DisplacedLoose_v3'
)

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamPhysicsDispJetBTagMuEGTau_datasetMuonEG_selector
streamPhysicsDispJetBTagMuEGTau_datasetMuonEG_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamPhysicsDispJetBTagMuEGTau_datasetMuonEG_selector.l1tResults = cms.InputTag('')
streamPhysicsDispJetBTagMuEGTau_datasetMuonEG_selector.throw      = cms.bool(False)
streamPhysicsDispJetBTagMuEGTau_datasetMuonEG_selector.triggerConditions = cms.vstring(
    'HLT_DiMu4_Ele9_CaloIdL_TrackIdL_DZ_Mass3p8_v19',
    'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ_v19',
    'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v19',
    'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v17',
    'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v9',
    'HLT_Mu17_Photon30_IsoCaloId_v8',
    'HLT_Mu20NoFiltersNoVtxDisplaced_Photon20_CaloCustomId_v3',
    'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v17',
    'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v9',
    'HLT_Mu27_Ele37_CaloIdL_MW_v7',
    'HLT_Mu37_Ele27_CaloIdL_MW_v7',
    'HLT_Mu38NoFiltersNoVtxDisplaced_Photon38_CaloIdL_v3',
    'HLT_Mu43NoFiltersNoVtxDisplaced_Photon43_CaloIdL_v3',
    'HLT_Mu43NoFiltersNoVtx_Photon43_CaloIdL_v7',
    'HLT_Mu48NoFiltersNoVtx_Photon48_CaloIdL_v7',
    'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZ_v20',
    'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v20',
    'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350_DZ_v21',
    'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350_v21',
    'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_CaloDiJet30_CaloBtagDeepCSV_1p5_v3',
    'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_CaloDiJet30_v3',
    'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PFBTagParticleNet_2BTagSum0p65_v2',
    'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PFBtagDeepCSV_1p5_v3',
    'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PFBtagDeepJet_1p5_v3',
    'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_v3',
    'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_QuadPFJet70_50_40_30_PFBTagParticleNet_2BTagSum0p65_v2',
    'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_QuadPFJet70_50_40_30_v2',
    'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v15',
    'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v13'
)

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamPhysicsDispJetBTagMuEGTau_datasetTau_selector
streamPhysicsDispJetBTagMuEGTau_datasetTau_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamPhysicsDispJetBTagMuEGTau_datasetTau_selector.l1tResults = cms.InputTag('')
streamPhysicsDispJetBTagMuEGTau_datasetTau_selector.throw      = cms.bool(False)
streamPhysicsDispJetBTagMuEGTau_datasetTau_selector.triggerConditions = cms.vstring(
    'HLT_DoubleMediumChargedIsoDisplacedPFTauHPS32_Trk1_eta2p1_v3',
    'HLT_DoubleMediumChargedIsoPFTauHPS40_Trk1_eta2p1_v3',
    'HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60_v2',
    'HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet75_v2',
    'HLT_DoubleMediumDeepTauPFTauHPS35_L2NN_eta2p1_v2',
    'HLT_DoublePFJets40_Mass500_MediumDeepTauPFTauHPS45_L2NN_MediumDeepTauPFTauHPS20_eta2p1_v2',
    'HLT_DoubleTightChargedIsoPFTauHPS35_Trk1_eta2p1_v3',
    'HLT_LooseDeepTauPFTauHPS180_L2NN_eta2p1_v3',
    'HLT_MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1_v14',
    'HLT_Photon35_TwoProngs35_v3',
    'HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1_v2',
    'HLT_VBF_DoubleTightChargedIsoPFTauHPS20_Trk1_eta2p1_v3'
)


# stream PhysicsEGamma

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamPhysicsEGamma_datasetEGamma_selector
streamPhysicsEGamma_datasetEGamma_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamPhysicsEGamma_datasetEGamma_selector.l1tResults = cms.InputTag('')
streamPhysicsEGamma_datasetEGamma_selector.throw      = cms.bool(False)
streamPhysicsEGamma_datasetEGamma_selector.triggerConditions = cms.vstring(
    'HLT_DiEle27_WPTightCaloOnly_L1DoubleEG_v6',
    'HLT_DiPhoton10Time1ns_v2',
    'HLT_DiPhoton10Time1p2ns_v2',
    'HLT_DiPhoton10Time1p4ns_v2',
    'HLT_DiPhoton10Time1p6ns_v2',
    'HLT_DiPhoton10Time1p8ns_v2',
    'HLT_DiPhoton10Time2ns_v2',
    'HLT_DiPhoton10_CaloIdL_v2',
    'HLT_DiPhoton10sminlt0p12_v2',
    'HLT_DiPhoton10sminlt0p1_v2',
    'HLT_DiSC30_18_EIso_AND_HE_Mass70_v15',
    'HLT_Diphoton20_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v2',
    'HLT_Diphoton20_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT_v2',
    'HLT_Diphoton22_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v2',
    'HLT_Diphoton22_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT_v2',
    'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_Mass55_v3',
    'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_v3',
    'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90_v15',
    'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95_v15',
    'HLT_DoubleEle25_CaloIdL_MW_v6',
    'HLT_DoubleEle27_CaloIdL_MW_v6',
    'HLT_DoubleEle33_CaloIdL_MW_v19',
    'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_DZ_PFHT350_v22',
    'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT350_v22',
    'HLT_DoublePhoton33_CaloIdL_v8',
    'HLT_DoublePhoton70_v8',
    'HLT_DoublePhoton85_v16',
    'HLT_ECALHT800_v12',
    'HLT_Ele115_CaloIdVT_GsfTrkIdT_v16',
    'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v20',
    'HLT_Ele135_CaloIdVT_GsfTrkIdT_v9',
    'HLT_Ele15_IsoVVVL_PFHT450_CaloBTagDeepCSV_4p5_v10',
    'HLT_Ele15_IsoVVVL_PFHT450_PFMET50_v18',
    'HLT_Ele15_IsoVVVL_PFHT450_v18',
    'HLT_Ele15_IsoVVVL_PFHT600_v22',
    'HLT_Ele15_WPLoose_Gsf_v5',
    'HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v11',
    'HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v18',
    'HLT_Ele20_WPLoose_Gsf_v8',
    'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v20',
    'HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v20',
    'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v21',
    'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v21',
    'HLT_Ele24_eta2p1_WPTight_Gsf_LooseDeepTauPFTauHPS30_eta2p1_CrossL1_v3',
    'HLT_Ele24_eta2p1_WPTight_Gsf_TightChargedIsoPFTauHPS30_eta2p1_CrossL1_v3',
    'HLT_Ele27_WPTight_Gsf_v18',
    'HLT_Ele28_HighEta_SC20_Mass55_v15',
    'HLT_Ele28_WPTight_Gsf_v3',
    'HLT_Ele28_eta2p1_WPTight_Gsf_HT150_v15',
    'HLT_Ele30_WPTight_Gsf_v3',
    'HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned_v15',
    'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v11',
    'HLT_Ele32_WPTight_Gsf_v17',
    'HLT_Ele35_WPTight_Gsf_L1EGMT_v7',
    'HLT_Ele35_WPTight_Gsf_v11',
    'HLT_Ele38_WPTight_Gsf_v11',
    'HLT_Ele40_WPTight_Gsf_v11',
    'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PFAK8ParticleNetBB0p35_v2',
    'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_v2',
    'HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v20',
    'HLT_Ele50_IsoVVVL_PFHT450_v18',
    'HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30_v18',
    'HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v20',
    'HLT_Photon100EBHE10_v4',
    'HLT_Photon110EB_TightID_TightIso_v4',
    'HLT_Photon120_R9Id90_HE10_IsoM_v16',
    'HLT_Photon120_v15',
    'HLT_Photon150_v8',
    'HLT_Photon165_R9Id90_HE10_IsoM_v17',
    'HLT_Photon175_v16',
    'HLT_Photon200_v15',
    'HLT_Photon20_HoverELoose_v12',
    'HLT_Photon20_v4',
    'HLT_Photon300_NoHE_v14',
    'HLT_Photon30EB_TightID_TightIso_v3',
    'HLT_Photon30_HoverELoose_v12',
    'HLT_Photon33_v7',
    'HLT_Photon50_R9Id90_HE10_IsoM_v16',
    'HLT_Photon50_v15',
    'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT350MinPFJet15_v13',
    'HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3_v7',
    'HLT_Photon75_R9Id90_HE10_IsoM_v16',
    'HLT_Photon75_v15',
    'HLT_Photon90_R9Id90_HE10_IsoM_v16',
    'HLT_Photon90_v15'
)


# stream PhysicsHLTPhysics

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamPhysicsHLTPhysics_datasetEphemeralHLTPhysics_selector
streamPhysicsHLTPhysics_datasetEphemeralHLTPhysics_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamPhysicsHLTPhysics_datasetEphemeralHLTPhysics_selector.l1tResults = cms.InputTag('')
streamPhysicsHLTPhysics_datasetEphemeralHLTPhysics_selector.throw      = cms.bool(False)
streamPhysicsHLTPhysics_datasetEphemeralHLTPhysics_selector.triggerConditions = cms.vstring('HLT_EphemeralPhysics_v2')


# stream PhysicsJetMET

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamPhysicsJetMET_datasetJetMET_selector
streamPhysicsJetMET_datasetJetMET_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamPhysicsJetMET_datasetJetMET_selector.l1tResults = cms.InputTag('')
streamPhysicsJetMET_datasetJetMET_selector.throw      = cms.bool(False)
streamPhysicsJetMET_datasetJetMET_selector.triggerConditions = cms.vstring(
    'HLT_AK8DiPFJet250_250_MassSD30_v2',
    'HLT_AK8DiPFJet250_250_MassSD50_v2',
    'HLT_AK8DiPFJet260_260_MassSD30_v2',
    'HLT_AK8DiPFJet270_270_MassSD30_v2',
    'HLT_AK8PFHT750_TrimMass50_v14',
    'HLT_AK8PFHT800_TrimMass50_v14',
    'HLT_AK8PFHT850_TrimMass50_v13',
    'HLT_AK8PFHT900_TrimMass50_v13',
    'HLT_AK8PFJet140_v17',
    'HLT_AK8PFJet200_v17',
    'HLT_AK8PFJet230_SoftDropMass40_PFAK8ParticleNetBB0p35_v3',
    'HLT_AK8PFJet230_SoftDropMass40_PFAK8ParticleNetTauTau0p30_v3',
    'HLT_AK8PFJet230_SoftDropMass40_v3',
    'HLT_AK8PFJet250_SoftDropMass40_PFAK8ParticleNetBB0p35_v3',
    'HLT_AK8PFJet250_SoftDropMass40_PFAK8ParticleNetTauTau0p30_v3',
    'HLT_AK8PFJet260_v18',
    'HLT_AK8PFJet275_SoftDropMass40_PFAK8ParticleNetBB0p35_v3',
    'HLT_AK8PFJet275_SoftDropMass40_PFAK8ParticleNetTauTau0p30_v3',
    'HLT_AK8PFJet320_v18',
    'HLT_AK8PFJet360_TrimMass30_v20',
    'HLT_AK8PFJet380_TrimMass30_v13',
    'HLT_AK8PFJet400_MassSD30_v2',
    'HLT_AK8PFJet400_SoftDropMass40_v3',
    'HLT_AK8PFJet400_TrimMass30_v14',
    'HLT_AK8PFJet400_v18',
    'HLT_AK8PFJet40_v18',
    'HLT_AK8PFJet420_MassSD30_v2',
    'HLT_AK8PFJet420_TrimMass30_v13',
    'HLT_AK8PFJet425_SoftDropMass40_v3',
    'HLT_AK8PFJet450_MassSD30_v2',
    'HLT_AK8PFJet450_SoftDropMass40_v3',
    'HLT_AK8PFJet450_v18',
    'HLT_AK8PFJet500_v18',
    'HLT_AK8PFJet550_v13',
    'HLT_AK8PFJet60_v17',
    'HLT_AK8PFJet80_v17',
    'HLT_AK8PFJetFwd140_v16',
    'HLT_AK8PFJetFwd15_v5',
    'HLT_AK8PFJetFwd200_v16',
    'HLT_AK8PFJetFwd25_v5',
    'HLT_AK8PFJetFwd260_v17',
    'HLT_AK8PFJetFwd320_v17',
    'HLT_AK8PFJetFwd400_v17',
    'HLT_AK8PFJetFwd40_v17',
    'HLT_AK8PFJetFwd450_v17',
    'HLT_AK8PFJetFwd500_v17',
    'HLT_AK8PFJetFwd60_v16',
    'HLT_AK8PFJetFwd80_v16',
    'HLT_CaloJet500_NoJetID_v14',
    'HLT_CaloJet550_NoJetID_v9',
    'HLT_CaloMET350_NotCleaned_v6',
    'HLT_CaloMET90_NotCleaned_v6',
    'HLT_CaloMHT90_v6',
    'HLT_DiJet110_35_Mjj650_PFMET110_v11',
    'HLT_DiJet110_35_Mjj650_PFMET120_v11',
    'HLT_DiJet110_35_Mjj650_PFMET130_v11',
    'HLT_DiPFJetAve100_HFJEC_v18',
    'HLT_DiPFJetAve140_v15',
    'HLT_DiPFJetAve160_HFJEC_v18',
    'HLT_DiPFJetAve200_v15',
    'HLT_DiPFJetAve220_HFJEC_v18',
    'HLT_DiPFJetAve260_HFJEC_v1',
    'HLT_DiPFJetAve260_v16',
    'HLT_DiPFJetAve300_HFJEC_v18',
    'HLT_DiPFJetAve320_v16',
    'HLT_DiPFJetAve400_v16',
    'HLT_DiPFJetAve40_v16',
    'HLT_DiPFJetAve500_v16',
    'HLT_DiPFJetAve60_HFJEC_v17',
    'HLT_DiPFJetAve60_v16',
    'HLT_DiPFJetAve80_HFJEC_v18',
    'HLT_DiPFJetAve80_v15',
    'HLT_DoublePFJets100_PFBTagDeepCSV_p71_v3',
    'HLT_DoublePFJets100_PFBTagDeepJet_p71_v3',
    'HLT_DoublePFJets116MaxDeta1p6_DoublePFBTagDeepCSV_p71_v3',
    'HLT_DoublePFJets116MaxDeta1p6_DoublePFBTagDeepJet_p71_v3',
    'HLT_DoublePFJets128MaxDeta1p6_DoublePFBTagDeepCSV_p71_v3',
    'HLT_DoublePFJets128MaxDeta1p6_DoublePFBTagDeepJet_p71_v3',
    'HLT_DoublePFJets200_PFBTagDeepCSV_p71_v3',
    'HLT_DoublePFJets200_PFBTagDeepJet_p71_v3',
    'HLT_DoublePFJets350_PFBTagDeepCSV_p71_v3',
    'HLT_DoublePFJets350_PFBTagDeepJet_p71_v3',
    'HLT_DoublePFJets40_PFBTagDeepCSV_p71_v3',
    'HLT_DoublePFJets40_PFBTagDeepJet_p71_v3',
    'HLT_L1ETMHadSeeds_v4',
    'HLT_MET105_IsoTrk50_v11',
    'HLT_MET120_IsoTrk50_v11',
    'HLT_Mu12_DoublePFJets100_PFBTagDeepCSV_p71_v3',
    'HLT_Mu12_DoublePFJets100_PFBTagDeepJet_p71_v3',
    'HLT_Mu12_DoublePFJets200_PFBTagDeepCSV_p71_v3',
    'HLT_Mu12_DoublePFJets200_PFBTagDeepJet_p71_v3',
    'HLT_Mu12_DoublePFJets350_PFBTagDeepCSV_p71_v3',
    'HLT_Mu12_DoublePFJets350_PFBTagDeepJet_p71_v3',
    'HLT_Mu12_DoublePFJets40MaxDeta1p6_DoublePFBTagDeepCSV_p71_v3',
    'HLT_Mu12_DoublePFJets40MaxDeta1p6_DoublePFBTagDeepJet_p71_v3',
    'HLT_Mu12_DoublePFJets40_PFBTagDeepCSV_p71_v3',
    'HLT_Mu12_DoublePFJets40_PFBTagDeepJet_p71_v3',
    'HLT_Mu12_DoublePFJets54MaxDeta1p6_DoublePFBTagDeepCSV_p71_v3',
    'HLT_Mu12_DoublePFJets54MaxDeta1p6_DoublePFBTagDeepJet_p71_v3',
    'HLT_Mu12eta2p3_PFJet40_v3',
    'HLT_Mu12eta2p3_v3',
    'HLT_PFHT1050_v20',
    'HLT_PFHT180_v19',
    'HLT_PFHT250_v19',
    'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5_v5',
    'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepJet_4p5_v3',
    'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_v11',
    'HLT_PFHT350_v21',
    'HLT_PFHT370_v19',
    'HLT_PFHT400_FivePFJet_100_100_60_30_30_DoublePFBTagDeepCSV_4p5_v10',
    'HLT_PFHT400_FivePFJet_100_100_60_30_30_DoublePFBTagDeepJet_4p5_v3',
    'HLT_PFHT400_FivePFJet_100_100_60_30_30_v10',
    'HLT_PFHT400_FivePFJet_120_120_60_30_30_DoublePFBTagDeepCSV_4p5_v10',
    'HLT_PFHT400_FivePFJet_120_120_60_30_30_DoublePFBTagDeepJet_4p5_v3',
    'HLT_PFHT400_SixPFJet32_DoublePFBTagDeepCSV_2p94_v10',
    'HLT_PFHT400_SixPFJet32_DoublePFBTagDeepJet_2p94_v3',
    'HLT_PFHT400_SixPFJet32_v10',
    'HLT_PFHT430_v19',
    'HLT_PFHT450_SixPFJet36_PFBTagDeepCSV_1p59_v9',
    'HLT_PFHT450_SixPFJet36_PFBTagDeepJet_1p59_v3',
    'HLT_PFHT450_SixPFJet36_v9',
    'HLT_PFHT500_PFMET100_PFMHT100_IDTight_v14',
    'HLT_PFHT500_PFMET110_PFMHT110_IDTight_v14',
    'HLT_PFHT510_v19',
    'HLT_PFHT590_v19',
    'HLT_PFHT680_v19',
    'HLT_PFHT700_PFMET85_PFMHT85_IDTight_v14',
    'HLT_PFHT780_v19',
    'HLT_PFHT800_PFMET75_PFMHT75_IDTight_v14',
    'HLT_PFHT890_v19',
    'HLT_PFJet110_v2',
    'HLT_PFJet140_v21',
    'HLT_PFJet200_v21',
    'HLT_PFJet260_v22',
    'HLT_PFJet320_v22',
    'HLT_PFJet400_v22',
    'HLT_PFJet40_v23',
    'HLT_PFJet450_v23',
    'HLT_PFJet500_v23',
    'HLT_PFJet550_v13',
    'HLT_PFJet60_v23',
    'HLT_PFJet80_v22',
    'HLT_PFJetFwd140_v20',
    'HLT_PFJetFwd15_v5',
    'HLT_PFJetFwd200_v20',
    'HLT_PFJetFwd25_v5',
    'HLT_PFJetFwd260_v21',
    'HLT_PFJetFwd320_v21',
    'HLT_PFJetFwd400_v21',
    'HLT_PFJetFwd40_v21',
    'HLT_PFJetFwd450_v21',
    'HLT_PFJetFwd500_v21',
    'HLT_PFJetFwd60_v21',
    'HLT_PFJetFwd80_v20',
    'HLT_PFMET100_PFMHT100_IDTight_PFHT60_v11',
    'HLT_PFMET105_IsoTrk50_v3',
    'HLT_PFMET110_PFJet100_v3',
    'HLT_PFMET110_PFMHT110_IDTight_v22',
    'HLT_PFMET120_PFMHT120_IDTight_PFHT60_v11',
    'HLT_PFMET120_PFMHT120_IDTight_v22',
    'HLT_PFMET130_PFMHT130_IDTight_v22',
    'HLT_PFMET140_PFMHT140_IDTight_v22',
    'HLT_PFMET200_BeamHaloCleaned_v11',
    'HLT_PFMET200_NotCleaned_v11',
    'HLT_PFMET250_NotCleaned_v11',
    'HLT_PFMET300_NotCleaned_v11',
    'HLT_PFMETNoMu100_PFMHTNoMu100_IDTight_PFHT60_v11',
    'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_FilterHF_v2',
    'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_v22',
    'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_FilterHF_v2',
    'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v11',
    'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v22',
    'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_FilterHF_v2',
    'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v21',
    'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_FilterHF_v2',
    'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v21',
    'HLT_PFMETTypeOne100_PFMHT100_IDTight_PFHT60_v11',
    'HLT_PFMETTypeOne110_PFMHT110_IDTight_v14',
    'HLT_PFMETTypeOne120_PFMHT120_IDTight_PFHT60_v11',
    'HLT_PFMETTypeOne120_PFMHT120_IDTight_v14',
    'HLT_PFMETTypeOne130_PFMHT130_IDTight_v14',
    'HLT_PFMETTypeOne140_PFMHT140_IDTight_v13',
    'HLT_PFMETTypeOne200_BeamHaloCleaned_v11',
    'HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v10',
    'HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v3',
    'HLT_QuadPFJet103_88_75_15_PFBTagDeepCSV_1p3_VBF2_v10',
    'HLT_QuadPFJet103_88_75_15_PFBTagDeepJet_1p3_VBF2_v3',
    'HLT_QuadPFJet103_88_75_15_v7',
    'HLT_QuadPFJet105_88_76_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v10',
    'HLT_QuadPFJet105_88_76_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v3',
    'HLT_QuadPFJet105_88_76_15_PFBTagDeepCSV_1p3_VBF2_v10',
    'HLT_QuadPFJet105_88_76_15_PFBTagDeepJet_1p3_VBF2_v3',
    'HLT_QuadPFJet105_88_76_15_v7',
    'HLT_QuadPFJet111_90_80_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v10',
    'HLT_QuadPFJet111_90_80_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v3',
    'HLT_QuadPFJet111_90_80_15_PFBTagDeepCSV_1p3_VBF2_v10',
    'HLT_QuadPFJet111_90_80_15_PFBTagDeepJet_1p3_VBF2_v3',
    'HLT_QuadPFJet111_90_80_15_v7',
    'HLT_QuadPFJet70_50_40_30_PFBTagParticleNet_2BTagSum0p65_v3',
    'HLT_QuadPFJet70_50_40_30_v3',
    'HLT_QuadPFJet70_50_40_35_PFBTagParticleNet_2BTagSum0p65_v3',
    'HLT_QuadPFJet70_50_45_35_PFBTagParticleNet_2BTagSum0p65_v3',
    'HLT_SingleJet30_Mu12_SinglePFJet40_v13',
    'HLT_TripleJet110_35_35_Mjj650_PFMET110_v11',
    'HLT_TripleJet110_35_35_Mjj650_PFMET120_v11',
    'HLT_TripleJet110_35_35_Mjj650_PFMET130_v11'
)


# stream PhysicsMuon

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamPhysicsMuon_datasetMuon_selector
streamPhysicsMuon_datasetMuon_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamPhysicsMuon_datasetMuon_selector.l1tResults = cms.InputTag('')
streamPhysicsMuon_datasetMuon_selector.throw      = cms.bool(False)
streamPhysicsMuon_datasetMuon_selector.triggerConditions = cms.vstring(
    'HLT_CascadeMu100_v5',
    'HLT_DoubleL2Mu10NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm_v2',
    'HLT_DoubleL2Mu10NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v3',
    'HLT_DoubleL2Mu12NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm_v2',
    'HLT_DoubleL2Mu12NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v2',
    'HLT_DoubleL2Mu14NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v2',
    'HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed_v3',
    'HLT_DoubleL2Mu23NoVtx_2Cha_v3',
    'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_Eta2p4_v3',
    'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_v3',
    'HLT_DoubleL2Mu25NoVtx_2Cha_Eta2p4_v3',
    'HLT_DoubleL2Mu25NoVtx_2Cha_v3',
    'HLT_DoubleL2Mu30NoVtx_2Cha_CosmicSeed_Eta2p4_v3',
    'HLT_DoubleL2Mu30NoVtx_2Cha_Eta2p4_v3',
    'HLT_DoubleL2Mu50_v3',
    'HLT_DoubleL2Mu_L3Mu16NoVtx_VetoL3Mu0DxyMax0p1cm_v2',
    'HLT_DoubleL2Mu_L3Mu18NoVtx_VetoL3Mu0DxyMax0p1cm_v2',
    'HLT_DoubleL3Mu16_10NoVtx_DxyMin0p01cm_v3',
    'HLT_DoubleL3Mu18_10NoVtx_DxyMin0p01cm_v2',
    'HLT_DoubleL3Mu20_10NoVtx_DxyMin0p01cm_v2',
    'HLT_DoubleL3dTksMu16_10NoVtx_DxyMin0p01cm_v2',
    'HLT_DoubleMu3_DCA_PFMET50_PFMHT60_v12',
    'HLT_DoubleMu3_DZ_PFMET50_PFMHT60_v12',
    'HLT_DoubleMu3_DZ_PFMET70_PFMHT70_v12',
    'HLT_DoubleMu3_DZ_PFMET90_PFMHT90_v12',
    'HLT_DoubleMu43NoFiltersNoVtx_v6',
    'HLT_DoubleMu48NoFiltersNoVtx_v6',
    'HLT_DoubleMu4_Mass3p8_DZ_PFHT350_v10',
    'HLT_HighPtTkMu100_v4',
    'HLT_IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1_v3',
    'HLT_IsoMu20_eta2p1_TightChargedIsoPFTauHPS27_eta2p1_CrossL1_v3',
    'HLT_IsoMu20_eta2p1_TightChargedIsoPFTauHPS27_eta2p1_TightID_CrossL1_v3',
    'HLT_IsoMu20_v17',
    'HLT_IsoMu24_TwoProngs35_v3',
    'HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS180_eta2p1_v3',
    'HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS30_eta2p1_CrossL1_v3',
    'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS20_eta2p1_SingleL1_v2',
    'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_CrossL1_v2',
    'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60_CrossL1_v2',
    'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet75_CrossL1_v2',
    'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS35_L2NN_eta2p1_CrossL1_v3',
    'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS45_L2NN_eta2p1_CrossL1_v2',
    'HLT_IsoMu24_eta2p1_v17',
    'HLT_IsoMu24_v15',
    'HLT_IsoMu27_MediumDeepTauPFTauHPS20_eta2p1_SingleL1_v2',
    'HLT_IsoMu27_v18',
    'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PFAK8ParticleNetBB0p35_v2',
    'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_v2',
    'HLT_L1SingleMu18_v4',
    'HLT_L1SingleMu25_v3',
    'HLT_L3dTksMu10_NoVtx_DxyMin0p01cm_v2',
    'HLT_Mu10_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT350_PFMETNoMu60_v17',
    'HLT_Mu15_IsoVVVL_PFHT450_CaloBTagDeepCSV_4p5_v10',
    'HLT_Mu15_IsoVVVL_PFHT450_PFMET50_v17',
    'HLT_Mu15_IsoVVVL_PFHT450_v17',
    'HLT_Mu15_IsoVVVL_PFHT600_v21',
    'HLT_Mu15_v5',
    'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v7',
    'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v7',
    'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v17',
    'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v16',
    'HLT_Mu17_TrkIsoVVL_v15',
    'HLT_Mu17_v15',
    'HLT_Mu18_Mu9_SameSign_v6',
    'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass3p8_v5',
    'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass8_v5',
    'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_v5',
    'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_v5',
    'HLT_Mu19_TrkIsoVVL_v6',
    'HLT_Mu19_v6',
    'HLT_Mu20_v14',
    'HLT_Mu27_v15',
    'HLT_Mu37_TkMu27_v7',
    'HLT_Mu3_PFJet40_v18',
    'HLT_Mu3er1p5_PFJet100er2p5_PFMET100_PFMHT100_IDTight_v4',
    'HLT_Mu3er1p5_PFJet100er2p5_PFMET70_PFMHT70_IDTight_v4',
    'HLT_Mu3er1p5_PFJet100er2p5_PFMET80_PFMHT80_IDTight_v4',
    'HLT_Mu3er1p5_PFJet100er2p5_PFMET90_PFMHT90_IDTight_v4',
    'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu100_PFMHTNoMu100_IDTight_v4',
    'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu70_PFMHTNoMu70_IDTight_v4',
    'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu80_PFMHTNoMu80_IDTight_v4',
    'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu90_PFMHTNoMu90_IDTight_v4',
    'HLT_Mu4_TrkIsoVVL_DiPFJet90_40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v17',
    'HLT_Mu50_IsoVVVL_PFHT450_v17',
    'HLT_Mu50_L1SingleMuShower_v1',
    'HLT_Mu50_v15',
    'HLT_Mu55_v5',
    'HLT_Mu8_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v18',
    'HLT_Mu8_TrkIsoVVL_v14',
    'HLT_Mu8_v14',
    'HLT_TripleMu_10_5_5_DZ_v12',
    'HLT_TripleMu_12_10_5_v12',
    'HLT_TripleMu_5_3_3_Mass3p8_DCA_v5',
    'HLT_TripleMu_5_3_3_Mass3p8_DZ_v10',
    'HLT_TrkMu12_DoubleTrkMu5NoFiltersNoVtx_v8'
)


# stream PhysicsReservedDoubleMuonLowMass

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamPhysicsReservedDoubleMuonLowMass_datasetReservedDoubleMuonLowMass_selector
streamPhysicsReservedDoubleMuonLowMass_datasetReservedDoubleMuonLowMass_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamPhysicsReservedDoubleMuonLowMass_datasetReservedDoubleMuonLowMass_selector.l1tResults = cms.InputTag('')
streamPhysicsReservedDoubleMuonLowMass_datasetReservedDoubleMuonLowMass_selector.throw      = cms.bool(False)
streamPhysicsReservedDoubleMuonLowMass_datasetReservedDoubleMuonLowMass_selector.triggerConditions = cms.vstring(
    'HLT_Dimuon0_Jpsi3p5_Muon2_v7',
    'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v9',
    'HLT_Dimuon0_Jpsi_L1_NoOS_v9',
    'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v9',
    'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v9',
    'HLT_Dimuon0_Jpsi_NoVertexing_v10',
    'HLT_Dimuon0_Jpsi_v10',
    'HLT_Dimuon0_LowMass_L1_0er1p5R_v9',
    'HLT_Dimuon0_LowMass_L1_0er1p5_v10',
    'HLT_Dimuon0_LowMass_L1_4R_v9',
    'HLT_Dimuon0_LowMass_L1_4_v10',
    'HLT_Dimuon0_LowMass_L1_TM530_v8',
    'HLT_Dimuon0_LowMass_v10',
    'HLT_Dimuon0_Upsilon_L1_4p5NoOS_v10',
    'HLT_Dimuon0_Upsilon_L1_4p5_v11',
    'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v9',
    'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v11',
    'HLT_Dimuon0_Upsilon_L1_5M_v10',
    'HLT_Dimuon0_Upsilon_L1_5_v11',
    'HLT_Dimuon0_Upsilon_Muon_L1_TM0_v8',
    'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v8',
    'HLT_Dimuon0_Upsilon_NoVertexing_v9',
    'HLT_Dimuon10_PsiPrime_Barrel_Seagulls_v9',
    'HLT_Dimuon12_Upsilon_y1p4_v4',
    'HLT_Dimuon14_Phi_Barrel_Seagulls_v9',
    'HLT_Dimuon18_PsiPrime_noCorrL1_v8',
    'HLT_Dimuon18_PsiPrime_v16',
    'HLT_Dimuon20_Jpsi_Barrel_Seagulls_v9',
    'HLT_Dimuon24_Phi_noCorrL1_v8',
    'HLT_Dimuon24_Upsilon_noCorrL1_v8',
    'HLT_Dimuon25_Jpsi_noCorrL1_v8',
    'HLT_Dimuon25_Jpsi_v16',
    'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v8',
    'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v6',
    'HLT_DoubleMu3_TkMu_DsTau3Mu_v6',
    'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v8',
    'HLT_DoubleMu3_Trk_Tau3mu_v14',
    'HLT_DoubleMu4_3_Bs_v17',
    'HLT_DoubleMu4_3_Jpsi_v17',
    'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v9',
    'HLT_DoubleMu4_Jpsi_Displaced_v9',
    'HLT_DoubleMu4_Jpsi_NoVertexing_v9',
    'HLT_DoubleMu4_MuMuTrk_Displaced_v17',
    'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v6',
    'HLT_Mu20_TkMu0_Phi_v10',
    'HLT_Mu25_TkMu0_Onia_v10',
    'HLT_Mu25_TkMu0_Phi_v10',
    'HLT_Mu30_TkMu0_Psi_v3',
    'HLT_Mu30_TkMu0_Upsilon_v3',
    'HLT_Mu4_L1DoubleMu_v3',
    'HLT_Mu7p5_L2Mu2_Jpsi_v12',
    'HLT_Mu7p5_L2Mu2_Upsilon_v12',
    'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v6',
    'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v6',
    'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v6',
    'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v6',
    'HLT_Trimuon5_3p5_2_Upsilon_Muon_v7',
    'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v5'
)


# stream PhysicsScoutingPFMonitor

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamPhysicsScoutingPFMonitor_datasetScoutingPFMonitor_selector
streamPhysicsScoutingPFMonitor_datasetScoutingPFMonitor_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamPhysicsScoutingPFMonitor_datasetScoutingPFMonitor_selector.l1tResults = cms.InputTag('')
streamPhysicsScoutingPFMonitor_datasetScoutingPFMonitor_selector.throw      = cms.bool(False)
streamPhysicsScoutingPFMonitor_datasetScoutingPFMonitor_selector.triggerConditions = cms.vstring(
    'DST_Run3_PFScoutingPixelTracking_v18',
    'HLT_Ele115_CaloIdVT_GsfTrkIdT_v16',
    'HLT_Ele35_WPTight_Gsf_v11',
    'HLT_IsoMu27_v18',
    'HLT_Mu50_v15',
    'HLT_PFHT1050_v20',
    'HLT_Photon200_v15'
)


# stream PhysicsZeroBias

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamPhysicsZeroBias_datasetEphemeralZeroBias_selector
streamPhysicsZeroBias_datasetEphemeralZeroBias_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamPhysicsZeroBias_datasetEphemeralZeroBias_selector.l1tResults = cms.InputTag('')
streamPhysicsZeroBias_datasetEphemeralZeroBias_selector.throw      = cms.bool(False)
streamPhysicsZeroBias_datasetEphemeralZeroBias_selector.triggerConditions = cms.vstring('HLT_EphemeralZeroBias_v2')

