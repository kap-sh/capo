"""Generated from Smithy shape ``com.amazonaws.wafv2#ListMobileSdkReleasesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.next_marker
    import capo_wafv2.types.pagination_limit
    import capo_wafv2.types.platform


class ListMobileSdkReleasesRequest(TypedDict, closed=True):
    platform: "capo_wafv2.types.platform.Platform"
    """<p>The device platform to retrieve the list for.</p>"""
    next_marker: NotRequired["capo_wafv2.types.next_marker.NextMarker"]
    """<p>When you request a list of objects with a <code>Limit</code> setting, if the number of objects that are still available for retrieval exceeds the limit, WAF returns a <code>NextMarker</code> value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.</p>"""
    limit: NotRequired["capo_wafv2.types.pagination_limit.PaginationLimit"]
    """<p>The maximum number of objects that you want WAF to return for this request. If more objects are available, in the response, WAF provides a <code>NextMarker</code> value that you can use in a subsequent call to get the next batch of objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMobileSdkReleasesRequest) -> dict:
    out: dict = {}
    import capo_wafv2.types.platform

    out["Platform"] = capo_wafv2.types.platform.serialize_aws_json_1_1(
        value["platform"]
    )
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMobileSdkReleasesRequest:
    out: ListMobileSdkReleasesRequest = {}  # type: ignore[typeddict-item]
    if data.get("Platform") is not None:
        import capo_wafv2.types.platform

        out["platform"] = capo_wafv2.types.platform.deserialize_aws_json_1_1(
            data["Platform"]
        )
    else:
        import typing

        out["platform"] = typing.cast("capo_wafv2.types.platform.Platform", "")
    if data.get("NextMarker") is not None:
        out["next_marker"] = data["NextMarker"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    return out
