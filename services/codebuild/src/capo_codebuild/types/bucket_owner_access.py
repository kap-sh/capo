"""Generated from Smithy shape ``com.amazonaws.codebuild#BucketOwnerAccess``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies the bucket owner's access for objects that another account uploads to their Amazon S3 bucket. By default, only the account that uploads the objects to the bucket has access to these objects. This property allows you to give the bucket owner access to these objects.</p> <note> <p>To use this property, your CodeBuild service role must have the <code>s3:PutBucketAcl</code> permission. This permission allows CodeBuild to modify the access control list for the bucket.</p> </note> <p>This property can be one of the following values:</p> <dl> <dt>NONE</dt> <dd> <p>The bucket owner does not have access to the objects. This is the default.</p> </dd> <dt>READ_ONLY</dt> <dd> <p>The bucket owner has read-only access to the objects. The uploading account retains ownership of the objects.</p> </dd> <dt>FULL</dt> <dd> <p>The bucket owner has full access to the objects. Object ownership is determined by the following criteria:</p> <ul> <li> <p>If the bucket is configured with the <b>Bucket owner preferred</b> setting, the bucket owner owns the objects. The uploading account will have object access as specified by the bucket's policy.</p> </li> <li> <p>Otherwise, the uploading account retains ownership of the objects.</p> </li> </ul> <p>For more information about Amazon S3 object ownership, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html">Controlling ownership of uploaded objects using S3 Object Ownership</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> </dd> </dl>"""
BucketOwnerAccess: TypeAlias = Literal[
    "NONE",
    "READ_ONLY",
    "FULL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BucketOwnerAccess) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BucketOwnerAccess:
    return cast(BucketOwnerAccess, data)
