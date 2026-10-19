"""Generated from Smithy shape ``com.amazonaws.controltower#EnableControlOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.arn
    import capo_controltower.types.operation_identifier


class EnableControlOutput(TypedDict, closed=True):
    operation_identifier: (
        "capo_controltower.types.operation_identifier.OperationIdentifier"
    )
    """<p>The ID of the asynchronous operation, which is used to track status. The operation is available for 90 days.</p>"""
    arn: NotRequired["capo_controltower.types.arn.Arn"]
    """<p>The ARN of the <code>EnabledControl</code> resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableControlOutput) -> dict:
    out: dict = {}
    out["operationIdentifier"] = value["operation_identifier"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> EnableControlOutput:
    out: EnableControlOutput = {}  # type: ignore[typeddict-item]
    if data.get("operationIdentifier") is not None:
        out["operation_identifier"] = data["operationIdentifier"]
    else:
        out["operation_identifier"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    return out
