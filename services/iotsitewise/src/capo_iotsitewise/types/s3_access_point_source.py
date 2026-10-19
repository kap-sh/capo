"""Generated from Smithy shape ``com.amazonaws.iotsitewise#S3AccessPointSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.mount_s3_access_point_arn
    import capo_iotsitewise.types.mount_s3_key_prefix


class S3AccessPointSource(TypedDict, closed=True):
    access_point_arn: (
        "capo_iotsitewise.types.mount_s3_access_point_arn.MountS3AccessPointArn"
    )
    """<p>The Amazon Resource Name (ARN) of the S3 access point.</p>"""
    prefix: NotRequired["capo_iotsitewise.types.mount_s3_key_prefix.MountS3KeyPrefix"]
    """<p>An optional key prefix to scope the mount to a subset of objects at the access point.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3AccessPointSource) -> dict:
    out: dict = {}
    out["accessPointArn"] = value["access_point_arn"]
    if "prefix" in value:
        out["prefix"] = value["prefix"]
    return out


def deserialize_json(data: dict) -> S3AccessPointSource:
    out: S3AccessPointSource = {}  # type: ignore[typeddict-item]
    if data.get("accessPointArn") is not None:
        out["access_point_arn"] = data["accessPointArn"]
    else:
        out["access_point_arn"] = ""
    if data.get("prefix") is not None:
        out["prefix"] = data["prefix"]
    return out
