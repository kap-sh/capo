"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SegmentSort``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.sort_attribute_list


class SegmentSort(TypedDict, closed=True):
    attributes: "capo_customer_profiles.types.sort_attribute_list.SortAttributeList"
    """<p>A list of attributes used to sort the segments and their ordering preferences.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SegmentSort) -> dict:
    out: dict = {}
    import capo_customer_profiles.types.sort_attribute_list

    out["Attributes"] = capo_customer_profiles.types.sort_attribute_list.serialize_json(
        value["attributes"]
    )
    return out


def deserialize_json(data: dict) -> SegmentSort:
    out: SegmentSort = {}  # type: ignore[typeddict-item]
    if data.get("Attributes") is not None:
        import capo_customer_profiles.types.sort_attribute_list

        out["attributes"] = (
            capo_customer_profiles.types.sort_attribute_list.deserialize_json(
                data["Attributes"]
            )
        )
    else:
        out["attributes"] = []
    return out
