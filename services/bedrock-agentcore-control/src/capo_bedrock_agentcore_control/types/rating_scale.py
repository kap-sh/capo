"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RatingScale``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.categorical_scale_definitions
    import capo_bedrock_agentcore_control.types.numerical_scale_definitions


class _RatingScale_numerical(TypedDict, closed=True):
    numerical: "capo_bedrock_agentcore_control.types.numerical_scale_definitions.NumericalScaleDefinitions"


class _RatingScale_categorical(TypedDict, closed=True):
    categorical: "capo_bedrock_agentcore_control.types.categorical_scale_definitions.CategoricalScaleDefinitions"


RatingScale: TypeAlias = (
    _RatingScale_numerical | _RatingScale_categorical | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RatingScale) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RatingScale: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "numerical" in value:
        import capo_bedrock_agentcore_control.types.numerical_scale_definitions

        return {
            "numerical": capo_bedrock_agentcore_control.types.numerical_scale_definitions.serialize_json(
                value["numerical"]
            )
        }
    elif "categorical" in value:
        import capo_bedrock_agentcore_control.types.categorical_scale_definitions

        return {
            "categorical": capo_bedrock_agentcore_control.types.categorical_scale_definitions.serialize_json(
                value["categorical"]
            )
        }
    else:
        raise SerializationError("RatingScale: no variant present")


def deserialize_json(data: dict) -> RatingScale:
    if data.get("numerical") is not None:
        import capo_bedrock_agentcore_control.types.numerical_scale_definitions

        return {
            "numerical": capo_bedrock_agentcore_control.types.numerical_scale_definitions.deserialize_json(
                data["numerical"]
            )
        }
    elif data.get("categorical") is not None:
        import capo_bedrock_agentcore_control.types.categorical_scale_definitions

        return {
            "categorical": capo_bedrock_agentcore_control.types.categorical_scale_definitions.deserialize_json(
                data["categorical"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("RatingScale: no recognized variant key")
