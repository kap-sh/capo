"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CustomerManagedS3Storage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.arn


class CustomerManagedS3Storage(TypedDict, closed=True):
    s3_resource_arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the Amazon S3 object. For more information about how to find the ARN for an Amazon S3 object, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-arn-format.html">Amazon S3 resources</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p>"""
    role_arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the Identity and Access Management role that allows IoT SiteWise to send data to Amazon S3.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomerManagedS3Storage) -> dict:
    out: dict = {}
    out["s3ResourceArn"] = value["s3_resource_arn"]
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> CustomerManagedS3Storage:
    out: CustomerManagedS3Storage = {}  # type: ignore[typeddict-item]
    if data.get("s3ResourceArn") is not None:
        out["s3_resource_arn"] = data["s3ResourceArn"]
    else:
        raise DeserializationError("CustomerManagedS3Storage.s3_resource_arn required")
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("CustomerManagedS3Storage.role_arn required")
    return out
