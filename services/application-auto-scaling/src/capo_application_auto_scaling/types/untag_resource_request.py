"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.amazon_resource_name
    import capo_application_auto_scaling.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: (
        "capo_application_auto_scaling.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>Identifies the Application Auto Scaling scalable target from which to remove tags.</p> <p>For example: <code>arn:aws:application-autoscaling:us-east-1:123456789012:scalable-target/1234abcd56ab78cd901ef1234567890ab123</code> </p> <p>To get the ARN for a scalable target, use <a>DescribeScalableTargets</a>.</p>"""
    tag_keys: "capo_application_auto_scaling.types.tag_key_list.TagKeyList"
    """<p>One or more tag keys. Specify only the tag keys, not the tag values.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_application_auto_scaling.types.tag_key_list

    out["TagKeys"] = (
        capo_application_auto_scaling.types.tag_key_list.serialize_aws_json_1_1(
            value["tag_keys"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        out["resource_arn"] = ""
    if data.get("TagKeys") is not None:
        import capo_application_auto_scaling.types.tag_key_list

        out["tag_keys"] = (
            capo_application_auto_scaling.types.tag_key_list.deserialize_aws_json_1_1(
                data["TagKeys"]
            )
        )
    else:
        out["tag_keys"] = []
    return out
