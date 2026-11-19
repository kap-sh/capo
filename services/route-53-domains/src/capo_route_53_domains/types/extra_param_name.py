"""Generated from Smithy shape ``com.amazonaws.route53domains#ExtraParamName``."""

from typing import Literal, TypeAlias, cast

ExtraParamName: TypeAlias = Literal[
    "DUNS_NUMBER",
    "BRAND_NUMBER",
    "BIRTH_DEPARTMENT",
    "BIRTH_DATE_IN_YYYY_MM_DD",
    "BIRTH_COUNTRY",
    "BIRTH_CITY",
    "DOCUMENT_NUMBER",
    "AU_ID_NUMBER",
    "AU_ID_TYPE",
    "CA_LEGAL_TYPE",
    "CA_BUSINESS_ENTITY_TYPE",
    "CA_LEGAL_REPRESENTATIVE",
    "CA_LEGAL_REPRESENTATIVE_CAPACITY",
    "ES_IDENTIFICATION",
    "ES_IDENTIFICATION_TYPE",
    "ES_LEGAL_FORM",
    "FI_BUSINESS_NUMBER",
    "FI_ID_NUMBER",
    "FI_NATIONALITY",
    "FI_ORGANIZATION_TYPE",
    "IT_NATIONALITY",
    "IT_PIN",
    "IT_REGISTRANT_ENTITY_TYPE",
    "RU_PASSPORT_DATA",
    "SE_ID_NUMBER",
    "SG_ID_NUMBER",
    "VAT_NUMBER",
    "UK_CONTACT_TYPE",
    "UK_COMPANY_NUMBER",
    "EU_COUNTRY_OF_CITIZENSHIP",
    "AU_PRIORITY_TOKEN",
    "AU_ELIGIBILITY_TYPE",
    "AU_POLICY_REASON",
    "AU_REGISTRANT_NAME",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExtraParamName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExtraParamName:
    return cast(ExtraParamName, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExtraParamName) -> str:
    return value


def deserialize_cbor(data: str) -> ExtraParamName:
    return cast(ExtraParamName, data)
