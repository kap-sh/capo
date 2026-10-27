"""Generated from Smithy shape ``com.amazonaws.connect#ApproximateDriftedResourceCount``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.approximate_total_count
    import capo_connect.types.aws_region
    import capo_connect.types.timestamp


class ApproximateDriftedResourceCount(TypedDict, closed=True):
    region: "capo_connect.types.aws_region.AwsRegion"
    """<p>The Amazon Web Services Region that the count applies to.</p>"""
    count: "capo_connect.types.approximate_total_count.ApproximateTotalCount"
    """<p>The approximate number of resources of the requested type that are not yet in sync in the Region. A value of zero means the resources are in sync.</p>"""
    timestamp: "capo_connect.types.timestamp.Timestamp"
    """<p>The time, in Unix epoch time, when the count was last calculated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApproximateDriftedResourceCount) -> dict:
    out: dict = {}
    out["Region"] = value["region"]
    out["Count"] = value["count"]
    import capo_connect.types.timestamp

    out["Timestamp"] = capo_connect.types.timestamp.serialize_json(value["timestamp"])
    return out


def deserialize_json(data: dict) -> ApproximateDriftedResourceCount:
    out: ApproximateDriftedResourceCount = {}  # type: ignore[typeddict-item]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    else:
        out["region"] = ""
    if data.get("Count") is not None:
        out["count"] = data["Count"]
    else:
        out["count"] = 0
    if data.get("Timestamp") is not None:
        import capo_connect.types.timestamp

        out["timestamp"] = capo_connect.types.timestamp.deserialize_json(
            data["Timestamp"]
        )
    else:
        import datetime

        out["timestamp"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
