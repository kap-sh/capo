"""Generated from Smithy shape ``com.amazonaws.controltower#CreateLandingZoneOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.arn
    import capo_controltower.types.operation_identifier


class CreateLandingZoneOutput(TypedDict, closed=True):
    arn: "capo_controltower.types.arn.Arn"
    """<p>The ARN of the landing zone resource.</p>"""
    operation_identifier: (
        "capo_controltower.types.operation_identifier.OperationIdentifier"
    )
    """<p>A unique identifier assigned to a <code>CreateLandingZone</code> operation. You can use this identifier as an input of <code>GetLandingZoneOperation</code> to check the operation's status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLandingZoneOutput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["operationIdentifier"] = value["operation_identifier"]
    return out


def deserialize_json(data: dict) -> CreateLandingZoneOutput:
    out: CreateLandingZoneOutput = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("operationIdentifier") is not None:
        out["operation_identifier"] = data["operationIdentifier"]
    else:
        out["operation_identifier"] = ""
    return out
