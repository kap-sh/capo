"""Generated from Smithy shape ``com.amazonaws.codebuild#ListSourceCredentialsInput``."""

from typing_extensions import TypedDict


class ListSourceCredentialsInput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSourceCredentialsInput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSourceCredentialsInput:
    out: ListSourceCredentialsInput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListSourceCredentialsInput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> ListSourceCredentialsInput:
    out: ListSourceCredentialsInput = {}  # type: ignore[typeddict-item]
    return out
