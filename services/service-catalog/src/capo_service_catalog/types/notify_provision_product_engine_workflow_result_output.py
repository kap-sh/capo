"""Generated from Smithy shape ``com.amazonaws.servicecatalog#NotifyProvisionProductEngineWorkflowResultOutput``."""

from typing_extensions import TypedDict


class NotifyProvisionProductEngineWorkflowResultOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: NotifyProvisionProductEngineWorkflowResultOutput,
) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> NotifyProvisionProductEngineWorkflowResultOutput:
    out: NotifyProvisionProductEngineWorkflowResultOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NotifyProvisionProductEngineWorkflowResultOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> NotifyProvisionProductEngineWorkflowResultOutput:
    out: NotifyProvisionProductEngineWorkflowResultOutput = {}  # type: ignore[typeddict-item]
    return out
