"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#CreateRotationOverrideResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.uuid


class CreateRotationOverrideResult(TypedDict, closed=True):
    rotation_override_id: "capo_ssm_contacts.types.uuid.Uuid"
    """<p>The Amazon Resource Name (ARN) of the created rotation override.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRotationOverrideResult) -> dict:
    out: dict = {}
    out["RotationOverrideId"] = value["rotation_override_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRotationOverrideResult:
    out: CreateRotationOverrideResult = {}  # type: ignore[typeddict-item]
    if data.get("RotationOverrideId") is not None:
        out["rotation_override_id"] = data["RotationOverrideId"]
    else:
        out["rotation_override_id"] = ""
    return out
