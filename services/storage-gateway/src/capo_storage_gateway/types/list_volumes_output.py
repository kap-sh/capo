"""Generated from Smithy shape ``com.amazonaws.storagegateway#ListVolumesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.gateway_arn
    import capo_storage_gateway.types.marker
    import capo_storage_gateway.types.volume_infos


class ListVolumesOutput(TypedDict, closed=True):
    gateway_arn: NotRequired["capo_storage_gateway.types.gateway_arn.GatewayARN"]
    marker: NotRequired["capo_storage_gateway.types.marker.Marker"]
    """<p>Use the marker in your next request to continue pagination of iSCSI volumes. If there are no more volumes to list, this field does not appear in the response body.</p>"""
    volume_infos: NotRequired["capo_storage_gateway.types.volume_infos.VolumeInfos"]
    """<p>An array of <a>VolumeInfo</a> objects, where each object describes an iSCSI volume. If no volumes are defined for the gateway, then <code>VolumeInfos</code> is an empty array "[]".</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListVolumesOutput) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["GatewayARN"] = value["gateway_arn"]
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "volume_infos" in value:
        import capo_storage_gateway.types.volume_infos

        out["VolumeInfos"] = (
            capo_storage_gateway.types.volume_infos.serialize_aws_json_1_1(
                value["volume_infos"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListVolumesOutput:
    out: ListVolumesOutput = {}  # type: ignore[typeddict-item]
    if data.get("GatewayARN") is not None:
        out["gateway_arn"] = data["GatewayARN"]
    if data.get("Marker") is not None:
        out["marker"] = data["Marker"]
    if data.get("VolumeInfos") is not None:
        import capo_storage_gateway.types.volume_infos

        out["volume_infos"] = (
            capo_storage_gateway.types.volume_infos.deserialize_aws_json_1_1(
                data["VolumeInfos"]
            )
        )
    return out
