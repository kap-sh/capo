"""Generated from Smithy shape ``com.amazonaws.storagegateway#SetSMBGuestPasswordInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.gateway_arn
    import capo_storage_gateway.types.smb_guest_password


class SetSMBGuestPasswordInput(TypedDict, closed=True):
    gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN"
    """<p>The Amazon Resource Name (ARN) of the S3 File Gateway the SMB file share is associated with.</p>"""
    password: "capo_storage_gateway.types.smb_guest_password.SMBGuestPassword"
    """<p>The password that you want to set for your SMB server.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetSMBGuestPasswordInput) -> dict:
    out: dict = {}
    out["GatewayARN"] = value["gateway_arn"]
    out["Password"] = value["password"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SetSMBGuestPasswordInput:
    out: SetSMBGuestPasswordInput = {}  # type: ignore[typeddict-item]
    if data.get("GatewayARN") is not None:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        out["gateway_arn"] = ""
    if data.get("Password") is not None:
        out["password"] = data["Password"]
    else:
        out["password"] = ""
    return out


def redact_sensitive(value: SetSMBGuestPasswordInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "password" in value:
        out["password"] = "*** Sensitive Data Redacted ***"
    return out
