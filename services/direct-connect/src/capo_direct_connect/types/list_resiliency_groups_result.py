"""Generated from Smithy shape ``com.amazonaws.directconnect#ListResiliencyGroupsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.pagination_token
    import capo_direct_connect.types.resiliency_group_summary_list


class ListResiliencyGroupsResult(TypedDict, closed=True):
    items: NotRequired[
        "capo_direct_connect.types.resiliency_group_summary_list.ResiliencyGroupSummaryList"
    ]
    """<p>Summary information about the resiliency groups.</p>"""
    next_token: NotRequired[
        "capo_direct_connect.types.pagination_token.PaginationToken"
    ]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResiliencyGroupsResult) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_direct_connect.types.resiliency_group_summary_list

        out["items"] = (
            capo_direct_connect.types.resiliency_group_summary_list.serialize_aws_json_1_1(
                value["items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResiliencyGroupsResult:
    out: ListResiliencyGroupsResult = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_direct_connect.types.resiliency_group_summary_list

        out["items"] = (
            capo_direct_connect.types.resiliency_group_summary_list.deserialize_aws_json_1_1(
                data["items"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListResiliencyGroupsResult) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_direct_connect.types.resiliency_group_summary_list

        out["items"] = (
            capo_direct_connect.types.resiliency_group_summary_list.serialize_cbor(
                value["items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListResiliencyGroupsResult:
    out: ListResiliencyGroupsResult = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_direct_connect.types.resiliency_group_summary_list

        out["items"] = (
            capo_direct_connect.types.resiliency_group_summary_list.deserialize_cbor(
                data["items"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
