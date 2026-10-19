"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#KmsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.key_type
    import capo_bedrock_agentcore_control.types.kms_key_arn


class KmsConfiguration(TypedDict, closed=True):
    key_type: "capo_bedrock_agentcore_control.types.key_type.KeyType"
    """<p>The type of KMS key (CustomerManagedKey or ServiceManagedKey).</p>"""
    kms_key_arn: NotRequired[
        "capo_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the KMS key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KmsConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.key_type

    out["keyType"] = capo_bedrock_agentcore_control.types.key_type.serialize_json(
        value["key_type"]
    )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> KmsConfiguration:
    out: KmsConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("keyType") is not None:
        import capo_bedrock_agentcore_control.types.key_type

        out["key_type"] = (
            capo_bedrock_agentcore_control.types.key_type.deserialize_json(
                data["keyType"]
            )
        )
    else:
        import typing

        out["key_type"] = typing.cast(
            "capo_bedrock_agentcore_control.types.key_type.KeyType", ""
        )
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
