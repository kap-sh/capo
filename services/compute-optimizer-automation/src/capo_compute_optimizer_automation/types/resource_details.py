"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#ResourceDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_compute_optimizer_automation.errors import (
    DeserializationError,
    SerializationError,
)
from capo_compute_optimizer_automation.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.ebs_volume


class _ResourceDetails_ebsVolume(TypedDict, closed=True):
    ebsVolume: "capo_compute_optimizer_automation.types.ebs_volume.EbsVolume"


ResourceDetails: TypeAlias = _ResourceDetails_ebsVolume | UnknownUnionMember


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ResourceDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "ebsVolume" in value:
        import capo_compute_optimizer_automation.types.ebs_volume

        return {
            "ebsVolume": capo_compute_optimizer_automation.types.ebs_volume.serialize_aws_json_1_0(
                value["ebsVolume"]
            )
        }
    else:
        raise SerializationError("ResourceDetails: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ResourceDetails:
    if data.get("ebsVolume") is not None:
        import capo_compute_optimizer_automation.types.ebs_volume

        return {
            "ebsVolume": capo_compute_optimizer_automation.types.ebs_volume.deserialize_aws_json_1_0(
                data["ebsVolume"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ResourceDetails: no recognized variant key")
