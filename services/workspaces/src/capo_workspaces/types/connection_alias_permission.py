"""Generated from Smithy shape ``com.amazonaws.workspaces#ConnectionAliasPermission``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.aws_account
    import capo_workspaces.types.boolean_object


class ConnectionAliasPermission(TypedDict, closed=True):
    shared_account_id: "capo_workspaces.types.aws_account.AwsAccount"
    """<p>The identifier of the Amazon Web Services account that the connection alias is shared with.</p>"""
    allow_association: "capo_workspaces.types.boolean_object.BooleanObject"
    """<p>Indicates whether the specified Amazon Web Services account is allowed to associate the connection alias with a directory.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionAliasPermission) -> dict:
    out: dict = {}
    out["SharedAccountId"] = value["shared_account_id"]
    out["AllowAssociation"] = value["allow_association"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectionAliasPermission:
    out: ConnectionAliasPermission = {}  # type: ignore[typeddict-item]
    if data.get("SharedAccountId") is not None:
        out["shared_account_id"] = data["SharedAccountId"]
    else:
        out["shared_account_id"] = ""
    if data.get("AllowAssociation") is not None:
        out["allow_association"] = data["AllowAssociation"]
    else:
        out["allow_association"] = False
    return out
