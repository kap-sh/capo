"""Generated from Smithy shape ``com.amazonaws.s3#GetBucketLocationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.bucket_location_constraint


class GetBucketLocationOutput(TypedDict, closed=True):
    location_constraint: NotRequired[
        "capo_s3.types.bucket_location_constraint.BucketLocationConstraint"
    ]
    """<p>Specifies the Region where the bucket resides. For a list of all the Amazon S3 supported location constraints by Region, see <a href="https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region">Regions and Endpoints</a>.</p> <p>Buckets in Region <code>us-east-1</code> have a LocationConstraint of <code>null</code>. Buckets with a LocationConstraint of <code>EU</code> reside in <code>eu-west-1</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetBucketLocationOutput, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "location_constraint" in value:
        import capo_s3.types.bucket_location_constraint

        capo_s3.types.bucket_location_constraint.serialize_xml(
            value["location_constraint"], el, "LocationConstraint"
        )


def deserialize_xml(el: Element) -> GetBucketLocationOutput:
    out: GetBucketLocationOutput = {}  # type: ignore[typeddict-item]
    child_location_constraint = el.find("LocationConstraint")
    if child_location_constraint is not None:
        import capo_s3.types.bucket_location_constraint

        out["location_constraint"] = (
            capo_s3.types.bucket_location_constraint.deserialize_xml(
                child_location_constraint
            )
        )
    return out
