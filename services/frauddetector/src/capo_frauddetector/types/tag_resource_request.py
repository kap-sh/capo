"""Generated from Smithy shape ``com.amazonaws.frauddetector#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.fraud_detector_arn
    import capo_frauddetector.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_frauddetector.types.fraud_detector_arn.fraudDetectorArn"
    """<p>The resource ARN.</p>"""
    tags: "capo_frauddetector.types.tag_list.tagList"
    """<p>The tags to assign to the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["resourceARN"] = value["resource_arn"]
    import capo_frauddetector.types.tag_list

    out["tags"] = capo_frauddetector.types.tag_list.serialize_aws_json_1_1(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceARN") is not None:
        out["resource_arn"] = data["resourceARN"]
    else:
        out["resource_arn"] = ""
    if data.get("tags") is not None:
        import capo_frauddetector.types.tag_list

        out["tags"] = capo_frauddetector.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    else:
        out["tags"] = []
    return out
