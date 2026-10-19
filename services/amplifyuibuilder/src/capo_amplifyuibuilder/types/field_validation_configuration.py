"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#FieldValidationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.num_values
    import capo_amplifyuibuilder.types.str_values


class FieldValidationConfiguration(TypedDict, closed=True):
    type: "str"
    """<p>The validation to perform on an object type.<code/> </p>"""
    str_values: NotRequired["capo_amplifyuibuilder.types.str_values.StrValues"]
    """<p>The validation to perform on a string value.</p>"""
    num_values: NotRequired["capo_amplifyuibuilder.types.num_values.NumValues"]
    """<p>The validation to perform on a number value.</p>"""
    validation_message: NotRequired["str"]
    """<p>The validation message to display.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldValidationConfiguration) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    if "str_values" in value:
        import capo_amplifyuibuilder.types.str_values

        out["strValues"] = capo_amplifyuibuilder.types.str_values.serialize_json(
            value["str_values"]
        )
    if "num_values" in value:
        import capo_amplifyuibuilder.types.num_values

        out["numValues"] = capo_amplifyuibuilder.types.num_values.serialize_json(
            value["num_values"]
        )
    if "validation_message" in value:
        out["validationMessage"] = value["validation_message"]
    return out


def deserialize_json(data: dict) -> FieldValidationConfiguration:
    out: FieldValidationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("strValues") is not None:
        import capo_amplifyuibuilder.types.str_values

        out["str_values"] = capo_amplifyuibuilder.types.str_values.deserialize_json(
            data["strValues"]
        )
    if data.get("numValues") is not None:
        import capo_amplifyuibuilder.types.num_values

        out["num_values"] = capo_amplifyuibuilder.types.num_values.deserialize_json(
            data["numValues"]
        )
    if data.get("validationMessage") is not None:
        out["validation_message"] = data["validationMessage"]
    return out
