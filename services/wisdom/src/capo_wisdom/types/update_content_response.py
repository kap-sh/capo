"""Generated from Smithy shape ``com.amazonaws.wisdom#UpdateContentResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wisdom.types.content_data


class UpdateContentResponse(TypedDict, closed=True):
    content: NotRequired["capo_wisdom.types.content_data.ContentData"]
    """<p>The content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateContentResponse) -> dict:
    out: dict = {}
    if "content" in value:
        import capo_wisdom.types.content_data

        out["content"] = capo_wisdom.types.content_data.serialize_json(value["content"])
    return out


def deserialize_json(data: dict) -> UpdateContentResponse:
    out: UpdateContentResponse = {}  # type: ignore[typeddict-item]
    if data.get("content") is not None:
        import capo_wisdom.types.content_data

        out["content"] = capo_wisdom.types.content_data.deserialize_json(
            data["content"]
        )
    return out


def redact_sensitive(value: UpdateContentResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        import capo_wisdom.types.content_data

        out["content"] = capo_wisdom.types.content_data.redact_sensitive(
            value["content"]
        )
    return out
