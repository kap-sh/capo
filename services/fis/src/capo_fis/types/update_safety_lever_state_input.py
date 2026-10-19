"""Generated from Smithy shape ``com.amazonaws.fis#UpdateSafetyLeverStateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_fis.types.safety_lever_status_input
    import capo_fis.types.safety_lever_status_reason


class UpdateSafetyLeverStateInput(TypedDict, closed=True):
    status: "capo_fis.types.safety_lever_status_input.SafetyLeverStatusInput"
    """<p> The updated state of the safety lever. </p>"""
    reason: "capo_fis.types.safety_lever_status_reason.SafetyLeverStatusReason"
    """<p> The reason for updating the state of the safety lever. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSafetyLeverStateInput) -> dict:
    out: dict = {}
    import capo_fis.types.safety_lever_status_input

    out["status"] = capo_fis.types.safety_lever_status_input.serialize_json(
        value["status"]
    )
    out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> UpdateSafetyLeverStateInput:
    out: UpdateSafetyLeverStateInput = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_fis.types.safety_lever_status_input

        out["status"] = capo_fis.types.safety_lever_status_input.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_fis.types.safety_lever_status_input.SafetyLeverStatusInput", ""
        )
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    else:
        out["reason"] = ""
    return out
