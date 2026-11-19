"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisionedProductPlanStatus``."""

from typing import Literal, TypeAlias, cast

ProvisionedProductPlanStatus: TypeAlias = Literal[
    "CREATE_IN_PROGRESS",
    "CREATE_SUCCESS",
    "CREATE_FAILED",
    "EXECUTE_IN_PROGRESS",
    "EXECUTE_SUCCESS",
    "EXECUTE_FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisionedProductPlanStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProvisionedProductPlanStatus:
    return cast(ProvisionedProductPlanStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProvisionedProductPlanStatus) -> str:
    return value


def deserialize_cbor(data: str) -> ProvisionedProductPlanStatus:
    return cast(ProvisionedProductPlanStatus, data)
