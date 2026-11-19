"""Generated from Smithy shape ``com.amazonaws.workspaces#DeleteConnectionAliasResult``."""

from typing_extensions import TypedDict


class DeleteConnectionAliasResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteConnectionAliasResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteConnectionAliasResult:
    out: DeleteConnectionAliasResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteConnectionAliasResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteConnectionAliasResult:
    out: DeleteConnectionAliasResult = {}  # type: ignore[typeddict-item]
    return out
