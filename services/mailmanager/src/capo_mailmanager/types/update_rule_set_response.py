"""Generated from Smithy shape ``com.amazonaws.mailmanager#UpdateRuleSetResponse``."""

from typing_extensions import TypedDict


class UpdateRuleSetResponse(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateRuleSetResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateRuleSetResponse:
    out: UpdateRuleSetResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateRuleSetResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UpdateRuleSetResponse:
    out: UpdateRuleSetResponse = {}  # type: ignore[typeddict-item]
    return out
