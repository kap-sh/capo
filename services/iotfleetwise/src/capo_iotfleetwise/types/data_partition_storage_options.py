"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#DataPartitionStorageOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.storage_location
    import capo_iotfleetwise.types.storage_maximum_size
    import capo_iotfleetwise.types.storage_minimum_time_to_live


class DataPartitionStorageOptions(TypedDict, closed=True):
    maximum_size: "capo_iotfleetwise.types.storage_maximum_size.StorageMaximumSize"
    """<p>The maximum storage size of the data stored in the data partition.</p> <note> <p>Newer data overwrites older data when the partition reaches the maximum size.</p> </note>"""
    storage_location: "capo_iotfleetwise.types.storage_location.StorageLocation"
    """<p>The folder name for the data partition under the campaign storage folder.</p>"""
    minimum_time_to_live: (
        "capo_iotfleetwise.types.storage_minimum_time_to_live.StorageMinimumTimeToLive"
    )
    """<p>The amount of time that data in this partition will be kept on disk.</p> <ul> <li> <p>After the designated amount of time passes, the data can be removed, but it's not guaranteed to be removed.</p> </li> <li> <p>Before the time expires, data in this partition can still be deleted if the partition reaches its configured maximum size.</p> </li> <li> <p>Newer data will overwrite older data when the partition reaches the maximum size.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DataPartitionStorageOptions) -> dict:
    out: dict = {}
    import capo_iotfleetwise.types.storage_maximum_size

    out["maximumSize"] = (
        capo_iotfleetwise.types.storage_maximum_size.serialize_aws_json_1_0(
            value["maximum_size"]
        )
    )
    out["storageLocation"] = value["storage_location"]
    import capo_iotfleetwise.types.storage_minimum_time_to_live

    out["minimumTimeToLive"] = (
        capo_iotfleetwise.types.storage_minimum_time_to_live.serialize_aws_json_1_0(
            value["minimum_time_to_live"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DataPartitionStorageOptions:
    out: DataPartitionStorageOptions = {}  # type: ignore[typeddict-item]
    if data.get("maximumSize") is not None:
        import capo_iotfleetwise.types.storage_maximum_size

        out["maximum_size"] = (
            capo_iotfleetwise.types.storage_maximum_size.deserialize_aws_json_1_0(
                data["maximumSize"]
            )
        )
    else:
        raise DeserializationError("DataPartitionStorageOptions.maximum_size required")
    if data.get("storageLocation") is not None:
        out["storage_location"] = data["storageLocation"]
    else:
        out["storage_location"] = ""
    if data.get("minimumTimeToLive") is not None:
        import capo_iotfleetwise.types.storage_minimum_time_to_live

        out["minimum_time_to_live"] = (
            capo_iotfleetwise.types.storage_minimum_time_to_live.deserialize_aws_json_1_0(
                data["minimumTimeToLive"]
            )
        )
    else:
        raise DeserializationError(
            "DataPartitionStorageOptions.minimum_time_to_live required"
        )
    return out


def redact_sensitive(value: DataPartitionStorageOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "storage_location" in value:
        out["storage_location"] = "*** Sensitive Data Redacted ***"
    return out
