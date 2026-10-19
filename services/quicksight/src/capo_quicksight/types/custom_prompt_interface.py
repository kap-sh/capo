"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomPromptInterface``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.model_profile_id
    import capo_quicksight.types.qbs_aws_account_id
    import capo_quicksight.types.sensitive_text
    import capo_quicksight.types.style_description
    import capo_quicksight.types.subscription_id


class CustomPromptInterface(TypedDict, closed=True):
    model_profile_id: "capo_quicksight.types.model_profile_id.ModelProfileId"
    """<p>The identifier of the model profile.</p>"""
    subscription_id: "capo_quicksight.types.subscription_id.SubscriptionId"
    """<p>The subscription identifier.</p>"""
    qbs_aws_account_id: "capo_quicksight.types.qbs_aws_account_id.QbsAwsAccountId"
    """<p>The Amazon Web Services account ID for the Q Business service.</p>"""
    response_length: NotRequired[
        "capo_quicksight.types.style_description.StyleDescription"
    ]
    """<p>Instructions for the desired response length.</p>"""
    output_style: NotRequired[
        "capo_quicksight.types.style_description.StyleDescription"
    ]
    """<p>Instructions for the desired output style.</p>"""
    identity: NotRequired["capo_quicksight.types.style_description.StyleDescription"]
    """<p>Instructions that define the agent's identity and persona.</p>"""
    tone: NotRequired["capo_quicksight.types.style_description.StyleDescription"]
    """<p>Instructions for the desired tone of responses.</p>"""
    custom_instructions: NotRequired[
        "capo_quicksight.types.style_description.StyleDescription"
    ]
    """<p>Custom instructions for the agent's behavior.</p>"""
    prompt_summary: NotRequired["capo_quicksight.types.sensitive_text.SensitiveText"]
    """<p>A summary of the custom prompt configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomPromptInterface) -> dict:
    out: dict = {}
    out["ModelProfileId"] = value["model_profile_id"]
    out["SubscriptionId"] = value["subscription_id"]
    out["QbsAwsAccountId"] = value["qbs_aws_account_id"]
    if "response_length" in value:
        out["ResponseLength"] = value["response_length"]
    if "output_style" in value:
        out["OutputStyle"] = value["output_style"]
    if "identity" in value:
        out["Identity"] = value["identity"]
    if "tone" in value:
        out["Tone"] = value["tone"]
    if "custom_instructions" in value:
        out["CustomInstructions"] = value["custom_instructions"]
    if "prompt_summary" in value:
        out["promptSummary"] = value["prompt_summary"]
    return out


def deserialize_json(data: dict) -> CustomPromptInterface:
    out: CustomPromptInterface = {}  # type: ignore[typeddict-item]
    if data.get("ModelProfileId") is not None:
        out["model_profile_id"] = data["ModelProfileId"]
    else:
        out["model_profile_id"] = ""
    if data.get("SubscriptionId") is not None:
        out["subscription_id"] = data["SubscriptionId"]
    else:
        out["subscription_id"] = ""
    if data.get("QbsAwsAccountId") is not None:
        out["qbs_aws_account_id"] = data["QbsAwsAccountId"]
    else:
        out["qbs_aws_account_id"] = ""
    if data.get("ResponseLength") is not None:
        out["response_length"] = data["ResponseLength"]
    if data.get("OutputStyle") is not None:
        out["output_style"] = data["OutputStyle"]
    if data.get("Identity") is not None:
        out["identity"] = data["Identity"]
    if data.get("Tone") is not None:
        out["tone"] = data["Tone"]
    if data.get("CustomInstructions") is not None:
        out["custom_instructions"] = data["CustomInstructions"]
    if data.get("promptSummary") is not None:
        out["prompt_summary"] = data["promptSummary"]
    return out


def redact_sensitive(value: CustomPromptInterface) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "response_length" in value:
        out["response_length"] = "*** Sensitive Data Redacted ***"
    if "output_style" in value:
        out["output_style"] = "*** Sensitive Data Redacted ***"
    if "identity" in value:
        out["identity"] = "*** Sensitive Data Redacted ***"
    if "tone" in value:
        out["tone"] = "*** Sensitive Data Redacted ***"
    if "custom_instructions" in value:
        out["custom_instructions"] = "*** Sensitive Data Redacted ***"
    if "prompt_summary" in value:
        out["prompt_summary"] = "*** Sensitive Data Redacted ***"
    return out
