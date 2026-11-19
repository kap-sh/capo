"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LicenseModel``."""

from typing import Literal, TypeAlias, cast

LicenseModel: TypeAlias = Literal[
    "LicenseIncluded",
    "BringYourOwnLicense",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LicenseModel) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LicenseModel:
    return cast(LicenseModel, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LicenseModel) -> str:
    return value


def deserialize_cbor(data: str) -> LicenseModel:
    return cast(LicenseModel, data)
