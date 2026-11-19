"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#EbsVolumeConfiguration``."""

from typing_extensions import NotRequired, TypedDict


class EbsVolumeConfiguration(TypedDict, closed=True):
    type: NotRequired["str"]
    """<p>The EBS volume type, such as gp2, gp3, io1, io2, st1, or sc1.</p>"""
    size_in_gib: NotRequired["int"]
    """<p>The size of the EBS volume in gibibytes (GiB).</p>"""
    iops: NotRequired["int"]
    """<p>The number of I/O operations per second (IOPS) provisioned for the volume.</p>"""
    throughput: NotRequired["int"]
    """<p>The throughput in MiB/s provisioned for the volume (applicable to gp3, io1, and io2bx volumes).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EbsVolumeConfiguration) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "size_in_gib" in value:
        out["sizeInGib"] = value["size_in_gib"]
    if "iops" in value:
        out["iops"] = value["iops"]
    if "throughput" in value:
        out["throughput"] = value["throughput"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EbsVolumeConfiguration:
    out: EbsVolumeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("sizeInGib") is not None:
        out["size_in_gib"] = data["sizeInGib"]
    if data.get("iops") is not None:
        out["iops"] = data["iops"]
    if data.get("throughput") is not None:
        out["throughput"] = data["throughput"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EbsVolumeConfiguration) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "size_in_gib" in value:
        out["sizeInGib"] = value["size_in_gib"]
    if "iops" in value:
        out["iops"] = value["iops"]
    if "throughput" in value:
        out["throughput"] = value["throughput"]
    return out


def deserialize_cbor(data: dict) -> EbsVolumeConfiguration:
    out: EbsVolumeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("sizeInGib") is not None:
        out["size_in_gib"] = data["sizeInGib"]
    if data.get("iops") is not None:
        out["iops"] = data["iops"]
    if data.get("throughput") is not None:
        out["throughput"] = data["throughput"]
    return out
