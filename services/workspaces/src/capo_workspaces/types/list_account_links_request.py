"""Generated from Smithy shape ``com.amazonaws.workspaces#ListAccountLinksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.limit
    import capo_workspaces.types.link_status_filter_list
    import capo_workspaces.types.pagination_token


class ListAccountLinksRequest(TypedDict, closed=True):
    link_status_filter: NotRequired[
        "capo_workspaces.types.link_status_filter_list.LinkStatusFilterList"
    ]
    """<p>Filters the account based on their link status.</p>"""
    next_token: NotRequired["capo_workspaces.types.pagination_token.PaginationToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return.</p>"""
    max_results: NotRequired["capo_workspaces.types.limit.Limit"]
    """<p>The maximum number of accounts to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAccountLinksRequest) -> dict:
    out: dict = {}
    if "link_status_filter" in value:
        import capo_workspaces.types.link_status_filter_list

        out["LinkStatusFilter"] = (
            capo_workspaces.types.link_status_filter_list.serialize_aws_json_1_1(
                value["link_status_filter"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAccountLinksRequest:
    out: ListAccountLinksRequest = {}  # type: ignore[typeddict-item]
    if data.get("LinkStatusFilter") is not None:
        import capo_workspaces.types.link_status_filter_list

        out["link_status_filter"] = (
            capo_workspaces.types.link_status_filter_list.deserialize_aws_json_1_1(
                data["LinkStatusFilter"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListAccountLinksRequest) -> dict:
    out: dict = {}
    if "link_status_filter" in value:
        import capo_workspaces.types.link_status_filter_list

        out["LinkStatusFilter"] = (
            capo_workspaces.types.link_status_filter_list.serialize_cbor(
                value["link_status_filter"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_cbor(data: dict) -> ListAccountLinksRequest:
    out: ListAccountLinksRequest = {}  # type: ignore[typeddict-item]
    if data.get("LinkStatusFilter") is not None:
        import capo_workspaces.types.link_status_filter_list

        out["link_status_filter"] = (
            capo_workspaces.types.link_status_filter_list.deserialize_cbor(
                data["LinkStatusFilter"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
