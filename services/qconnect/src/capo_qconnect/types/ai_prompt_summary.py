"""Generated from Smithy shape ``com.amazonaws.qconnect#AIPromptSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_qconnect.types.ai_prompt_api_format
    import capo_qconnect.types.ai_prompt_model_identifier
    import capo_qconnect.types.ai_prompt_template_type
    import capo_qconnect.types.ai_prompt_type
    import capo_qconnect.types.arn
    import capo_qconnect.types.description
    import capo_qconnect.types.name
    import capo_qconnect.types.origin
    import capo_qconnect.types.status
    import capo_qconnect.types.tags
    import capo_qconnect.types.uuid
    import capo_qconnect.types.visibility_status


class AIPromptSummary(TypedDict, closed=True):
    name: "capo_qconnect.types.name.Name"
    """<p>The name of the AI Prompt.</p>"""
    assistant_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    assistant_arn: "capo_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Q in Connect assistant.</p>"""
    ai_prompt_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the Amazon Q in Connect AI prompt.</p>"""
    type: "capo_qconnect.types.ai_prompt_type.AIPromptType"
    """<p>The type of this AI Prompt.</p>"""
    ai_prompt_arn: "capo_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the AI Prompt.</p>"""
    modified_time: NotRequired["datetime.datetime"]
    """<p>The time the AI Prompt was last modified.</p>"""
    template_type: "capo_qconnect.types.ai_prompt_template_type.AIPromptTemplateType"
    """<p>The type of the prompt template for this AI Prompt.</p>"""
    model_id: "capo_qconnect.types.ai_prompt_model_identifier.AIPromptModelIdentifier"
    """<p>The identifier of the model used for this AI Prompt. Model Ids supported are: <code>anthropic.claude-3-haiku-20240307-v1:0</code>.</p>"""
    api_format: "capo_qconnect.types.ai_prompt_api_format.AIPromptAPIFormat"
    """<p>The API format used for this AI Prompt.</p>"""
    visibility_status: "capo_qconnect.types.visibility_status.VisibilityStatus"
    """<p>The visibility status of the AI Prompt.</p>"""
    origin: NotRequired["capo_qconnect.types.origin.Origin"]
    """<p>The origin of the AI Prompt. <code>SYSTEM</code> for a default AI Prompt created by Q in Connect or <code>CUSTOMER</code> for an AI Prompt created by calling AI Prompt creation APIs. </p>"""
    description: NotRequired["capo_qconnect.types.description.Description"]
    """<p>The description of the AI Prompt.</p>"""
    status: NotRequired["capo_qconnect.types.status.Status"]
    """<p>The status of the AI Prompt.</p>"""
    tags: NotRequired["capo_qconnect.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AIPromptSummary) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["assistantId"] = value["assistant_id"]
    out["assistantArn"] = value["assistant_arn"]
    out["aiPromptId"] = value["ai_prompt_id"]
    out["type"] = value["type"]
    out["aiPromptArn"] = value["ai_prompt_arn"]
    if "modified_time" in value:
        import capo_qconnect.types._prelude.timestamp

        out["modifiedTime"] = capo_qconnect.types._prelude.timestamp.serialize_json(
            value["modified_time"]
        )
    out["templateType"] = value["template_type"]
    out["modelId"] = value["model_id"]
    out["apiFormat"] = value["api_format"]
    out["visibilityStatus"] = value["visibility_status"]
    if "origin" in value:
        out["origin"] = value["origin"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        out["status"] = value["status"]
    if "tags" in value:
        import capo_qconnect.types.tags

        out["tags"] = capo_qconnect.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> AIPromptSummary:
    out: AIPromptSummary = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("assistantId") is not None:
        out["assistant_id"] = data["assistantId"]
    else:
        out["assistant_id"] = ""
    if data.get("assistantArn") is not None:
        out["assistant_arn"] = data["assistantArn"]
    else:
        out["assistant_arn"] = ""
    if data.get("aiPromptId") is not None:
        out["ai_prompt_id"] = data["aiPromptId"]
    else:
        out["ai_prompt_id"] = ""
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("aiPromptArn") is not None:
        out["ai_prompt_arn"] = data["aiPromptArn"]
    else:
        out["ai_prompt_arn"] = ""
    if data.get("modifiedTime") is not None:
        import capo_qconnect.types._prelude.timestamp

        out["modified_time"] = capo_qconnect.types._prelude.timestamp.deserialize_json(
            data["modifiedTime"]
        )
    if data.get("templateType") is not None:
        out["template_type"] = data["templateType"]
    else:
        out["template_type"] = ""
    if data.get("modelId") is not None:
        out["model_id"] = data["modelId"]
    else:
        out["model_id"] = ""
    if data.get("apiFormat") is not None:
        out["api_format"] = data["apiFormat"]
    else:
        out["api_format"] = ""
    if data.get("visibilityStatus") is not None:
        out["visibility_status"] = data["visibilityStatus"]
    else:
        out["visibility_status"] = ""
    if data.get("origin") is not None:
        out["origin"] = data["origin"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("tags") is not None:
        import capo_qconnect.types.tags

        out["tags"] = capo_qconnect.types.tags.deserialize_json(data["tags"])
    return out
