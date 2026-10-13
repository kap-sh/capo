"""Generated from Smithy shape ``com.amazonaws.wisdom#UpdateQuickResponseResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wisdom.types.quick_response_data


class UpdateQuickResponseResponse(TypedDict, closed=True):
    quick_response: NotRequired[
        "capo_wisdom.types.quick_response_data.QuickResponseData"
    ]
    """<p>The quick response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQuickResponseResponse) -> dict:
    out: dict = {}
    if "quick_response" in value:
        import capo_wisdom.types.quick_response_data

        out["quickResponse"] = capo_wisdom.types.quick_response_data.serialize_json(
            value["quick_response"]
        )
    return out


def deserialize_json(data: dict) -> UpdateQuickResponseResponse:
    out: UpdateQuickResponseResponse = {}  # type: ignore[typeddict-item]
    if data.get("quickResponse") is not None:
        import capo_wisdom.types.quick_response_data

        out["quick_response"] = capo_wisdom.types.quick_response_data.deserialize_json(
            data["quickResponse"]
        )
    return out


def redact_sensitive(value: UpdateQuickResponseResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "quick_response" in value:
        import capo_wisdom.types.quick_response_data

        out["quick_response"] = capo_wisdom.types.quick_response_data.redact_sensitive(
            value["quick_response"]
        )
    return out
