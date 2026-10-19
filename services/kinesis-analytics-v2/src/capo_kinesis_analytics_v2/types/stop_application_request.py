"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#StopApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_name
    import capo_kinesis_analytics_v2.types.boolean_object


class StopApplicationRequest(TypedDict, closed=True):
    application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName"
    """<p>The name of the running application to stop.</p>"""
    force: NotRequired["capo_kinesis_analytics_v2.types.boolean_object.BooleanObject"]
    """<p>Set to <code>true</code> to force the application to stop. If you set <code>Force</code> to <code>true</code>, Managed Service for Apache Flink stops the application without taking a snapshot. </p> <note> <p>Force-stopping your application may lead to data loss or duplication. To prevent data loss or duplicate processing of data during application restarts, we recommend you to take frequent snapshots of your application.</p> </note> <p>You can only force stop a Managed Service for Apache Flink application. You can't force stop a SQL-based Kinesis Data Analytics application.</p> <p>The application must be in the <code>STARTING</code>, <code>UPDATING</code>, <code>STOPPING</code>, <code>AUTOSCALING</code>, or <code>RUNNING</code> status. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopApplicationRequest) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    if "force" in value:
        out["Force"] = value["force"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopApplicationRequest:
    out: StopApplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationName") is not None:
        out["application_name"] = data["ApplicationName"]
    else:
        out["application_name"] = ""
    if data.get("Force") is not None:
        out["force"] = data["Force"]
    return out
