"""Generated from Smithy shape ``com.amazonaws.transcribe#PiiEntityType``."""

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
    "LICENSE_PLATE",
    "VEHICLE_IDENTIFICATION_NUMBER",
    "US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER",
    "CA_HEALTH_NUMBER",
    "CA_SOCIAL_INSURANCE_NUMBER",
    "INTERNATIONAL_BANK_ACCOUNT_NUMBER",
    "SWIFT_CODE",
    "ALL",
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
