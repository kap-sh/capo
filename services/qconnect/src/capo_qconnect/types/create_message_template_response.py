"""Generated from Smithy shape ``com.amazonaws.qconnect#CreateMessageTemplateResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.message_template_data


class CreateMessageTemplateResponse(TypedDict, closed=True):
    message_template: NotRequired[
        "capo_qconnect.types.message_template_data.MessageTemplateData"
    ]
    """<p>The message template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMessageTemplateResponse) -> dict:
    out: dict = {}
    if "message_template" in value:
        import capo_qconnect.types.message_template_data

        out["messageTemplate"] = (
            capo_qconnect.types.message_template_data.serialize_json(
                value["message_template"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateMessageTemplateResponse:
    out: CreateMessageTemplateResponse = {}  # type: ignore[typeddict-item]
    if data.get("messageTemplate") is not None:
        import capo_qconnect.types.message_template_data

        out["message_template"] = (
            capo_qconnect.types.message_template_data.deserialize_json(
                data["messageTemplate"]
            )
        )
    return out


def redact_sensitive(value: CreateMessageTemplateResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "message_template" in value:
        import capo_qconnect.types.message_template_data

        out["message_template"] = (
            capo_qconnect.types.message_template_data.redact_sensitive(
                value["message_template"]
            )
        )
    return out
