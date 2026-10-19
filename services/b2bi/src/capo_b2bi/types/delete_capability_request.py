"""Generated from Smithy shape ``com.amazonaws.b2bi#DeleteCapabilityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.capability_id


class DeleteCapabilityRequest(TypedDict, closed=True):
    capability_id: "capo_b2bi.types.capability_id.CapabilityId"
    """<p>Specifies a system-assigned unique identifier for the capability.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteCapabilityRequest) -> dict:
    out: dict = {}
    out["capabilityId"] = value["capability_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteCapabilityRequest:
    out: DeleteCapabilityRequest = {}  # type: ignore[typeddict-item]
    if data.get("capabilityId") is not None:
        out["capability_id"] = data["capabilityId"]
    else:
        out["capability_id"] = ""
    return out
