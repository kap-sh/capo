"""Generated from Smithy shape ``com.amazonaws.controltower#UpdateEnabledControlOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.operation_identifier


class UpdateEnabledControlOutput(TypedDict, closed=True):
    operation_identifier: (
        "capo_controltower.types.operation_identifier.OperationIdentifier"
    )
    """<p> The operation identifier for this <code>UpdateEnabledControl</code> operation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEnabledControlOutput) -> dict:
    out: dict = {}
    out["operationIdentifier"] = value["operation_identifier"]
    return out


def deserialize_json(data: dict) -> UpdateEnabledControlOutput:
    out: UpdateEnabledControlOutput = {}  # type: ignore[typeddict-item]
    if data.get("operationIdentifier") is not None:
        out["operation_identifier"] = data["operationIdentifier"]
    else:
        out["operation_identifier"] = ""
    return out
