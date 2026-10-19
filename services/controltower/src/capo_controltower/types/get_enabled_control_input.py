"""Generated from Smithy shape ``com.amazonaws.controltower#GetEnabledControlInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.arn


class GetEnabledControlInput(TypedDict, closed=True):
    enabled_control_identifier: "capo_controltower.types.arn.Arn"
    """<p>The <code>controlIdentifier</code> of the enabled control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEnabledControlInput) -> dict:
    out: dict = {}
    out["enabledControlIdentifier"] = value["enabled_control_identifier"]
    return out


def deserialize_json(data: dict) -> GetEnabledControlInput:
    out: GetEnabledControlInput = {}  # type: ignore[typeddict-item]
    if data.get("enabledControlIdentifier") is not None:
        out["enabled_control_identifier"] = data["enabledControlIdentifier"]
    else:
        out["enabled_control_identifier"] = ""
    return out
