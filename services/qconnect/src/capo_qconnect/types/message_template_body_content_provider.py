"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageTemplateBodyContentProvider``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError
from capo_qconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qconnect.types.non_empty_unlimited_string


class MessageTemplateBodyContentProviderContentMember(TypedDict, closed=True):
    content: "capo_qconnect.types.non_empty_unlimited_string.NonEmptyUnlimitedString"


MessageTemplateBodyContentProvider: TypeAlias = (
    MessageTemplateBodyContentProviderContentMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: MessageTemplateBodyContentProvider) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"MessageTemplateBodyContentProvider: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "content" in value:
        return {"content": value["content"]}
    else:
        raise SerializationError(
            "MessageTemplateBodyContentProvider: no variant present"
        )


def deserialize_json(data: dict) -> MessageTemplateBodyContentProvider:
    if data.get("content") is not None:
        return {"content": data["content"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "MessageTemplateBodyContentProvider: no recognized variant key"
        )


def redact_sensitive(value: MessageTemplateBodyContentProvider) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        out["content"] = "*** Sensitive Data Redacted ***"
    return out
