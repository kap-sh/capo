"""Generated from Smithy shape ``com.amazonaws.iot#CreateFleetMetricRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.aggregation_field
    import capo_iot.types.aggregation_type
    import capo_iot.types.fleet_metric_description
    import capo_iot.types.fleet_metric_name
    import capo_iot.types.fleet_metric_period
    import capo_iot.types.fleet_metric_unit
    import capo_iot.types.index_name
    import capo_iot.types.query_string
    import capo_iot.types.query_version
    import capo_iot.types.tag_list


class CreateFleetMetricRequest(TypedDict, closed=True):
    metric_name: "capo_iot.types.fleet_metric_name.FleetMetricName"
    """<p>The name of the fleet metric to create.</p>"""
    query_string: "capo_iot.types.query_string.QueryString"
    """<p>The search query string.</p>"""
    aggregation_type: "capo_iot.types.aggregation_type.AggregationType"
    """<p>The type of the aggregation query.</p>"""
    period: "capo_iot.types.fleet_metric_period.FleetMetricPeriod"
    """<p>The time in seconds between fleet metric emissions. Range [60(1 min), 86400(1 day)] and must be multiple of 60.</p>"""
    aggregation_field: "capo_iot.types.aggregation_field.AggregationField"
    """<p>The field to aggregate.</p>"""
    description: NotRequired[
        "capo_iot.types.fleet_metric_description.FleetMetricDescription"
    ]
    """<p>The fleet metric description.</p>"""
    query_version: NotRequired["capo_iot.types.query_version.QueryVersion"]
    """<p>The query version.</p>"""
    index_name: NotRequired["capo_iot.types.index_name.IndexName"]
    """<p>The name of the index to search.</p>"""
    unit: NotRequired["capo_iot.types.fleet_metric_unit.FleetMetricUnit"]
    """<p>Used to support unit transformation such as milliseconds to seconds. The unit must be supported by <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricDatum.html">CW metric</a>. Default to null.</p>"""
    tags: NotRequired["capo_iot.types.tag_list.TagList"]
    """<p>Metadata, which can be used to manage the fleet metric.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFleetMetricRequest) -> dict:
    out: dict = {}
    out["queryString"] = value["query_string"]
    import capo_iot.types.aggregation_type

    out["aggregationType"] = capo_iot.types.aggregation_type.serialize_json(
        value["aggregation_type"]
    )
    out["period"] = value["period"]
    out["aggregationField"] = value["aggregation_field"]
    if "description" in value:
        out["description"] = value["description"]
    if "query_version" in value:
        out["queryVersion"] = value["query_version"]
    if "index_name" in value:
        out["indexName"] = value["index_name"]
    if "unit" in value:
        import capo_iot.types.fleet_metric_unit

        out["unit"] = capo_iot.types.fleet_metric_unit.serialize_json(value["unit"])
    if "tags" in value:
        import capo_iot.types.tag_list

        out["tags"] = capo_iot.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateFleetMetricRequest:
    out: CreateFleetMetricRequest = {}  # type: ignore[typeddict-item]
    if data.get("queryString") is not None:
        out["query_string"] = data["queryString"]
    else:
        raise DeserializationError("CreateFleetMetricRequest.query_string required")
    if data.get("aggregationType") is not None:
        import capo_iot.types.aggregation_type

        out["aggregation_type"] = capo_iot.types.aggregation_type.deserialize_json(
            data["aggregationType"]
        )
    else:
        raise DeserializationError("CreateFleetMetricRequest.aggregation_type required")
    if data.get("period") is not None:
        out["period"] = data["period"]
    else:
        raise DeserializationError("CreateFleetMetricRequest.period required")
    if data.get("aggregationField") is not None:
        out["aggregation_field"] = data["aggregationField"]
    else:
        raise DeserializationError(
            "CreateFleetMetricRequest.aggregation_field required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("queryVersion") is not None:
        out["query_version"] = data["queryVersion"]
    if data.get("indexName") is not None:
        out["index_name"] = data["indexName"]
    if data.get("unit") is not None:
        import capo_iot.types.fleet_metric_unit

        out["unit"] = capo_iot.types.fleet_metric_unit.deserialize_json(data["unit"])
    if data.get("tags") is not None:
        import capo_iot.types.tag_list

        out["tags"] = capo_iot.types.tag_list.deserialize_json(data["tags"])
    return out
