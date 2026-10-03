"""Generated from Smithy shape ``com.amazonaws.qconnect#CreateAIPromptRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.ai_prompt_api_format
    import capo_qconnect.types.ai_prompt_inference_configuration
    import capo_qconnect.types.ai_prompt_model_identifier
    import capo_qconnect.types.ai_prompt_template_configuration
    import capo_qconnect.types.ai_prompt_template_type
    import capo_qconnect.types.ai_prompt_type
    import capo_qconnect.types.client_token
    import capo_qconnect.types.description
    import capo_qconnect.types.name
    import capo_qconnect.types.tags
    import capo_qconnect.types.uuid_or_arn
    import capo_qconnect.types.visibility_status


class CreateAIPromptRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_qconnect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>..</p>"""
    assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    name: "capo_qconnect.types.name.Name"
    """<p>The name of the AI Prompt.</p>"""
    type: "capo_qconnect.types.ai_prompt_type.AIPromptType"
    """<p>The type of this AI Prompt.</p>"""
    template_configuration: "capo_qconnect.types.ai_prompt_template_configuration.AIPromptTemplateConfiguration"
    """<p>The configuration of the prompt template for this AI Prompt.</p>"""
    visibility_status: "capo_qconnect.types.visibility_status.VisibilityStatus"
    """<p>The visibility status of the AI Prompt.</p>"""
    template_type: "capo_qconnect.types.ai_prompt_template_type.AIPromptTemplateType"
    """<p>The type of the prompt template for this AI Prompt.</p>"""
    model_id: "capo_qconnect.types.ai_prompt_model_identifier.AIPromptModelIdentifier"
    """<p>The identifier of the model used for this AI Prompt.</p> <note> <p>For information about which models are supported in each Amazon Web Services Region, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/create-ai-prompts.html#cli-create-aiprompt">Supported models for system/custom prompts</a>.</p> </note>"""
    api_format: "capo_qconnect.types.ai_prompt_api_format.AIPromptAPIFormat"
    """<p>The API Format of the AI Prompt.</p> <p>Recommended values: <code>MESSAGES | TEXT_COMPLETIONS</code> </p> <note> <p>The values <code>ANTHROPIC_CLAUDE_MESSAGES | ANTHROPIC_CLAUDE_TEXT_COMPLETIONS</code> will be deprecated.</p> </note>"""
    tags: NotRequired["capo_qconnect.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""
    description: NotRequired["capo_qconnect.types.description.Description"]
    """<p>The description of the AI Prompt.</p>"""
    inference_configuration: NotRequired[
        "capo_qconnect.types.ai_prompt_inference_configuration.AIPromptInferenceConfiguration"
    ]
    """<p>The inference configuration for the AI Prompt being created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAIPromptRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["name"] = value["name"]
    out["type"] = value["type"]
    import capo_qconnect.types.ai_prompt_template_configuration

    out["templateConfiguration"] = (
        capo_qconnect.types.ai_prompt_template_configuration.serialize_json(
            value["template_configuration"]
        )
    )
    out["visibilityStatus"] = value["visibility_status"]
    out["templateType"] = value["template_type"]
    out["modelId"] = value["model_id"]
    out["apiFormat"] = value["api_format"]
    if "tags" in value:
        import capo_qconnect.types.tags

        out["tags"] = capo_qconnect.types.tags.serialize_json(value["tags"])
    if "description" in value:
        out["description"] = value["description"]
    if "inference_configuration" in value:
        import capo_qconnect.types.ai_prompt_inference_configuration

        out["inferenceConfiguration"] = (
            capo_qconnect.types.ai_prompt_inference_configuration.serialize_json(
                value["inference_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateAIPromptRequest:
    out: CreateAIPromptRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAIPromptRequest.name required")
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        raise DeserializationError("CreateAIPromptRequest.type required")
    if data.get("templateConfiguration") is not None:
        import capo_qconnect.types.ai_prompt_template_configuration

        out["template_configuration"] = (
            capo_qconnect.types.ai_prompt_template_configuration.deserialize_json(
                data["templateConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAIPromptRequest.template_configuration required"
        )
    if data.get("visibilityStatus") is not None:
        out["visibility_status"] = data["visibilityStatus"]
    else:
        raise DeserializationError("CreateAIPromptRequest.visibility_status required")
    if data.get("templateType") is not None:
        out["template_type"] = data["templateType"]
    else:
        raise DeserializationError("CreateAIPromptRequest.template_type required")
    if data.get("modelId") is not None:
        out["model_id"] = data["modelId"]
    else:
        raise DeserializationError("CreateAIPromptRequest.model_id required")
    if data.get("apiFormat") is not None:
        out["api_format"] = data["apiFormat"]
    else:
        raise DeserializationError("CreateAIPromptRequest.api_format required")
    if data.get("tags") is not None:
        import capo_qconnect.types.tags

        out["tags"] = capo_qconnect.types.tags.deserialize_json(data["tags"])
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("inferenceConfiguration") is not None:
        import capo_qconnect.types.ai_prompt_inference_configuration

        out["inference_configuration"] = (
            capo_qconnect.types.ai_prompt_inference_configuration.deserialize_json(
                data["inferenceConfiguration"]
            )
        )
    return out
