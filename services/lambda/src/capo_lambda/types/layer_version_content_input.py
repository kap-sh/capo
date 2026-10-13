"""Generated from Smithy shape ``com.amazonaws.lambda#LayerVersionContentInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.blob
    import capo_lambda.types.s3_bucket
    import capo_lambda.types.s3_key
    import capo_lambda.types.s3_object_storage_mode
    import capo_lambda.types.s3_object_version


class LayerVersionContentInput(TypedDict, closed=True):
    s3_bucket: NotRequired["capo_lambda.types.s3_bucket.S3Bucket"]
    """<p>The Amazon S3 bucket of the layer archive.</p>"""
    s3_key: NotRequired["capo_lambda.types.s3_key.S3Key"]
    """<p>The Amazon S3 key of the layer archive.</p>"""
    s3_object_version: NotRequired[
        "capo_lambda.types.s3_object_version.S3ObjectVersion"
    ]
    """<p>For versioned objects, the version of the layer archive object to use.</p>"""
    s3_object_storage_mode: NotRequired[
        "capo_lambda.types.s3_object_storage_mode.S3ObjectStorageMode"
    ]
    """<p>Specifies how the layer archive is stored. Valid values:</p> <ul> <li> <p> <code>COPY</code> (default) – Uploads a copy of your layer archive to Lambda.</p> </li> <li> <p> <code>REFERENCE</code> – Lambda references the layer archive from the specified Amazon S3 bucket.</p> </li> </ul>"""
    zip_file: NotRequired["capo_lambda.types.blob.Blob"]
    """<p>The base64-encoded contents of the layer archive. Amazon Web Services SDK and Amazon Web Services CLI clients handle the encoding for you.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LayerVersionContentInput) -> dict:
    out: dict = {}
    if "s3_bucket" in value:
        out["S3Bucket"] = value["s3_bucket"]
    if "s3_key" in value:
        out["S3Key"] = value["s3_key"]
    if "s3_object_version" in value:
        out["S3ObjectVersion"] = value["s3_object_version"]
    if "s3_object_storage_mode" in value:
        import capo_lambda.types.s3_object_storage_mode

        out["S3ObjectStorageMode"] = (
            capo_lambda.types.s3_object_storage_mode.serialize_json(
                value["s3_object_storage_mode"]
            )
        )
    if "zip_file" in value:
        import capo_lambda.types.blob

        out["ZipFile"] = capo_lambda.types.blob.serialize_json(value["zip_file"])
    return out


def deserialize_json(data: dict) -> LayerVersionContentInput:
    out: LayerVersionContentInput = {}  # type: ignore[typeddict-item]
    if data.get("S3Bucket") is not None:
        out["s3_bucket"] = data["S3Bucket"]
    if data.get("S3Key") is not None:
        out["s3_key"] = data["S3Key"]
    if data.get("S3ObjectVersion") is not None:
        out["s3_object_version"] = data["S3ObjectVersion"]
    if data.get("S3ObjectStorageMode") is not None:
        import capo_lambda.types.s3_object_storage_mode

        out["s3_object_storage_mode"] = (
            capo_lambda.types.s3_object_storage_mode.deserialize_json(
                data["S3ObjectStorageMode"]
            )
        )
    if data.get("ZipFile") is not None:
        import capo_lambda.types.blob

        out["zip_file"] = capo_lambda.types.blob.deserialize_json(data["ZipFile"])
    return out


def redact_sensitive(value: LayerVersionContentInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "zip_file" in value:
        out["zip_file"] = "*** Sensitive Data Redacted ***"
    return out
