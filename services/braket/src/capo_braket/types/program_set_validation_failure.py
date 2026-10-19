"""Generated from Smithy shape ``com.amazonaws.braket#ProgramSetValidationFailure``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_braket.types.program_validation_failures_list


class ProgramSetValidationFailure(TypedDict, closed=True):
    program_index: "int"
    """<p>The index of the program within the program set that failed validation.</p>"""
    inputs_index: NotRequired["int"]
    """<p>The index of the input within the program set that failed validation.</p>"""
    errors: NotRequired[
        "capo_braket.types.program_validation_failures_list.ProgramValidationFailuresList"
    ]
    """<p>A list of error messages describing the validation failures that occurred.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProgramSetValidationFailure) -> dict:
    out: dict = {}
    out["programIndex"] = value["program_index"]
    if "inputs_index" in value:
        out["inputsIndex"] = value["inputs_index"]
    if "errors" in value:
        import capo_braket.types.program_validation_failures_list

        out["errors"] = (
            capo_braket.types.program_validation_failures_list.serialize_json(
                value["errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProgramSetValidationFailure:
    out: ProgramSetValidationFailure = {}  # type: ignore[typeddict-item]
    if data.get("programIndex") is not None:
        out["program_index"] = data["programIndex"]
    else:
        out["program_index"] = 0
    if data.get("inputsIndex") is not None:
        out["inputs_index"] = data["inputsIndex"]
    if data.get("errors") is not None:
        import capo_braket.types.program_validation_failures_list

        out["errors"] = (
            capo_braket.types.program_validation_failures_list.deserialize_json(
                data["errors"]
            )
        )
    return out
