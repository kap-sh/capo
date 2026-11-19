"""Generated from Smithy shape ``com.amazonaws.workspaces#DisassociateConnectionAliasResult``."""

from typing_extensions import TypedDict


class DisassociateConnectionAliasResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateConnectionAliasResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateConnectionAliasResult:
    out: DisassociateConnectionAliasResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DisassociateConnectionAliasResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DisassociateConnectionAliasResult:
    out: DisassociateConnectionAliasResult = {}  # type: ignore[typeddict-item]
    return out
