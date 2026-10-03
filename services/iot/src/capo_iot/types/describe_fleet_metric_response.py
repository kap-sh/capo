"""Generated from Smithy shape ``com.amazonaws.iot#DescribeFleetMetricResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.aggregation_field
    import capo_iot.types.aggregation_type
    import capo_iot.types.creation_date
    import capo_iot.types.fleet_metric_arn
    import capo_iot.types.fleet_metric_description
    import capo_iot.types.fleet_metric_name
    import capo_iot.types.fleet_metric_period
    import capo_iot.types.fleet_metric_unit
    import capo_iot.types.index_name
    import capo_iot.types.last_modified_date
    import capo_iot.types.query_string
    import capo_iot.types.query_version
    import capo_iot.types.version


class DescribeFleetMetricResponse(TypedDict, closed=True):
    metric_name: NotRequired["capo_iot.types.fleet_metric_name.FleetMetricName"]
    """<p>The name of the fleet metric to describe.</p>"""
    query_string: NotRequired["capo_iot.types.query_string.QueryString"]
    """<p>The search query string.</p>"""
    aggregation_type: NotRequired["capo_iot.types.aggregation_type.AggregationType"]
    """<p>The type of the aggregation query.</p>"""
    period: NotRequired["capo_iot.types.fleet_metric_period.FleetMetricPeriod"]
    """<p>The time in seconds between fleet metric emissions. Range [60(1 min), 86400(1 day)] and must be multiple of 60.</p>"""
    aggregation_field: NotRequired["capo_iot.types.aggregation_field.AggregationField"]
    """<p>The field to aggregate.</p>"""
    description: NotRequired[
        "capo_iot.types.fleet_metric_description.FleetMetricDescription"
    ]
    """<p>The fleet metric description.</p>"""
    query_version: NotRequired["capo_iot.types.query_version.QueryVersion"]
    """<p>The query version.</p>"""
    index_name: NotRequired["capo_iot.types.index_name.IndexName"]
    """<p>The name of the index to search.</p>"""
    creation_date: NotRequired["capo_iot.types.creation_date.CreationDate"]
    """<p>The date when the fleet metric is created.</p>"""
    last_modified_date: NotRequired[
        "capo_iot.types.last_modified_date.LastModifiedDate"
    ]
    """<p>The date when the fleet metric is last modified.</p>"""
    unit: NotRequired["capo_iot.types.fleet_metric_unit.FleetMetricUnit"]
    """<p>Used to support unit transformation such as milliseconds to seconds. The unit must be supported by <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricDatum.html">CW metric</a>.</p>"""
    version: "capo_iot.types.version.Version"
    """<p>The version of the fleet metric.</p>"""
    metric_arn: NotRequired["capo_iot.types.fleet_metric_arn.FleetMetricArn"]
    """<p>The ARN of the fleet metric to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeFleetMetricResponse) -> dict:
    out: dict = {}
    if "metric_name" in value:
        out["metricName"] = value["metric_name"]
    if "query_string" in value:
        out["queryString"] = value["query_string"]
    if "aggregation_type" in value:
        import capo_iot.types.aggregation_type

        out["aggregationType"] = capo_iot.types.aggregation_type.serialize_json(
            value["aggregation_type"]
        )
    if "period" in value:
        out["period"] = value["period"]
    if "aggregation_field" in value:
        out["aggregationField"] = value["aggregation_field"]
    if "description" in value:
        out["description"] = value["description"]
    if "query_version" in value:
        out["queryVersion"] = value["query_version"]
    if "index_name" in value:
        out["indexName"] = value["index_name"]
    if "creation_date" in value:
        import capo_iot.types.creation_date

        out["creationDate"] = capo_iot.types.creation_date.serialize_json(
            value["creation_date"]
        )
    if "last_modified_date" in value:
        import capo_iot.types.last_modified_date

        out["lastModifiedDate"] = capo_iot.types.last_modified_date.serialize_json(
            value["last_modified_date"]
        )
    if "unit" in value:
        import capo_iot.types.fleet_metric_unit

        out["unit"] = capo_iot.types.fleet_metric_unit.serialize_json(value["unit"])
    out["version"] = value.get("version", 0)
    if "metric_arn" in value:
        out["metricArn"] = value["metric_arn"]
    return out


def deserialize_json(data: dict) -> DescribeFleetMetricResponse:
    out: DescribeFleetMetricResponse = {}  # type: ignore[typeddict-item]
    if data.get("metricName") is not None:
        out["metric_name"] = data["metricName"]
    if data.get("queryString") is not None:
        out["query_string"] = data["queryString"]
    if data.get("aggregationType") is not None:
        import capo_iot.types.aggregation_type

        out["aggregation_type"] = capo_iot.types.aggregation_type.deserialize_json(
            data["aggregationType"]
        )
    if data.get("period") is not None:
        out["period"] = data["period"]
    if data.get("aggregationField") is not None:
        out["aggregation_field"] = data["aggregationField"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("queryVersion") is not None:
        out["query_version"] = data["queryVersion"]
    if data.get("indexName") is not None:
        out["index_name"] = data["indexName"]
    if data.get("creationDate") is not None:
        import capo_iot.types.creation_date

        out["creation_date"] = capo_iot.types.creation_date.deserialize_json(
            data["creationDate"]
        )
    if data.get("lastModifiedDate") is not None:
        import capo_iot.types.last_modified_date

        out["last_modified_date"] = capo_iot.types.last_modified_date.deserialize_json(
            data["lastModifiedDate"]
        )
    if data.get("unit") is not None:
        import capo_iot.types.fleet_metric_unit

        out["unit"] = capo_iot.types.fleet_metric_unit.deserialize_json(data["unit"])
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        out["version"] = 0
    if data.get("metricArn") is not None:
        out["metric_arn"] = data["metricArn"]
    return out
