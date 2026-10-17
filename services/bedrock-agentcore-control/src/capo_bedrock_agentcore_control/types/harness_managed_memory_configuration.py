"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessManagedMemoryConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_managed_memory_strategy_list
    import capo_bedrock_agentcore_control.types.kms_key_arn
    import capo_bedrock_agentcore_control.types.memory_arn


class HarnessManagedMemoryConfiguration(TypedDict, closed=True):
    arn: NotRequired["capo_bedrock_agentcore_control.types.memory_arn.MemoryArn"]
    """<p>The ARN of the managed AgentCore Memory resource. Read-only on Get, ignored on Create/Update input.</p>"""
    strategies: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_managed_memory_strategy_list.HarnessManagedMemoryStrategyList"
    ]
    """<p>Strategy types to enable. Defaults to [SEMANTIC, SUMMARIZATION].</p>"""
    event_expiry_duration: NotRequired["int"]
    """<p>Event retention in days. Defaults to 30.</p>"""
    encryption_key_arn: NotRequired[
        "capo_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>Customer-managed KMS key. Defaults to AWS-owned key. Not updatable after creation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessManagedMemoryConfiguration) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "strategies" in value:
        import capo_bedrock_agentcore_control.types.harness_managed_memory_strategy_list

        out["strategies"] = (
            capo_bedrock_agentcore_control.types.harness_managed_memory_strategy_list.serialize_json(
                value["strategies"]
            )
        )
    if "event_expiry_duration" in value:
        out["eventExpiryDuration"] = value["event_expiry_duration"]
    if "encryption_key_arn" in value:
        out["encryptionKeyArn"] = value["encryption_key_arn"]
    return out


def deserialize_json(data: dict) -> HarnessManagedMemoryConfiguration:
    out: HarnessManagedMemoryConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("strategies") is not None:
        import capo_bedrock_agentcore_control.types.harness_managed_memory_strategy_list

        out["strategies"] = (
            capo_bedrock_agentcore_control.types.harness_managed_memory_strategy_list.deserialize_json(
                data["strategies"]
            )
        )
    if data.get("eventExpiryDuration") is not None:
        out["event_expiry_duration"] = data["eventExpiryDuration"]
    if data.get("encryptionKeyArn") is not None:
        out["encryption_key_arn"] = data["encryptionKeyArn"]
    return out
