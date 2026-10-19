"""Generated from Smithy shape ``com.amazonaws.iotsitewise#File``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_property_alias
    import capo_iotsitewise.types.bucket
    import capo_iotsitewise.types.file_format
    import capo_iotsitewise.types.string
    import capo_iotsitewise.types.time_in_nanos


class File(TypedDict, closed=True):
    bucket: "capo_iotsitewise.types.bucket.Bucket"
    """<p>The name of the Amazon S3 bucket from which data is imported.</p>"""
    key: "capo_iotsitewise.types.string.String"
    """<p>The key of the Amazon S3 object that contains your data. Each object has a key that is a unique identifier. Each object has exactly one key.</p>"""
    version_id: NotRequired["capo_iotsitewise.types.string.String"]
    """<p>The version ID to identify a specific version of the Amazon S3 object that contains your data.</p>"""
    alias: NotRequired["capo_iotsitewise.types.asset_property_alias.AssetPropertyAlias"]
    """<p>The alias associated with the file's time series.</p>"""
    start_time: NotRequired["capo_iotsitewise.types.time_in_nanos.TimeInNanos"]
    """<p>The nanosecond-precision start time for the file data.</p>"""
    file_format: NotRequired["capo_iotsitewise.types.file_format.FileFormat"]
    """<p>The file format of the data in S3.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: File) -> dict:
    out: dict = {}
    out["bucket"] = value["bucket"]
    out["key"] = value["key"]
    if "version_id" in value:
        out["versionId"] = value["version_id"]
    if "alias" in value:
        out["alias"] = value["alias"]
    if "start_time" in value:
        import capo_iotsitewise.types.time_in_nanos

        out["startTime"] = capo_iotsitewise.types.time_in_nanos.serialize_json(
            value["start_time"]
        )
    if "file_format" in value:
        import capo_iotsitewise.types.file_format

        out["fileFormat"] = capo_iotsitewise.types.file_format.serialize_json(
            value["file_format"]
        )
    return out


def deserialize_json(data: dict) -> File:
    out: File = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    else:
        out["bucket"] = ""
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("versionId") is not None:
        out["version_id"] = data["versionId"]
    if data.get("alias") is not None:
        out["alias"] = data["alias"]
    if data.get("startTime") is not None:
        import capo_iotsitewise.types.time_in_nanos

        out["start_time"] = capo_iotsitewise.types.time_in_nanos.deserialize_json(
            data["startTime"]
        )
    if data.get("fileFormat") is not None:
        import capo_iotsitewise.types.file_format

        out["file_format"] = capo_iotsitewise.types.file_format.deserialize_json(
            data["fileFormat"]
        )
    return out
