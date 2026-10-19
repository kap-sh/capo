"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#DeleteApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_name
    import capo_kinesis_analytics_v2.types.timestamp


class DeleteApplicationRequest(TypedDict, closed=True):
    application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName"
    """<p>The name of the application to delete.</p>"""
    create_timestamp: "capo_kinesis_analytics_v2.types.timestamp.Timestamp"
    """<p>Use the <code>DescribeApplication</code> operation to get this value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteApplicationRequest) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    import capo_kinesis_analytics_v2.types.timestamp

    out["CreateTimestamp"] = (
        capo_kinesis_analytics_v2.types.timestamp.serialize_aws_json_1_1(
            value["create_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteApplicationRequest:
    out: DeleteApplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationName") is not None:
        out["application_name"] = data["ApplicationName"]
    else:
        out["application_name"] = ""
    if data.get("CreateTimestamp") is not None:
        import capo_kinesis_analytics_v2.types.timestamp

        out["create_timestamp"] = (
            capo_kinesis_analytics_v2.types.timestamp.deserialize_aws_json_1_1(
                data["CreateTimestamp"]
            )
        )
    else:
        import datetime

        out["create_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
