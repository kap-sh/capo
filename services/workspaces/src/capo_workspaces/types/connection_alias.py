"""Generated from Smithy shape ``com.amazonaws.workspaces#ConnectionAlias``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.aws_account
    import capo_workspaces.types.connection_alias_association_list
    import capo_workspaces.types.connection_alias_id
    import capo_workspaces.types.connection_alias_state
    import capo_workspaces.types.connection_string


class ConnectionAlias(TypedDict, closed=True):
    connection_string: NotRequired[
        "capo_workspaces.types.connection_string.ConnectionString"
    ]
    """<p>The connection string specified for the connection alias. The connection string must be in the form of a fully qualified domain name (FQDN), such as <code>www.example.com</code>.</p>"""
    alias_id: NotRequired["capo_workspaces.types.connection_alias_id.ConnectionAliasId"]
    """<p>The identifier of the connection alias.</p>"""
    state: NotRequired[
        "capo_workspaces.types.connection_alias_state.ConnectionAliasState"
    ]
    """<p>The current state of the connection alias.</p>"""
    owner_account_id: NotRequired["capo_workspaces.types.aws_account.AwsAccount"]
    """<p>The identifier of the Amazon Web Services account that owns the connection alias.</p>"""
    associations: NotRequired[
        "capo_workspaces.types.connection_alias_association_list.ConnectionAliasAssociationList"
    ]
    """<p>The association status of the connection alias.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionAlias) -> dict:
    out: dict = {}
    if "connection_string" in value:
        out["ConnectionString"] = value["connection_string"]
    if "alias_id" in value:
        out["AliasId"] = value["alias_id"]
    if "state" in value:
        import capo_workspaces.types.connection_alias_state

        out["State"] = (
            capo_workspaces.types.connection_alias_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "owner_account_id" in value:
        out["OwnerAccountId"] = value["owner_account_id"]
    if "associations" in value:
        import capo_workspaces.types.connection_alias_association_list

        out["Associations"] = (
            capo_workspaces.types.connection_alias_association_list.serialize_aws_json_1_1(
                value["associations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectionAlias:
    out: ConnectionAlias = {}  # type: ignore[typeddict-item]
    if data.get("ConnectionString") is not None:
        out["connection_string"] = data["ConnectionString"]
    if data.get("AliasId") is not None:
        out["alias_id"] = data["AliasId"]
    if data.get("State") is not None:
        import capo_workspaces.types.connection_alias_state

        out["state"] = (
            capo_workspaces.types.connection_alias_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if data.get("OwnerAccountId") is not None:
        out["owner_account_id"] = data["OwnerAccountId"]
    if data.get("Associations") is not None:
        import capo_workspaces.types.connection_alias_association_list

        out["associations"] = (
            capo_workspaces.types.connection_alias_association_list.deserialize_aws_json_1_1(
                data["Associations"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConnectionAlias) -> dict:
    out: dict = {}
    if "connection_string" in value:
        out["ConnectionString"] = value["connection_string"]
    if "alias_id" in value:
        out["AliasId"] = value["alias_id"]
    if "state" in value:
        import capo_workspaces.types.connection_alias_state

        out["State"] = capo_workspaces.types.connection_alias_state.serialize_cbor(
            value["state"]
        )
    if "owner_account_id" in value:
        out["OwnerAccountId"] = value["owner_account_id"]
    if "associations" in value:
        import capo_workspaces.types.connection_alias_association_list

        out["Associations"] = (
            capo_workspaces.types.connection_alias_association_list.serialize_cbor(
                value["associations"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ConnectionAlias:
    out: ConnectionAlias = {}  # type: ignore[typeddict-item]
    if data.get("ConnectionString") is not None:
        out["connection_string"] = data["ConnectionString"]
    if data.get("AliasId") is not None:
        out["alias_id"] = data["AliasId"]
    if data.get("State") is not None:
        import capo_workspaces.types.connection_alias_state

        out["state"] = capo_workspaces.types.connection_alias_state.deserialize_cbor(
            data["State"]
        )
    if data.get("OwnerAccountId") is not None:
        out["owner_account_id"] = data["OwnerAccountId"]
    if data.get("Associations") is not None:
        import capo_workspaces.types.connection_alias_association_list

        out["associations"] = (
            capo_workspaces.types.connection_alias_association_list.deserialize_cbor(
                data["Associations"]
            )
        )
    return out
