"""Generated from Smithy shape ``com.amazonaws.cloudformation#RecordHandlerProgressInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.client_request_token
    import capo_cloudformation.types.client_token
    import capo_cloudformation.types.handler_error_code
    import capo_cloudformation.types.operation_status
    import capo_cloudformation.types.resource_model
    import capo_cloudformation.types.status_message


class RecordHandlerProgressInput(TypedDict, closed=True):
    bearer_token: NotRequired["capo_cloudformation.types.client_token.ClientToken"]
    """<p>Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.</p>"""
    operation_status: NotRequired[
        "capo_cloudformation.types.operation_status.OperationStatus"
    ]
    """<p>Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.</p>"""
    current_operation_status: NotRequired[
        "capo_cloudformation.types.operation_status.OperationStatus"
    ]
    """<p>Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.</p>"""
    status_message: NotRequired[
        "capo_cloudformation.types.status_message.StatusMessage"
    ]
    """<p>Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.</p>"""
    error_code: NotRequired[
        "capo_cloudformation.types.handler_error_code.HandlerErrorCode"
    ]
    """<p>Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.</p>"""
    resource_model: NotRequired[
        "capo_cloudformation.types.resource_model.ResourceModel"
    ]
    """<p>Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.</p>"""
    client_request_token: NotRequired[
        "capo_cloudformation.types.client_request_token.ClientRequestToken"
    ]
    """<p>Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RecordHandlerProgressInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "bearer_token" in value:
        pairs.append((f"{key_prefix}BearerToken", str(value["bearer_token"])))
    if "operation_status" in value:
        import capo_cloudformation.types.operation_status

        capo_cloudformation.types.operation_status.serialize_query(
            value["operation_status"], pairs, f"{key_prefix}OperationStatus"
        )
    if "current_operation_status" in value:
        import capo_cloudformation.types.operation_status

        capo_cloudformation.types.operation_status.serialize_query(
            value["current_operation_status"],
            pairs,
            f"{key_prefix}CurrentOperationStatus",
        )
    if "status_message" in value:
        pairs.append((f"{key_prefix}StatusMessage", str(value["status_message"])))
    if "error_code" in value:
        import capo_cloudformation.types.handler_error_code

        capo_cloudformation.types.handler_error_code.serialize_query(
            value["error_code"], pairs, f"{key_prefix}ErrorCode"
        )
    if "resource_model" in value:
        pairs.append((f"{key_prefix}ResourceModel", str(value["resource_model"])))
    if "client_request_token" in value:
        pairs.append(
            (f"{key_prefix}ClientRequestToken", str(value["client_request_token"]))
        )


def deserialize_query(el: Element) -> RecordHandlerProgressInput:
    out: RecordHandlerProgressInput = {}  # type: ignore[typeddict-item]
    child_bearer_token = el.find("BearerToken")
    if child_bearer_token is not None:
        out["bearer_token"] = str(child_bearer_token.text or "")
    child_operation_status = el.find("OperationStatus")
    if child_operation_status is not None:
        import capo_cloudformation.types.operation_status

        out["operation_status"] = (
            capo_cloudformation.types.operation_status.deserialize_query(
                child_operation_status
            )
        )
    child_current_operation_status = el.find("CurrentOperationStatus")
    if child_current_operation_status is not None:
        import capo_cloudformation.types.operation_status

        out["current_operation_status"] = (
            capo_cloudformation.types.operation_status.deserialize_query(
                child_current_operation_status
            )
        )
    child_status_message = el.find("StatusMessage")
    if child_status_message is not None:
        out["status_message"] = str(child_status_message.text or "")
    child_error_code = el.find("ErrorCode")
    if child_error_code is not None:
        import capo_cloudformation.types.handler_error_code

        out["error_code"] = (
            capo_cloudformation.types.handler_error_code.deserialize_query(
                child_error_code
            )
        )
    child_resource_model = el.find("ResourceModel")
    if child_resource_model is not None:
        out["resource_model"] = str(child_resource_model.text or "")
    child_client_request_token = el.find("ClientRequestToken")
    if child_client_request_token is not None:
        out["client_request_token"] = str(child_client_request_token.text or "")
    return out
