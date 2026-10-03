"""Generated from Smithy shape ``com.amazonaws.connect#GetEvaluationFormValidationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.resource_id
    import capo_connect.types.version_number


class GetEvaluationFormValidationRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    evaluation_form_id: "capo_connect.types.resource_id.ResourceId"
    """<p>The unique identifier for the evaluation form.</p>"""
    evaluation_form_version: NotRequired[
        "capo_connect.types.version_number.VersionNumber"
    ]
    """<p>The version of the evaluation form to retrieve validation results for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEvaluationFormValidationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEvaluationFormValidationRequest:
    out: GetEvaluationFormValidationRequest = {}  # type: ignore[typeddict-item]
    return out
