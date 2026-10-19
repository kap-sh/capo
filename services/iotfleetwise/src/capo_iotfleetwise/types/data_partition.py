"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#DataPartition``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.data_partition_id
    import capo_iotfleetwise.types.data_partition_storage_options
    import capo_iotfleetwise.types.data_partition_upload_options


class DataPartition(TypedDict, closed=True):
    id: "capo_iotfleetwise.types.data_partition_id.DataPartitionId"
    """<p>The ID of the data partition. The data partition ID must be unique within a campaign. You can establish a data partition as the default partition for a campaign by using <code>default</code> as the ID.</p>"""
    storage_options: "capo_iotfleetwise.types.data_partition_storage_options.DataPartitionStorageOptions"
    """<p>The storage options for a data partition.</p>"""
    upload_options: NotRequired[
        "capo_iotfleetwise.types.data_partition_upload_options.DataPartitionUploadOptions"
    ]
    """<p>The upload options for the data partition.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DataPartition) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import capo_iotfleetwise.types.data_partition_storage_options

    out["storageOptions"] = (
        capo_iotfleetwise.types.data_partition_storage_options.serialize_aws_json_1_0(
            value["storage_options"]
        )
    )
    if "upload_options" in value:
        import capo_iotfleetwise.types.data_partition_upload_options

        out["uploadOptions"] = (
            capo_iotfleetwise.types.data_partition_upload_options.serialize_aws_json_1_0(
                value["upload_options"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DataPartition:
    out: DataPartition = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("storageOptions") is not None:
        import capo_iotfleetwise.types.data_partition_storage_options

        out["storage_options"] = (
            capo_iotfleetwise.types.data_partition_storage_options.deserialize_aws_json_1_0(
                data["storageOptions"]
            )
        )
    else:
        raise DeserializationError("DataPartition.storage_options required")
    if data.get("uploadOptions") is not None:
        import capo_iotfleetwise.types.data_partition_upload_options

        out["upload_options"] = (
            capo_iotfleetwise.types.data_partition_upload_options.deserialize_aws_json_1_0(
                data["uploadOptions"]
            )
        )
    return out


def redact_sensitive(value: DataPartition) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "storage_options" in value:
        import capo_iotfleetwise.types.data_partition_storage_options

        out["storage_options"] = (
            capo_iotfleetwise.types.data_partition_storage_options.redact_sensitive(
                value["storage_options"]
            )
        )
    if "upload_options" in value:
        import capo_iotfleetwise.types.data_partition_upload_options

        out["upload_options"] = (
            capo_iotfleetwise.types.data_partition_upload_options.redact_sensitive(
                value["upload_options"]
            )
        )
    return out
