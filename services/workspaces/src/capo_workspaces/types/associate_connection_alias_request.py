"""Generated from Smithy shape ``com.amazonaws.workspaces#AssociateConnectionAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.connection_alias_id
    import capo_workspaces.types.non_empty_string


class AssociateConnectionAliasRequest(TypedDict, closed=True):
    alias_id: "capo_workspaces.types.connection_alias_id.ConnectionAliasId"
    """<p>The identifier of the connection alias.</p>"""
    resource_id: "capo_workspaces.types.non_empty_string.NonEmptyString"
    """<p>The identifier of the directory to associate the connection alias with.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateConnectionAliasRequest) -> dict:
    out: dict = {}
    out["AliasId"] = value["alias_id"]
    out["ResourceId"] = value["resource_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateConnectionAliasRequest:
    out: AssociateConnectionAliasRequest = {}  # type: ignore[typeddict-item]
    if data.get("AliasId") is not None:
        out["alias_id"] = data["AliasId"]
    else:
        out["alias_id"] = ""
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    return out
