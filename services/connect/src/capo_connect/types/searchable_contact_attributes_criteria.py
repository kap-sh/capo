"""Generated from Smithy shape ``com.amazonaws.connect#SearchableContactAttributesCriteria``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.searchable_contact_attribute_key
    import capo_connect.types.searchable_contact_attribute_value_list


class SearchableContactAttributesCriteria(TypedDict, closed=True):
    key: "capo_connect.types.searchable_contact_attribute_key.SearchableContactAttributeKey"
    """<p>The key containing a searchable user-defined contact attribute.</p>"""
    values: "capo_connect.types.searchable_contact_attribute_value_list.SearchableContactAttributeValueList"
    """<p>The list of values to search for within a user-defined contact attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchableContactAttributesCriteria) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    import capo_connect.types.searchable_contact_attribute_value_list

    out["Values"] = (
        capo_connect.types.searchable_contact_attribute_value_list.serialize_json(
            value["values"]
        )
    )
    return out


def deserialize_json(data: dict) -> SearchableContactAttributesCriteria:
    out: SearchableContactAttributesCriteria = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        out["key"] = ""
    if data.get("Values") is not None:
        import capo_connect.types.searchable_contact_attribute_value_list

        out["values"] = (
            capo_connect.types.searchable_contact_attribute_value_list.deserialize_json(
                data["Values"]
            )
        )
    else:
        out["values"] = []
    return out


def redact_sensitive(value: SearchableContactAttributesCriteria) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "key" in value:
        out["key"] = "*** Sensitive Data Redacted ***"
    if "values" in value:
        import capo_connect.types.searchable_contact_attribute_value_list

        out["values"] = (
            capo_connect.types.searchable_contact_attribute_value_list.redact_sensitive(
                value["values"]
            )
        )
    return out
