"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#EntitySubType``."""

from typing import Literal, TypeAlias, cast

EntitySubType: TypeAlias = Literal[
    "NAME",
    "DX_NAME",
    "DOSAGE",
    "ROUTE_OR_MODE",
    "FORM",
    "FREQUENCY",
    "DURATION",
    "GENERIC_NAME",
    "BRAND_NAME",
    "STRENGTH",
    "RATE",
    "ACUITY",
    "TEST_NAME",
    "TEST_VALUE",
    "TEST_UNITS",
    "TEST_UNIT",
    "PROCEDURE_NAME",
    "TREATMENT_NAME",
    "DATE",
    "AGE",
    "CONTACT_POINT",
    "PHONE_OR_FAX",
    "EMAIL",
    "IDENTIFIER",
    "ID",
    "URL",
    "ADDRESS",
    "PROFESSION",
    "SYSTEM_ORGAN_SITE",
    "DIRECTION",
    "QUALITY",
    "QUANTITY",
    "TIME_EXPRESSION",
    "TIME_TO_MEDICATION_NAME",
    "TIME_TO_DX_NAME",
    "TIME_TO_TEST_NAME",
    "TIME_TO_PROCEDURE_NAME",
    "TIME_TO_TREATMENT_NAME",
    "AMOUNT",
    "GENDER",
    "RACE_ETHNICITY",
    "ALLERGIES",
    "TOBACCO_USE",
    "ALCOHOL_CONSUMPTION",
    "REC_DRUG_USE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntitySubType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EntitySubType:
    return cast(EntitySubType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EntitySubType) -> str:
    return value


def deserialize_cbor(data: str) -> EntitySubType:
    return cast(EntitySubType, data)
