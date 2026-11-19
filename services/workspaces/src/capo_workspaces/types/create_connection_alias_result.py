"""Generated from Smithy shape ``com.amazonaws.workspaces#CreateConnectionAliasResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.connection_alias_id


class CreateConnectionAliasResult(TypedDict, closed=True):
    alias_id: NotRequired["capo_workspaces.types.connection_alias_id.ConnectionAliasId"]
    """<p>The identifier of the connection alias.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateConnectionAliasResult) -> dict:
    out: dict = {}
    if "alias_id" in value:
        out["AliasId"] = value["alias_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateConnectionAliasResult:
    out: CreateConnectionAliasResult = {}  # type: ignore[typeddict-item]
    if data.get("AliasId") is not None:
        out["alias_id"] = data["AliasId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateConnectionAliasResult) -> dict:
    out: dict = {}
    if "alias_id" in value:
        out["AliasId"] = value["alias_id"]
    return out


def deserialize_cbor(data: dict) -> CreateConnectionAliasResult:
    out: CreateConnectionAliasResult = {}  # type: ignore[typeddict-item]
    if data.get("AliasId") is not None:
        out["alias_id"] = data["AliasId"]
    return out
