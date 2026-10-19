"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#CloudTrailProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.timestamp
    import capo_accessanalyzer.types.trail_properties_list


class CloudTrailProperties(TypedDict, closed=True):
    trail_properties: (
        "capo_accessanalyzer.types.trail_properties_list.TrailPropertiesList"
    )
    """<p>A <code>TrailProperties</code> object that contains settings for trail properties.</p>"""
    start_time: "capo_accessanalyzer.types.timestamp.Timestamp"
    """<p>The start of the time range for which IAM Access Analyzer reviews your CloudTrail events. Events with a timestamp before this time are not considered to generate a policy.</p>"""
    end_time: "capo_accessanalyzer.types.timestamp.Timestamp"
    """<p>The end of the time range for which IAM Access Analyzer reviews your CloudTrail events. Events with a timestamp after this time are not considered to generate a policy. If this is not included in the request, the default value is the current time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudTrailProperties) -> dict:
    out: dict = {}
    import capo_accessanalyzer.types.trail_properties_list

    out["trailProperties"] = (
        capo_accessanalyzer.types.trail_properties_list.serialize_json(
            value["trail_properties"]
        )
    )
    import capo_accessanalyzer.types.timestamp

    out["startTime"] = capo_accessanalyzer.types.timestamp.serialize_json(
        value["start_time"]
    )
    import capo_accessanalyzer.types.timestamp

    out["endTime"] = capo_accessanalyzer.types.timestamp.serialize_json(
        value["end_time"]
    )
    return out


def deserialize_json(data: dict) -> CloudTrailProperties:
    out: CloudTrailProperties = {}  # type: ignore[typeddict-item]
    if data.get("trailProperties") is not None:
        import capo_accessanalyzer.types.trail_properties_list

        out["trail_properties"] = (
            capo_accessanalyzer.types.trail_properties_list.deserialize_json(
                data["trailProperties"]
            )
        )
    else:
        out["trail_properties"] = []
    if data.get("startTime") is not None:
        import capo_accessanalyzer.types.timestamp

        out["start_time"] = capo_accessanalyzer.types.timestamp.deserialize_json(
            data["startTime"]
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("endTime") is not None:
        import capo_accessanalyzer.types.timestamp

        out["end_time"] = capo_accessanalyzer.types.timestamp.deserialize_json(
            data["endTime"]
        )
    else:
        import datetime

        out["end_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
