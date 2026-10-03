"""Generated from Smithy shape ``com.amazonaws.connect#DeleteEvaluationFormRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.resource_id
    import capo_connect.types.version_number


class DeleteEvaluationFormRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    evaluation_form_id: "capo_connect.types.resource_id.ResourceId"
    """<p>The unique identifier for the evaluation form.</p>"""
    evaluation_form_version: NotRequired[
        "capo_connect.types.version_number.VersionNumber"
    ]
    """<p>The unique identifier for the evaluation form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEvaluationFormRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEvaluationFormRequest:
    out: DeleteEvaluationFormRequest = {}  # type: ignore[typeddict-item]
    return out
