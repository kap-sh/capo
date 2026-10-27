"""Generated from Smithy shape ``com.amazonaws.deadline#FleetAttributeCapability``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.attribute_capability_name
    import capo_deadline.types.attribute_capability_values_list


class FleetAttributeCapability(TypedDict, closed=True):
    name: "capo_deadline.types.attribute_capability_name.AttributeCapabilityName"
    """The name of the fleet attribute capability for the worker."""
    values: "capo_deadline.types.attribute_capability_values_list.AttributeCapabilityValuesList"
    """The number of fleet attribute capabilities."""


# --- restJson1 ser/de ---
def serialize_json(value: FleetAttributeCapability) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_deadline.types.attribute_capability_values_list

    out["values"] = capo_deadline.types.attribute_capability_values_list.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> FleetAttributeCapability:
    out: FleetAttributeCapability = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("values") is not None:
        import capo_deadline.types.attribute_capability_values_list

        out["values"] = (
            capo_deadline.types.attribute_capability_values_list.deserialize_json(
                data["values"]
            )
        )
    else:
        out["values"] = []
    return out
