"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestSetImportInputLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.s3_bucket_name
    import capo_lex_models_v2.types.s3_object_path


class TestSetImportInputLocation(TypedDict, closed=True):
    s3_bucket_name: "capo_lex_models_v2.types.s3_bucket_name.S3BucketName"
    """<p>The name of the Amazon S3 bucket.</p>"""
    s3_path: "capo_lex_models_v2.types.s3_object_path.S3ObjectPath"
    """<p>The path inside the Amazon S3 bucket pointing to the test-set CSV file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestSetImportInputLocation) -> dict:
    out: dict = {}
    out["s3BucketName"] = value["s3_bucket_name"]
    out["s3Path"] = value["s3_path"]
    return out


def deserialize_json(data: dict) -> TestSetImportInputLocation:
    out: TestSetImportInputLocation = {}  # type: ignore[typeddict-item]
    if data.get("s3BucketName") is not None:
        out["s3_bucket_name"] = data["s3BucketName"]
    else:
        out["s3_bucket_name"] = ""
    if data.get("s3Path") is not None:
        out["s3_path"] = data["s3Path"]
    else:
        out["s3_path"] = ""
    return out
