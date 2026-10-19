"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#AmazonMachineImageEbsVolume``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.amazon_machine_image_ebs_volume_type_list


class AmazonMachineImageEbsVolume(TypedDict, closed=True):
    volume_types: "capo_marketplace_discovery.types.amazon_machine_image_ebs_volume_type_list.AmazonMachineImageEbsVolumeTypeList"
    """<p>The supported Amazon EBS volume types.</p>"""
    iops: NotRequired["int"]
    """<p>The total number of provisioned IOPS supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmazonMachineImageEbsVolume) -> dict:
    out: dict = {}
    import capo_marketplace_discovery.types.amazon_machine_image_ebs_volume_type_list

    out["volumeTypes"] = (
        capo_marketplace_discovery.types.amazon_machine_image_ebs_volume_type_list.serialize_json(
            value["volume_types"]
        )
    )
    if "iops" in value:
        out["iops"] = value["iops"]
    return out


def deserialize_json(data: dict) -> AmazonMachineImageEbsVolume:
    out: AmazonMachineImageEbsVolume = {}  # type: ignore[typeddict-item]
    if data.get("volumeTypes") is not None:
        import capo_marketplace_discovery.types.amazon_machine_image_ebs_volume_type_list

        out["volume_types"] = (
            capo_marketplace_discovery.types.amazon_machine_image_ebs_volume_type_list.deserialize_json(
                data["volumeTypes"]
            )
        )
    else:
        out["volume_types"] = []
    if data.get("iops") is not None:
        out["iops"] = data["iops"]
    return out
