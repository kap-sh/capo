"""Generated from Smithy shape ``com.amazonaws.controltower#DeleteLandingZoneOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.operation_identifier


class DeleteLandingZoneOutput(TypedDict, closed=True):
    operation_identifier: (
        "capo_controltower.types.operation_identifier.OperationIdentifier"
    )
    """<p>&gt;A unique identifier assigned to a <code>DeleteLandingZone</code> operation. You can use this identifier as an input parameter of <code>GetLandingZoneOperation</code> to check the operation's status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLandingZoneOutput) -> dict:
    out: dict = {}
    out["operationIdentifier"] = value["operation_identifier"]
    return out


def deserialize_json(data: dict) -> DeleteLandingZoneOutput:
    out: DeleteLandingZoneOutput = {}  # type: ignore[typeddict-item]
    if data.get("operationIdentifier") is not None:
        out["operation_identifier"] = data["operationIdentifier"]
    else:
        out["operation_identifier"] = ""
    return out
