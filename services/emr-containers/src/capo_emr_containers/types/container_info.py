"""Generated from Smithy shape ``com.amazonaws.emrcontainers#ContainerInfo``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_emr_containers.errors import DeserializationError, SerializationError
from capo_emr_containers.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_emr_containers.types.eks_info


class _ContainerInfo_eksInfo(TypedDict, closed=True):
    eksInfo: "capo_emr_containers.types.eks_info.EksInfo"


ContainerInfo: TypeAlias = _ContainerInfo_eksInfo | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: ContainerInfo) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"ContainerInfo: cannot serialize unknown variant {value.name!r}"
        )
    elif "eksInfo" in value:
        import capo_emr_containers.types.eks_info

        return {
            "eksInfo": capo_emr_containers.types.eks_info.serialize_json(
                value["eksInfo"]
            )
        }
    else:
        raise SerializationError("ContainerInfo: no variant present")


def deserialize_json(data: dict) -> ContainerInfo:
    if data.get("eksInfo") is not None:
        import capo_emr_containers.types.eks_info

        return {
            "eksInfo": capo_emr_containers.types.eks_info.deserialize_json(
                data["eksInfo"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("ContainerInfo: no recognized variant key")
