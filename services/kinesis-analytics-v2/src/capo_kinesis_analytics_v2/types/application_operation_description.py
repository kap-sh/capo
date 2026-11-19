"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationOperationDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_name
    import capo_kinesis_analytics_v2.types.operation_id


class ApplicationOperationDescription(TypedDict, closed=True):
    application_operation_id: NotRequired[
        "capo_kinesis_analytics_v2.types.operation_id.OperationId"
    ]
    application_name: NotRequired[
        "capo_kinesis_analytics_v2.types.application_name.ApplicationName"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationOperationDescription) -> dict:
    out: dict = {}
    if "application_operation_id" in value:
        out["ApplicationOperationId"] = value["application_operation_id"]
    if "application_name" in value:
        out["ApplicationName"] = value["application_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationOperationDescription:
    out: ApplicationOperationDescription = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationOperationId") is not None:
        out["application_operation_id"] = data["ApplicationOperationId"]
    if data.get("ApplicationName") is not None:
        out["application_name"] = data["ApplicationName"]
    return out
