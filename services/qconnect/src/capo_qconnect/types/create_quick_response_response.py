"""Generated from Smithy shape ``com.amazonaws.qconnect#CreateQuickResponseResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.quick_response_data


class CreateQuickResponseResponse(TypedDict, closed=True):
    quick_response: NotRequired[
        "capo_qconnect.types.quick_response_data.QuickResponseData"
    ]
    """<p>The quick response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateQuickResponseResponse) -> dict:
    out: dict = {}
    if "quick_response" in value:
        import capo_qconnect.types.quick_response_data

        out["quickResponse"] = capo_qconnect.types.quick_response_data.serialize_json(
            value["quick_response"]
        )
    return out


def deserialize_json(data: dict) -> CreateQuickResponseResponse:
    out: CreateQuickResponseResponse = {}  # type: ignore[typeddict-item]
    if data.get("quickResponse") is not None:
        import capo_qconnect.types.quick_response_data

        out["quick_response"] = (
            capo_qconnect.types.quick_response_data.deserialize_json(
                data["quickResponse"]
            )
        )
    return out


def redact_sensitive(value: CreateQuickResponseResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "quick_response" in value:
        import capo_qconnect.types.quick_response_data

        out["quick_response"] = (
            capo_qconnect.types.quick_response_data.redact_sensitive(
                value["quick_response"]
            )
        )
    return out
