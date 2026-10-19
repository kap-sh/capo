"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#KinesisResource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.arn
    import capo_bedrock_agentcore_control.types.content_configuration_list


class KinesisResource(TypedDict, closed=True):
    data_stream_arn: "capo_bedrock_agentcore_control.types.arn.Arn"
    """<p>ARN of the Kinesis Data Stream.</p>"""
    content_configurations: "capo_bedrock_agentcore_control.types.content_configuration_list.ContentConfigurationList"
    """<p>Content configurations for stream delivery.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KinesisResource) -> dict:
    out: dict = {}
    out["dataStreamArn"] = value["data_stream_arn"]
    import capo_bedrock_agentcore_control.types.content_configuration_list

    out["contentConfigurations"] = (
        capo_bedrock_agentcore_control.types.content_configuration_list.serialize_json(
            value["content_configurations"]
        )
    )
    return out


def deserialize_json(data: dict) -> KinesisResource:
    out: KinesisResource = {}  # type: ignore[typeddict-item]
    if data.get("dataStreamArn") is not None:
        out["data_stream_arn"] = data["dataStreamArn"]
    else:
        out["data_stream_arn"] = ""
    if data.get("contentConfigurations") is not None:
        import capo_bedrock_agentcore_control.types.content_configuration_list

        out["content_configurations"] = (
            capo_bedrock_agentcore_control.types.content_configuration_list.deserialize_json(
                data["contentConfigurations"]
            )
        )
    else:
        out["content_configurations"] = []
    return out
