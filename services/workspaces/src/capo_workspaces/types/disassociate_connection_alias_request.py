"""Generated from Smithy shape ``com.amazonaws.workspaces#DisassociateConnectionAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.connection_alias_id


class DisassociateConnectionAliasRequest(TypedDict, closed=True):
    alias_id: "capo_workspaces.types.connection_alias_id.ConnectionAliasId"
    """<p>The identifier of the connection alias to disassociate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateConnectionAliasRequest) -> dict:
    out: dict = {}
    out["AliasId"] = value["alias_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateConnectionAliasRequest:
    out: DisassociateConnectionAliasRequest = {}  # type: ignore[typeddict-item]
    if data.get("AliasId") is not None:
        out["alias_id"] = data["AliasId"]
    else:
        out["alias_id"] = ""
    return out
