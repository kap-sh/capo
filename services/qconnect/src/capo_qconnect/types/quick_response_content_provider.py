"""Generated from Smithy shape ``com.amazonaws.qconnect#QuickResponseContentProvider``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError
from capo_qconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qconnect.types.quick_response_content


class _QuickResponseContentProvider_content(TypedDict, closed=True):
    content: "capo_qconnect.types.quick_response_content.QuickResponseContent"


QuickResponseContentProvider: TypeAlias = (
    _QuickResponseContentProvider_content | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: QuickResponseContentProvider) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"QuickResponseContentProvider: cannot serialize unknown variant {value.name!r}"
        )
    elif "content" in value:
        return {"content": value["content"]}
    else:
        raise SerializationError("QuickResponseContentProvider: no variant present")


def deserialize_json(data: dict) -> QuickResponseContentProvider:
    if data.get("content") is not None:
        return {"content": data["content"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "QuickResponseContentProvider: no recognized variant key"
        )


def redact_sensitive(
    value: QuickResponseContentProvider,
) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "content" in value:
        out["content"] = "*** Sensitive Data Redacted ***"
    return out
