"""Generated from Smithy shape ``com.amazonaws.qconnect#UpdateAIPromptRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.ai_prompt_inference_configuration
    import capo_qconnect.types.ai_prompt_model_identifier
    import capo_qconnect.types.ai_prompt_template_configuration
    import capo_qconnect.types.client_token
    import capo_qconnect.types.description
    import capo_qconnect.types.uuid_or_arn
    import capo_qconnect.types.uuid_or_arn_or_either_with_qualifier
    import capo_qconnect.types.visibility_status


class UpdateAIPromptRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_qconnect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>..</p>"""
    assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    ai_prompt_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier"
    """<p>The identifier of the Amazon Q in Connect AI Prompt.</p>"""
    visibility_status: "capo_qconnect.types.visibility_status.VisibilityStatus"
    """<p>The visibility status of the Amazon Q in Connect AI prompt.</p>"""
    template_configuration: NotRequired[
        "capo_qconnect.types.ai_prompt_template_configuration.AIPromptTemplateConfiguration"
    ]
    """<p>The configuration of the prompt template for this AI Prompt.</p>"""
    description: NotRequired["capo_qconnect.types.description.Description"]
    """<p>The description of the Amazon Q in Connect AI Prompt.</p>"""
    model_id: NotRequired[
        "capo_qconnect.types.ai_prompt_model_identifier.AIPromptModelIdentifier"
    ]
    """<p>The identifier of the model used for this AI Prompt.</p> <note> <p>For information about which models are supported in each Amazon Web Services Region, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/create-ai-prompts.html#cli-create-aiprompt">Supported models for system/custom prompts</a>.</p> </note>"""
    inference_configuration: NotRequired[
        "capo_qconnect.types.ai_prompt_inference_configuration.AIPromptInferenceConfiguration"
    ]
    """<p>The updated inference configuration for the AI Prompt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAIPromptRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["visibilityStatus"] = value["visibility_status"]
    if "template_configuration" in value:
        import capo_qconnect.types.ai_prompt_template_configuration

        out["templateConfiguration"] = (
            capo_qconnect.types.ai_prompt_template_configuration.serialize_json(
                value["template_configuration"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "model_id" in value:
        out["modelId"] = value["model_id"]
    if "inference_configuration" in value:
        import capo_qconnect.types.ai_prompt_inference_configuration

        out["inferenceConfiguration"] = (
            capo_qconnect.types.ai_prompt_inference_configuration.serialize_json(
                value["inference_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAIPromptRequest:
    out: UpdateAIPromptRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("visibilityStatus") is not None:
        out["visibility_status"] = data["visibilityStatus"]
    else:
        raise DeserializationError("UpdateAIPromptRequest.visibility_status required")
    if data.get("templateConfiguration") is not None:
        import capo_qconnect.types.ai_prompt_template_configuration

        out["template_configuration"] = (
            capo_qconnect.types.ai_prompt_template_configuration.deserialize_json(
                data["templateConfiguration"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("modelId") is not None:
        out["model_id"] = data["modelId"]
    if data.get("inferenceConfiguration") is not None:
        import capo_qconnect.types.ai_prompt_inference_configuration

        out["inference_configuration"] = (
            capo_qconnect.types.ai_prompt_inference_configuration.deserialize_json(
                data["inferenceConfiguration"]
            )
        )
    return out
