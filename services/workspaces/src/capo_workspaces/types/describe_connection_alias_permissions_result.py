"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeConnectionAliasPermissionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.connection_alias_id
    import capo_workspaces.types.connection_alias_permissions
    import capo_workspaces.types.pagination_token


class DescribeConnectionAliasPermissionsResult(TypedDict, closed=True):
    alias_id: NotRequired["capo_workspaces.types.connection_alias_id.ConnectionAliasId"]
    """<p>The identifier of the connection alias.</p>"""
    connection_alias_permissions: NotRequired[
        "capo_workspaces.types.connection_alias_permissions.ConnectionAliasPermissions"
    ]
    """<p>The permissions associated with a connection alias.</p>"""
    next_token: NotRequired["capo_workspaces.types.pagination_token.PaginationToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConnectionAliasPermissionsResult) -> dict:
    out: dict = {}
    if "alias_id" in value:
        out["AliasId"] = value["alias_id"]
    if "connection_alias_permissions" in value:
        import capo_workspaces.types.connection_alias_permissions

        out["ConnectionAliasPermissions"] = (
            capo_workspaces.types.connection_alias_permissions.serialize_aws_json_1_1(
                value["connection_alias_permissions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConnectionAliasPermissionsResult:
    out: DescribeConnectionAliasPermissionsResult = {}  # type: ignore[typeddict-item]
    if data.get("AliasId") is not None:
        out["alias_id"] = data["AliasId"]
    if data.get("ConnectionAliasPermissions") is not None:
        import capo_workspaces.types.connection_alias_permissions

        out["connection_alias_permissions"] = (
            capo_workspaces.types.connection_alias_permissions.deserialize_aws_json_1_1(
                data["ConnectionAliasPermissions"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeConnectionAliasPermissionsResult) -> dict:
    out: dict = {}
    if "alias_id" in value:
        out["AliasId"] = value["alias_id"]
    if "connection_alias_permissions" in value:
        import capo_workspaces.types.connection_alias_permissions

        out["ConnectionAliasPermissions"] = (
            capo_workspaces.types.connection_alias_permissions.serialize_cbor(
                value["connection_alias_permissions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeConnectionAliasPermissionsResult:
    out: DescribeConnectionAliasPermissionsResult = {}  # type: ignore[typeddict-item]
    if data.get("AliasId") is not None:
        out["alias_id"] = data["AliasId"]
    if data.get("ConnectionAliasPermissions") is not None:
        import capo_workspaces.types.connection_alias_permissions

        out["connection_alias_permissions"] = (
            capo_workspaces.types.connection_alias_permissions.deserialize_cbor(
                data["ConnectionAliasPermissions"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
