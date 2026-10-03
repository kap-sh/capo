"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_application_auto_scaling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.amazon_resource_name
    import capo_application_auto_scaling.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: (
        "capo_application_auto_scaling.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>Identifies the Application Auto Scaling scalable target that you want to apply tags to.</p> <p>For example: <code>arn:aws:application-autoscaling:us-east-1:123456789012:scalable-target/1234abcd56ab78cd901ef1234567890ab123</code> </p> <p>To get the ARN for a scalable target, use <a>DescribeScalableTargets</a>.</p>"""
    tags: "capo_application_auto_scaling.types.tag_map.TagMap"
    """<p>The tags assigned to the resource. A tag is a label that you assign to an Amazon Web Services resource.</p> <p>Each tag consists of a tag key and a tag value.</p> <p>You cannot have more than one tag on an Application Auto Scaling scalable target with the same tag key. If you specify an existing tag key with a different tag value, Application Auto Scaling replaces the current tag value with the specified one.</p> <p>For information about the rules that apply to tag keys and tag values, see <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html">User-defined tag restrictions</a> in the <i>Amazon Web Services Billing User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_application_auto_scaling.types.tag_map

    out["Tags"] = capo_application_auto_scaling.types.tag_map.serialize_aws_json_1_1(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if data.get("Tags") is not None:
        import capo_application_auto_scaling.types.tag_map

        out["tags"] = (
            capo_application_auto_scaling.types.tag_map.deserialize_aws_json_1_1(
                data["Tags"]
            )
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
