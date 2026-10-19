"""Generated from Smithy shape ``com.amazonaws.braket#InstanceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_braket.types.instance_type


class InstanceConfig(TypedDict, closed=True):
    instance_type: "capo_braket.types.instance_type.InstanceType"
    """<p>Configures the type of resource instances to use while running an Amazon Braket hybrid job.</p>"""
    volume_size_in_gb: "int"
    """<p>The size of the storage volume, in GB, to provision.</p>"""
    instance_count: NotRequired["int"]
    """<p>Configures the number of resource instances to use while running an Amazon Braket hybrid job on Amazon Braket. The default value is 1.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InstanceConfig) -> dict:
    out: dict = {}
    out["instanceType"] = value["instance_type"]
    out["volumeSizeInGb"] = value["volume_size_in_gb"]
    if "instance_count" in value:
        out["instanceCount"] = value["instance_count"]
    return out


def deserialize_json(data: dict) -> InstanceConfig:
    out: InstanceConfig = {}  # type: ignore[typeddict-item]
    if data.get("instanceType") is not None:
        out["instance_type"] = data["instanceType"]
    else:
        out["instance_type"] = ""
    if data.get("volumeSizeInGb") is not None:
        out["volume_size_in_gb"] = data["volumeSizeInGb"]
    else:
        out["volume_size_in_gb"] = 0
    if data.get("instanceCount") is not None:
        out["instance_count"] = data["instanceCount"]
    return out
