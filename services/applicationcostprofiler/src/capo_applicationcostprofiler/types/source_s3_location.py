"""Generated from Smithy shape ``com.amazonaws.applicationcostprofiler#SourceS3Location``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_applicationcostprofiler.types.s3_bucket
    import capo_applicationcostprofiler.types.s3_bucket_region
    import capo_applicationcostprofiler.types.s3_key


class SourceS3Location(TypedDict, closed=True):
    bucket: "capo_applicationcostprofiler.types.s3_bucket.S3Bucket"
    """<p>Name of the bucket.</p>"""
    key: "capo_applicationcostprofiler.types.s3_key.S3Key"
    """<p>Key of the object.</p>"""
    region: NotRequired[
        "capo_applicationcostprofiler.types.s3_bucket_region.S3BucketRegion"
    ]
    """<p>Region of the bucket. Only required for Regions that are disabled by default. For more infomration about Regions that are disabled by default, see <a href="https://docs.aws.amazon.com/general/latest/gr/rande-manage.html#rande-manage-enable"> Enabling a Region</a> in the <i>AWS General Reference guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceS3Location) -> dict:
    out: dict = {}
    out["bucket"] = value["bucket"]
    out["key"] = value["key"]
    if "region" in value:
        import capo_applicationcostprofiler.types.s3_bucket_region

        out["region"] = (
            capo_applicationcostprofiler.types.s3_bucket_region.serialize_json(
                value["region"]
            )
        )
    return out


def deserialize_json(data: dict) -> SourceS3Location:
    out: SourceS3Location = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    else:
        out["bucket"] = ""
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("region") is not None:
        import capo_applicationcostprofiler.types.s3_bucket_region

        out["region"] = (
            capo_applicationcostprofiler.types.s3_bucket_region.deserialize_json(
                data["region"]
            )
        )
    return out
