"""Generated from Smithy shape ``com.amazonaws.iot#GetStatisticsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.aggregation_field
    import capo_iot.types.index_name
    import capo_iot.types.query_string
    import capo_iot.types.query_version


class GetStatisticsRequest(TypedDict, closed=True):
    index_name: NotRequired["capo_iot.types.index_name.IndexName"]
    """<p>The name of the index to search. The default value is <code>AWS_Things</code>.</p>"""
    query_string: "capo_iot.types.query_string.QueryString"
    """<p>The query used to search. You can specify "*" for the query string to get the count of all indexed things in your Amazon Web Services account.</p>"""
    aggregation_field: NotRequired["capo_iot.types.aggregation_field.AggregationField"]
    """<p>The aggregation field name.</p>"""
    query_version: NotRequired["capo_iot.types.query_version.QueryVersion"]
    """<p>The version of the query used to search.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStatisticsRequest) -> dict:
    out: dict = {}
    if "index_name" in value:
        out["indexName"] = value["index_name"]
    out["queryString"] = value["query_string"]
    if "aggregation_field" in value:
        out["aggregationField"] = value["aggregation_field"]
    if "query_version" in value:
        out["queryVersion"] = value["query_version"]
    return out


def deserialize_json(data: dict) -> GetStatisticsRequest:
    out: GetStatisticsRequest = {}  # type: ignore[typeddict-item]
    if data.get("indexName") is not None:
        out["index_name"] = data["indexName"]
    if data.get("queryString") is not None:
        out["query_string"] = data["queryString"]
    else:
        raise DeserializationError("GetStatisticsRequest.query_string required")
    if data.get("aggregationField") is not None:
        out["aggregation_field"] = data["aggregationField"]
    if data.get("queryVersion") is not None:
        out["query_version"] = data["queryVersion"]
    return out
