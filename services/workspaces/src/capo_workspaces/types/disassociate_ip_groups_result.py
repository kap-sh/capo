"""Generated from Smithy shape ``com.amazonaws.workspaces#DisassociateIpGroupsResult``."""

from typing_extensions import TypedDict


class DisassociateIpGroupsResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateIpGroupsResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateIpGroupsResult:
    out: DisassociateIpGroupsResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DisassociateIpGroupsResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DisassociateIpGroupsResult:
    out: DisassociateIpGroupsResult = {}  # type: ignore[typeddict-item]
    return out
