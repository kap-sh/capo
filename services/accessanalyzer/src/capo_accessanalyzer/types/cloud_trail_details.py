"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#CloudTrailDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.role_arn
    import capo_accessanalyzer.types.timestamp
    import capo_accessanalyzer.types.trail_list


class CloudTrailDetails(TypedDict, closed=True):
    trails: "capo_accessanalyzer.types.trail_list.TrailList"
    """<p>A <code>Trail</code> object that contains settings for a trail.</p>"""
    access_role: "capo_accessanalyzer.types.role_arn.RoleArn"
    """<p>The ARN of the service role that IAM Access Analyzer uses to access your CloudTrail trail and service last accessed information.</p>"""
    start_time: "capo_accessanalyzer.types.timestamp.Timestamp"
    """<p>The start of the time range for which IAM Access Analyzer reviews your CloudTrail events. Events with a timestamp before this time are not considered to generate a policy.</p>"""
    end_time: NotRequired["capo_accessanalyzer.types.timestamp.Timestamp"]
    """<p>The end of the time range for which IAM Access Analyzer reviews your CloudTrail events. Events with a timestamp after this time are not considered to generate a policy. If this is not included in the request, the default value is the current time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudTrailDetails) -> dict:
    out: dict = {}
    import capo_accessanalyzer.types.trail_list

    out["trails"] = capo_accessanalyzer.types.trail_list.serialize_json(value["trails"])
    out["accessRole"] = value["access_role"]
    import capo_accessanalyzer.types.timestamp

    out["startTime"] = capo_accessanalyzer.types.timestamp.serialize_json(
        value["start_time"]
    )
    if "end_time" in value:
        import capo_accessanalyzer.types.timestamp

        out["endTime"] = capo_accessanalyzer.types.timestamp.serialize_json(
            value["end_time"]
        )
    return out


def deserialize_json(data: dict) -> CloudTrailDetails:
    out: CloudTrailDetails = {}  # type: ignore[typeddict-item]
    if data.get("trails") is not None:
        import capo_accessanalyzer.types.trail_list

        out["trails"] = capo_accessanalyzer.types.trail_list.deserialize_json(
            data["trails"]
        )
    else:
        out["trails"] = []
    if data.get("accessRole") is not None:
        out["access_role"] = data["accessRole"]
    else:
        out["access_role"] = ""
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
    return out
