"""Generated from Smithy shape ``com.amazonaws.customerprofiles#EventTriggerDimension``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.object_attributes


class EventTriggerDimension(TypedDict, closed=True):
    object_attributes: "capo_customer_profiles.types.object_attributes.ObjectAttributes"
    """<p>A list of object attributes to be evaluated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventTriggerDimension) -> dict:
    out: dict = {}
    import capo_customer_profiles.types.object_attributes

    out["ObjectAttributes"] = (
        capo_customer_profiles.types.object_attributes.serialize_json(
            value["object_attributes"]
        )
    )
    return out


def deserialize_json(data: dict) -> EventTriggerDimension:
    out: EventTriggerDimension = {}  # type: ignore[typeddict-item]
    if data.get("ObjectAttributes") is not None:
        import capo_customer_profiles.types.object_attributes

        out["object_attributes"] = (
            capo_customer_profiles.types.object_attributes.deserialize_json(
                data["ObjectAttributes"]
            )
        )
    else:
        out["object_attributes"] = []
    return out
