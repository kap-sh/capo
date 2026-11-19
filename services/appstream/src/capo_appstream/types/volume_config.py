"""Generated from Smithy shape ``com.amazonaws.appstream#VolumeConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.integer


class VolumeConfig(TypedDict, closed=True):
    volume_size_in_gb: NotRequired["capo_appstream.types.integer.Integer"]
    """<p>The size of the root volume in GB. Valid range is 200-500 GB. The default is 200 GB, which is included in the hourly instance rate. Additional storage beyond 200 GB incurs extra charges and applies to instances regardless of their running state.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VolumeConfig) -> dict:
    out: dict = {}
    if "volume_size_in_gb" in value:
        out["VolumeSizeInGb"] = value["volume_size_in_gb"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VolumeConfig:
    out: VolumeConfig = {}  # type: ignore[typeddict-item]
    if data.get("VolumeSizeInGb") is not None:
        out["volume_size_in_gb"] = data["VolumeSizeInGb"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: VolumeConfig) -> dict:
    out: dict = {}
    if "volume_size_in_gb" in value:
        out["VolumeSizeInGb"] = value["volume_size_in_gb"]
    return out


def deserialize_cbor(data: dict) -> VolumeConfig:
    out: VolumeConfig = {}  # type: ignore[typeddict-item]
    if data.get("VolumeSizeInGb") is not None:
        out["volume_size_in_gb"] = data["VolumeSizeInGb"]
    return out
