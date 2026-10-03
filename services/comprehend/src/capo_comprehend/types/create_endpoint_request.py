"""Generated from Smithy shape ``com.amazonaws.comprehend#CreateEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import capo_comprehend.types.client_request_token_string
    import capo_comprehend.types.comprehend_endpoint_name
    import capo_comprehend.types.comprehend_flywheel_arn
    import capo_comprehend.types.comprehend_model_arn
    import capo_comprehend.types.iam_role_arn
    import capo_comprehend.types.inference_units_integer
    import capo_comprehend.types.tag_list


class CreateEndpointRequest(TypedDict, closed=True):
    endpoint_name: (
        "capo_comprehend.types.comprehend_endpoint_name.ComprehendEndpointName"
    )
    """<p>This is the descriptive suffix that becomes part of the <code>EndpointArn</code> used for all subsequent requests to this resource. </p>"""
    model_arn: NotRequired[
        "capo_comprehend.types.comprehend_model_arn.ComprehendModelArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the model to which the endpoint will be attached.</p>"""
    desired_inference_units: (
        "capo_comprehend.types.inference_units_integer.InferenceUnitsInteger"
    )
    """<p> The desired number of inference units to be used by the model using this endpoint. Each inference unit represents of a throughput of 100 characters per second.</p>"""
    client_request_token: NotRequired[
        "capo_comprehend.types.client_request_token_string.ClientRequestTokenString"
    ]
    """<p>An idempotency token provided by the customer. If this token matches a previous endpoint creation request, Amazon Comprehend will not return a <code>ResourceInUseException</code>. </p>"""
    tags: NotRequired["capo_comprehend.types.tag_list.TagList"]
    """<p>Tags to associate with the endpoint. A tag is a key-value pair that adds metadata to the endpoint. For example, a tag with "Sales" as the key might be added to an endpoint to indicate its use by the sales department. </p>"""
    data_access_role_arn: NotRequired["capo_comprehend.types.iam_role_arn.IamRoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to trained custom models encrypted with a customer managed key (ModelKmsKeyId).</p>"""
    flywheel_arn: NotRequired[
        "capo_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the flywheel to which the endpoint will be attached.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateEndpointRequest) -> dict:
    out: dict = {}
    out["EndpointName"] = value["endpoint_name"]
    if "model_arn" in value:
        out["ModelArn"] = value["model_arn"]
    out["DesiredInferenceUnits"] = value["desired_inference_units"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import capo_comprehend.types.tag_list

        out["Tags"] = capo_comprehend.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "data_access_role_arn" in value:
        out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "flywheel_arn" in value:
        out["FlywheelArn"] = value["flywheel_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateEndpointRequest:
    out: CreateEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("EndpointName") is not None:
        out["endpoint_name"] = data["EndpointName"]
    else:
        raise DeserializationError("CreateEndpointRequest.endpoint_name required")
    if data.get("ModelArn") is not None:
        out["model_arn"] = data["ModelArn"]
    if data.get("DesiredInferenceUnits") is not None:
        out["desired_inference_units"] = data["DesiredInferenceUnits"]
    else:
        raise DeserializationError(
            "CreateEndpointRequest.desired_inference_units required"
        )
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("Tags") is not None:
        import capo_comprehend.types.tag_list

        out["tags"] = capo_comprehend.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("DataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    if data.get("FlywheelArn") is not None:
        out["flywheel_arn"] = data["FlywheelArn"]
    return out
