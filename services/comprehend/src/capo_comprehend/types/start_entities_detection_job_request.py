"""Generated from Smithy shape ``com.amazonaws.comprehend#StartEntitiesDetectionJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import capo_comprehend.types.client_request_token_string
    import capo_comprehend.types.comprehend_flywheel_arn
    import capo_comprehend.types.entity_recognizer_arn
    import capo_comprehend.types.iam_role_arn
    import capo_comprehend.types.input_data_config
    import capo_comprehend.types.job_name
    import capo_comprehend.types.kms_key_id
    import capo_comprehend.types.language_code
    import capo_comprehend.types.output_data_config
    import capo_comprehend.types.tag_list
    import capo_comprehend.types.vpc_config


class StartEntitiesDetectionJobRequest(TypedDict, closed=True):
    input_data_config: "capo_comprehend.types.input_data_config.InputDataConfig"
    """<p>Specifies the format and location of the input data for the job.</p>"""
    output_data_config: "capo_comprehend.types.output_data_config.OutputDataConfig"
    """<p>Specifies where to send the output files.</p>"""
    data_access_role_arn: "capo_comprehend.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data. For more information, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/security_iam_id-based-policy-examples.html#auth-role-permissions">Role-based permissions</a>.</p>"""
    job_name: NotRequired["capo_comprehend.types.job_name.JobName"]
    """<p>The identifier of the job.</p>"""
    entity_recognizer_arn: NotRequired[
        "capo_comprehend.types.entity_recognizer_arn.EntityRecognizerArn"
    ]
    """<p>The Amazon Resource Name (ARN) that identifies the specific entity recognizer to be used by the <code>StartEntitiesDetectionJob</code>. This ARN is optional and is only used for a custom entity recognition job.</p>"""
    language_code: "capo_comprehend.types.language_code.LanguageCode"
    """<p>The language of the input documents. All documents must be in the same language. You can specify any of the languages supported by Amazon Comprehend. If custom entities recognition is used, this parameter is ignored and the language used for training the model is used instead.</p>"""
    client_request_token: NotRequired[
        "capo_comprehend.types.client_request_token_string.ClientRequestTokenString"
    ]
    """<p>A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.</p>"""
    volume_kms_key_id: NotRequired["capo_comprehend.types.kms_key_id.KmsKeyId"]
    """<p>ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>"1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> </ul>"""
    vpc_config: NotRequired["capo_comprehend.types.vpc_config.VpcConfig"]
    """<p>Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for your entity detection job. For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html">Amazon VPC</a>. </p>"""
    tags: NotRequired["capo_comprehend.types.tag_list.TagList"]
    """<p>Tags to associate with the entities detection job. A tag is a key-value pair that adds metadata to a resource used by Amazon Comprehend. For example, a tag with "Sales" as the key might be added to a resource to indicate its use by the sales department.</p>"""
    flywheel_arn: NotRequired[
        "capo_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the flywheel associated with the model to use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartEntitiesDetectionJobRequest) -> dict:
    out: dict = {}
    import capo_comprehend.types.input_data_config

    out["InputDataConfig"] = (
        capo_comprehend.types.input_data_config.serialize_aws_json_1_1(
            value["input_data_config"]
        )
    )
    import capo_comprehend.types.output_data_config

    out["OutputDataConfig"] = (
        capo_comprehend.types.output_data_config.serialize_aws_json_1_1(
            value["output_data_config"]
        )
    )
    out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "entity_recognizer_arn" in value:
        out["EntityRecognizerArn"] = value["entity_recognizer_arn"]
    import capo_comprehend.types.language_code

    out["LanguageCode"] = capo_comprehend.types.language_code.serialize_aws_json_1_1(
        value["language_code"]
    )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "volume_kms_key_id" in value:
        out["VolumeKmsKeyId"] = value["volume_kms_key_id"]
    if "vpc_config" in value:
        import capo_comprehend.types.vpc_config

        out["VpcConfig"] = capo_comprehend.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "tags" in value:
        import capo_comprehend.types.tag_list

        out["Tags"] = capo_comprehend.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "flywheel_arn" in value:
        out["FlywheelArn"] = value["flywheel_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartEntitiesDetectionJobRequest:
    out: StartEntitiesDetectionJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("InputDataConfig") is not None:
        import capo_comprehend.types.input_data_config

        out["input_data_config"] = (
            capo_comprehend.types.input_data_config.deserialize_aws_json_1_1(
                data["InputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "StartEntitiesDetectionJobRequest.input_data_config required"
        )
    if data.get("OutputDataConfig") is not None:
        import capo_comprehend.types.output_data_config

        out["output_data_config"] = (
            capo_comprehend.types.output_data_config.deserialize_aws_json_1_1(
                data["OutputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "StartEntitiesDetectionJobRequest.output_data_config required"
        )
    if data.get("DataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    else:
        raise DeserializationError(
            "StartEntitiesDetectionJobRequest.data_access_role_arn required"
        )
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    if data.get("EntityRecognizerArn") is not None:
        out["entity_recognizer_arn"] = data["EntityRecognizerArn"]
    if data.get("LanguageCode") is not None:
        import capo_comprehend.types.language_code

        out["language_code"] = (
            capo_comprehend.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    else:
        raise DeserializationError(
            "StartEntitiesDetectionJobRequest.language_code required"
        )
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("VolumeKmsKeyId") is not None:
        out["volume_kms_key_id"] = data["VolumeKmsKeyId"]
    if data.get("VpcConfig") is not None:
        import capo_comprehend.types.vpc_config

        out["vpc_config"] = capo_comprehend.types.vpc_config.deserialize_aws_json_1_1(
            data["VpcConfig"]
        )
    if data.get("Tags") is not None:
        import capo_comprehend.types.tag_list

        out["tags"] = capo_comprehend.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("FlywheelArn") is not None:
        out["flywheel_arn"] = data["FlywheelArn"]
    return out
