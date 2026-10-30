"""Generated from Smithy shape ``com.amazonaws.ecs#SharingStrategy``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_ecs.errors import DeserializationError, SerializationError
from capo_ecs.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_ecs.types.nvidia_mps_allocation


class SharingStrategyNvidiaMpsMember(TypedDict, closed=True):
    nvidiaMps: "capo_ecs.types.nvidia_mps_allocation.NvidiaMpsAllocation"


SharingStrategy: TypeAlias = SharingStrategyNvidiaMpsMember | UnknownUnionMember


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SharingStrategy) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SharingStrategy: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "nvidiaMps" in value:
        import capo_ecs.types.nvidia_mps_allocation

        return {
            "nvidiaMps": capo_ecs.types.nvidia_mps_allocation.serialize_aws_json_1_1(
                value["nvidiaMps"]
            )
        }
    else:
        raise SerializationError("SharingStrategy: no variant present")


def deserialize_aws_json_1_1(data: dict) -> SharingStrategy:
    if data.get("nvidiaMps") is not None:
        import capo_ecs.types.nvidia_mps_allocation

        return {
            "nvidiaMps": capo_ecs.types.nvidia_mps_allocation.deserialize_aws_json_1_1(
                data["nvidiaMps"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("SharingStrategy: no recognized variant key")
