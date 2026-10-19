"""Generated from Smithy shape ``com.amazonaws.qconnect#ActivateMessageTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.arn_with_qualifier
    import capo_qconnect.types.uuid
    import capo_qconnect.types.version


class ActivateMessageTemplateResponse(TypedDict, closed=True):
    message_template_arn: "capo_qconnect.types.arn_with_qualifier.ArnWithQualifier"
    """<p>The Amazon Resource Name (ARN) of the message template.</p>"""
    message_template_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the message template.</p>"""
    version_number: "capo_qconnect.types.version.Version"
    """<p>The version number of the message template version that is activated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActivateMessageTemplateResponse) -> dict:
    out: dict = {}
    out["messageTemplateArn"] = value["message_template_arn"]
    out["messageTemplateId"] = value["message_template_id"]
    out["versionNumber"] = value["version_number"]
    return out


def deserialize_json(data: dict) -> ActivateMessageTemplateResponse:
    out: ActivateMessageTemplateResponse = {}  # type: ignore[typeddict-item]
    if data.get("messageTemplateArn") is not None:
        out["message_template_arn"] = data["messageTemplateArn"]
    else:
        out["message_template_arn"] = ""
    if data.get("messageTemplateId") is not None:
        out["message_template_id"] = data["messageTemplateId"]
    else:
        out["message_template_id"] = ""
    if data.get("versionNumber") is not None:
        out["version_number"] = data["versionNumber"]
    else:
        out["version_number"] = 0
    return out
