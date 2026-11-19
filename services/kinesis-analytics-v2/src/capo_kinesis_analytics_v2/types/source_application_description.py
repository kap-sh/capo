"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#SourceApplicationDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_name
    import capo_kinesis_analytics_v2.types.application_version_id
    import capo_kinesis_analytics_v2.types.timestamp


class SourceApplicationDescription(TypedDict, closed=True):
    application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName"
    application_creation_timestamp: (
        "capo_kinesis_analytics_v2.types.timestamp.Timestamp"
    )
    """<p>The timestamp that indicates when the source application was created.</p>"""
    application_version_id: (
        "capo_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
    )
    """<p>The version ID of the source application when the snapshot was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceApplicationDescription) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    import capo_kinesis_analytics_v2.types.timestamp

    out["ApplicationCreationTimestamp"] = (
        capo_kinesis_analytics_v2.types.timestamp.serialize_aws_json_1_1(
            value["application_creation_timestamp"]
        )
    )
    out["ApplicationVersionId"] = value["application_version_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceApplicationDescription:
    out: SourceApplicationDescription = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationName") is not None:
        out["application_name"] = data["ApplicationName"]
    else:
        out["application_name"] = ""
    if data.get("ApplicationCreationTimestamp") is not None:
        import capo_kinesis_analytics_v2.types.timestamp

        out["application_creation_timestamp"] = (
            capo_kinesis_analytics_v2.types.timestamp.deserialize_aws_json_1_1(
                data["ApplicationCreationTimestamp"]
            )
        )
    else:
        import datetime

        out["application_creation_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("ApplicationVersionId") is not None:
        out["application_version_id"] = data["ApplicationVersionId"]
    else:
        out["application_version_id"] = 0
    return out
