"""Generated from Smithy shape ``com.amazonaws.iot#S3Action``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.aws_arn
    import capo_iot.types.bucket_name
    import capo_iot.types.canned_access_control_list
    import capo_iot.types.key


class S3Action(TypedDict, closed=True):
    role_arn: "capo_iot.types.aws_arn.AwsArn"
    """<p>The ARN of the IAM role that grants access.</p>"""
    bucket_name: "capo_iot.types.bucket_name.BucketName"
    """<p>The Amazon S3 bucket.</p>"""
    key: "capo_iot.types.key.Key"
    """<p>The object key. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/list_amazons3.html">Actions, resources, and condition keys for Amazon S3</a>.</p>"""
    canned_acl: NotRequired[
        "capo_iot.types.canned_access_control_list.CannedAccessControlList"
    ]
    """<p>The Amazon S3 canned ACL that controls access to the object identified by the object key. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl">S3 canned ACLs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Action) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    out["bucketName"] = value["bucket_name"]
    out["key"] = value["key"]
    if "canned_acl" in value:
        import capo_iot.types.canned_access_control_list

        out["cannedAcl"] = capo_iot.types.canned_access_control_list.serialize_json(
            value["canned_acl"]
        )
    return out


def deserialize_json(data: dict) -> S3Action:
    out: S3Action = {}  # type: ignore[typeddict-item]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("S3Action.role_arn required")
    if data.get("bucketName") is not None:
        out["bucket_name"] = data["bucketName"]
    else:
        raise DeserializationError("S3Action.bucket_name required")
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        raise DeserializationError("S3Action.key required")
    if data.get("cannedAcl") is not None:
        import capo_iot.types.canned_access_control_list

        out["canned_acl"] = capo_iot.types.canned_access_control_list.deserialize_json(
            data["cannedAcl"]
        )
    return out
