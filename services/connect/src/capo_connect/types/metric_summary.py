"""Generated from Smithy shape ``com.amazonaws.connect#MetricSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.metric_id
    import capo_connect.types.metric_name
    import capo_connect.types.metric_status
    import capo_connect.types.metric_type
    import capo_connect.types.region_name
    import capo_connect.types.timestamp


class MetricSummary(TypedDict, closed=True):
    arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the metric.</p>"""
    id: "capo_connect.types.metric_id.MetricId"
    """<p>The identifier of the metric.</p>"""
    name: "capo_connect.types.metric_name.MetricName"
    """<p>The name of the metric.</p>"""
    status: "capo_connect.types.metric_status.MetricStatus"
    """<p>The publish status of the metric.</p>"""
    type: "capo_connect.types.metric_type.MetricType"
    """<p>The type of the metric.</p>"""
    last_modified_region: NotRequired["capo_connect.types.region_name.RegionName"]
    """<p>The region where the metric was last modified.</p>"""
    last_modified_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp of when the metric was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricSummary) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["Id"] = value["id"]
    out["Name"] = value["name"]
    import capo_connect.types.metric_status

    out["Status"] = capo_connect.types.metric_status.serialize_json(value["status"])
    import capo_connect.types.metric_type

    out["Type"] = capo_connect.types.metric_type.serialize_json(value["type"])
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    if "last_modified_time" in value:
        import capo_connect.types.timestamp

        out["LastModifiedTime"] = capo_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    return out


def deserialize_json(data: dict) -> MetricSummary:
    out: MetricSummary = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Status") is not None:
        import capo_connect.types.metric_status

        out["status"] = capo_connect.types.metric_status.deserialize_json(
            data["Status"]
        )
    else:
        import typing

        out["status"] = typing.cast("capo_connect.types.metric_status.MetricStatus", "")
    if data.get("Type") is not None:
        import capo_connect.types.metric_type

        out["type"] = capo_connect.types.metric_type.deserialize_json(data["Type"])
    else:
        import typing

        out["type"] = typing.cast("capo_connect.types.metric_type.MetricType", "")
    if data.get("LastModifiedRegion") is not None:
        out["last_modified_region"] = data["LastModifiedRegion"]
    if data.get("LastModifiedTime") is not None:
        import capo_connect.types.timestamp

        out["last_modified_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    return out
