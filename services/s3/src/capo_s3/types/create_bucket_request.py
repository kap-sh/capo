"""Generated from Smithy shape ``com.amazonaws.s3#CreateBucketRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.bucket_canned_acl
    import capo_s3.types.bucket_name
    import capo_s3.types.bucket_namespace
    import capo_s3.types.create_bucket_configuration
    import capo_s3.types.grant_full_control
    import capo_s3.types.grant_read
    import capo_s3.types.grant_read_acp
    import capo_s3.types.grant_write
    import capo_s3.types.grant_write_acp
    import capo_s3.types.object_lock_enabled_for_bucket
    import capo_s3.types.object_ownership


class CreateBucketRequest(TypedDict, closed=True):
    acl: NotRequired["capo_s3.types.bucket_canned_acl.BucketCannedACL"]
    """<p>The canned ACL to apply to the bucket.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p>The name of the bucket to create.</p> <p> <b>General purpose buckets</b> - For information about bucket naming restrictions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html">Bucket naming rules</a> in the <i>Amazon S3 User Guide</i>.</p> <p> <b>Directory buckets </b> - When you use this operation with a directory bucket, you must use path-style requests in the format <code>https://s3express-control.<i>region-code</i>.amazonaws.com/<i>bucket-name</i> </code>. Virtual-hosted-style requests aren't supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must also follow the format <code> <i>bucket-base-name</i>--<i>zone-id</i>--x-s3</code> (for example, <code> <i>DOC-EXAMPLE-BUCKET</i>--<i>usw2-az1</i>--x-s3</code>). For information about bucket naming restrictions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html">Directory bucket naming rules</a> in the <i>Amazon S3 User Guide</i> </p>"""
    create_bucket_configuration: NotRequired[
        "capo_s3.types.create_bucket_configuration.CreateBucketConfiguration"
    ]
    """<p>The configuration information for the bucket.</p>"""
    grant_full_control: NotRequired["capo_s3.types.grant_full_control.GrantFullControl"]
    """<p>Allows grantee the read, write, read ACP, and write ACP permissions on the bucket.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    grant_read: NotRequired["capo_s3.types.grant_read.GrantRead"]
    """<p>Allows grantee to list the objects in the bucket.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    grant_read_acp: NotRequired["capo_s3.types.grant_read_acp.GrantReadACP"]
    """<p>Allows grantee to read the bucket ACL.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    grant_write: NotRequired["capo_s3.types.grant_write.GrantWrite"]
    """<p>Allows grantee to create new objects in the bucket.</p> <p>For the bucket and object owners of existing objects, also allows deletions and overwrites of those objects.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    grant_write_acp: NotRequired["capo_s3.types.grant_write_acp.GrantWriteACP"]
    """<p>Allows grantee to write the ACL for the applicable bucket.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    object_lock_enabled_for_bucket: NotRequired[
        "capo_s3.types.object_lock_enabled_for_bucket.ObjectLockEnabledForBucket"
    ]
    """<p>Specifies whether you want S3 Object Lock to be enabled for the new bucket.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    object_ownership: NotRequired["capo_s3.types.object_ownership.ObjectOwnership"]
    bucket_namespace: NotRequired["capo_s3.types.bucket_namespace.BucketNamespace"]
    """<p>Specifies the namespace where you want to create your general purpose bucket. When you create a general purpose bucket, you can choose to create a bucket in the shared global namespace or you can choose to create a bucket in your account regional namespace. Your account regional namespace is a subdivision of the global namespace that only your account can create buckets in. For more information on bucket namespaces, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/gpbucketnamespaces.html">Namespaces for general purpose buckets</a>.</p> <p>General purpose buckets in your account regional namespace must follow a specific naming convention. These buckets consist of a bucket name prefix that you create, and a suffix that contains your 12-digit Amazon Web Services Account ID, the Amazon Web Services Region code, and ends with <code>-an</code>. Bucket names must follow the format <code>bucket-name-prefix-accountId-region-an</code> (for example, <code>amzn-s3-demo-bucket-111122223333-us-west-2-an</code>). For information about bucket naming restrictions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html#account-regional-naming-rules">Account regional namespace naming rules</a> in the <i>Amazon S3 User Guide</i>.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(value: CreateBucketRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "create_bucket_configuration" in value:
        import capo_s3.types.create_bucket_configuration

        capo_s3.types.create_bucket_configuration.serialize_xml(
            value["create_bucket_configuration"], el, "CreateBucketConfiguration"
        )


def deserialize_xml(el: Element) -> CreateBucketRequest:
    out: CreateBucketRequest = {}  # type: ignore[typeddict-item]
    child_create_bucket_configuration = el.find("CreateBucketConfiguration")
    if child_create_bucket_configuration is not None:
        import capo_s3.types.create_bucket_configuration

        out["create_bucket_configuration"] = (
            capo_s3.types.create_bucket_configuration.deserialize_xml(
                child_create_bucket_configuration
            )
        )
    return out
