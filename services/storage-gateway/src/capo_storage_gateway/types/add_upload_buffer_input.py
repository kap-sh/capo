"""Generated from Smithy shape ``com.amazonaws.storagegateway#AddUploadBufferInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.disk_ids
    import capo_storage_gateway.types.gateway_arn


class AddUploadBufferInput(TypedDict, closed=True):
    gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN"
    disk_ids: "capo_storage_gateway.types.disk_ids.DiskIds"
    """<p>An array of strings that identify disks that are to be configured as working storage. Each string has a minimum length of 1 and maximum length of 300. You can get the disk IDs from the <a>ListLocalDisks</a> API.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddUploadBufferInput) -> dict:
    out: dict = {}
    out["GatewayARN"] = value["gateway_arn"]
    import capo_storage_gateway.types.disk_ids

    out["DiskIds"] = capo_storage_gateway.types.disk_ids.serialize_aws_json_1_1(
        value["disk_ids"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddUploadBufferInput:
    out: AddUploadBufferInput = {}  # type: ignore[typeddict-item]
    if data.get("GatewayARN") is not None:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        out["gateway_arn"] = ""
    if data.get("DiskIds") is not None:
        import capo_storage_gateway.types.disk_ids

        out["disk_ids"] = capo_storage_gateway.types.disk_ids.deserialize_aws_json_1_1(
            data["DiskIds"]
        )
    else:
        out["disk_ids"] = []
    return out
