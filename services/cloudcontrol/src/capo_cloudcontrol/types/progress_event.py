"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#ProgressEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudcontrol.types.handler_error_code
    import capo_cloudcontrol.types.identifier
    import capo_cloudcontrol.types.operation
    import capo_cloudcontrol.types.operation_status
    import capo_cloudcontrol.types.properties
    import capo_cloudcontrol.types.request_token
    import capo_cloudcontrol.types.status_message
    import capo_cloudcontrol.types.timestamp
    import capo_cloudcontrol.types.type_name


class ProgressEvent(TypedDict, closed=True):
    type_name: NotRequired["capo_cloudcontrol.types.type_name.TypeName"]
    """<p>The name of the resource type used in the operation.</p>"""
    identifier: NotRequired["capo_cloudcontrol.types.identifier.Identifier"]
    """<p>The primary identifier for the resource.</p> <note> <p>In some cases, the resource identifier may be available before the resource operation has reached a status of <code>SUCCESS</code>.</p> </note>"""
    request_token: NotRequired["capo_cloudcontrol.types.request_token.RequestToken"]
    """<p>The unique token representing this resource operation request.</p> <p>Use the <code>RequestToken</code> with <a href="https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_GetResourceRequestStatus.html">GetResourceRequestStatus</a> to return the current status of a resource operation request.</p>"""
    hooks_request_token: NotRequired[
        "capo_cloudcontrol.types.request_token.RequestToken"
    ]
    """<p>The unique token representing the Hooks operation for the request.</p>"""
    operation: NotRequired["capo_cloudcontrol.types.operation.Operation"]
    """<p>The resource operation type.</p>"""
    operation_status: NotRequired[
        "capo_cloudcontrol.types.operation_status.OperationStatus"
    ]
    """<p>The current status of the resource operation request.</p> <ul> <li> <p> <code>PENDING</code>: The resource operation hasn't yet started.</p> </li> <li> <p> <code>IN_PROGRESS</code>: The resource operation is currently in progress.</p> </li> <li> <p> <code>SUCCESS</code>: The resource operation has successfully completed.</p> </li> <li> <p> <code>FAILED</code>: The resource operation has failed. Refer to the error code and status message for more information.</p> </li> <li> <p> <code>CANCEL_IN_PROGRESS</code>: The resource operation is in the process of being canceled.</p> </li> <li> <p> <code>CANCEL_COMPLETE</code>: The resource operation has been canceled.</p> </li> </ul>"""
    event_time: NotRequired["capo_cloudcontrol.types.timestamp.Timestamp"]
    """<p>When the resource operation request was initiated.</p>"""
    resource_model: NotRequired["capo_cloudcontrol.types.properties.Properties"]
    """<p>A JSON string containing the resource model, consisting of each resource property and its current value.</p>"""
    status_message: NotRequired["capo_cloudcontrol.types.status_message.StatusMessage"]
    """<p>Any message explaining the current status.</p>"""
    error_code: NotRequired[
        "capo_cloudcontrol.types.handler_error_code.HandlerErrorCode"
    ]
    """<p>For requests with a status of <code>FAILED</code>, the associated error code.</p> <p>For error code definitions, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-test-contract-errors.html">Handler error codes</a> in the <i>CloudFormation Command Line Interface User Guide for Extension Development</i>.</p>"""
    retry_after: NotRequired["capo_cloudcontrol.types.timestamp.Timestamp"]
    """<p>When to next request the status of this resource operation request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProgressEvent) -> dict:
    out: dict = {}
    if "type_name" in value:
        out["TypeName"] = value["type_name"]
    if "identifier" in value:
        out["Identifier"] = value["identifier"]
    if "request_token" in value:
        out["RequestToken"] = value["request_token"]
    if "hooks_request_token" in value:
        out["HooksRequestToken"] = value["hooks_request_token"]
    if "operation" in value:
        out["Operation"] = value["operation"]
    if "operation_status" in value:
        out["OperationStatus"] = value["operation_status"]
    if "event_time" in value:
        import capo_cloudcontrol.types.timestamp

        out["EventTime"] = capo_cloudcontrol.types.timestamp.serialize_aws_json_1_0(
            value["event_time"]
        )
    if "resource_model" in value:
        out["ResourceModel"] = value["resource_model"]
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "retry_after" in value:
        import capo_cloudcontrol.types.timestamp

        out["RetryAfter"] = capo_cloudcontrol.types.timestamp.serialize_aws_json_1_0(
            value["retry_after"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ProgressEvent:
    out: ProgressEvent = {}  # type: ignore[typeddict-item]
    if data.get("TypeName") is not None:
        out["type_name"] = data["TypeName"]
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    if data.get("RequestToken") is not None:
        out["request_token"] = data["RequestToken"]
    if data.get("HooksRequestToken") is not None:
        out["hooks_request_token"] = data["HooksRequestToken"]
    if data.get("Operation") is not None:
        out["operation"] = data["Operation"]
    if data.get("OperationStatus") is not None:
        out["operation_status"] = data["OperationStatus"]
    if data.get("EventTime") is not None:
        import capo_cloudcontrol.types.timestamp

        out["event_time"] = capo_cloudcontrol.types.timestamp.deserialize_aws_json_1_0(
            data["EventTime"]
        )
    if data.get("ResourceModel") is not None:
        out["resource_model"] = data["ResourceModel"]
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("RetryAfter") is not None:
        import capo_cloudcontrol.types.timestamp

        out["retry_after"] = capo_cloudcontrol.types.timestamp.deserialize_aws_json_1_0(
            data["RetryAfter"]
        )
    return out
