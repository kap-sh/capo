"""Generated from Smithy shape ``com.amazonaws.accountaccess#IdentityCenterDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_account_access.errors import DeserializationError

if TYPE_CHECKING:
    import capo_account_access.types.identity_center_application_arn
    import capo_account_access.types.identity_center_instance_arn


class IdentityCenterDetails(TypedDict, closed=True):
    instance_arn: "capo_account_access.types.identity_center_instance_arn.IdentityCenterInstanceArn"
    """<p>The ARN of the IAM Identity Center instance.</p>"""
    application_arn: NotRequired[
        "capo_account_access.types.identity_center_application_arn.IdentityCenterApplicationArn"
    ]
    """<p>The ARN of the IAM Identity Center application created for this account access manager application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdentityCenterDetails) -> dict:
    out: dict = {}
    out["instanceArn"] = value["instance_arn"]
    if "application_arn" in value:
        out["applicationArn"] = value["application_arn"]
    return out


def deserialize_json(data: dict) -> IdentityCenterDetails:
    out: IdentityCenterDetails = {}  # type: ignore[typeddict-item]
    if data.get("instanceArn") is not None:
        out["instance_arn"] = data["instanceArn"]
    else:
        raise DeserializationError("IdentityCenterDetails.instance_arn required")
    if data.get("applicationArn") is not None:
        out["application_arn"] = data["applicationArn"]
    return out
