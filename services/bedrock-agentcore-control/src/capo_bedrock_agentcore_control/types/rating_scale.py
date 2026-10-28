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
    import capo_bedrock_agentcore_control.types.evaluation_dimensions
    import capo_bedrock_agentcore_control.types.numerical_scale_definitions


class RatingScaleNumericalMember(TypedDict, closed=True):
    numerical: "capo_bedrock_agentcore_control.types.numerical_scale_definitions.NumericalScaleDefinitions"


class RatingScaleCategoricalMember(TypedDict, closed=True):
    categorical: "capo_bedrock_agentcore_control.types.categorical_scale_definitions.CategoricalScaleDefinitions"


class RatingScaleMultiDimensionalMember(TypedDict, closed=True):
    multiDimensional: "capo_bedrock_agentcore_control.types.evaluation_dimensions.EvaluationDimensions"


RatingScale: TypeAlias = (
    RatingScaleNumericalMember
    | RatingScaleCategoricalMember
    | RatingScaleMultiDimensionalMember
    | UnknownUnionMember
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
    elif "multiDimensional" in value:
        import capo_bedrock_agentcore_control.types.evaluation_dimensions

        return {
            "multiDimensional": capo_bedrock_agentcore_control.types.evaluation_dimensions.serialize_json(
                value["multiDimensional"]
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
    elif data.get("multiDimensional") is not None:
        import capo_bedrock_agentcore_control.types.evaluation_dimensions

        return {
            "multiDimensional": capo_bedrock_agentcore_control.types.evaluation_dimensions.deserialize_json(
                data["multiDimensional"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("RatingScale: no recognized variant key")
