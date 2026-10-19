"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#DeleteRotationOverrideRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.ssm_contacts_arn
    import capo_ssm_contacts.types.uuid


class DeleteRotationOverrideRequest(TypedDict, closed=True):
    rotation_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the rotation that was overridden.</p>"""
    rotation_override_id: "capo_ssm_contacts.types.uuid.Uuid"
    """<p>The Amazon Resource Name (ARN) of the on-call rotation override to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRotationOverrideRequest) -> dict:
    out: dict = {}
    out["RotationId"] = value["rotation_id"]
    out["RotationOverrideId"] = value["rotation_override_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRotationOverrideRequest:
    out: DeleteRotationOverrideRequest = {}  # type: ignore[typeddict-item]
    if data.get("RotationId") is not None:
        out["rotation_id"] = data["RotationId"]
    else:
        out["rotation_id"] = ""
    if data.get("RotationOverrideId") is not None:
        out["rotation_override_id"] = data["RotationOverrideId"]
    else:
        out["rotation_override_id"] = ""
    return out
