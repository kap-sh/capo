"""Generated from Smithy shape ``com.amazonaws.workspaces#AssociateConnectionAliasResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.connection_identifier


class AssociateConnectionAliasResult(TypedDict, closed=True):
    connection_identifier: NotRequired[
        "capo_workspaces.types.connection_identifier.ConnectionIdentifier"
    ]
    """<p>The identifier of the connection alias association. You use the connection identifier in the DNS TXT record when you're configuring your DNS routing policies. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateConnectionAliasResult) -> dict:
    out: dict = {}
    if "connection_identifier" in value:
        out["ConnectionIdentifier"] = value["connection_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateConnectionAliasResult:
    out: AssociateConnectionAliasResult = {}  # type: ignore[typeddict-item]
    if data.get("ConnectionIdentifier") is not None:
        out["connection_identifier"] = data["ConnectionIdentifier"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AssociateConnectionAliasResult) -> dict:
    out: dict = {}
    if "connection_identifier" in value:
        out["ConnectionIdentifier"] = value["connection_identifier"]
    return out


def deserialize_cbor(data: dict) -> AssociateConnectionAliasResult:
    out: AssociateConnectionAliasResult = {}  # type: ignore[typeddict-item]
    if data.get("ConnectionIdentifier") is not None:
        out["connection_identifier"] = data["ConnectionIdentifier"]
    return out
