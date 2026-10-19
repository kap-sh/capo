"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#CreateRotationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.ssm_contacts_arn


class CreateRotationResult(TypedDict, closed=True):
    rotation_arn: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the created rotation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRotationResult) -> dict:
    out: dict = {}
    out["RotationArn"] = value["rotation_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRotationResult:
    out: CreateRotationResult = {}  # type: ignore[typeddict-item]
    if data.get("RotationArn") is not None:
        out["rotation_arn"] = data["RotationArn"]
    else:
        out["rotation_arn"] = ""
    return out
