"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeConnectionAliasesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.connection_alias_list
    import capo_workspaces.types.pagination_token


class DescribeConnectionAliasesResult(TypedDict, closed=True):
    connection_aliases: NotRequired[
        "capo_workspaces.types.connection_alias_list.ConnectionAliasList"
    ]
    """<p>Information about the specified connection aliases.</p>"""
    next_token: NotRequired["capo_workspaces.types.pagination_token.PaginationToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConnectionAliasesResult) -> dict:
    out: dict = {}
    if "connection_aliases" in value:
        import capo_workspaces.types.connection_alias_list

        out["ConnectionAliases"] = (
            capo_workspaces.types.connection_alias_list.serialize_aws_json_1_1(
                value["connection_aliases"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConnectionAliasesResult:
    out: DescribeConnectionAliasesResult = {}  # type: ignore[typeddict-item]
    if data.get("ConnectionAliases") is not None:
        import capo_workspaces.types.connection_alias_list

        out["connection_aliases"] = (
            capo_workspaces.types.connection_alias_list.deserialize_aws_json_1_1(
                data["ConnectionAliases"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeConnectionAliasesResult) -> dict:
    out: dict = {}
    if "connection_aliases" in value:
        import capo_workspaces.types.connection_alias_list

        out["ConnectionAliases"] = (
            capo_workspaces.types.connection_alias_list.serialize_cbor(
                value["connection_aliases"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeConnectionAliasesResult:
    out: DescribeConnectionAliasesResult = {}  # type: ignore[typeddict-item]
    if data.get("ConnectionAliases") is not None:
        import capo_workspaces.types.connection_alias_list

        out["connection_aliases"] = (
            capo_workspaces.types.connection_alias_list.deserialize_cbor(
                data["ConnectionAliases"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
