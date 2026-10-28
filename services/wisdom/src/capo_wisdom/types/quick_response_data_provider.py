"""Generated from Smithy shape ``com.amazonaws.wisdom#QuickResponseDataProvider``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_wisdom.errors import DeserializationError, SerializationError
from capo_wisdom.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_wisdom.types.quick_response_content


class QuickResponseDataProviderContentMember(TypedDict, closed=True):
    content: "capo_wisdom.types.quick_response_content.QuickResponseContent"


QuickResponseDataProvider: TypeAlias = (
    QuickResponseDataProviderContentMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: QuickResponseDataProvider) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"QuickResponseDataProvider: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "content" in value:
        return {"content": value["content"]}
    else:
        raise SerializationError("QuickResponseDataProvider: no variant present")


def deserialize_json(data: dict) -> QuickResponseDataProvider:
    if data.get("content") is not None:
        return {"content": data["content"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "QuickResponseDataProvider: no recognized variant key"
        )


def redact_sensitive(value: QuickResponseDataProvider) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        out["content"] = "*** Sensitive Data Redacted ***"
    return out
