"""Generated from Smithy shape ``com.amazonaws.fms#ListAppsListsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.apps_lists_data
    import capo_fms.types.pagination_token


class ListAppsListsResponse(TypedDict, closed=True):
    apps_lists: NotRequired["capo_fms.types.apps_lists_data.AppsListsData"]
    """<p>An array of <code>AppsListDataSummary</code> objects.</p>"""
    next_token: NotRequired["capo_fms.types.pagination_token.PaginationToken"]
    """<p>If you specify a value for <code>MaxResults</code> in your list request, and you have more objects than the maximum, Firewall Manager returns this token in the response. You can use this token in subsequent requests to retrieve the next batch of objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAppsListsResponse) -> dict:
    out: dict = {}
    if "apps_lists" in value:
        import capo_fms.types.apps_lists_data

        out["AppsLists"] = capo_fms.types.apps_lists_data.serialize_aws_json_1_1(
            value["apps_lists"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAppsListsResponse:
    out: ListAppsListsResponse = {}  # type: ignore[typeddict-item]
    if data.get("AppsLists") is not None:
        import capo_fms.types.apps_lists_data

        out["apps_lists"] = capo_fms.types.apps_lists_data.deserialize_aws_json_1_1(
            data["AppsLists"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListAppsListsResponse) -> dict:
    out: dict = {}
    if "apps_lists" in value:
        import capo_fms.types.apps_lists_data

        out["AppsLists"] = capo_fms.types.apps_lists_data.serialize_cbor(
            value["apps_lists"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListAppsListsResponse:
    out: ListAppsListsResponse = {}  # type: ignore[typeddict-item]
    if data.get("AppsLists") is not None:
        import capo_fms.types.apps_lists_data

        out["apps_lists"] = capo_fms.types.apps_lists_data.deserialize_cbor(
            data["AppsLists"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
