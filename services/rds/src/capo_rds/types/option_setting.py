"""Generated from Smithy shape ``com.amazonaws.rds#OptionSetting``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean
    import capo_rds.types.potentially_sensitive_option_setting_value
    import capo_rds.types.string


class OptionSetting(TypedDict, closed=True):
    name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the option that has settings that you can set.</p>"""
    value: NotRequired[
        "capo_rds.types.potentially_sensitive_option_setting_value.PotentiallySensitiveOptionSettingValue"
    ]
    """<p>The current value of the option setting.</p>"""
    default_value: NotRequired["capo_rds.types.string.String"]
    """<p>The default value of the option setting.</p>"""
    description: NotRequired["capo_rds.types.string.String"]
    """<p>The description of the option setting.</p>"""
    apply_type: NotRequired["capo_rds.types.string.String"]
    """<p>The DB engine specific parameter type.</p>"""
    data_type: NotRequired["capo_rds.types.string.String"]
    """<p>The data type of the option setting.</p>"""
    allowed_values: NotRequired["capo_rds.types.string.String"]
    """<p>The allowed values of the option setting.</p>"""
    is_modifiable: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether the option setting can be modified from the default.</p>"""
    is_collection: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether the option setting is part of a collection.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: OptionSetting, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))
    if "value" in value:
        pairs.append((f"{key_prefix}Value", str(value["value"])))
    if "default_value" in value:
        pairs.append((f"{key_prefix}DefaultValue", str(value["default_value"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "apply_type" in value:
        pairs.append((f"{key_prefix}ApplyType", str(value["apply_type"])))
    if "data_type" in value:
        pairs.append((f"{key_prefix}DataType", str(value["data_type"])))
    if "allowed_values" in value:
        pairs.append((f"{key_prefix}AllowedValues", str(value["allowed_values"])))
    if "is_modifiable" in value:
        pairs.append(
            (f"{key_prefix}IsModifiable", "true" if value["is_modifiable"] else "false")
        )
    if "is_collection" in value:
        pairs.append(
            (f"{key_prefix}IsCollection", "true" if value["is_collection"] else "false")
        )


def deserialize_query(el: Element) -> OptionSetting:
    out: OptionSetting = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    child_default_value = el.find("DefaultValue")
    if child_default_value is not None:
        out["default_value"] = str(child_default_value.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_apply_type = el.find("ApplyType")
    if child_apply_type is not None:
        out["apply_type"] = str(child_apply_type.text or "")
    child_data_type = el.find("DataType")
    if child_data_type is not None:
        out["data_type"] = str(child_data_type.text or "")
    child_allowed_values = el.find("AllowedValues")
    if child_allowed_values is not None:
        out["allowed_values"] = str(child_allowed_values.text or "")
    child_is_modifiable = el.find("IsModifiable")
    if child_is_modifiable is not None:
        out["is_modifiable"] = (child_is_modifiable.text or "").lower() == "true"
    child_is_collection = el.find("IsCollection")
    if child_is_collection is not None:
        out["is_collection"] = (child_is_collection.text or "").lower() == "true"
    return out


def redact_sensitive(value: OptionSetting) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "value" in value:
        out["value"] = "*** Sensitive Data Redacted ***"
    return out
