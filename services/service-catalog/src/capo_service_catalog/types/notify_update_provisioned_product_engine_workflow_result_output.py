"""Generated from Smithy shape ``com.amazonaws.servicecatalog#NotifyUpdateProvisionedProductEngineWorkflowResultOutput``."""

from typing_extensions import TypedDict


class NotifyUpdateProvisionedProductEngineWorkflowResultOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: NotifyUpdateProvisionedProductEngineWorkflowResultOutput,
) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> NotifyUpdateProvisionedProductEngineWorkflowResultOutput:
    out: NotifyUpdateProvisionedProductEngineWorkflowResultOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(
    value: NotifyUpdateProvisionedProductEngineWorkflowResultOutput,
) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(
    data: dict,
) -> NotifyUpdateProvisionedProductEngineWorkflowResultOutput:
    out: NotifyUpdateProvisionedProductEngineWorkflowResultOutput = {}  # type: ignore[typeddict-item]
    return out
