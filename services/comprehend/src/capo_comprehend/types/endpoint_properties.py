"""Generated from Smithy shape ``com.amazonaws.comprehend#EndpointProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.any_length_string
    import capo_comprehend.types.comprehend_endpoint_arn
    import capo_comprehend.types.comprehend_flywheel_arn
    import capo_comprehend.types.comprehend_model_arn
    import capo_comprehend.types.endpoint_status
    import capo_comprehend.types.iam_role_arn
    import capo_comprehend.types.inference_units_integer
    import capo_comprehend.types.timestamp


class EndpointProperties(TypedDict, closed=True):
    endpoint_arn: NotRequired[
        "capo_comprehend.types.comprehend_endpoint_arn.ComprehendEndpointArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the endpoint.</p>"""
    status: NotRequired["capo_comprehend.types.endpoint_status.EndpointStatus"]
    """<p>Specifies the status of the endpoint. Because the endpoint updates and creation are asynchronous, so customers will need to wait for the endpoint to be <code>Ready</code> status before making inference requests.</p>"""
    message: NotRequired["capo_comprehend.types.any_length_string.AnyLengthString"]
    """<p>Specifies a reason for failure in cases of <code>Failed</code> status.</p>"""
    model_arn: NotRequired[
        "capo_comprehend.types.comprehend_model_arn.ComprehendModelArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the model to which the endpoint is attached.</p>"""
    desired_model_arn: NotRequired[
        "capo_comprehend.types.comprehend_model_arn.ComprehendModelArn"
    ]
    """<p>ARN of the new model to use for updating an existing endpoint. This ARN is going to be different from the model ARN when the update is in progress</p>"""
    desired_inference_units: NotRequired[
        "capo_comprehend.types.inference_units_integer.InferenceUnitsInteger"
    ]
    """<p>The desired number of inference units to be used by the model using this endpoint. Each inference unit represents of a throughput of 100 characters per second.</p>"""
    current_inference_units: NotRequired[
        "capo_comprehend.types.inference_units_integer.InferenceUnitsInteger"
    ]
    """<p>The number of inference units currently used by the model using this endpoint.</p>"""
    creation_time: NotRequired["capo_comprehend.types.timestamp.Timestamp"]
    """<p>The creation date and time of the endpoint.</p>"""
    last_modified_time: NotRequired["capo_comprehend.types.timestamp.Timestamp"]
    """<p>The date and time that the endpoint was last modified.</p>"""
    data_access_role_arn: NotRequired["capo_comprehend.types.iam_role_arn.IamRoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to trained custom models encrypted with a customer managed key (ModelKmsKeyId).</p>"""
    desired_data_access_role_arn: NotRequired[
        "capo_comprehend.types.iam_role_arn.IamRoleArn"
    ]
    """<p>Data access role ARN to use in case the new model is encrypted with a customer KMS key.</p>"""
    flywheel_arn: NotRequired[
        "capo_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the flywheel</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointProperties) -> dict:
    out: dict = {}
    if "endpoint_arn" in value:
        out["EndpointArn"] = value["endpoint_arn"]
    if "status" in value:
        import capo_comprehend.types.endpoint_status

        out["Status"] = capo_comprehend.types.endpoint_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "model_arn" in value:
        out["ModelArn"] = value["model_arn"]
    if "desired_model_arn" in value:
        out["DesiredModelArn"] = value["desired_model_arn"]
    if "desired_inference_units" in value:
        out["DesiredInferenceUnits"] = value["desired_inference_units"]
    if "current_inference_units" in value:
        out["CurrentInferenceUnits"] = value["current_inference_units"]
    if "creation_time" in value:
        import capo_comprehend.types.timestamp

        out["CreationTime"] = capo_comprehend.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_comprehend.types.timestamp

        out["LastModifiedTime"] = (
            capo_comprehend.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "data_access_role_arn" in value:
        out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "desired_data_access_role_arn" in value:
        out["DesiredDataAccessRoleArn"] = value["desired_data_access_role_arn"]
    if "flywheel_arn" in value:
        out["FlywheelArn"] = value["flywheel_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EndpointProperties:
    out: EndpointProperties = {}  # type: ignore[typeddict-item]
    if data.get("EndpointArn") is not None:
        out["endpoint_arn"] = data["EndpointArn"]
    if data.get("Status") is not None:
        import capo_comprehend.types.endpoint_status

        out["status"] = capo_comprehend.types.endpoint_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("ModelArn") is not None:
        out["model_arn"] = data["ModelArn"]
    if data.get("DesiredModelArn") is not None:
        out["desired_model_arn"] = data["DesiredModelArn"]
    if data.get("DesiredInferenceUnits") is not None:
        out["desired_inference_units"] = data["DesiredInferenceUnits"]
    if data.get("CurrentInferenceUnits") is not None:
        out["current_inference_units"] = data["CurrentInferenceUnits"]
    if data.get("CreationTime") is not None:
        import capo_comprehend.types.timestamp

        out["creation_time"] = capo_comprehend.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("LastModifiedTime") is not None:
        import capo_comprehend.types.timestamp

        out["last_modified_time"] = (
            capo_comprehend.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if data.get("DataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    if data.get("DesiredDataAccessRoleArn") is not None:
        out["desired_data_access_role_arn"] = data["DesiredDataAccessRoleArn"]
    if data.get("FlywheelArn") is not None:
        out["flywheel_arn"] = data["FlywheelArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EndpointProperties) -> dict:
    out: dict = {}
    if "endpoint_arn" in value:
        out["EndpointArn"] = value["endpoint_arn"]
    if "status" in value:
        import capo_comprehend.types.endpoint_status

        out["Status"] = capo_comprehend.types.endpoint_status.serialize_cbor(
            value["status"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "model_arn" in value:
        out["ModelArn"] = value["model_arn"]
    if "desired_model_arn" in value:
        out["DesiredModelArn"] = value["desired_model_arn"]
    if "desired_inference_units" in value:
        out["DesiredInferenceUnits"] = value["desired_inference_units"]
    if "current_inference_units" in value:
        out["CurrentInferenceUnits"] = value["current_inference_units"]
    if "creation_time" in value:
        import capo_comprehend.types.timestamp

        out["CreationTime"] = capo_comprehend.types.timestamp.serialize_cbor(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_comprehend.types.timestamp

        out["LastModifiedTime"] = capo_comprehend.types.timestamp.serialize_cbor(
            value["last_modified_time"]
        )
    if "data_access_role_arn" in value:
        out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "desired_data_access_role_arn" in value:
        out["DesiredDataAccessRoleArn"] = value["desired_data_access_role_arn"]
    if "flywheel_arn" in value:
        out["FlywheelArn"] = value["flywheel_arn"]
    return out


def deserialize_cbor(data: dict) -> EndpointProperties:
    out: EndpointProperties = {}  # type: ignore[typeddict-item]
    if data.get("EndpointArn") is not None:
        out["endpoint_arn"] = data["EndpointArn"]
    if data.get("Status") is not None:
        import capo_comprehend.types.endpoint_status

        out["status"] = capo_comprehend.types.endpoint_status.deserialize_cbor(
            data["Status"]
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("ModelArn") is not None:
        out["model_arn"] = data["ModelArn"]
    if data.get("DesiredModelArn") is not None:
        out["desired_model_arn"] = data["DesiredModelArn"]
    if data.get("DesiredInferenceUnits") is not None:
        out["desired_inference_units"] = data["DesiredInferenceUnits"]
    if data.get("CurrentInferenceUnits") is not None:
        out["current_inference_units"] = data["CurrentInferenceUnits"]
    if data.get("CreationTime") is not None:
        import capo_comprehend.types.timestamp

        out["creation_time"] = capo_comprehend.types.timestamp.deserialize_cbor(
            data["CreationTime"]
        )
    if data.get("LastModifiedTime") is not None:
        import capo_comprehend.types.timestamp

        out["last_modified_time"] = capo_comprehend.types.timestamp.deserialize_cbor(
            data["LastModifiedTime"]
        )
    if data.get("DataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    if data.get("DesiredDataAccessRoleArn") is not None:
        out["desired_data_access_role_arn"] = data["DesiredDataAccessRoleArn"]
    if data.get("FlywheelArn") is not None:
        out["flywheel_arn"] = data["FlywheelArn"]
    return out
