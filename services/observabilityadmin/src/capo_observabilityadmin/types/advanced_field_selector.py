"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AdvancedFieldSelector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.string_list


class AdvancedFieldSelector(TypedDict, closed=True):
    field: "str"
    """<p> The name of the field to use for selection. </p>"""
    equals: NotRequired["capo_observabilityadmin.types.string_list.StringList"]
    """<p> Matches if the field value equals the specified value. </p>"""
    starts_with: NotRequired["capo_observabilityadmin.types.string_list.StringList"]
    """<p> Matches if the field value starts with the specified value. </p>"""
    ends_with: NotRequired["capo_observabilityadmin.types.string_list.StringList"]
    """<p> Matches if the field value ends with the specified value. </p>"""
    not_equals: NotRequired["capo_observabilityadmin.types.string_list.StringList"]
    """<p> Matches if the field value does not equal the specified value. </p>"""
    not_starts_with: NotRequired["capo_observabilityadmin.types.string_list.StringList"]
    """<p> Matches if the field value does not start with the specified value. </p>"""
    not_ends_with: NotRequired["capo_observabilityadmin.types.string_list.StringList"]
    """<p> Matches if the field value does not end with the specified value. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdvancedFieldSelector) -> dict:
    out: dict = {}
    out["Field"] = value["field"]
    if "equals" in value:
        import capo_observabilityadmin.types.string_list

        out["Equals"] = capo_observabilityadmin.types.string_list.serialize_json(
            value["equals"]
        )
    if "starts_with" in value:
        import capo_observabilityadmin.types.string_list

        out["StartsWith"] = capo_observabilityadmin.types.string_list.serialize_json(
            value["starts_with"]
        )
    if "ends_with" in value:
        import capo_observabilityadmin.types.string_list

        out["EndsWith"] = capo_observabilityadmin.types.string_list.serialize_json(
            value["ends_with"]
        )
    if "not_equals" in value:
        import capo_observabilityadmin.types.string_list

        out["NotEquals"] = capo_observabilityadmin.types.string_list.serialize_json(
            value["not_equals"]
        )
    if "not_starts_with" in value:
        import capo_observabilityadmin.types.string_list

        out["NotStartsWith"] = capo_observabilityadmin.types.string_list.serialize_json(
            value["not_starts_with"]
        )
    if "not_ends_with" in value:
        import capo_observabilityadmin.types.string_list

        out["NotEndsWith"] = capo_observabilityadmin.types.string_list.serialize_json(
            value["not_ends_with"]
        )
    return out


def deserialize_json(data: dict) -> AdvancedFieldSelector:
    out: AdvancedFieldSelector = {}  # type: ignore[typeddict-item]
    if data.get("Field") is not None:
        out["field"] = data["Field"]
    else:
        out["field"] = ""
    if data.get("Equals") is not None:
        import capo_observabilityadmin.types.string_list

        out["equals"] = capo_observabilityadmin.types.string_list.deserialize_json(
            data["Equals"]
        )
    if data.get("StartsWith") is not None:
        import capo_observabilityadmin.types.string_list

        out["starts_with"] = capo_observabilityadmin.types.string_list.deserialize_json(
            data["StartsWith"]
        )
    if data.get("EndsWith") is not None:
        import capo_observabilityadmin.types.string_list

        out["ends_with"] = capo_observabilityadmin.types.string_list.deserialize_json(
            data["EndsWith"]
        )
    if data.get("NotEquals") is not None:
        import capo_observabilityadmin.types.string_list

        out["not_equals"] = capo_observabilityadmin.types.string_list.deserialize_json(
            data["NotEquals"]
        )
    if data.get("NotStartsWith") is not None:
        import capo_observabilityadmin.types.string_list

        out["not_starts_with"] = (
            capo_observabilityadmin.types.string_list.deserialize_json(
                data["NotStartsWith"]
            )
        )
    if data.get("NotEndsWith") is not None:
        import capo_observabilityadmin.types.string_list

        out["not_ends_with"] = (
            capo_observabilityadmin.types.string_list.deserialize_json(
                data["NotEndsWith"]
            )
        )
    return out
