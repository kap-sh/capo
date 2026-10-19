"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#MagneticStoreWriteProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_write.types.boolean
    import capo_timestream_write.types.magnetic_store_rejected_data_location


class MagneticStoreWriteProperties(TypedDict, closed=True):
    enable_magnetic_store_writes: "capo_timestream_write.types.boolean.Boolean"
    """<p>A flag to enable magnetic store writes.</p>"""
    magnetic_store_rejected_data_location: NotRequired[
        "capo_timestream_write.types.magnetic_store_rejected_data_location.MagneticStoreRejectedDataLocation"
    ]
    """<p>The location to write error reports for records rejected asynchronously during magnetic store writes.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MagneticStoreWriteProperties) -> dict:
    out: dict = {}
    out["EnableMagneticStoreWrites"] = value["enable_magnetic_store_writes"]
    if "magnetic_store_rejected_data_location" in value:
        import capo_timestream_write.types.magnetic_store_rejected_data_location

        out["MagneticStoreRejectedDataLocation"] = (
            capo_timestream_write.types.magnetic_store_rejected_data_location.serialize_aws_json_1_0(
                value["magnetic_store_rejected_data_location"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> MagneticStoreWriteProperties:
    out: MagneticStoreWriteProperties = {}  # type: ignore[typeddict-item]
    if data.get("EnableMagneticStoreWrites") is not None:
        out["enable_magnetic_store_writes"] = data["EnableMagneticStoreWrites"]
    else:
        out["enable_magnetic_store_writes"] = False
    if data.get("MagneticStoreRejectedDataLocation") is not None:
        import capo_timestream_write.types.magnetic_store_rejected_data_location

        out["magnetic_store_rejected_data_location"] = (
            capo_timestream_write.types.magnetic_store_rejected_data_location.deserialize_aws_json_1_0(
                data["MagneticStoreRejectedDataLocation"]
            )
        )
    return out
