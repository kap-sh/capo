"""Generated from Smithy shape ``com.amazonaws.health#DescribeEventTypesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.event_type_filter
    import capo_health.types.locale
    import capo_health.types.max_results
    import capo_health.types.next_token


class DescribeEventTypesRequest(TypedDict, closed=True):
    filter: NotRequired["capo_health.types.event_type_filter.EventTypeFilter"]
    """<p>Values to narrow the results returned.</p>"""
    locale: NotRequired["capo_health.types.locale.locale"]
    """<p>The locale (language) to return information in. English (en) is the default and the only supported value at this time.</p>"""
    next_token: NotRequired["capo_health.types.next_token.nextToken"]
    """<p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.</p>"""
    max_results: NotRequired["capo_health.types.max_results.maxResults"]
    """<p>The maximum number of items to return in one batch, between 10 and 100, inclusive.</p> <note> <p>If you don't specify the <code>maxResults</code> parameter, this operation returns a maximum of 30 items by default.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventTypesRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import capo_health.types.event_type_filter

        out["filter"] = capo_health.types.event_type_filter.serialize_aws_json_1_1(
            value["filter"]
        )
    if "locale" in value:
        out["locale"] = value["locale"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEventTypesRequest:
    out: DescribeEventTypesRequest = {}  # type: ignore[typeddict-item]
    if data.get("filter") is not None:
        import capo_health.types.event_type_filter

        out["filter"] = capo_health.types.event_type_filter.deserialize_aws_json_1_1(
            data["filter"]
        )
    if data.get("locale") is not None:
        out["locale"] = data["locale"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeEventTypesRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import capo_health.types.event_type_filter

        out["filter"] = capo_health.types.event_type_filter.serialize_cbor(
            value["filter"]
        )
    if "locale" in value:
        out["locale"] = value["locale"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_cbor(data: dict) -> DescribeEventTypesRequest:
    out: DescribeEventTypesRequest = {}  # type: ignore[typeddict-item]
    if data.get("filter") is not None:
        import capo_health.types.event_type_filter

        out["filter"] = capo_health.types.event_type_filter.deserialize_cbor(
            data["filter"]
        )
    if data.get("locale") is not None:
        out["locale"] = data["locale"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
