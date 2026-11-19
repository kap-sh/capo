"""Generated from Smithy shape ``com.amazonaws.workspaces#RevokeIpRulesResult``."""

from typing_extensions import TypedDict


class RevokeIpRulesResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RevokeIpRulesResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> RevokeIpRulesResult:
    out: RevokeIpRulesResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RevokeIpRulesResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> RevokeIpRulesResult:
    out: RevokeIpRulesResult = {}  # type: ignore[typeddict-item]
    return out
