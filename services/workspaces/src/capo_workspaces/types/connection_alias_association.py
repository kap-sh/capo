"""Generated from Smithy shape ``com.amazonaws.workspaces#ConnectionAliasAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.association_status
    import capo_workspaces.types.aws_account
    import capo_workspaces.types.connection_identifier
    import capo_workspaces.types.non_empty_string


class ConnectionAliasAssociation(TypedDict, closed=True):
    association_status: NotRequired[
        "capo_workspaces.types.association_status.AssociationStatus"
    ]
    """<p>The association status of the connection alias.</p>"""
    associated_account_id: NotRequired["capo_workspaces.types.aws_account.AwsAccount"]
    """<p>The identifier of the Amazon Web Services account that associated the connection alias with a directory.</p>"""
    resource_id: NotRequired["capo_workspaces.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the directory associated with a connection alias.</p>"""
    connection_identifier: NotRequired[
        "capo_workspaces.types.connection_identifier.ConnectionIdentifier"
    ]
    """<p>The identifier of the connection alias association. You use the connection identifier in the DNS TXT record when you're configuring your DNS routing policies.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionAliasAssociation) -> dict:
    out: dict = {}
    if "association_status" in value:
        import capo_workspaces.types.association_status

        out["AssociationStatus"] = (
            capo_workspaces.types.association_status.serialize_aws_json_1_1(
                value["association_status"]
            )
        )
    if "associated_account_id" in value:
        out["AssociatedAccountId"] = value["associated_account_id"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "connection_identifier" in value:
        out["ConnectionIdentifier"] = value["connection_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectionAliasAssociation:
    out: ConnectionAliasAssociation = {}  # type: ignore[typeddict-item]
    if data.get("AssociationStatus") is not None:
        import capo_workspaces.types.association_status

        out["association_status"] = (
            capo_workspaces.types.association_status.deserialize_aws_json_1_1(
                data["AssociationStatus"]
            )
        )
    if data.get("AssociatedAccountId") is not None:
        out["associated_account_id"] = data["AssociatedAccountId"]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    if data.get("ConnectionIdentifier") is not None:
        out["connection_identifier"] = data["ConnectionIdentifier"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConnectionAliasAssociation) -> dict:
    out: dict = {}
    if "association_status" in value:
        import capo_workspaces.types.association_status

        out["AssociationStatus"] = (
            capo_workspaces.types.association_status.serialize_cbor(
                value["association_status"]
            )
        )
    if "associated_account_id" in value:
        out["AssociatedAccountId"] = value["associated_account_id"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "connection_identifier" in value:
        out["ConnectionIdentifier"] = value["connection_identifier"]
    return out


def deserialize_cbor(data: dict) -> ConnectionAliasAssociation:
    out: ConnectionAliasAssociation = {}  # type: ignore[typeddict-item]
    if data.get("AssociationStatus") is not None:
        import capo_workspaces.types.association_status

        out["association_status"] = (
            capo_workspaces.types.association_status.deserialize_cbor(
                data["AssociationStatus"]
            )
        )
    if data.get("AssociatedAccountId") is not None:
        out["associated_account_id"] = data["AssociatedAccountId"]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    if data.get("ConnectionIdentifier") is not None:
        out["connection_identifier"] = data["ConnectionIdentifier"]
    return out
