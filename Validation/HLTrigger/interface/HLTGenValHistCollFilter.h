#ifndef Validation_HLTrigger_HLTGenValHistCollFilter_h
#define Validation_HLTrigger_HLTGenValHistCollFilter_h

//********************************************************************************
//
// Description:
//   This contains a collection of HLTGenvalHists used to measure the efficiency of a
//   specified filter. It is resonsible for booking and filling the histograms of all vsVars
//   histograms are desired for a specific filter.
//
// Author : Finn Labe, UHH, Oct. 2021
// (Heavily borrowed from Sam Harpers HLTDQMFilterEffHists)
//
//***********************************************************************************

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ParameterSet/interface/ParameterSetDescription.h"

#include "DQMServices/Core/interface/DQMStore.h"

#include "DataFormats/HLTReco/interface/TriggerEvent.h"

#include "Validation/HLTrigger/interface/HLTGenValHist.h"
#include "DQMOffline/Trigger/interface/FunctionDefs.h"
#include "DQMOffline/Trigger/interface/UtilFuncs.h"

#include "Validation/HLTrigger/interface/HLTGenValObject.h"

#include "DataFormats/Math/interface/deltaR.h"

#include <utility>

// class containing a collection of HLTGenValHist for a specific filter
// at object creation time, the object type (used for systematically naming the histogram),
// path and dR2limit (for deltaR matching) need to be specified
// functions for initial booking of hists, and filling of hists for a single object, are available
class HLTGenValHistCollFilter {
public:
  typedef dqm::legacy::MonitorElement MonitorElement;
  typedef dqm::legacy::DQMStore DQMStore;

  explicit HLTGenValHistCollFilter(std::string objType, std::string path, std::string hltprocessname, double dR2limit);

  void bookHists(DQMStore::IBooker& iBooker, std::vector<edm::ParameterSet>& histConfigs, std::vector<edm::ParameterSet>& histConfigs2D);
  void fillHists(const HLTGenValObject& obj, edm::Handle<trigger::TriggerEvent>& triggerEvent);

private:
  void book1D(DQMStore::IBooker& iBooker, edm::ParameterSet& histConfig);
  void book2D(DQMStore::IBooker& iBooker, edm::ParameterSet& histConfig2D);

  std::vector<std::unique_ptr<HLTGenValHist>> hists_; // the collection of histograms
  std::string objType_;
  std::string filter_;
  std::string hltprocessname_;
  double dR2limit_;
};


#endif
