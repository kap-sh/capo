"""Generated from Smithy shape ``com.amazonaws.workspaces#UpdateRulesOfIpGroupResult``."""

from typing_extensions import TypedDict


class UpdateRulesOfIpGroupResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateRulesOfIpGroupResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateRulesOfIpGroupResult:
    out: UpdateRulesOfIpGroupResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateRulesOfIpGroupResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UpdateRulesOfIpGroupResult:
    out: UpdateRulesOfIpGroupResult = {}  # type: ignore[typeddict-item]
    return out
