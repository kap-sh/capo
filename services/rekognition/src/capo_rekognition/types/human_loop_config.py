"""Generated from Smithy shape ``com.amazonaws.rekognition#HumanLoopConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rekognition.types.flow_definition_arn
    import capo_rekognition.types.human_loop_data_attributes
    import capo_rekognition.types.human_loop_name


class HumanLoopConfig(TypedDict, closed=True):
    human_loop_name: "capo_rekognition.types.human_loop_name.HumanLoopName"
    """<p>The name of the human review used for this image. This should be kept unique within a region.</p>"""
    flow_definition_arn: "capo_rekognition.types.flow_definition_arn.FlowDefinitionArn"
    """<p>The Amazon Resource Name (ARN) of the flow definition. You can create a flow definition by using the Amazon Sagemaker <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateFlowDefinition.html">CreateFlowDefinition</a> Operation. </p>"""
    data_attributes: NotRequired[
        "capo_rekognition.types.human_loop_data_attributes.HumanLoopDataAttributes"
    ]
    """<p>Sets attributes of the input data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HumanLoopConfig) -> dict:
    out: dict = {}
    out["HumanLoopName"] = value["human_loop_name"]
    out["FlowDefinitionArn"] = value["flow_definition_arn"]
    if "data_attributes" in value:
        import capo_rekognition.types.human_loop_data_attributes

        out["DataAttributes"] = (
            capo_rekognition.types.human_loop_data_attributes.serialize_aws_json_1_1(
                value["data_attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HumanLoopConfig:
    out: HumanLoopConfig = {}  # type: ignore[typeddict-item]
    if data.get("HumanLoopName") is not None:
        out["human_loop_name"] = data["HumanLoopName"]
    else:
        raise DeserializationError("HumanLoopConfig.human_loop_name required")
    if data.get("FlowDefinitionArn") is not None:
        out["flow_definition_arn"] = data["FlowDefinitionArn"]
    else:
        raise DeserializationError("HumanLoopConfig.flow_definition_arn required")
    if data.get("DataAttributes") is not None:
        import capo_rekognition.types.human_loop_data_attributes

        out["data_attributes"] = (
            capo_rekognition.types.human_loop_data_attributes.deserialize_aws_json_1_1(
                data["DataAttributes"]
            )
        )
    return out
