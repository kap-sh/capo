"""Generated from Smithy shape ``com.amazonaws.s3#CreateBucketConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.bucket_info
    import capo_s3.types.bucket_location_constraint
    import capo_s3.types.location_info
    import capo_s3.types.tag_set


class CreateBucketConfiguration(TypedDict, closed=True):
    location_constraint: NotRequired[
        "capo_s3.types.bucket_location_constraint.BucketLocationConstraint"
    ]
    """<p>Specifies the Region where the bucket will be created. You might choose a Region to optimize latency, minimize costs, or address regulatory requirements. For example, if you reside in Europe, you will probably find it advantageous to create buckets in the Europe (Ireland) Region.</p> <p>If you don't specify a Region, the bucket is created in the US East (N. Virginia) Region (us-east-1) by default. Configurations using the value <code>EU</code> will create a bucket in <code>eu-west-1</code>.</p> <p>For a list of the valid values for all of the Amazon Web Services Regions, see <a href="https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region">Regions and Endpoints</a>.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    location: NotRequired["capo_s3.types.location_info.LocationInfo"]
    """<p>Specifies the location where the bucket will be created.</p> <p> <b>Directory buckets </b> - The location type is Availability Zone or Local Zone. To use the Local Zone location type, your account must be enabled for Local Zones. Otherwise, you get an HTTP <code>403 Forbidden</code> error with the error code <code>AccessDenied</code>. To learn more, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/opt-in-directory-bucket-lz.html">Enable accounts for Local Zones</a> in the <i>Amazon S3 User Guide</i>. </p> <note> <p>This functionality is only supported by directory buckets.</p> </note>"""
    bucket: NotRequired["capo_s3.types.bucket_info.BucketInfo"]
    """<p>Specifies the information about the bucket that will be created.</p> <note> <p>This functionality is only supported by directory buckets.</p> </note>"""
    tags: NotRequired["capo_s3.types.tag_set.TagSet"]
    """<p>An array of tags that you can apply to the bucket that you're creating. Tags are key-value pairs of metadata used to categorize and organize your buckets, track costs, and control access. </p> <p>You must have the <code>s3:TagResource</code> permission to create a general purpose bucket with tags or the <code>s3express:TagResource</code> permission to create a directory bucket with tags.</p> <p>When creating buckets with tags, note that tag-based conditions using <code>aws:ResourceTag</code> and <code>s3:BucketTag</code> condition keys are applicable only after ABAC is enabled on the bucket. To learn more, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/buckets-tagging-enable-abac.html">Enabling ABAC in general purpose buckets</a>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CreateBucketConfiguration, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "location_constraint" in value:
        import capo_s3.types.bucket_location_constraint

        capo_s3.types.bucket_location_constraint.serialize_xml(
            value["location_constraint"], el, "LocationConstraint"
        )
    if "location" in value:
        import capo_s3.types.location_info

        capo_s3.types.location_info.serialize_xml(value["location"], el, "Location")
    if "bucket" in value:
        import capo_s3.types.bucket_info

        capo_s3.types.bucket_info.serialize_xml(value["bucket"], el, "Bucket")
    if "tags" in value:
        import capo_s3.types.tag_set

        capo_s3.types.tag_set.serialize_xml(value["tags"], el, "Tags")


def deserialize_xml(el: Element) -> CreateBucketConfiguration:
    out: CreateBucketConfiguration = {}  # type: ignore[typeddict-item]
    child_location_constraint = el.find("LocationConstraint")
    if child_location_constraint is not None:
        import capo_s3.types.bucket_location_constraint

        out["location_constraint"] = (
            capo_s3.types.bucket_location_constraint.deserialize_xml(
                child_location_constraint
            )
        )
    child_location = el.find("Location")
    if child_location is not None:
        import capo_s3.types.location_info

        out["location"] = capo_s3.types.location_info.deserialize_xml(child_location)
    child_bucket = el.find("Bucket")
    if child_bucket is not None:
        import capo_s3.types.bucket_info

        out["bucket"] = capo_s3.types.bucket_info.deserialize_xml(child_bucket)
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_s3.types.tag_set

        out["tags"] = capo_s3.types.tag_set.deserialize_xml(child_tags)
    return out
