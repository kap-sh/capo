"""Generated from Smithy shape ``com.amazonaws.wisdom#QuickResponseContentProvider``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_wisdom.errors import DeserializationError, SerializationError
from capo_wisdom.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_wisdom.types.quick_response_content


class _QuickResponseContentProvider_content(TypedDict, closed=True):
    content: "capo_wisdom.types.quick_response_content.QuickResponseContent"


QuickResponseContentProvider: TypeAlias = (
    _QuickResponseContentProvider_content | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: QuickResponseContentProvider) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"QuickResponseContentProvider: cannot serialize unknown variant {value['$unknown']['name']!r}"
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
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "QuickResponseContentProvider: no recognized variant key"
        )


def redact_sensitive(value: QuickResponseContentProvider) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        out["content"] = "*** Sensitive Data Redacted ***"
    return out
