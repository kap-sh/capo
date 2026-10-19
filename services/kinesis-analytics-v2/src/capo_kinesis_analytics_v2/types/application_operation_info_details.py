"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationOperationInfoDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_version_change_details
    import capo_kinesis_analytics_v2.types.operation
    import capo_kinesis_analytics_v2.types.operation_failure_details
    import capo_kinesis_analytics_v2.types.operation_status
    import capo_kinesis_analytics_v2.types.timestamp


class ApplicationOperationInfoDetails(TypedDict, closed=True):
    operation: "capo_kinesis_analytics_v2.types.operation.Operation"
    start_time: "capo_kinesis_analytics_v2.types.timestamp.Timestamp"
    """<p>The timestamp that indicates when the operation was created.</p>"""
    end_time: "capo_kinesis_analytics_v2.types.timestamp.Timestamp"
    """<p>The timestamp that indicates when the operation finished.</p>"""
    operation_status: "capo_kinesis_analytics_v2.types.operation_status.OperationStatus"
    application_version_change_details: NotRequired[
        "capo_kinesis_analytics_v2.types.application_version_change_details.ApplicationVersionChangeDetails"
    ]
    operation_failure_details: NotRequired[
        "capo_kinesis_analytics_v2.types.operation_failure_details.OperationFailureDetails"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationOperationInfoDetails) -> dict:
    out: dict = {}
    out["Operation"] = value["operation"]
    import capo_kinesis_analytics_v2.types.timestamp

    out["StartTime"] = capo_kinesis_analytics_v2.types.timestamp.serialize_aws_json_1_1(
        value["start_time"]
    )
    import capo_kinesis_analytics_v2.types.timestamp

    out["EndTime"] = capo_kinesis_analytics_v2.types.timestamp.serialize_aws_json_1_1(
        value["end_time"]
    )
    import capo_kinesis_analytics_v2.types.operation_status

    out["OperationStatus"] = (
        capo_kinesis_analytics_v2.types.operation_status.serialize_aws_json_1_1(
            value["operation_status"]
        )
    )
    if "application_version_change_details" in value:
        import capo_kinesis_analytics_v2.types.application_version_change_details

        out["ApplicationVersionChangeDetails"] = (
            capo_kinesis_analytics_v2.types.application_version_change_details.serialize_aws_json_1_1(
                value["application_version_change_details"]
            )
        )
    if "operation_failure_details" in value:
        import capo_kinesis_analytics_v2.types.operation_failure_details

        out["OperationFailureDetails"] = (
            capo_kinesis_analytics_v2.types.operation_failure_details.serialize_aws_json_1_1(
                value["operation_failure_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationOperationInfoDetails:
    out: ApplicationOperationInfoDetails = {}  # type: ignore[typeddict-item]
    if data.get("Operation") is not None:
        out["operation"] = data["Operation"]
    else:
        out["operation"] = ""
    if data.get("StartTime") is not None:
        import capo_kinesis_analytics_v2.types.timestamp

        out["start_time"] = (
            capo_kinesis_analytics_v2.types.timestamp.deserialize_aws_json_1_1(
                data["StartTime"]
            )
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("EndTime") is not None:
        import capo_kinesis_analytics_v2.types.timestamp

        out["end_time"] = (
            capo_kinesis_analytics_v2.types.timestamp.deserialize_aws_json_1_1(
                data["EndTime"]
            )
        )
    else:
        import datetime

        out["end_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("OperationStatus") is not None:
        import capo_kinesis_analytics_v2.types.operation_status

        out["operation_status"] = (
            capo_kinesis_analytics_v2.types.operation_status.deserialize_aws_json_1_1(
                data["OperationStatus"]
            )
        )
    else:
        import typing

        out["operation_status"] = typing.cast(
            "capo_kinesis_analytics_v2.types.operation_status.OperationStatus", ""
        )
    if data.get("ApplicationVersionChangeDetails") is not None:
        import capo_kinesis_analytics_v2.types.application_version_change_details

        out["application_version_change_details"] = (
            capo_kinesis_analytics_v2.types.application_version_change_details.deserialize_aws_json_1_1(
                data["ApplicationVersionChangeDetails"]
            )
        )
    if data.get("OperationFailureDetails") is not None:
        import capo_kinesis_analytics_v2.types.operation_failure_details

        out["operation_failure_details"] = (
            capo_kinesis_analytics_v2.types.operation_failure_details.deserialize_aws_json_1_1(
                data["OperationFailureDetails"]
            )
        )
    return out
