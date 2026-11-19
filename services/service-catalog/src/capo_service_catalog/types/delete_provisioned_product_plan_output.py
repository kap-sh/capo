"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DeleteProvisionedProductPlanOutput``."""

from typing_extensions import TypedDict


class DeleteProvisionedProductPlanOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteProvisionedProductPlanOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteProvisionedProductPlanOutput:
    out: DeleteProvisionedProductPlanOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteProvisionedProductPlanOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteProvisionedProductPlanOutput:
    out: DeleteProvisionedProductPlanOutput = {}  # type: ignore[typeddict-item]
    return out
