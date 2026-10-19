"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#FieldInputConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.file_uploader_field_config
    import capo_amplifyuibuilder.types.value_mappings


class FieldInputConfig(TypedDict, closed=True):
    type: "str"
    """<p>The input type for the field. </p>"""
    required: NotRequired["bool"]
    """<p>Specifies a field that requires input.</p>"""
    read_only: NotRequired["bool"]
    """<p>Specifies a read only field.</p>"""
    placeholder: NotRequired["str"]
    """<p>The text to display as a placeholder for the field.</p>"""
    default_value: NotRequired["str"]
    """<p>The default value for the field.</p>"""
    descriptive_text: NotRequired["str"]
    """<p>The text to display to describe the field.</p>"""
    default_checked: NotRequired["bool"]
    """<p>Specifies whether a field has a default value.</p>"""
    default_country_code: NotRequired["str"]
    """<p>The default country code for a phone number.</p>"""
    value_mappings: NotRequired[
        "capo_amplifyuibuilder.types.value_mappings.ValueMappings"
    ]
    """<p>The information to use to customize the input fields with data at runtime.</p>"""
    name: NotRequired["str"]
    """<p>The name of the field.</p>"""
    min_value: NotRequired["float"]
    """<p>The minimum value to display for the field.</p>"""
    max_value: NotRequired["float"]
    """<p>The maximum value to display for the field.</p>"""
    step: NotRequired["float"]
    """<p>The stepping increment for a numeric value in a field.</p>"""
    value: NotRequired["str"]
    """<p>The value for the field.</p>"""
    is_array: NotRequired["bool"]
    """<p>Specifies whether to render the field as an array. This property is ignored if the <code>dataSourceType</code> for the form is a Data Store.</p>"""
    file_uploader_config: NotRequired[
        "capo_amplifyuibuilder.types.file_uploader_field_config.FileUploaderFieldConfig"
    ]
    """<p>The configuration for the file uploader field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldInputConfig) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    if "required" in value:
        out["required"] = value["required"]
    if "read_only" in value:
        out["readOnly"] = value["read_only"]
    if "placeholder" in value:
        out["placeholder"] = value["placeholder"]
    if "default_value" in value:
        out["defaultValue"] = value["default_value"]
    if "descriptive_text" in value:
        out["descriptiveText"] = value["descriptive_text"]
    if "default_checked" in value:
        out["defaultChecked"] = value["default_checked"]
    if "default_country_code" in value:
        out["defaultCountryCode"] = value["default_country_code"]
    if "value_mappings" in value:
        import capo_amplifyuibuilder.types.value_mappings

        out["valueMappings"] = (
            capo_amplifyuibuilder.types.value_mappings.serialize_json(
                value["value_mappings"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "min_value" in value:
        out["minValue"] = (
            "NaN"
            if value["min_value"] != value["min_value"]
            else "Infinity"
            if value["min_value"] == float("inf")
            else "-Infinity"
            if value["min_value"] == float("-inf")
            else value["min_value"]
        )
    if "max_value" in value:
        out["maxValue"] = (
            "NaN"
            if value["max_value"] != value["max_value"]
            else "Infinity"
            if value["max_value"] == float("inf")
            else "-Infinity"
            if value["max_value"] == float("-inf")
            else value["max_value"]
        )
    if "step" in value:
        out["step"] = (
            "NaN"
            if value["step"] != value["step"]
            else "Infinity"
            if value["step"] == float("inf")
            else "-Infinity"
            if value["step"] == float("-inf")
            else value["step"]
        )
    if "value" in value:
        out["value"] = value["value"]
    if "is_array" in value:
        out["isArray"] = value["is_array"]
    if "file_uploader_config" in value:
        import capo_amplifyuibuilder.types.file_uploader_field_config

        out["fileUploaderConfig"] = (
            capo_amplifyuibuilder.types.file_uploader_field_config.serialize_json(
                value["file_uploader_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> FieldInputConfig:
    out: FieldInputConfig = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("required") is not None:
        out["required"] = data["required"]
    if data.get("readOnly") is not None:
        out["read_only"] = data["readOnly"]
    if data.get("placeholder") is not None:
        out["placeholder"] = data["placeholder"]
    if data.get("defaultValue") is not None:
        out["default_value"] = data["defaultValue"]
    if data.get("descriptiveText") is not None:
        out["descriptive_text"] = data["descriptiveText"]
    if data.get("defaultChecked") is not None:
        out["default_checked"] = data["defaultChecked"]
    if data.get("defaultCountryCode") is not None:
        out["default_country_code"] = data["defaultCountryCode"]
    if data.get("valueMappings") is not None:
        import capo_amplifyuibuilder.types.value_mappings

        out["value_mappings"] = (
            capo_amplifyuibuilder.types.value_mappings.deserialize_json(
                data["valueMappings"]
            )
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("minValue") is not None:
        out["min_value"] = float(data["minValue"])
    if data.get("maxValue") is not None:
        out["max_value"] = float(data["maxValue"])
    if data.get("step") is not None:
        out["step"] = float(data["step"])
    if data.get("value") is not None:
        out["value"] = data["value"]
    if data.get("isArray") is not None:
        out["is_array"] = data["isArray"]
    if data.get("fileUploaderConfig") is not None:
        import capo_amplifyuibuilder.types.file_uploader_field_config

        out["file_uploader_config"] = (
            capo_amplifyuibuilder.types.file_uploader_field_config.deserialize_json(
                data["fileUploaderConfig"]
            )
        )
    return out
