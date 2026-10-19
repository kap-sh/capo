"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLProblemTypeResolvedAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_sagemaker.errors import DeserializationError, SerializationError
from capo_sagemaker.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_sagemaker.types.tabular_resolved_attributes
    import capo_sagemaker.types.text_generation_resolved_attributes


class _AutoMLProblemTypeResolvedAttributes_TabularResolvedAttributes(
    TypedDict, closed=True
):
    TabularResolvedAttributes: (
        "capo_sagemaker.types.tabular_resolved_attributes.TabularResolvedAttributes"
    )


class _AutoMLProblemTypeResolvedAttributes_TextGenerationResolvedAttributes(
    TypedDict, closed=True
):
    TextGenerationResolvedAttributes: "capo_sagemaker.types.text_generation_resolved_attributes.TextGenerationResolvedAttributes"


AutoMLProblemTypeResolvedAttributes: TypeAlias = (
    _AutoMLProblemTypeResolvedAttributes_TabularResolvedAttributes
    | _AutoMLProblemTypeResolvedAttributes_TextGenerationResolvedAttributes
    | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLProblemTypeResolvedAttributes) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"AutoMLProblemTypeResolvedAttributes: cannot serialize unknown variant {value.name!r}"
        )
    elif "TabularResolvedAttributes" in value:
        import capo_sagemaker.types.tabular_resolved_attributes

        return {
            "TabularResolvedAttributes": capo_sagemaker.types.tabular_resolved_attributes.serialize_aws_json_1_1(
                value["TabularResolvedAttributes"]
            )
        }
    elif "TextGenerationResolvedAttributes" in value:
        import capo_sagemaker.types.text_generation_resolved_attributes

        return {
            "TextGenerationResolvedAttributes": capo_sagemaker.types.text_generation_resolved_attributes.serialize_aws_json_1_1(
                value["TextGenerationResolvedAttributes"]
            )
        }
    else:
        raise SerializationError(
            "AutoMLProblemTypeResolvedAttributes: no variant present"
        )


def deserialize_aws_json_1_1(data: dict) -> AutoMLProblemTypeResolvedAttributes:
    if data.get("TabularResolvedAttributes") is not None:
        import capo_sagemaker.types.tabular_resolved_attributes

        return {
            "TabularResolvedAttributes": capo_sagemaker.types.tabular_resolved_attributes.deserialize_aws_json_1_1(
                data["TabularResolvedAttributes"]
            )
        }
    elif data.get("TextGenerationResolvedAttributes") is not None:
        import capo_sagemaker.types.text_generation_resolved_attributes

        return {
            "TextGenerationResolvedAttributes": capo_sagemaker.types.text_generation_resolved_attributes.deserialize_aws_json_1_1(
                data["TextGenerationResolvedAttributes"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "AutoMLProblemTypeResolvedAttributes: no recognized variant key"
        )
