"""Generated from Smithy shape ``com.amazonaws.textract#HumanLoopConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.flow_definition_arn
    import capo_textract.types.human_loop_data_attributes
    import capo_textract.types.human_loop_name


class HumanLoopConfig(TypedDict, closed=True):
    human_loop_name: "capo_textract.types.human_loop_name.HumanLoopName"
    """<p>The name of the human workflow used for this image. This should be kept unique within a region.</p>"""
    flow_definition_arn: "capo_textract.types.flow_definition_arn.FlowDefinitionArn"
    """<p>The Amazon Resource Name (ARN) of the flow definition.</p>"""
    data_attributes: NotRequired[
        "capo_textract.types.human_loop_data_attributes.HumanLoopDataAttributes"
    ]
    """<p>Sets attributes of the input data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HumanLoopConfig) -> dict:
    out: dict = {}
    out["HumanLoopName"] = value["human_loop_name"]
    out["FlowDefinitionArn"] = value["flow_definition_arn"]
    if "data_attributes" in value:
        import capo_textract.types.human_loop_data_attributes

        out["DataAttributes"] = (
            capo_textract.types.human_loop_data_attributes.serialize_aws_json_1_1(
                value["data_attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HumanLoopConfig:
    out: HumanLoopConfig = {}  # type: ignore[typeddict-item]
    if data.get("HumanLoopName") is not None:
        out["human_loop_name"] = data["HumanLoopName"]
    else:
        out["human_loop_name"] = ""
    if data.get("FlowDefinitionArn") is not None:
        out["flow_definition_arn"] = data["FlowDefinitionArn"]
    else:
        out["flow_definition_arn"] = ""
    if data.get("DataAttributes") is not None:
        import capo_textract.types.human_loop_data_attributes

        out["data_attributes"] = (
            capo_textract.types.human_loop_data_attributes.deserialize_aws_json_1_1(
                data["DataAttributes"]
            )
        )
    return out
