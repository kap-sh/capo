"""Generated from Smithy shape ``com.amazonaws.deadline#Ec2EbsVolume``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.ebs_iops
    import capo_deadline.types.ebs_throughput_mi_b
    import capo_deadline.types.integer


class Ec2EbsVolume(TypedDict, closed=True):
    size_gi_b: "capo_deadline.types.integer.Integer"
    """The EBS volume size in GiB."""
    iops: "capo_deadline.types.ebs_iops.EbsIops"
    """The IOPS per volume."""
    throughput_mi_b: "capo_deadline.types.ebs_throughput_mi_b.EbsThroughputMiB"
    """The throughput per volume in MiB."""


# --- restJson1 ser/de ---
def serialize_json(value: Ec2EbsVolume) -> dict:
    out: dict = {}
    out["sizeGiB"] = value.get("size_gi_b", 250)
    out["iops"] = value.get("iops", 3000)
    out["throughputMiB"] = value.get("throughput_mi_b", 125)
    return out


def deserialize_json(data: dict) -> Ec2EbsVolume:
    out: Ec2EbsVolume = {}  # type: ignore[typeddict-item]
    if data.get("sizeGiB") is not None:
        out["size_gi_b"] = data["sizeGiB"]
    else:
        out["size_gi_b"] = 250
    if data.get("iops") is not None:
        out["iops"] = data["iops"]
    else:
        out["iops"] = 3000
    if data.get("throughputMiB") is not None:
        out["throughput_mi_b"] = data["throughputMiB"]
    else:
        out["throughput_mi_b"] = 125
    return out
