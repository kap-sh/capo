"""Generated from Smithy shape ``com.amazonaws.datazone#S3FilesLocation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.s3_bucket_name
    import capo_datazone.types.s3_file_list


class S3FilesLocation(TypedDict, closed=True):
    bucket: "capo_datazone.types.s3_bucket_name.S3BucketName"
    """<p>The name of the Amazon Simple Storage Service bucket that contains the files to import.</p>"""
    file_list: "capo_datazone.types.s3_file_list.S3FileList"
    """<p>The files to import. Cells are created in the order in which you list the files. You can specify between 1 and 100 files.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3FilesLocation) -> dict:
    out: dict = {}
    out["bucket"] = value["bucket"]
    import capo_datazone.types.s3_file_list

    out["fileList"] = capo_datazone.types.s3_file_list.serialize_json(
        value["file_list"]
    )
    return out


def deserialize_json(data: dict) -> S3FilesLocation:
    out: S3FilesLocation = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    else:
        out["bucket"] = ""
    if data.get("fileList") is not None:
        import capo_datazone.types.s3_file_list

        out["file_list"] = capo_datazone.types.s3_file_list.deserialize_json(
            data["fileList"]
        )
    else:
        out["file_list"] = []
    return out


def redact_sensitive(value: S3FilesLocation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "bucket" in value:
        out["bucket"] = "*** Sensitive Data Redacted ***"
    if "file_list" in value:
        import capo_datazone.types.s3_file_list

        out["file_list"] = capo_datazone.types.s3_file_list.redact_sensitive(
            value["file_list"]
        )
    return out
