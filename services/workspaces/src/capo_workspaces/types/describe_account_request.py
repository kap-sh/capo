"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeAccountRequest``."""

from typing_extensions import TypedDict


class DescribeAccountRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAccountRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAccountRequest:
    out: DescribeAccountRequest = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeAccountRequest) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DescribeAccountRequest:
    out: DescribeAccountRequest = {}  # type: ignore[typeddict-item]
    return out
