"""Generated from Smithy shape ``com.amazonaws.deadline#StepRequiredCapabilities``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.step_amount_capabilities
    import capo_deadline.types.step_attribute_capabilities


class StepRequiredCapabilities(TypedDict, closed=True):
    attributes: (
        "capo_deadline.types.step_attribute_capabilities.StepAttributeCapabilities"
    )
    """The capability attributes that the step requires."""
    amounts: "capo_deadline.types.step_amount_capabilities.StepAmountCapabilities"
    """The capability amounts that the step requires."""


# --- restJson1 ser/de ---
def serialize_json(value: StepRequiredCapabilities) -> dict:
    out: dict = {}
    import capo_deadline.types.step_attribute_capabilities

    out["attributes"] = capo_deadline.types.step_attribute_capabilities.serialize_json(
        value["attributes"]
    )
    import capo_deadline.types.step_amount_capabilities

    out["amounts"] = capo_deadline.types.step_amount_capabilities.serialize_json(
        value["amounts"]
    )
    return out


def deserialize_json(data: dict) -> StepRequiredCapabilities:
    out: StepRequiredCapabilities = {}  # type: ignore[typeddict-item]
    if data.get("attributes") is not None:
        import capo_deadline.types.step_attribute_capabilities

        out["attributes"] = (
            capo_deadline.types.step_attribute_capabilities.deserialize_json(
                data["attributes"]
            )
        )
    else:
        out["attributes"] = []
    if data.get("amounts") is not None:
        import capo_deadline.types.step_amount_capabilities

        out["amounts"] = capo_deadline.types.step_amount_capabilities.deserialize_json(
            data["amounts"]
        )
    else:
        out["amounts"] = []
    return out
