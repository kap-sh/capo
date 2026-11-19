"""Generated from Smithy shape ``com.amazonaws.workspaces#UpdateConnectionAliasPermissionResult``."""

from typing_extensions import TypedDict


class UpdateConnectionAliasPermissionResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateConnectionAliasPermissionResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateConnectionAliasPermissionResult:
    out: UpdateConnectionAliasPermissionResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateConnectionAliasPermissionResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UpdateConnectionAliasPermissionResult:
    out: UpdateConnectionAliasPermissionResult = {}  # type: ignore[typeddict-item]
    return out
