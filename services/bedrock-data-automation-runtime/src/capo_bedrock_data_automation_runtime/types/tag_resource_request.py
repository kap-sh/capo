"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation_runtime.types.tag_list
    import capo_bedrock_data_automation_runtime.types.taggable_resource_arn


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_bedrock_data_automation_runtime.types.taggable_resource_arn.TaggableResourceArn"
    tags: "capo_bedrock_data_automation_runtime.types.tag_list.TagList"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["resourceARN"] = value["resource_arn"]
    import capo_bedrock_data_automation_runtime.types.tag_list

    out["tags"] = (
        capo_bedrock_data_automation_runtime.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceARN") is not None:
        out["resource_arn"] = data["resourceARN"]
    else:
        out["resource_arn"] = ""
    if data.get("tags") is not None:
        import capo_bedrock_data_automation_runtime.types.tag_list

        out["tags"] = (
            capo_bedrock_data_automation_runtime.types.tag_list.deserialize_aws_json_1_1(
                data["tags"]
            )
        )
    else:
        out["tags"] = []
    return out
