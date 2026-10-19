"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ValueMappings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.form_input_binding_properties
    import capo_amplifyuibuilder.types.value_mapping_list


class ValueMappings(TypedDict, closed=True):
    values: "capo_amplifyuibuilder.types.value_mapping_list.ValueMappingList"
    """<p>The value and display value pairs.</p>"""
    binding_properties: NotRequired[
        "capo_amplifyuibuilder.types.form_input_binding_properties.FormInputBindingProperties"
    ]
    """<p>The information to bind fields to data at runtime.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValueMappings) -> dict:
    out: dict = {}
    import capo_amplifyuibuilder.types.value_mapping_list

    out["values"] = capo_amplifyuibuilder.types.value_mapping_list.serialize_json(
        value["values"]
    )
    if "binding_properties" in value:
        import capo_amplifyuibuilder.types.form_input_binding_properties

        out["bindingProperties"] = (
            capo_amplifyuibuilder.types.form_input_binding_properties.serialize_json(
                value["binding_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> ValueMappings:
    out: ValueMappings = {}  # type: ignore[typeddict-item]
    if data.get("values") is not None:
        import capo_amplifyuibuilder.types.value_mapping_list

        out["values"] = capo_amplifyuibuilder.types.value_mapping_list.deserialize_json(
            data["values"]
        )
    else:
        out["values"] = []
    if data.get("bindingProperties") is not None:
        import capo_amplifyuibuilder.types.form_input_binding_properties

        out["binding_properties"] = (
            capo_amplifyuibuilder.types.form_input_binding_properties.deserialize_json(
                data["bindingProperties"]
            )
        )
    return out
