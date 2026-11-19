"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisionedProductStatus``."""

from typing import Literal, TypeAlias, cast

ProvisionedProductStatus: TypeAlias = Literal[
    "AVAILABLE",
    "UNDER_CHANGE",
    "TAINTED",
    "ERROR",
    "PLAN_IN_PROGRESS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisionedProductStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProvisionedProductStatus:
    return cast(ProvisionedProductStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProvisionedProductStatus) -> str:
    return value


def deserialize_cbor(data: str) -> ProvisionedProductStatus:
    return cast(ProvisionedProductStatus, data)
