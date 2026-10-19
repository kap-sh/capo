"""Generated from Smithy shape ``com.amazonaws.connectcases#ParentChildFieldOptionsMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.parent_child_field_option_value
    import capo_connectcases.types.parent_child_field_option_value_list


class ParentChildFieldOptionsMapping(TypedDict, closed=True):
    parent_field_option_value: "capo_connectcases.types.parent_child_field_option_value.ParentChildFieldOptionValue"
    """<p>The value in the parent field.</p>"""
    child_field_option_values: "capo_connectcases.types.parent_child_field_option_value_list.ParentChildFieldOptionValueList"
    """<p>A list of allowed values in the child field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParentChildFieldOptionsMapping) -> dict:
    out: dict = {}
    out["parentFieldOptionValue"] = value["parent_field_option_value"]
    import capo_connectcases.types.parent_child_field_option_value_list

    out["childFieldOptionValues"] = (
        capo_connectcases.types.parent_child_field_option_value_list.serialize_json(
            value["child_field_option_values"]
        )
    )
    return out


def deserialize_json(data: dict) -> ParentChildFieldOptionsMapping:
    out: ParentChildFieldOptionsMapping = {}  # type: ignore[typeddict-item]
    if data.get("parentFieldOptionValue") is not None:
        out["parent_field_option_value"] = data["parentFieldOptionValue"]
    else:
        out["parent_field_option_value"] = ""
    if data.get("childFieldOptionValues") is not None:
        import capo_connectcases.types.parent_child_field_option_value_list

        out["child_field_option_values"] = (
            capo_connectcases.types.parent_child_field_option_value_list.deserialize_json(
                data["childFieldOptionValues"]
            )
        )
    else:
        out["child_field_option_values"] = []
    return out
