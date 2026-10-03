"""Generated from Smithy shape ``com.amazonaws.connect#StartContactMediaProcessingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.contact_id
    import capo_connect.types.contact_media_processing_failure_mode
    import capo_connect.types.instance_id


class StartContactMediaProcessingRequest(TypedDict, closed=True):
    instance_id: NotRequired["capo_connect.types.instance_id.InstanceId"]
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_id: NotRequired["capo_connect.types.contact_id.ContactId"]
    """<p>The identifier of the contact.</p>"""
    processor_arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p> The Amazon Resource Name (ARN) of the Lambda processor. You can find the Amazon Resource Name of the lambda in the lambda console. </p>"""
    failure_mode: NotRequired[
        "capo_connect.types.contact_media_processing_failure_mode.ContactMediaProcessingFailureMode"
    ]
    """<p> The desired behavior for failed message processing. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartContactMediaProcessingRequest) -> dict:
    out: dict = {}
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "contact_id" in value:
        out["ContactId"] = value["contact_id"]
    if "processor_arn" in value:
        out["ProcessorArn"] = value["processor_arn"]
    if "failure_mode" in value:
        import capo_connect.types.contact_media_processing_failure_mode

        out["FailureMode"] = (
            capo_connect.types.contact_media_processing_failure_mode.serialize_json(
                value["failure_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartContactMediaProcessingRequest:
    out: StartContactMediaProcessingRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    if data.get("ContactId") is not None:
        out["contact_id"] = data["ContactId"]
    if data.get("ProcessorArn") is not None:
        out["processor_arn"] = data["ProcessorArn"]
    if data.get("FailureMode") is not None:
        import capo_connect.types.contact_media_processing_failure_mode

        out["failure_mode"] = (
            capo_connect.types.contact_media_processing_failure_mode.deserialize_json(
                data["FailureMode"]
            )
        )
    return out
