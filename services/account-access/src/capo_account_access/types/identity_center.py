"""Generated from Smithy shape ``com.amazonaws.accountaccess#IdentityCenter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_account_access.errors import DeserializationError

if TYPE_CHECKING:
    import capo_account_access.types.identity_center_instance_arn


class IdentityCenter(TypedDict, closed=True):
    instance_arn: "capo_account_access.types.identity_center_instance_arn.IdentityCenterInstanceArn"
    """<p>The ARN of the IAM Identity Center instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdentityCenter) -> dict:
    out: dict = {}
    out["instanceArn"] = value["instance_arn"]
    return out


def deserialize_json(data: dict) -> IdentityCenter:
    out: IdentityCenter = {}  # type: ignore[typeddict-item]
    if data.get("instanceArn") is not None:
        out["instance_arn"] = data["instanceArn"]
    else:
        raise DeserializationError("IdentityCenter.instance_arn required")
    return out
