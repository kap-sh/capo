"""Generated from Smithy shape ``com.amazonaws.iot#ProvisioningHook``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.payload_version
    import capo_iot.types.target_arn


class ProvisioningHook(TypedDict, closed=True):
    payload_version: NotRequired["capo_iot.types.payload_version.PayloadVersion"]
    """<p>The payload that was sent to the target function.</p> <p> <i>Note:</i> Only Lambda functions are currently supported.</p>"""
    target_arn: "capo_iot.types.target_arn.TargetArn"
    """<p>The ARN of the target function.</p> <p> <i>Note:</i> Only Lambda functions are currently supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProvisioningHook) -> dict:
    out: dict = {}
    if "payload_version" in value:
        out["payloadVersion"] = value["payload_version"]
    out["targetArn"] = value["target_arn"]
    return out


def deserialize_json(data: dict) -> ProvisioningHook:
    out: ProvisioningHook = {}  # type: ignore[typeddict-item]
    if data.get("payloadVersion") is not None:
        out["payload_version"] = data["payloadVersion"]
    if data.get("targetArn") is not None:
        out["target_arn"] = data["targetArn"]
    else:
        out["target_arn"] = ""
    return out
