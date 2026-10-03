"""Generated from Smithy shape ``com.amazonaws.connect#DeactivateEvaluationFormRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.resource_id
    import capo_connect.types.version_number


class DeactivateEvaluationFormRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    evaluation_form_id: "capo_connect.types.resource_id.ResourceId"
    """<p>The unique identifier for the evaluation form.</p>"""
    evaluation_form_version: "capo_connect.types.version_number.VersionNumber"
    """<p>A version of the evaluation form. If the version property is not provided, the latest version of the evaluation form is deactivated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeactivateEvaluationFormRequest) -> dict:
    out: dict = {}
    out["EvaluationFormVersion"] = value.get("evaluation_form_version", 0)
    return out


def deserialize_json(data: dict) -> DeactivateEvaluationFormRequest:
    out: DeactivateEvaluationFormRequest = {}  # type: ignore[typeddict-item]
    if data.get("EvaluationFormVersion") is not None:
        out["evaluation_form_version"] = data["EvaluationFormVersion"]
    else:
        out["evaluation_form_version"] = 0
    return out
