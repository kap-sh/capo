"""Generated from Smithy shape ``com.amazonaws.qconnect#DeactivateMessageTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.uuid_or_arn
    import capo_qconnect.types.uuid_or_arn_or_either_with_qualifier
    import capo_qconnect.types.version


class DeactivateMessageTemplateRequest(TypedDict, closed=True):
    knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    message_template_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier"
    """<p>The identifier of the message template. Can be either the ID or the ARN. It cannot contain any qualifier.</p>"""
    version_number: "capo_qconnect.types.version.Version"
    """<p>The version number of the message template version to deactivate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeactivateMessageTemplateRequest) -> dict:
    out: dict = {}
    out["versionNumber"] = value["version_number"]
    return out


def deserialize_json(data: dict) -> DeactivateMessageTemplateRequest:
    out: DeactivateMessageTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("versionNumber") is not None:
        out["version_number"] = data["versionNumber"]
    else:
        out["version_number"] = 0
    return out
