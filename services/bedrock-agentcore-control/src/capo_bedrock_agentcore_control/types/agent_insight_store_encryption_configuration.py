"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AgentInsightStoreEncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.agent_insight_store_encryption_mode
    import capo_bedrock_agentcore_control.types.kms_key_arn


class AgentInsightStoreEncryptionConfiguration(TypedDict, closed=True):
    mode: "capo_bedrock_agentcore_control.types.agent_insight_store_encryption_mode.AgentInsightStoreEncryptionMode"
    """<p>Specifies the encryption mode used to protect new Agent Insights.</p>"""
    kms_key_arn: NotRequired[
        "capo_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>Specifies the Amazon Resource Name (ARN) of the customer managed AWS KMS key that you use to encrypt new Agent Insights. This field is required when <code>mode</code> is <code>CUSTOMER_MANAGED_KMS</code> and cannot be specified when <code>mode</code> is <code>AWS_OWNED_KMS_KEY</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentInsightStoreEncryptionConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.agent_insight_store_encryption_mode

    out["mode"] = (
        capo_bedrock_agentcore_control.types.agent_insight_store_encryption_mode.serialize_json(
            value["mode"]
        )
    )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> AgentInsightStoreEncryptionConfiguration:
    out: AgentInsightStoreEncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("mode") is not None:
        import capo_bedrock_agentcore_control.types.agent_insight_store_encryption_mode

        out["mode"] = (
            capo_bedrock_agentcore_control.types.agent_insight_store_encryption_mode.deserialize_json(
                data["mode"]
            )
        )
    else:
        import typing

        out["mode"] = typing.cast(
            "capo_bedrock_agentcore_control.types.agent_insight_store_encryption_mode.AgentInsightStoreEncryptionMode",
            "",
        )
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
