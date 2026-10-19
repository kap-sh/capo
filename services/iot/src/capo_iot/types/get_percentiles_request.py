"""Generated from Smithy shape ``com.amazonaws.iot#GetPercentilesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.aggregation_field
    import capo_iot.types.index_name
    import capo_iot.types.percent_list
    import capo_iot.types.query_string
    import capo_iot.types.query_version


class GetPercentilesRequest(TypedDict, closed=True):
    index_name: NotRequired["capo_iot.types.index_name.IndexName"]
    """<p>The name of the index to search.</p>"""
    query_string: "capo_iot.types.query_string.QueryString"
    """<p>The search query string.</p>"""
    aggregation_field: NotRequired["capo_iot.types.aggregation_field.AggregationField"]
    """<p>The field to aggregate.</p>"""
    query_version: NotRequired["capo_iot.types.query_version.QueryVersion"]
    """<p>The query version.</p>"""
    percents: NotRequired["capo_iot.types.percent_list.PercentList"]
    """<p>The percentile groups returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPercentilesRequest) -> dict:
    out: dict = {}
    if "index_name" in value:
        out["indexName"] = value["index_name"]
    out["queryString"] = value["query_string"]
    if "aggregation_field" in value:
        out["aggregationField"] = value["aggregation_field"]
    if "query_version" in value:
        out["queryVersion"] = value["query_version"]
    if "percents" in value:
        import capo_iot.types.percent_list

        out["percents"] = capo_iot.types.percent_list.serialize_json(value["percents"])
    return out


def deserialize_json(data: dict) -> GetPercentilesRequest:
    out: GetPercentilesRequest = {}  # type: ignore[typeddict-item]
    if data.get("indexName") is not None:
        out["index_name"] = data["indexName"]
    if data.get("queryString") is not None:
        out["query_string"] = data["queryString"]
    else:
        out["query_string"] = ""
    if data.get("aggregationField") is not None:
        out["aggregation_field"] = data["aggregationField"]
    if data.get("queryVersion") is not None:
        out["query_version"] = data["queryVersion"]
    if data.get("percents") is not None:
        import capo_iot.types.percent_list

        out["percents"] = capo_iot.types.percent_list.deserialize_json(data["percents"])
    return out
