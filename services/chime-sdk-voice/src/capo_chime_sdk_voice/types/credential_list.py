"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#CredentialList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.credential

CredentialList: TypeAlias = list["capo_chime_sdk_voice.types.credential.Credential"]


# --- restJson1 ser/de ---
def serialize_json(value: CredentialList) -> list:
    import capo_chime_sdk_voice.types.credential

    out: list = []
    for item in value:
        out.append(capo_chime_sdk_voice.types.credential.serialize_json(item))
    return out


def deserialize_json(data: list) -> CredentialList:
    import capo_chime_sdk_voice.types.credential

    out: CredentialList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_chime_sdk_voice.types.credential.deserialize_json(item))
    return out


def redact_sensitive(value: CredentialList) -> list[Any]:
    import capo_chime_sdk_voice.types.credential

    return [
        capo_chime_sdk_voice.types.credential.redact_sensitive(item) for item in value
    ]
