"""Generated from Smithy shape ``com.amazonaws.s3control#CreateAccessPointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement
from capo_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3_control.types.access_point_name
    import capo_s3_control.types.account_id
    import capo_s3_control.types.bucket_name
    import capo_s3_control.types.public_access_block_configuration
    import capo_s3_control.types.scope
    import capo_s3_control.types.tag_list
    import capo_s3_control.types.vpc_configuration


class CreateAccessPointRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID for the account that owns the specified access point.</p>"""
    name: "capo_s3_control.types.access_point_name.AccessPointName"
    """<p>The name you want to assign to this access point.</p> <p>For directory buckets, the access point name must consist of a base name that you provide and suffix that includes the <code>ZoneID</code> (Amazon Web Services Availability Zone or Local Zone) of your bucket location, followed by <code>--xa-s3</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-directory-buckets.html">Managing access to shared datasets in directory buckets with access points</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    bucket: "capo_s3_control.types.bucket_name.BucketName"
    """<p>The name of the bucket that you want to associate this access point with.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format <code>arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name></code>. For example, to access the bucket <code>reports</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports</code>. The value must be URL encoded. </p>"""
    vpc_configuration: NotRequired[
        "capo_s3_control.types.vpc_configuration.VpcConfiguration"
    ]
    """<p>If you include this field, Amazon S3 restricts access to this access point to requests from the specified virtual private cloud (VPC).</p> <note> <p>This is required for creating an access point for Amazon S3 on Outposts buckets.</p> </note>"""
    public_access_block_configuration: NotRequired[
        "capo_s3_control.types.public_access_block_configuration.PublicAccessBlockConfiguration"
    ]
    """<p> The <code>PublicAccessBlock</code> configuration that you want to apply to the access point. </p>"""
    bucket_account_id: NotRequired["capo_s3_control.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID associated with the S3 bucket associated with this access point.</p> <p>For same account access point when your bucket and access point belong to the same account owner, the <code>BucketAccountId</code> is not required. For cross-account access point when your bucket and access point are not in the same account, the <code>BucketAccountId</code> is required. </p>"""
    scope: NotRequired["capo_s3_control.types.scope.Scope"]
    """<p>For directory buckets, you can filter access control to specific prefixes, API operations, or a combination of both. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-directory-buckets.html">Managing access to shared datasets in directory buckets with access points</a> in the <i>Amazon S3 User Guide</i>.</p> <note> <p>Scope is only supported for access points attached to directory buckets.</p> </note>"""
    tags: NotRequired["capo_s3_control.types.tag_list.TagList"]
    """<p>An array of tags that you can apply to an access point. Tags are key-value pairs of metadata used to control access to your access points. For more information about tags, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html">Using tags with Amazon S3</a>. For information about tagging access points, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html#using-tags-for-abac">Using tags for attribute-based access control (ABAC)</a>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CreateAccessPointRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Bucket").text = str(value["bucket"])
    if "vpc_configuration" in value:
        import capo_s3_control.types.vpc_configuration

        capo_s3_control.types.vpc_configuration.serialize_xml(
            value["vpc_configuration"], el, "VpcConfiguration"
        )
    if "public_access_block_configuration" in value:
        import capo_s3_control.types.public_access_block_configuration

        capo_s3_control.types.public_access_block_configuration.serialize_xml(
            value["public_access_block_configuration"],
            el,
            "PublicAccessBlockConfiguration",
        )
    if "bucket_account_id" in value:
        SubElement(el, "BucketAccountId").text = str(value["bucket_account_id"])
    if "scope" in value:
        import capo_s3_control.types.scope

        capo_s3_control.types.scope.serialize_xml(value["scope"], el, "Scope")
    if "tags" in value:
        import capo_s3_control.types.tag_list

        capo_s3_control.types.tag_list.serialize_xml(value["tags"], el, "Tags")


def deserialize_xml(el: Element) -> CreateAccessPointRequest:
    out: CreateAccessPointRequest = {}  # type: ignore[typeddict-item]
    child_bucket = el.find("Bucket")
    if child_bucket is not None:
        out["bucket"] = str(child_bucket.text or "")
    else:
        raise DeserializationError("CreateAccessPointRequest.bucket required")
    child_vpc_configuration = el.find("VpcConfiguration")
    if child_vpc_configuration is not None:
        import capo_s3_control.types.vpc_configuration

        out["vpc_configuration"] = (
            capo_s3_control.types.vpc_configuration.deserialize_xml(
                child_vpc_configuration
            )
        )
    child_public_access_block_configuration = el.find("PublicAccessBlockConfiguration")
    if child_public_access_block_configuration is not None:
        import capo_s3_control.types.public_access_block_configuration

        out["public_access_block_configuration"] = (
            capo_s3_control.types.public_access_block_configuration.deserialize_xml(
                child_public_access_block_configuration
            )
        )
    child_bucket_account_id = el.find("BucketAccountId")
    if child_bucket_account_id is not None:
        out["bucket_account_id"] = str(child_bucket_account_id.text or "")
    child_scope = el.find("Scope")
    if child_scope is not None:
        import capo_s3_control.types.scope

        out["scope"] = capo_s3_control.types.scope.deserialize_xml(child_scope)
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_s3_control.types.tag_list

        out["tags"] = capo_s3_control.types.tag_list.deserialize_xml(child_tags)
    return out
