"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeCachediSCSIVolumesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.volume_ar_ns


class DescribeCachediSCSIVolumesInput(TypedDict, closed=True):
    volume_ar_ns: "capo_storage_gateway.types.volume_ar_ns.VolumeARNs"
    """<p>An array of strings where each string represents the Amazon Resource Name (ARN) of a cached volume. All of the specified cached volumes must be from the same gateway. Use <a>ListVolumes</a> to get volume ARNs for a gateway.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCachediSCSIVolumesInput) -> dict:
    out: dict = {}
    import capo_storage_gateway.types.volume_ar_ns

    out["VolumeARNs"] = capo_storage_gateway.types.volume_ar_ns.serialize_aws_json_1_1(
        value["volume_ar_ns"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCachediSCSIVolumesInput:
    out: DescribeCachediSCSIVolumesInput = {}  # type: ignore[typeddict-item]
    if data.get("VolumeARNs") is not None:
        import capo_storage_gateway.types.volume_ar_ns

        out["volume_ar_ns"] = (
            capo_storage_gateway.types.volume_ar_ns.deserialize_aws_json_1_1(
                data["VolumeARNs"]
            )
        )
    else:
        out["volume_ar_ns"] = []
    return out
