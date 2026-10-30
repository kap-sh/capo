"""Generated from Smithy shape ``com.amazonaws.continuum#S3Target``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.delivery_object_key
    import capo_continuum.types.delivery_version_id
    import capo_continuum.types.environment_source_bucket_name


class S3Target(TypedDict, closed=True):
    bucket: "capo_continuum.types.environment_source_bucket_name.EnvironmentSourceBucketName"
    key: "capo_continuum.types.delivery_object_key.DeliveryObjectKey"
    """The object key of the delivered patch."""
    version: NotRequired["capo_continuum.types.delivery_version_id.DeliveryVersionId"]
    """The S3 version ID of the delivered object, when the bucket is versioned."""


# --- restJson1 ser/de ---
def serialize_json(value: S3Target) -> dict:
    out: dict = {}
    out["bucket"] = value["bucket"]
    out["key"] = value["key"]
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> S3Target:
    out: S3Target = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    else:
        out["bucket"] = ""
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("version") is not None:
        out["version"] = data["version"]
    return out
