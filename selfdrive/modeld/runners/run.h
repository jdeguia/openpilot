#ifndef RUN_H
#define RUN_H

#include "runmodel.h"

#ifdef QCOM
  #include "snpemodel.h"
  #define DefaultRunModel SNPEModel
#else
  #ifdef USE_TF_MODEL
    #include "tfmodel.h"
    #define DefaultRunModel TFModel
  #else
    #define DefaultRunModel SNPEModel
  #endif
#endif

#endif
