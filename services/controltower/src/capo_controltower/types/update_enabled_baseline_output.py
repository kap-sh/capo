"""Generated from Smithy shape ``com.amazonaws.controltower#UpdateEnabledBaselineOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.operation_identifier


class UpdateEnabledBaselineOutput(TypedDict, closed=True):
    operation_identifier: (
        "capo_controltower.types.operation_identifier.OperationIdentifier"
    )
    """<p>The ID (in UUID format) of the asynchronous <code>UpdateEnabledBaseline</code> operation. This <code>operationIdentifier</code> is used to track status through calls to the <code>GetBaselineOperation</code> API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEnabledBaselineOutput) -> dict:
    out: dict = {}
    out["operationIdentifier"] = value["operation_identifier"]
    return out


def deserialize_json(data: dict) -> UpdateEnabledBaselineOutput:
    out: UpdateEnabledBaselineOutput = {}  # type: ignore[typeddict-item]
    if data.get("operationIdentifier") is not None:
        out["operation_identifier"] = data["operationIdentifier"]
    else:
        out["operation_identifier"] = ""
    return out
