"""Generated from Smithy shape ``com.amazonaws.health#DescribeAffectedEntitiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_health.errors import DeserializationError

if TYPE_CHECKING:
    import capo_health.types.entity_filter
    import capo_health.types.locale
    import capo_health.types.max_results_lower_range
    import capo_health.types.next_token


class DescribeAffectedEntitiesRequest(TypedDict, closed=True):
    filter: "capo_health.types.entity_filter.EntityFilter"
    """<p>Values to narrow the results returned. At least one event ARN is required.</p>"""
    locale: NotRequired["capo_health.types.locale.locale"]
    """<p>The locale (language) to return information in. English (en) is the default and the only supported value at this time.</p>"""
    next_token: NotRequired["capo_health.types.next_token.nextToken"]
    """<p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.</p>"""
    max_results: NotRequired[
        "capo_health.types.max_results_lower_range.maxResultsLowerRange"
    ]
    """<p>The maximum number of items to return in one batch, between 1 and 100, inclusive.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAffectedEntitiesRequest) -> dict:
    out: dict = {}
    import capo_health.types.entity_filter

    out["filter"] = capo_health.types.entity_filter.serialize_aws_json_1_1(
        value["filter"]
    )
    if "locale" in value:
        out["locale"] = value["locale"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAffectedEntitiesRequest:
    out: DescribeAffectedEntitiesRequest = {}  # type: ignore[typeddict-item]
    if data.get("filter") is not None:
        import capo_health.types.entity_filter

        out["filter"] = capo_health.types.entity_filter.deserialize_aws_json_1_1(
            data["filter"]
        )
    else:
        raise DeserializationError("DescribeAffectedEntitiesRequest.filter required")
    if data.get("locale") is not None:
        out["locale"] = data["locale"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeAffectedEntitiesRequest) -> dict:
    out: dict = {}
    import capo_health.types.entity_filter

    out["filter"] = capo_health.types.entity_filter.serialize_cbor(value["filter"])
    if "locale" in value:
        out["locale"] = value["locale"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_cbor(data: dict) -> DescribeAffectedEntitiesRequest:
    out: DescribeAffectedEntitiesRequest = {}  # type: ignore[typeddict-item]
    if data.get("filter") is not None:
        import capo_health.types.entity_filter

        out["filter"] = capo_health.types.entity_filter.deserialize_cbor(data["filter"])
    else:
        raise DeserializationError("DescribeAffectedEntitiesRequest.filter required")
    if data.get("locale") is not None:
        out["locale"] = data["locale"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
