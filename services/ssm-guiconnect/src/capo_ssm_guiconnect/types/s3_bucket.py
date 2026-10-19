"""Generated from Smithy shape ``com.amazonaws.ssmguiconnect#S3Bucket``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_guiconnect.types.account_id
    import capo_ssm_guiconnect.types.bucket_name


class S3Bucket(TypedDict, closed=True):
    bucket_owner: "capo_ssm_guiconnect.types.account_id.AccountId"
    """<p>The Amazon Web Services account number that owns the S3 bucket.</p>"""
    bucket_name: "capo_ssm_guiconnect.types.bucket_name.BucketName"
    """<p>The name of the S3 bucket where RDP connection recordings are stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Bucket) -> dict:
    out: dict = {}
    out["BucketOwner"] = value["bucket_owner"]
    out["BucketName"] = value["bucket_name"]
    return out


def deserialize_json(data: dict) -> S3Bucket:
    out: S3Bucket = {}  # type: ignore[typeddict-item]
    if data.get("BucketOwner") is not None:
        out["bucket_owner"] = data["BucketOwner"]
    else:
        out["bucket_owner"] = ""
    if data.get("BucketName") is not None:
        out["bucket_name"] = data["BucketName"]
    else:
        out["bucket_name"] = ""
    return out
