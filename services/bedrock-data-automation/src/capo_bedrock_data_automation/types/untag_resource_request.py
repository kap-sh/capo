"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.tag_key_list
    import capo_bedrock_data_automation.types.taggable_resource_arn


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: (
        "capo_bedrock_data_automation.types.taggable_resource_arn.TaggableResourceArn"
    )
    tag_keys: "capo_bedrock_data_automation.types.tag_key_list.TagKeyList"


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["resourceARN"] = value["resource_arn"]
    import capo_bedrock_data_automation.types.tag_key_list

    out["tagKeys"] = capo_bedrock_data_automation.types.tag_key_list.serialize_json(
        value["tag_keys"]
    )
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceARN") is not None:
        out["resource_arn"] = data["resourceARN"]
    else:
        out["resource_arn"] = ""
    if data.get("tagKeys") is not None:
        import capo_bedrock_data_automation.types.tag_key_list

        out["tag_keys"] = (
            capo_bedrock_data_automation.types.tag_key_list.deserialize_json(
                data["tagKeys"]
            )
        )
    else:
        out["tag_keys"] = []
    return out
