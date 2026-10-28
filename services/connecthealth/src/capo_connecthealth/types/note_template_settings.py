"""Generated from Smithy shape ``com.amazonaws.connecthealth#NoteTemplateSettings``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_connecthealth.errors import DeserializationError, SerializationError
from capo_connecthealth.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connecthealth.types.custom_template
    import capo_connecthealth.types.managed_template


class NoteTemplateSettingsManagedTemplateMember(TypedDict, closed=True):
    managedTemplate: "capo_connecthealth.types.managed_template.ManagedTemplate"


class NoteTemplateSettingsCustomTemplateMember(TypedDict, closed=True):
    customTemplate: "capo_connecthealth.types.custom_template.CustomTemplate"


NoteTemplateSettings: TypeAlias = (
    NoteTemplateSettingsManagedTemplateMember
    | NoteTemplateSettingsCustomTemplateMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: NoteTemplateSettings) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"NoteTemplateSettings: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "managedTemplate" in value:
        import capo_connecthealth.types.managed_template

        return {
            "managedTemplate": capo_connecthealth.types.managed_template.serialize_json(
                value["managedTemplate"]
            )
        }
    elif "customTemplate" in value:
        import capo_connecthealth.types.custom_template

        return {
            "customTemplate": capo_connecthealth.types.custom_template.serialize_json(
                value["customTemplate"]
            )
        }
    else:
        raise SerializationError("NoteTemplateSettings: no variant present")


def deserialize_json(data: dict) -> NoteTemplateSettings:
    if data.get("managedTemplate") is not None:
        import capo_connecthealth.types.managed_template

        return {
            "managedTemplate": capo_connecthealth.types.managed_template.deserialize_json(
                data["managedTemplate"]
            )
        }
    elif data.get("customTemplate") is not None:
        import capo_connecthealth.types.custom_template

        return {
            "customTemplate": capo_connecthealth.types.custom_template.deserialize_json(
                data["customTemplate"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("NoteTemplateSettings: no recognized variant key")


def redact_sensitive(value: NoteTemplateSettings) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "customTemplate" in value:
        import capo_connecthealth.types.custom_template

        out["customTemplate"] = (
            capo_connecthealth.types.custom_template.redact_sensitive(
                value["customTemplate"]
            )
        )
    return out
