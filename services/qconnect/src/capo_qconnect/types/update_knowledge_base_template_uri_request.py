"""Generated from Smithy shape ``com.amazonaws.qconnect#UpdateKnowledgeBaseTemplateUriRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.uri
    import capo_qconnect.types.uuid_or_arn


class UpdateKnowledgeBaseTemplateUriRequest(TypedDict, closed=True):
    knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    template_uri: "capo_qconnect.types.uri.Uri"
    """<p>The template URI to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateKnowledgeBaseTemplateUriRequest) -> dict:
    out: dict = {}
    out["templateUri"] = value["template_uri"]
    return out


def deserialize_json(data: dict) -> UpdateKnowledgeBaseTemplateUriRequest:
    out: UpdateKnowledgeBaseTemplateUriRequest = {}  # type: ignore[typeddict-item]
    if data.get("templateUri") is not None:
        out["template_uri"] = data["templateUri"]
    else:
        out["template_uri"] = ""
    return out
