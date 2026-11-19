"""Generated from Smithy shape ``com.amazonaws.workspaces#ModifySamlPropertiesResult``."""

from typing_extensions import TypedDict


class ModifySamlPropertiesResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifySamlPropertiesResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifySamlPropertiesResult:
    out: ModifySamlPropertiesResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ModifySamlPropertiesResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> ModifySamlPropertiesResult:
    out: ModifySamlPropertiesResult = {}  # type: ignore[typeddict-item]
    return out
