"""Generated from Smithy shape ``com.amazonaws.connecthealth#NoteTemplateSettingsResponse``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connecthealth.errors import DeserializationError, SerializationError
from capo_connecthealth.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connecthealth.types.custom_template_response
    import capo_connecthealth.types.managed_template_response


class _NoteTemplateSettingsResponse_managedTemplate(TypedDict, closed=True):
    managedTemplate: (
        "capo_connecthealth.types.managed_template_response.ManagedTemplateResponse"
    )


class _NoteTemplateSettingsResponse_customTemplate(TypedDict, closed=True):
    customTemplate: (
        "capo_connecthealth.types.custom_template_response.CustomTemplateResponse"
    )


NoteTemplateSettingsResponse: TypeAlias = (
    _NoteTemplateSettingsResponse_managedTemplate
    | _NoteTemplateSettingsResponse_customTemplate
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: NoteTemplateSettingsResponse) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"NoteTemplateSettingsResponse: cannot serialize unknown variant {value.name!r}"
        )
    elif "managedTemplate" in value:
        import capo_connecthealth.types.managed_template_response

        return {
            "managedTemplate": capo_connecthealth.types.managed_template_response.serialize_json(
                value["managedTemplate"]
            )
        }
    elif "customTemplate" in value:
        import capo_connecthealth.types.custom_template_response

        return {
            "customTemplate": capo_connecthealth.types.custom_template_response.serialize_json(
                value["customTemplate"]
            )
        }
    else:
        raise SerializationError("NoteTemplateSettingsResponse: no variant present")


def deserialize_json(data: dict) -> NoteTemplateSettingsResponse:
    if data.get("managedTemplate") is not None:
        import capo_connecthealth.types.managed_template_response

        return {
            "managedTemplate": capo_connecthealth.types.managed_template_response.deserialize_json(
                data["managedTemplate"]
            )
        }
    elif data.get("customTemplate") is not None:
        import capo_connecthealth.types.custom_template_response

        return {
            "customTemplate": capo_connecthealth.types.custom_template_response.deserialize_json(
                data["customTemplate"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "NoteTemplateSettingsResponse: no recognized variant key"
        )
