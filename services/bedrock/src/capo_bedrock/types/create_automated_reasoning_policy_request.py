"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateAutomatedReasoningPolicyRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition
    import capo_bedrock.types.automated_reasoning_policy_description
    import capo_bedrock.types.automated_reasoning_policy_name
    import capo_bedrock.types.idempotency_token
    import capo_bedrock.types.kms_key_id
    import capo_bedrock.types.tag_list


class CreateAutomatedReasoningPolicyRequest(TypedDict, closed=True):
    name: "capo_bedrock.types.automated_reasoning_policy_name.AutomatedReasoningPolicyName"
    """<p>A unique name for the Automated Reasoning policy. The name must be between 1 and 63 characters and can contain letters, numbers, hyphens, and underscores.</p>"""
    description: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_description.AutomatedReasoningPolicyDescription"
    ]
    """<p>A description of the Automated Reasoning policy. Use this to provide context about the policy's purpose and the types of validations it performs.</p>"""
    client_request_token: NotRequired[
        "capo_bedrock.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than once. If this token matches a previous request, Amazon Bedrock ignores the request but doesn't return an error.</p>"""
    policy_definition: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_definition.AutomatedReasoningPolicyDefinition"
    ]
    """<p>The policy definition that contains the formal logic rules, variables, and custom variable types used to validate foundation model responses in your application.</p>"""
    kms_key_id: NotRequired["capo_bedrock.types.kms_key_id.KmsKeyId"]
    """<p>The identifier of the KMS key to use for encrypting the automated reasoning policy and its associated artifacts. If you don't specify a KMS key, Amazon Bedrock uses an KMS managed key for encryption. For enhanced security and control, you can specify a customer managed KMS key.</p>"""
    tags: NotRequired["capo_bedrock.types.tag_list.TagList"]
    """<p>A list of tags to associate with the Automated Reasoning policy. Tags help you organize and manage your policies.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAutomatedReasoningPolicyRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    if "policy_definition" in value:
        import capo_bedrock.types.automated_reasoning_policy_definition

        out["policyDefinition"] = (
            capo_bedrock.types.automated_reasoning_policy_definition.serialize_json(
                value["policy_definition"]
            )
        )
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "tags" in value:
        import capo_bedrock.types.tag_list

        out["tags"] = capo_bedrock.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateAutomatedReasoningPolicyRequest:
    out: CreateAutomatedReasoningPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "CreateAutomatedReasoningPolicyRequest.name required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    if data.get("policyDefinition") is not None:
        import capo_bedrock.types.automated_reasoning_policy_definition

        out["policy_definition"] = (
            capo_bedrock.types.automated_reasoning_policy_definition.deserialize_json(
                data["policyDefinition"]
            )
        )
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("tags") is not None:
        import capo_bedrock.types.tag_list

        out["tags"] = capo_bedrock.types.tag_list.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: CreateAutomatedReasoningPolicyRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "policy_definition" in value:
        import capo_bedrock.types.automated_reasoning_policy_definition

        out["policy_definition"] = (
            capo_bedrock.types.automated_reasoning_policy_definition.redact_sensitive(
                value["policy_definition"]
            )
        )
    return out
