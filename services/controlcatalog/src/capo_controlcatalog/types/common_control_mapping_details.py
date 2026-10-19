"""Generated from Smithy shape ``com.amazonaws.controlcatalog#CommonControlMappingDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_controlcatalog.types.common_control_arn


class CommonControlMappingDetails(TypedDict, closed=True):
    common_control_arn: "capo_controlcatalog.types.common_control_arn.CommonControlArn"
    """<p>The Amazon Resource Name (ARN) that identifies the common control in the mapping.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CommonControlMappingDetails) -> dict:
    out: dict = {}
    out["CommonControlArn"] = value["common_control_arn"]
    return out


def deserialize_json(data: dict) -> CommonControlMappingDetails:
    out: CommonControlMappingDetails = {}  # type: ignore[typeddict-item]
    if data.get("CommonControlArn") is not None:
        out["common_control_arn"] = data["CommonControlArn"]
    else:
        out["common_control_arn"] = ""
    return out
