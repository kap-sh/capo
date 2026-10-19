"""Generated from Smithy shape ``com.amazonaws.customerprofiles#FilterDimension``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.attribute_map


class FilterDimension(TypedDict, closed=True):
    attributes: "capo_customer_profiles.types.attribute_map.AttributeMap"
    """<p>Is the attribute within the FilterDimension map</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterDimension) -> dict:
    out: dict = {}
    import capo_customer_profiles.types.attribute_map

    out["Attributes"] = capo_customer_profiles.types.attribute_map.serialize_json(
        value["attributes"]
    )
    return out


def deserialize_json(data: dict) -> FilterDimension:
    out: FilterDimension = {}  # type: ignore[typeddict-item]
    if data.get("Attributes") is not None:
        import capo_customer_profiles.types.attribute_map

        out["attributes"] = capo_customer_profiles.types.attribute_map.deserialize_json(
            data["Attributes"]
        )
    else:
        out["attributes"] = {}
    return out
