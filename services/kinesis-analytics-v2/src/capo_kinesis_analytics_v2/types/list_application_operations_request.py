"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ListApplicationOperationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_name
    import capo_kinesis_analytics_v2.types.list_application_operations_input_limit
    import capo_kinesis_analytics_v2.types.next_token
    import capo_kinesis_analytics_v2.types.operation
    import capo_kinesis_analytics_v2.types.operation_status


class ListApplicationOperationsRequest(TypedDict, closed=True):
    application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName"
    limit: NotRequired[
        "capo_kinesis_analytics_v2.types.list_application_operations_input_limit.ListApplicationOperationsInputLimit"
    ]
    next_token: NotRequired["capo_kinesis_analytics_v2.types.next_token.NextToken"]
    operation: NotRequired["capo_kinesis_analytics_v2.types.operation.Operation"]
    operation_status: NotRequired[
        "capo_kinesis_analytics_v2.types.operation_status.OperationStatus"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApplicationOperationsRequest) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "operation" in value:
        out["Operation"] = value["operation"]
    if "operation_status" in value:
        import capo_kinesis_analytics_v2.types.operation_status

        out["OperationStatus"] = (
            capo_kinesis_analytics_v2.types.operation_status.serialize_aws_json_1_1(
                value["operation_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApplicationOperationsRequest:
    out: ListApplicationOperationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationName") is not None:
        out["application_name"] = data["ApplicationName"]
    else:
        out["application_name"] = ""
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Operation") is not None:
        out["operation"] = data["Operation"]
    if data.get("OperationStatus") is not None:
        import capo_kinesis_analytics_v2.types.operation_status

        out["operation_status"] = (
            capo_kinesis_analytics_v2.types.operation_status.deserialize_aws_json_1_1(
                data["OperationStatus"]
            )
        )
    return out
