"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#GetRotationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.ssm_contacts_arn


class GetRotationRequest(TypedDict, closed=True):
    rotation_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the on-call rotation to retrieve information about.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRotationRequest) -> dict:
    out: dict = {}
    out["RotationId"] = value["rotation_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRotationRequest:
    out: GetRotationRequest = {}  # type: ignore[typeddict-item]
    if data.get("RotationId") is not None:
        out["rotation_id"] = data["RotationId"]
    else:
        out["rotation_id"] = ""
    return out
