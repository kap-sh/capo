"""Generated from Smithy shape ``com.amazonaws.comprehend#PiiEntityType``."""

from typing import Literal, TypeAlias, cast

PiiEntityType: TypeAlias = Literal[
    "BANK_ACCOUNT_NUMBER",
    "BANK_ROUTING",
    "CREDIT_DEBIT_NUMBER",
    "CREDIT_DEBIT_CVV",
    "CREDIT_DEBIT_EXPIRY",
    "PIN",
    "EMAIL",
    "ADDRESS",
    "NAME",
    "PHONE",
    "SSN",
    "DATE_TIME",
    "PASSPORT_NUMBER",
    "DRIVER_ID",
    "URL",
    "AGE",
    "USERNAME",
    "PASSWORD",
    "AWS_ACCESS_KEY",
    "AWS_SECRET_KEY",
    "IP_ADDRESS",
    "MAC_ADDRESS",
    "ALL",
    "LICENSE_PLATE",
    "VEHICLE_IDENTIFICATION_NUMBER",
    "UK_NATIONAL_INSURANCE_NUMBER",
    "CA_SOCIAL_INSURANCE_NUMBER",
    "US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER",
    "UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER",
    "IN_PERMANENT_ACCOUNT_NUMBER",
    "IN_NREGA",
    "INTERNATIONAL_BANK_ACCOUNT_NUMBER",
    "SWIFT_CODE",
    "UK_NATIONAL_HEALTH_SERVICE_NUMBER",
    "CA_HEALTH_NUMBER",
    "IN_AADHAAR",
    "IN_VOTER_NUMBER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PiiEntityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PiiEntityType:
    return cast(PiiEntityType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PiiEntityType) -> str:
    return value


def deserialize_cbor(data: str) -> PiiEntityType:
    return cast(PiiEntityType, data)
