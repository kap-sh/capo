"""Generated from Smithy shape ``com.amazonaws.continuum#ValidationProofOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.validation_proof_console_output


class ValidationProofOutput(TypedDict, closed=True):
    console_output: "capo_continuum.types.validation_proof_console_output.ValidationProofConsoleOutput"
    """What the run printed: standard output and standard error merged, as retained. The text may be empty."""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationProofOutput) -> dict:
    out: dict = {}
    out["consoleOutput"] = value["console_output"]
    return out


def deserialize_json(data: dict) -> ValidationProofOutput:
    out: ValidationProofOutput = {}  # type: ignore[typeddict-item]
    if data.get("consoleOutput") is not None:
        out["console_output"] = data["consoleOutput"]
    else:
        out["console_output"] = ""
    return out
