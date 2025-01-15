#!/usr/bin/env python3

#
# Example Program to Demonstrate Validation of the BasicStudyDesign JSON Template
#

import sys
import os
import json
from pathlib import Path
import jsonschema
import jsonschema.validators

from referencing import Registry, Resource
from referencing.exceptions import NoSuchResource

from jsonschema import validate
from jsonschema.exceptions import ValidationError

#
# Load in the JSON Instance
#
with open('../examples/basic_study_design.json','r') as f:
    document = json.load(f)

#
# Load in the JSON Schema
#
with open('../json-templates/basic_study_design.json','r') as f:
    schema = json.load(f)

with open('../json-templates/basic_study_design.study.json','r') as f:
    basic_study_design_study = Resource.from_contents(json.load(f))
with open('../json-templates/basic_study_design.studyCategorization.json','r') as f:
    basic_study_design_studyCategorization = Resource.from_contents(json.load(f))
with open('../json-templates/basic_study_design.study2ConditionOrDisease.json','r') as f:
    basic_study_design_study2ConditionOrDisease = Resource.from_contents(json.load(f))
with open('../json-templates/basic_study_design.armOrCohort.json','r') as f:
    basic_study_design_armOrCohort = Resource.from_contents(json.load(f))
with open('../json-templates/basic_study_design.studyPersonnel.json','r') as f:
    basic_study_design_studyPersonnel = Resource.from_contents(json.load(f))
with open('../json-templates/basic_study_design.plannedVisit.json','r') as f:
    basic_study_design_plannedVisit = Resource.from_contents(json.load(f))
with open('../json-templates/basic_study_design.inclusionExclusion.json','r') as f:
    basic_study_design_inclusionExclusion = Resource.from_contents(json.load(f))
with open('../json-templates/basic_study_design.study2Protocol.json','r') as f:
    basic_study_design_study2Protocol = Resource.from_contents(json.load(f))
with open('../json-templates/basic_study_design.studyFile.json','r') as f:
    basic_study_design_studyFile = Resource.from_contents(json.load(f))
with open('../json-templates/basic_study_design.studyLink.json','r') as f:
    basic_study_design_studyLink = Resource.from_contents(json.load(f))
with open('../json-templates/basic_study_design.studyPubmed.json','r') as f:
    basic_study_design_studyPubmed = Resource.from_contents(json.load(f))

registry = Registry().with_resources(
    [
        ("basic_study_design.study.json", basic_study_design_study),
        ("basic_study_design.studyCategorization.json", basic_study_design_studyCategorization),
        ("basic_study_design.study2ConditionOrDisease.json", basic_study_design_study2ConditionOrDisease),
        ("basic_study_design.armOrCohort.json", basic_study_design_armOrCohort),
        ("basic_study_design.studyPersonnel.json", basic_study_design_studyPersonnel),
        ("basic_study_design.plannedVisit.json", basic_study_design_plannedVisit),
        ("basic_study_design.inclusionExclusion.json", basic_study_design_inclusionExclusion),
        ("basic_study_design.study2Protocol.json", basic_study_design_study2Protocol),
        ("basic_study_design.studyFile.json", basic_study_design_studyFile),
        ("basic_study_design.studyLink.json", basic_study_design_studyLink),
        ("basic_study_design.studyPubmed.json", basic_study_design_studyPubmed)
    ]
)

#
# Validate the Instance against the Schema
#
try:
    validate(document, schema, registry=registry)
    print("Validation Completed No Errors")
except ValidationError as e:
    print("Validation failed!")
    print(f"Error message: {e.message}")

