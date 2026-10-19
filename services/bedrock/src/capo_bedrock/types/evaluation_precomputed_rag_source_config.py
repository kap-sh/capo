"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationPrecomputedRagSourceConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError
from capo_bedrock.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock.types.evaluation_precomputed_retrieve_and_generate_source_config
    import capo_bedrock.types.evaluation_precomputed_retrieve_source_config


class _EvaluationPrecomputedRagSourceConfig_retrieveSourceConfig(
    TypedDict, closed=True
):
    retrieveSourceConfig: "capo_bedrock.types.evaluation_precomputed_retrieve_source_config.EvaluationPrecomputedRetrieveSourceConfig"


class _EvaluationPrecomputedRagSourceConfig_retrieveAndGenerateSourceConfig(
    TypedDict, closed=True
):
    retrieveAndGenerateSourceConfig: "capo_bedrock.types.evaluation_precomputed_retrieve_and_generate_source_config.EvaluationPrecomputedRetrieveAndGenerateSourceConfig"


EvaluationPrecomputedRagSourceConfig: TypeAlias = (
    _EvaluationPrecomputedRagSourceConfig_retrieveSourceConfig
    | _EvaluationPrecomputedRagSourceConfig_retrieveAndGenerateSourceConfig
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationPrecomputedRagSourceConfig) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"EvaluationPrecomputedRagSourceConfig: cannot serialize unknown variant {value.name!r}"
        )
    elif "retrieveSourceConfig" in value:
        import capo_bedrock.types.evaluation_precomputed_retrieve_source_config

        return {
            "retrieveSourceConfig": capo_bedrock.types.evaluation_precomputed_retrieve_source_config.serialize_json(
                value["retrieveSourceConfig"]
            )
        }
    elif "retrieveAndGenerateSourceConfig" in value:
        import capo_bedrock.types.evaluation_precomputed_retrieve_and_generate_source_config

        return {
            "retrieveAndGenerateSourceConfig": capo_bedrock.types.evaluation_precomputed_retrieve_and_generate_source_config.serialize_json(
                value["retrieveAndGenerateSourceConfig"]
            )
        }
    else:
        raise SerializationError(
            "EvaluationPrecomputedRagSourceConfig: no variant present"
        )


def deserialize_json(data: dict) -> EvaluationPrecomputedRagSourceConfig:
    if data.get("retrieveSourceConfig") is not None:
        import capo_bedrock.types.evaluation_precomputed_retrieve_source_config

        return {
            "retrieveSourceConfig": capo_bedrock.types.evaluation_precomputed_retrieve_source_config.deserialize_json(
                data["retrieveSourceConfig"]
            )
        }
    elif data.get("retrieveAndGenerateSourceConfig") is not None:
        import capo_bedrock.types.evaluation_precomputed_retrieve_and_generate_source_config

        return {
            "retrieveAndGenerateSourceConfig": capo_bedrock.types.evaluation_precomputed_retrieve_and_generate_source_config.deserialize_json(
                data["retrieveAndGenerateSourceConfig"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "EvaluationPrecomputedRagSourceConfig: no recognized variant key"
        )
