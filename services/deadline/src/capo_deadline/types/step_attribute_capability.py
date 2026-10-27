"""Generated from Smithy shape ``com.amazonaws.deadline#StepAttributeCapability``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.attribute_capability_name
    import capo_deadline.types.list_attribute_capability_value


class StepAttributeCapability(TypedDict, closed=True):
    name: "capo_deadline.types.attribute_capability_name.AttributeCapabilityName"
    """The name of the step attribute."""
    any_of: NotRequired[
        "capo_deadline.types.list_attribute_capability_value.ListAttributeCapabilityValue"
    ]
    """Requires any of the step attributes in a given list."""
    all_of: NotRequired[
        "capo_deadline.types.list_attribute_capability_value.ListAttributeCapabilityValue"
    ]
    """Requires all of the step attribute values."""


# --- restJson1 ser/de ---
def serialize_json(value: StepAttributeCapability) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "any_of" in value:
        import capo_deadline.types.list_attribute_capability_value

        out["anyOf"] = (
            capo_deadline.types.list_attribute_capability_value.serialize_json(
                value["any_of"]
            )
        )
    if "all_of" in value:
        import capo_deadline.types.list_attribute_capability_value

        out["allOf"] = (
            capo_deadline.types.list_attribute_capability_value.serialize_json(
                value["all_of"]
            )
        )
    return out


def deserialize_json(data: dict) -> StepAttributeCapability:
    out: StepAttributeCapability = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("anyOf") is not None:
        import capo_deadline.types.list_attribute_capability_value

        out["any_of"] = (
            capo_deadline.types.list_attribute_capability_value.deserialize_json(
                data["anyOf"]
            )
        )
    if data.get("allOf") is not None:
        import capo_deadline.types.list_attribute_capability_value

        out["all_of"] = (
            capo_deadline.types.list_attribute_capability_value.deserialize_json(
                data["allOf"]
            )
        )
    return out
