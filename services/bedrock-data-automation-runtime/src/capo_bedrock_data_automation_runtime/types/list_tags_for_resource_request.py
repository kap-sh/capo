"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation_runtime.types.taggable_resource_arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_bedrock_data_automation_runtime.types.taggable_resource_arn.TaggableResourceArn"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    out["resourceARN"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceARN") is not None:
        out["resource_arn"] = data["resourceARN"]
    else:
        out["resource_arn"] = ""
    return out
