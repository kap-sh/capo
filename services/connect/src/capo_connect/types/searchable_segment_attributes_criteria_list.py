"""Generated from Smithy shape ``com.amazonaws.connect#SearchableSegmentAttributesCriteriaList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.searchable_segment_attributes_criteria

SearchableSegmentAttributesCriteriaList: TypeAlias = list[
    "capo_connect.types.searchable_segment_attributes_criteria.SearchableSegmentAttributesCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchableSegmentAttributesCriteriaList) -> list:
    import capo_connect.types.searchable_segment_attributes_criteria

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.searchable_segment_attributes_criteria.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SearchableSegmentAttributesCriteriaList:
    import capo_connect.types.searchable_segment_attributes_criteria

    out: SearchableSegmentAttributesCriteriaList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_connect.types.searchable_segment_attributes_criteria.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: SearchableSegmentAttributesCriteriaList) -> list[Any]:
    import capo_connect.types.searchable_segment_attributes_criteria

    return [
        capo_connect.types.searchable_segment_attributes_criteria.redact_sensitive(item)
        for item in value
    ]
