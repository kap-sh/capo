"""Generated from Smithy shape ``com.amazonaws.ssm#DeleteActivationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.activation_id


class DeleteActivationRequest(TypedDict, closed=True):
    activation_id: "capo_ssm.types.activation_id.ActivationId"
    """<p>The ID of the activation that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteActivationRequest) -> dict:
    out: dict = {}
    out["ActivationId"] = value["activation_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteActivationRequest:
    out: DeleteActivationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ActivationId") is not None:
        out["activation_id"] = data["ActivationId"]
    else:
        out["activation_id"] = ""
    return out
