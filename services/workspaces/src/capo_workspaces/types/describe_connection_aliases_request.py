"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeConnectionAliasesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.connection_alias_id_list
    import capo_workspaces.types.limit
    import capo_workspaces.types.non_empty_string
    import capo_workspaces.types.pagination_token


class DescribeConnectionAliasesRequest(TypedDict, closed=True):
    alias_ids: NotRequired[
        "capo_workspaces.types.connection_alias_id_list.ConnectionAliasIdList"
    ]
    """<p>The identifiers of the connection aliases to describe.</p>"""
    resource_id: NotRequired["capo_workspaces.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the directory associated with the connection alias.</p>"""
    limit: NotRequired["capo_workspaces.types.limit.Limit"]
    """<p>The maximum number of connection aliases to return.</p>"""
    next_token: NotRequired["capo_workspaces.types.pagination_token.PaginationToken"]
    """<p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConnectionAliasesRequest) -> dict:
    out: dict = {}
    if "alias_ids" in value:
        import capo_workspaces.types.connection_alias_id_list

        out["AliasIds"] = (
            capo_workspaces.types.connection_alias_id_list.serialize_aws_json_1_1(
                value["alias_ids"]
            )
        )
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConnectionAliasesRequest:
    out: DescribeConnectionAliasesRequest = {}  # type: ignore[typeddict-item]
    if data.get("AliasIds") is not None:
        import capo_workspaces.types.connection_alias_id_list

        out["alias_ids"] = (
            capo_workspaces.types.connection_alias_id_list.deserialize_aws_json_1_1(
                data["AliasIds"]
            )
        )
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeConnectionAliasesRequest) -> dict:
    out: dict = {}
    if "alias_ids" in value:
        import capo_workspaces.types.connection_alias_id_list

        out["AliasIds"] = capo_workspaces.types.connection_alias_id_list.serialize_cbor(
            value["alias_ids"]
        )
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeConnectionAliasesRequest:
    out: DescribeConnectionAliasesRequest = {}  # type: ignore[typeddict-item]
    if data.get("AliasIds") is not None:
        import capo_workspaces.types.connection_alias_id_list

        out["alias_ids"] = (
            capo_workspaces.types.connection_alias_id_list.deserialize_cbor(
                data["AliasIds"]
            )
        )
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
