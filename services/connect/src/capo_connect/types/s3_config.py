"""Generated from Smithy shape ``com.amazonaws.connect#S3Config``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.bucket_name
    import capo_connect.types.encryption_config
    import capo_connect.types.prefix


class S3Config(TypedDict, closed=True):
    bucket_name: "capo_connect.types.bucket_name.BucketName"
    """<p>The S3 bucket name.</p>"""
    bucket_prefix: "capo_connect.types.prefix.Prefix"
    """<p>The S3 bucket prefix.</p>"""
    encryption_config: NotRequired[
        "capo_connect.types.encryption_config.EncryptionConfig"
    ]
    """<p>The Amazon S3 encryption configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Config) -> dict:
    out: dict = {}
    out["BucketName"] = value["bucket_name"]
    out["BucketPrefix"] = value["bucket_prefix"]
    if "encryption_config" in value:
        import capo_connect.types.encryption_config

        out["EncryptionConfig"] = capo_connect.types.encryption_config.serialize_json(
            value["encryption_config"]
        )
    return out


def deserialize_json(data: dict) -> S3Config:
    out: S3Config = {}  # type: ignore[typeddict-item]
    if data.get("BucketName") is not None:
        out["bucket_name"] = data["BucketName"]
    else:
        out["bucket_name"] = ""
    if data.get("BucketPrefix") is not None:
        out["bucket_prefix"] = data["BucketPrefix"]
    else:
        out["bucket_prefix"] = ""
    if data.get("EncryptionConfig") is not None:
        import capo_connect.types.encryption_config

        out["encryption_config"] = (
            capo_connect.types.encryption_config.deserialize_json(
                data["EncryptionConfig"]
            )
        )
    return out
