"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ABTestEvaluationConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.online_evaluation_config_arn
    import capo_bedrock_agentcore.types.per_variant_online_evaluation_config_list


class ABTestEvaluationConfigOnlineEvaluationConfigArnMember(TypedDict, closed=True):
    onlineEvaluationConfigArn: "capo_bedrock_agentcore.types.online_evaluation_config_arn.OnlineEvaluationConfigArn"


class ABTestEvaluationConfigPerVariantOnlineEvaluationConfigMember(
    TypedDict, closed=True
):
    perVariantOnlineEvaluationConfig: "capo_bedrock_agentcore.types.per_variant_online_evaluation_config_list.PerVariantOnlineEvaluationConfigList"


ABTestEvaluationConfig: TypeAlias = (
    ABTestEvaluationConfigOnlineEvaluationConfigArnMember
    | ABTestEvaluationConfigPerVariantOnlineEvaluationConfigMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ABTestEvaluationConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ABTestEvaluationConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "onlineEvaluationConfigArn" in value:
        return {"onlineEvaluationConfigArn": value["onlineEvaluationConfigArn"]}
    elif "perVariantOnlineEvaluationConfig" in value:
        import capo_bedrock_agentcore.types.per_variant_online_evaluation_config_list

        return {
            "perVariantOnlineEvaluationConfig": capo_bedrock_agentcore.types.per_variant_online_evaluation_config_list.serialize_json(
                value["perVariantOnlineEvaluationConfig"]
            )
        }
    else:
        raise SerializationError("ABTestEvaluationConfig: no variant present")


def deserialize_json(data: dict) -> ABTestEvaluationConfig:
    if data.get("onlineEvaluationConfigArn") is not None:
        return {"onlineEvaluationConfigArn": data["onlineEvaluationConfigArn"]}
    elif data.get("perVariantOnlineEvaluationConfig") is not None:
        import capo_bedrock_agentcore.types.per_variant_online_evaluation_config_list

        return {
            "perVariantOnlineEvaluationConfig": capo_bedrock_agentcore.types.per_variant_online_evaluation_config_list.deserialize_json(
                data["perVariantOnlineEvaluationConfig"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ABTestEvaluationConfig: no recognized variant key")
