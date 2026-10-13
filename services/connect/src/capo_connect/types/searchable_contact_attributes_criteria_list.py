"""Generated from Smithy shape ``com.amazonaws.connect#SearchableContactAttributesCriteriaList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.searchable_contact_attributes_criteria

SearchableContactAttributesCriteriaList: TypeAlias = list[
    "capo_connect.types.searchable_contact_attributes_criteria.SearchableContactAttributesCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchableContactAttributesCriteriaList) -> list:
    import capo_connect.types.searchable_contact_attributes_criteria

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.searchable_contact_attributes_criteria.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SearchableContactAttributesCriteriaList:
    import capo_connect.types.searchable_contact_attributes_criteria

    out: SearchableContactAttributesCriteriaList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_connect.types.searchable_contact_attributes_criteria.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: SearchableContactAttributesCriteriaList) -> list[Any]:
    import capo_connect.types.searchable_contact_attributes_criteria

    return [
        capo_connect.types.searchable_contact_attributes_criteria.redact_sensitive(item)
        for item in value
    ]
