"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Consolidation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.matching_attributes_list


class Consolidation(TypedDict, closed=True):
    matching_attributes_list: (
        "capo_customer_profiles.types.matching_attributes_list.MatchingAttributesList"
    )
    """<p>A list of matching criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Consolidation) -> dict:
    out: dict = {}
    import capo_customer_profiles.types.matching_attributes_list

    out["MatchingAttributesList"] = (
        capo_customer_profiles.types.matching_attributes_list.serialize_json(
            value["matching_attributes_list"]
        )
    )
    return out


def deserialize_json(data: dict) -> Consolidation:
    out: Consolidation = {}  # type: ignore[typeddict-item]
    if data.get("MatchingAttributesList") is not None:
        import capo_customer_profiles.types.matching_attributes_list

        out["matching_attributes_list"] = (
            capo_customer_profiles.types.matching_attributes_list.deserialize_json(
                data["MatchingAttributesList"]
            )
        )
    else:
        out["matching_attributes_list"] = []
    return out
