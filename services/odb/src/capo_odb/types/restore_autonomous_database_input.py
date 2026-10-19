"""Generated from Smithy shape ``com.amazonaws.odb#RestoreAutonomousDatabaseInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_odb.types.resource_id_or_arn


class RestoreAutonomousDatabaseInput(TypedDict, closed=True):
    autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the Autonomous Database to restore.</p>"""
    timestamp: "datetime.datetime"
    """<p>The date and time to which to restore the Autonomous Database.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RestoreAutonomousDatabaseInput) -> dict:
    out: dict = {}
    out["autonomousDatabaseId"] = value["autonomous_database_id"]
    import capo_odb._protocol.serialize

    out["timestamp"] = capo_odb._protocol.serialize.fmt_date_time(value["timestamp"])
    return out


def deserialize_aws_json_1_0(data: dict) -> RestoreAutonomousDatabaseInput:
    out: RestoreAutonomousDatabaseInput = {}  # type: ignore[typeddict-item]
    if data.get("autonomousDatabaseId") is not None:
        out["autonomous_database_id"] = data["autonomousDatabaseId"]
    else:
        out["autonomous_database_id"] = ""
    if data.get("timestamp") is not None:
        import datetime

        out["timestamp"] = datetime.datetime.fromisoformat(
            data["timestamp"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["timestamp"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
