"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#DeleteAutomationRuleResponse``."""

from typing_extensions import TypedDict


class DeleteAutomationRuleResponse(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteAutomationRuleResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteAutomationRuleResponse:
    out: DeleteAutomationRuleResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteAutomationRuleResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteAutomationRuleResponse:
    out: DeleteAutomationRuleResponse = {}  # type: ignore[typeddict-item]
    return out
