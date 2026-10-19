"""Generated from Smithy shape ``com.amazonaws.synthetics#DisassociateResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_synthetics.types.canary_arn
    import capo_synthetics.types.group_identifier


class DisassociateResourceRequest(TypedDict, closed=True):
    group_identifier: "capo_synthetics.types.group_identifier.GroupIdentifier"
    """<p>Specifies the group. You can specify the group name, the ARN, or the group ID as the <code>GroupIdentifier</code>.</p>"""
    resource_arn: "capo_synthetics.types.canary_arn.CanaryArn"
    """<p>The ARN of the canary that you want to remove from the specified group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> DisassociateResourceRequest:
    out: DisassociateResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    return out
