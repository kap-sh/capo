"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ResourceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanroomsml.types.instance_type


class ResourceConfig(TypedDict, closed=True):
    instance_count: "int"
    """<p>The number of resources that are used to train the model.</p>"""
    instance_type: "capo_cleanroomsml.types.instance_type.InstanceType"
    """<p>The instance type that is used to train the model.</p>"""
    volume_size_in_gb: "int"
    """<p>The volume size of the instance that is used to train the model. Please see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-store-volumes.html">EC2 volume limit</a> for volume size limitations on different instance types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceConfig) -> dict:
    out: dict = {}
    out["instanceCount"] = value.get("instance_count", 1)
    import capo_cleanroomsml.types.instance_type

    out["instanceType"] = capo_cleanroomsml.types.instance_type.serialize_json(
        value["instance_type"]
    )
    out["volumeSizeInGB"] = value["volume_size_in_gb"]
    return out


def deserialize_json(data: dict) -> ResourceConfig:
    out: ResourceConfig = {}  # type: ignore[typeddict-item]
    if data.get("instanceCount") is not None:
        out["instance_count"] = data["instanceCount"]
    else:
        out["instance_count"] = 1
    if data.get("instanceType") is not None:
        import capo_cleanroomsml.types.instance_type

        out["instance_type"] = capo_cleanroomsml.types.instance_type.deserialize_json(
            data["instanceType"]
        )
    else:
        raise DeserializationError("ResourceConfig.instance_type required")
    if data.get("volumeSizeInGB") is not None:
        out["volume_size_in_gb"] = data["volumeSizeInGB"]
    else:
        raise DeserializationError("ResourceConfig.volume_size_in_gb required")
    return out
