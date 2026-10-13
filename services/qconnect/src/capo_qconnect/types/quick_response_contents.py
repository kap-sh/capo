"""Generated from Smithy shape ``com.amazonaws.qconnect#QuickResponseContents``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.quick_response_content_provider


class QuickResponseContents(TypedDict, closed=True):
    plain_text: NotRequired[
        "capo_qconnect.types.quick_response_content_provider.QuickResponseContentProvider"
    ]
    markdown: NotRequired[
        "capo_qconnect.types.quick_response_content_provider.QuickResponseContentProvider"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: QuickResponseContents) -> dict:
    out: dict = {}
    if "plain_text" in value:
        import capo_qconnect.types.quick_response_content_provider

        out["plainText"] = (
            capo_qconnect.types.quick_response_content_provider.serialize_json(
                value["plain_text"]
            )
        )
    if "markdown" in value:
        import capo_qconnect.types.quick_response_content_provider

        out["markdown"] = (
            capo_qconnect.types.quick_response_content_provider.serialize_json(
                value["markdown"]
            )
        )
    return out


def deserialize_json(data: dict) -> QuickResponseContents:
    out: QuickResponseContents = {}  # type: ignore[typeddict-item]
    if data.get("plainText") is not None:
        import capo_qconnect.types.quick_response_content_provider

        out["plain_text"] = (
            capo_qconnect.types.quick_response_content_provider.deserialize_json(
                data["plainText"]
            )
        )
    if data.get("markdown") is not None:
        import capo_qconnect.types.quick_response_content_provider

        out["markdown"] = (
            capo_qconnect.types.quick_response_content_provider.deserialize_json(
                data["markdown"]
            )
        )
    return out


def redact_sensitive(value: QuickResponseContents) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "plain_text" in value:
        import capo_qconnect.types.quick_response_content_provider

        out["plain_text"] = (
            capo_qconnect.types.quick_response_content_provider.redact_sensitive(
                value["plain_text"]
            )
        )
    if "markdown" in value:
        import capo_qconnect.types.quick_response_content_provider

        out["markdown"] = (
            capo_qconnect.types.quick_response_content_provider.redact_sensitive(
                value["markdown"]
            )
        )
    return out
