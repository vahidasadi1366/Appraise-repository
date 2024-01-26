"""
Appraise evaluation framework

See LICENSE for usage details
"""
from .base_models import *
from .data_assessment import *
from .direct_assessment import *
from .direct_assessment_context import *
from .direct_assessment_document import *
from .multi_modal_assessment import *
from .pairwise_assessment import *
from .pairwise_assessment_document import *
from .task_agenda import *
from .direct_assessment_long_document import *
from .direct_assessment_DocLevelDA_Window import *

# Task definitions: user-friendly name, task class, task result class, URL name

TASK_DEFINITIONS = (
    (
        'Direct',
        DirectAssessmentTask,
        DirectAssessmentResult,
        'direct-assessment',
        TextPair,
        'evaldata_directassessmenttasks',
        'evaldata_directassessmentresults',
    ),
    (
        'DocLevelDA',
        DirectAssessmentContextTask,
        DirectAssessmentContextResult,
        'direct-assessment-context',
        TextPairWithContext,
        'evaldata_directassessmentcontexttasks',
        'evaldata_directassessmentcontextresults',
    ),
    (
        'Document',
        DirectAssessmentDocumentTask,
        DirectAssessmentDocumentResult,
        'direct-assessment-document',
        TextPairWithContext,
        'evaldata_directassessmentdocumenttasks',
        'evaldata_directassessmentdocumentresults',
    ),
  (
       'LongDocument',
       DirectAssessmentLongDocumentTask,
       DirectAssessmentLongDocumentResult,
       'direct-assessment-long-document',
       TextPairWithContext,
       'evaldata_directassessmentlongdocumenttasks',
       'evaldata_directassessmentlongdocumentresults',
   ),
    (
        'DocLevelDA-Window',
        DirectAssessmentDocLevelDAWindowTask,
        DirectAssessmentDocLevelDAWindowResult,
        'direct-assessment-document-window',
        TextPairWithContext,
        'evaldata_directassessmentdocleveldawindowtasks',
        'evaldata_directassessmentdocleveldawindowresults',
    ),
    # (
    #     'Window',
    #     DirectAssessmentWindowDocumentTask,
    #     DirectAssessmentWindowDocumentResult,
    #     'direct-assessment-window-document',
    #     TextPairWithContext,
    #     'evaldata_directassessmentwindowdocumenttasks',
    #     'evaldata_directassessmentwindowdocumentresults',
    # ),
     (
        'MultiModal',
        MultiModalAssessmentTask,
        MultiModalAssessmentResult,
        'multimodal-assessment',
        TextPairWithImage,
        'evaldata_multimodalassessmenttasks',
        'evaldata_multimodalassessmentresults',
    ),
    (
        'Pairwise',
        PairwiseAssessmentTask,
        PairwiseAssessmentResult,
        'pairwise-assessment',
        TextSegmentWithTwoTargets,
        'evaldata_pairwiseassessmenttasks',
        'evaldata_pairwiseassessmentresults',
    ),
    (
        'PairwiseDocument',
        PairwiseAssessmentDocumentTask,
        PairwiseAssessmentDocumentResult,
        'pairwise-assessment-document',
        TextSegmentWithTwoTargetsWithContext,
        'evaldata_pairwiseassessmentdocumenttasks',
        'evaldata_pairwiseassessmentdocumentresults',
    ),
    (
        'Data',
        DataAssessmentTask,
        DataAssessmentResult,
        'data-assessment',
        TextPairWithDomain,
        'evaldata_dataassessmenttasks',
        'evaldata_dataassessmentresults',
    )
)

# Map convenient task type names into their corresponding task classes
CAMPAIGN_TASK_TYPES = {tup[0]: tup[1] for tup in TASK_DEFINITIONS}

# List of task result types
RESULT_TYPES = tuple([tup[2] for tup in TASK_DEFINITIONS])
