"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AgentInsightStoreEncryptionMode``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies the encryption mode used to protect new Agent Insights. Valid values:</p> <dl> <dt>AWS_OWNED_KMS_KEY</dt> <dd> <p>Uses an AWS owned key.</p> </dd> <dt>CUSTOMER_MANAGED_KMS</dt> <dd> <p>Uses a customer managed AWS Key Management Service (AWS KMS) key.</p> </dd> </dl>"""
AgentInsightStoreEncryptionMode: TypeAlias = Literal[
    "AWS_OWNED_KMS_KEY",
    "CUSTOMER_MANAGED_KMS",
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentInsightStoreEncryptionMode) -> str:
    return value


def deserialize_json(data: str) -> AgentInsightStoreEncryptionMode:
    return cast(AgentInsightStoreEncryptionMode, data)
