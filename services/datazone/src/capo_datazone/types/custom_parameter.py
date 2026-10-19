"""Generated from Smithy shape ``com.amazonaws.datazone#CustomParameter``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.description


class CustomParameter(TypedDict, closed=True):
    key_name: "str"
    """<p>The key name of the parameter.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of the parameter.</p>"""
    field_type: "str"
    """<p>The filed type of the parameter.</p>"""
    default_value: NotRequired["str"]
    """<p>The default value of the parameter.</p>"""
    is_editable: NotRequired["bool"]
    """<p>Specifies whether the parameter is editable.</p>"""
    is_optional: NotRequired["bool"]
    """<p>Specifies whether the custom parameter is optional.</p>"""
    is_update_supported: NotRequired["bool"]
    """<p>Specifies whether a parameter value can be updated after creation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomParameter) -> dict:
    out: dict = {}
    out["keyName"] = value["key_name"]
    if "description" in value:
        out["description"] = value["description"]
    out["fieldType"] = value["field_type"]
    if "default_value" in value:
        out["defaultValue"] = value["default_value"]
    if "is_editable" in value:
        out["isEditable"] = value["is_editable"]
    if "is_optional" in value:
        out["isOptional"] = value["is_optional"]
    if "is_update_supported" in value:
        out["isUpdateSupported"] = value["is_update_supported"]
    return out


def deserialize_json(data: dict) -> CustomParameter:
    out: CustomParameter = {}  # type: ignore[typeddict-item]
    if data.get("keyName") is not None:
        out["key_name"] = data["keyName"]
    else:
        out["key_name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("fieldType") is not None:
        out["field_type"] = data["fieldType"]
    else:
        out["field_type"] = ""
    if data.get("defaultValue") is not None:
        out["default_value"] = data["defaultValue"]
    if data.get("isEditable") is not None:
        out["is_editable"] = data["isEditable"]
    if data.get("isOptional") is not None:
        out["is_optional"] = data["isOptional"]
    if data.get("isUpdateSupported") is not None:
        out["is_update_supported"] = data["isUpdateSupported"]
    return out


def redact_sensitive(value: CustomParameter) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
