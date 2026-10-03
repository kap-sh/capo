"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateEvaluatorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.evaluator_config
    import capo_bedrock_agentcore_control.types.evaluator_description
    import capo_bedrock_agentcore_control.types.evaluator_id
    import capo_bedrock_agentcore_control.types.evaluator_level
    import capo_bedrock_agentcore_control.types.kms_key_arn


class UpdateEvaluatorRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""
    evaluator_id: "capo_bedrock_agentcore_control.types.evaluator_id.EvaluatorId"
    """<p> The unique identifier of the evaluator to update. </p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.evaluator_description.EvaluatorDescription"
    ]
    """<p> The updated description of the evaluator. </p>"""
    evaluator_config: NotRequired[
        "capo_bedrock_agentcore_control.types.evaluator_config.EvaluatorConfig"
    ]
    """<p> The updated configuration for the evaluator. Specify either LLM-as-a-Judge settings with instructions, rating scale, and model configuration, or code-based settings with a customer-managed Lambda function. </p>"""
    level: NotRequired[
        "capo_bedrock_agentcore_control.types.evaluator_level.EvaluatorLevel"
    ]
    """<p> The updated evaluation level (<code>TOOL_CALL</code>, <code>TRACE</code>, or <code>SESSION</code>) that determines the scope of evaluation. </p>"""
    kms_key_arn: NotRequired[
        "capo_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
    ]
    """<p> The Amazon Resource Name (ARN) of a customer managed KMS key to use for encrypting sensitive evaluator data. Specify a new key ARN to rotate the encryption key, or specify a key ARN to add encryption to an evaluator that was previously created without one. When you rotate to a new key, the service decrypts the existing data with the old key and re-encrypts it with the new key. Only symmetric encryption KMS keys are supported. For more information, see <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations-encryption.html">Encryption at rest for AgentCore Evaluations</a>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEvaluatorRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "description" in value:
        out["description"] = value["description"]
    if "evaluator_config" in value:
        import capo_bedrock_agentcore_control.types.evaluator_config

        out["evaluatorConfig"] = (
            capo_bedrock_agentcore_control.types.evaluator_config.serialize_json(
                value["evaluator_config"]
            )
        )
    if "level" in value:
        import capo_bedrock_agentcore_control.types.evaluator_level

        out["level"] = (
            capo_bedrock_agentcore_control.types.evaluator_level.serialize_json(
                value["level"]
            )
        )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> UpdateEvaluatorRequest:
    out: UpdateEvaluatorRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("evaluatorConfig") is not None:
        import capo_bedrock_agentcore_control.types.evaluator_config

        out["evaluator_config"] = (
            capo_bedrock_agentcore_control.types.evaluator_config.deserialize_json(
                data["evaluatorConfig"]
            )
        )
    if data.get("level") is not None:
        import capo_bedrock_agentcore_control.types.evaluator_level

        out["level"] = (
            capo_bedrock_agentcore_control.types.evaluator_level.deserialize_json(
                data["level"]
            )
        )
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
