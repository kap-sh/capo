"""Generated from Smithy shape ``com.amazonaws.controltower#UpdateEnabledControlInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.arn
    import capo_controltower.types.enabled_control_parameters


class UpdateEnabledControlInput(TypedDict, closed=True):
    parameters: (
        "capo_controltower.types.enabled_control_parameters.EnabledControlParameters"
    )
    """<p>A key/value pair, where <code>Key</code> is of type <code>String</code> and <code>Value</code> is of type <code>Document</code>.</p>"""
    enabled_control_identifier: "capo_controltower.types.arn.Arn"
    """<p> The ARN of the enabled control that will be updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEnabledControlInput) -> dict:
    out: dict = {}
    import capo_controltower.types.enabled_control_parameters

    out["parameters"] = (
        capo_controltower.types.enabled_control_parameters.serialize_json(
            value["parameters"]
        )
    )
    out["enabledControlIdentifier"] = value["enabled_control_identifier"]
    return out


def deserialize_json(data: dict) -> UpdateEnabledControlInput:
    out: UpdateEnabledControlInput = {}  # type: ignore[typeddict-item]
    if data.get("parameters") is not None:
        import capo_controltower.types.enabled_control_parameters

        out["parameters"] = (
            capo_controltower.types.enabled_control_parameters.deserialize_json(
                data["parameters"]
            )
        )
    else:
        out["parameters"] = []
    if data.get("enabledControlIdentifier") is not None:
        out["enabled_control_identifier"] = data["enabledControlIdentifier"]
    else:
        out["enabled_control_identifier"] = ""
    return out
