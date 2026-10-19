"""Generated from Smithy shape ``com.amazonaws.bedrock#CustomModelDataSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError
from capo_bedrock.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock.types.model_package_arn_data_source


class _CustomModelDataSource_modelPackageArnDataSource(TypedDict, closed=True):
    modelPackageArnDataSource: (
        "capo_bedrock.types.model_package_arn_data_source.ModelPackageArnDataSource"
    )


CustomModelDataSource: TypeAlias = (
    _CustomModelDataSource_modelPackageArnDataSource | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: CustomModelDataSource) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"CustomModelDataSource: cannot serialize unknown variant {value.name!r}"
        )
    elif "modelPackageArnDataSource" in value:
        import capo_bedrock.types.model_package_arn_data_source

        return {
            "modelPackageArnDataSource": capo_bedrock.types.model_package_arn_data_source.serialize_json(
                value["modelPackageArnDataSource"]
            )
        }
    else:
        raise SerializationError("CustomModelDataSource: no variant present")


def deserialize_json(data: dict) -> CustomModelDataSource:
    if data.get("modelPackageArnDataSource") is not None:
        import capo_bedrock.types.model_package_arn_data_source

        return {
            "modelPackageArnDataSource": capo_bedrock.types.model_package_arn_data_source.deserialize_json(
                data["modelPackageArnDataSource"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("CustomModelDataSource: no recognized variant key")
