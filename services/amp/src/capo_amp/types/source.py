"""Generated from Smithy shape ``com.amazonaws.amp#Source``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_amp.errors import DeserializationError, SerializationError
from capo_amp.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_amp.types.eks_configuration
    import capo_amp.types.vpc_configuration


class _Source_eksConfiguration(TypedDict, closed=True):
    eksConfiguration: "capo_amp.types.eks_configuration.EksConfiguration"


class _Source_vpcConfiguration(TypedDict, closed=True):
    vpcConfiguration: "capo_amp.types.vpc_configuration.VpcConfiguration"


Source: TypeAlias = (
    _Source_eksConfiguration | _Source_vpcConfiguration | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: Source) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"Source: cannot serialize unknown variant {value.name!r}"
        )
    elif "eksConfiguration" in value:
        import capo_amp.types.eks_configuration

        return {
            "eksConfiguration": capo_amp.types.eks_configuration.serialize_json(
                value["eksConfiguration"]
            )
        }
    elif "vpcConfiguration" in value:
        import capo_amp.types.vpc_configuration

        return {
            "vpcConfiguration": capo_amp.types.vpc_configuration.serialize_json(
                value["vpcConfiguration"]
            )
        }
    else:
        raise SerializationError("Source: no variant present")


def deserialize_json(data: dict) -> Source:
    if data.get("eksConfiguration") is not None:
        import capo_amp.types.eks_configuration

        return {
            "eksConfiguration": capo_amp.types.eks_configuration.deserialize_json(
                data["eksConfiguration"]
            )
        }
    elif data.get("vpcConfiguration") is not None:
        import capo_amp.types.vpc_configuration

        return {
            "vpcConfiguration": capo_amp.types.vpc_configuration.deserialize_json(
                data["vpcConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("Source: no recognized variant key")
