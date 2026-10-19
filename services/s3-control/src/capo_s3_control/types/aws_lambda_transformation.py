"""Generated from Smithy shape ``com.amazonaws.s3control#AwsLambdaTransformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.aws_lambda_transformation_payload
    import capo_s3_control.types.function_arn_string


class AwsLambdaTransformation(TypedDict, closed=True):
    function_arn: "capo_s3_control.types.function_arn_string.FunctionArnString"
    """<p>The Amazon Resource Name (ARN) of the Lambda function.</p>"""
    function_payload: NotRequired[
        "capo_s3_control.types.aws_lambda_transformation_payload.AwsLambdaTransformationPayload"
    ]
    """<p>Additional JSON that provides supplemental data to the Lambda function used to transform objects.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: AwsLambdaTransformation, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "FunctionArn").text = str(value["function_arn"])
    if "function_payload" in value:
        SubElement(el, "FunctionPayload").text = str(value["function_payload"])


def deserialize_xml(el: Element) -> AwsLambdaTransformation:
    out: AwsLambdaTransformation = {}  # type: ignore[typeddict-item]
    child_function_arn = el.find("FunctionArn")
    if child_function_arn is not None:
        out["function_arn"] = str(child_function_arn.text or "")
    else:
        out["function_arn"] = ""
    child_function_payload = el.find("FunctionPayload")
    if child_function_payload is not None:
        out["function_payload"] = str(child_function_payload.text or "")
    return out
