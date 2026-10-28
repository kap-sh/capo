"""Generated from Smithy shape ``com.amazonaws.qbusiness#RetrieverConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError, SerializationError
from capo_qbusiness.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qbusiness.types.kendra_index_configuration
    import capo_qbusiness.types.native_index_configuration


class RetrieverConfigurationNativeIndexConfigurationMember(TypedDict, closed=True):
    nativeIndexConfiguration: (
        "capo_qbusiness.types.native_index_configuration.NativeIndexConfiguration"
    )


class RetrieverConfigurationKendraIndexConfigurationMember(TypedDict, closed=True):
    kendraIndexConfiguration: (
        "capo_qbusiness.types.kendra_index_configuration.KendraIndexConfiguration"
    )


RetrieverConfiguration: TypeAlias = (
    RetrieverConfigurationNativeIndexConfigurationMember
    | RetrieverConfigurationKendraIndexConfigurationMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RetrieverConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RetrieverConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "nativeIndexConfiguration" in value:
        import capo_qbusiness.types.native_index_configuration

        return {
            "nativeIndexConfiguration": capo_qbusiness.types.native_index_configuration.serialize_json(
                value["nativeIndexConfiguration"]
            )
        }
    elif "kendraIndexConfiguration" in value:
        import capo_qbusiness.types.kendra_index_configuration

        return {
            "kendraIndexConfiguration": capo_qbusiness.types.kendra_index_configuration.serialize_json(
                value["kendraIndexConfiguration"]
            )
        }
    else:
        raise SerializationError("RetrieverConfiguration: no variant present")


def deserialize_json(data: dict) -> RetrieverConfiguration:
    if data.get("nativeIndexConfiguration") is not None:
        import capo_qbusiness.types.native_index_configuration

        return {
            "nativeIndexConfiguration": capo_qbusiness.types.native_index_configuration.deserialize_json(
                data["nativeIndexConfiguration"]
            )
        }
    elif data.get("kendraIndexConfiguration") is not None:
        import capo_qbusiness.types.kendra_index_configuration

        return {
            "kendraIndexConfiguration": capo_qbusiness.types.kendra_index_configuration.deserialize_json(
                data["kendraIndexConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("RetrieverConfiguration: no recognized variant key")
