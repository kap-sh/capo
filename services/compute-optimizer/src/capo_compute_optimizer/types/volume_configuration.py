"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#VolumeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.root_volume
    import capo_compute_optimizer.types.volume_baseline_iops
    import capo_compute_optimizer.types.volume_baseline_throughput
    import capo_compute_optimizer.types.volume_burst_iops
    import capo_compute_optimizer.types.volume_burst_throughput
    import capo_compute_optimizer.types.volume_size
    import capo_compute_optimizer.types.volume_type


class VolumeConfiguration(TypedDict, closed=True):
    volume_type: NotRequired["capo_compute_optimizer.types.volume_type.VolumeType"]
    """<p>The volume type.</p> <p>The volume types can be the following:</p> <ul> <li> <p>General Purpose SSD <code>gp2</code> and <code>gp3</code> </p> </li> <li> <p>Provisioned IOPS SSD <code>io1</code>, <code>io2</code>, and <code>io2 Block Express</code> </p> </li> <li> <p>Throughput Optimized HDD <code>st1</code> </p> </li> <li> <p>Cold HDD <code>sc1</code> </p> </li> <li> <p>Magnetic volumes <code>standard</code> </p> </li> </ul>"""
    volume_size: "capo_compute_optimizer.types.volume_size.VolumeSize"
    """<p>The size of the volume, in GiB.</p>"""
    volume_baseline_iops: (
        "capo_compute_optimizer.types.volume_baseline_iops.VolumeBaselineIOPS"
    )
    """<p>The baseline IOPS of the volume.</p>"""
    volume_burst_iops: "capo_compute_optimizer.types.volume_burst_iops.VolumeBurstIOPS"
    """<p>The burst IOPS of the volume.</p>"""
    volume_baseline_throughput: "capo_compute_optimizer.types.volume_baseline_throughput.VolumeBaselineThroughput"
    """<p>The baseline throughput of the volume.</p>"""
    volume_burst_throughput: (
        "capo_compute_optimizer.types.volume_burst_throughput.VolumeBurstThroughput"
    )
    """<p>The burst throughput of the volume.</p>"""
    root_volume: NotRequired["capo_compute_optimizer.types.root_volume.RootVolume"]
    """<p> Contains the image used to boot the instance during launch. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VolumeConfiguration) -> dict:
    out: dict = {}
    if "volume_type" in value:
        out["volumeType"] = value["volume_type"]
    out["volumeSize"] = value.get("volume_size", 0)
    out["volumeBaselineIOPS"] = value.get("volume_baseline_iops", 0)
    out["volumeBurstIOPS"] = value.get("volume_burst_iops", 0)
    out["volumeBaselineThroughput"] = value.get("volume_baseline_throughput", 0)
    out["volumeBurstThroughput"] = value.get("volume_burst_throughput", 0)
    if "root_volume" in value:
        out["rootVolume"] = value["root_volume"]
    return out


def deserialize_aws_json_1_0(data: dict) -> VolumeConfiguration:
    out: VolumeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("volumeType") is not None:
        out["volume_type"] = data["volumeType"]
    if data.get("volumeSize") is not None:
        out["volume_size"] = data["volumeSize"]
    else:
        out["volume_size"] = 0
    if data.get("volumeBaselineIOPS") is not None:
        out["volume_baseline_iops"] = data["volumeBaselineIOPS"]
    else:
        out["volume_baseline_iops"] = 0
    if data.get("volumeBurstIOPS") is not None:
        out["volume_burst_iops"] = data["volumeBurstIOPS"]
    else:
        out["volume_burst_iops"] = 0
    if data.get("volumeBaselineThroughput") is not None:
        out["volume_baseline_throughput"] = data["volumeBaselineThroughput"]
    else:
        out["volume_baseline_throughput"] = 0
    if data.get("volumeBurstThroughput") is not None:
        out["volume_burst_throughput"] = data["volumeBurstThroughput"]
    else:
        out["volume_burst_throughput"] = 0
    if data.get("rootVolume") is not None:
        out["root_volume"] = data["rootVolume"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: VolumeConfiguration) -> dict:
    out: dict = {}
    if "volume_type" in value:
        out["volumeType"] = value["volume_type"]
    out["volumeSize"] = value.get("volume_size", 0)
    out["volumeBaselineIOPS"] = value.get("volume_baseline_iops", 0)
    out["volumeBurstIOPS"] = value.get("volume_burst_iops", 0)
    out["volumeBaselineThroughput"] = value.get("volume_baseline_throughput", 0)
    out["volumeBurstThroughput"] = value.get("volume_burst_throughput", 0)
    if "root_volume" in value:
        out["rootVolume"] = value["root_volume"]
    return out


def deserialize_cbor(data: dict) -> VolumeConfiguration:
    out: VolumeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("volumeType") is not None:
        out["volume_type"] = data["volumeType"]
    if data.get("volumeSize") is not None:
        out["volume_size"] = data["volumeSize"]
    else:
        out["volume_size"] = 0
    if data.get("volumeBaselineIOPS") is not None:
        out["volume_baseline_iops"] = data["volumeBaselineIOPS"]
    else:
        out["volume_baseline_iops"] = 0
    if data.get("volumeBurstIOPS") is not None:
        out["volume_burst_iops"] = data["volumeBurstIOPS"]
    else:
        out["volume_burst_iops"] = 0
    if data.get("volumeBaselineThroughput") is not None:
        out["volume_baseline_throughput"] = data["volumeBaselineThroughput"]
    else:
        out["volume_baseline_throughput"] = 0
    if data.get("volumeBurstThroughput") is not None:
        out["volume_burst_throughput"] = data["volumeBurstThroughput"]
    else:
        out["volume_burst_throughput"] = 0
    if data.get("rootVolume") is not None:
        out["root_volume"] = data["rootVolume"]
    return out
