"""Generated from Smithy shape ``com.amazonaws.finspace#CreateKxVolumeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.availability_zone_ids
    import capo_finspace.types.client_token
    import capo_finspace.types.description
    import capo_finspace.types.kx_az_mode
    import capo_finspace.types.kx_environment_id
    import capo_finspace.types.kx_nas1_configuration
    import capo_finspace.types.kx_volume_name
    import capo_finspace.types.kx_volume_type
    import capo_finspace.types.tag_map


class CreateKxVolumeRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_finspace.types.client_token.ClientToken"]
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""
    environment_id: "capo_finspace.types.kx_environment_id.KxEnvironmentId"
    """<p>A unique identifier for the kdb environment, whose clusters can attach to the volume. </p>"""
    volume_type: "capo_finspace.types.kx_volume_type.KxVolumeType"
    """<p> The type of file system volume. Currently, FinSpace only supports <code>NAS_1</code> volume type. When you select <code>NAS_1</code> volume type, you must also provide <code>nas1Configuration</code>. </p>"""
    volume_name: "capo_finspace.types.kx_volume_name.KxVolumeName"
    """<p>A unique identifier for the volume.</p>"""
    description: NotRequired["capo_finspace.types.description.Description"]
    """<p> A description of the volume. </p>"""
    nas1_configuration: NotRequired[
        "capo_finspace.types.kx_nas1_configuration.KxNAS1Configuration"
    ]
    """<p> Specifies the configuration for the Network attached storage (NAS_1) file system volume. This parameter is required when you choose <code>volumeType</code> as <i>NAS_1</i>.</p>"""
    az_mode: "capo_finspace.types.kx_az_mode.KxAzMode"
    """<p>The number of availability zones you want to assign per volume. Currently, FinSpace only supports <code>SINGLE</code> for volumes. This places dataview in a single AZ.</p>"""
    availability_zone_ids: (
        "capo_finspace.types.availability_zone_ids.AvailabilityZoneIds"
    )
    """<p>The identifier of the availability zones.</p>"""
    tags: NotRequired["capo_finspace.types.tag_map.TagMap"]
    """<p> A list of key-value pairs to label the volume. You can add up to 50 tags to a volume. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateKxVolumeRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import capo_finspace.types.kx_volume_type

    out["volumeType"] = capo_finspace.types.kx_volume_type.serialize_json(
        value["volume_type"]
    )
    out["volumeName"] = value["volume_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "nas1_configuration" in value:
        import capo_finspace.types.kx_nas1_configuration

        out["nas1Configuration"] = (
            capo_finspace.types.kx_nas1_configuration.serialize_json(
                value["nas1_configuration"]
            )
        )
    import capo_finspace.types.kx_az_mode

    out["azMode"] = capo_finspace.types.kx_az_mode.serialize_json(value["az_mode"])
    import capo_finspace.types.availability_zone_ids

    out["availabilityZoneIds"] = (
        capo_finspace.types.availability_zone_ids.serialize_json(
            value["availability_zone_ids"]
        )
    )
    if "tags" in value:
        import capo_finspace.types.tag_map

        out["tags"] = capo_finspace.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateKxVolumeRequest:
    out: CreateKxVolumeRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("volumeType") is not None:
        import capo_finspace.types.kx_volume_type

        out["volume_type"] = capo_finspace.types.kx_volume_type.deserialize_json(
            data["volumeType"]
        )
    else:
        import typing

        out["volume_type"] = typing.cast(
            "capo_finspace.types.kx_volume_type.KxVolumeType", ""
        )
    if data.get("volumeName") is not None:
        out["volume_name"] = data["volumeName"]
    else:
        out["volume_name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("nas1Configuration") is not None:
        import capo_finspace.types.kx_nas1_configuration

        out["nas1_configuration"] = (
            capo_finspace.types.kx_nas1_configuration.deserialize_json(
                data["nas1Configuration"]
            )
        )
    if data.get("azMode") is not None:
        import capo_finspace.types.kx_az_mode

        out["az_mode"] = capo_finspace.types.kx_az_mode.deserialize_json(data["azMode"])
    else:
        import typing

        out["az_mode"] = typing.cast("capo_finspace.types.kx_az_mode.KxAzMode", "")
    if data.get("availabilityZoneIds") is not None:
        import capo_finspace.types.availability_zone_ids

        out["availability_zone_ids"] = (
            capo_finspace.types.availability_zone_ids.deserialize_json(
                data["availabilityZoneIds"]
            )
        )
    else:
        out["availability_zone_ids"] = []
    if data.get("tags") is not None:
        import capo_finspace.types.tag_map

        out["tags"] = capo_finspace.types.tag_map.deserialize_json(data["tags"])
    return out
