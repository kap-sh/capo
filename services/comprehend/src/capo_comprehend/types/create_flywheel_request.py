"""Generated from Smithy shape ``com.amazonaws.comprehend#CreateFlywheelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.client_request_token_string
    import capo_comprehend.types.comprehend_arn_name
    import capo_comprehend.types.comprehend_model_arn
    import capo_comprehend.types.data_security_config
    import capo_comprehend.types.flywheel_s3_uri
    import capo_comprehend.types.iam_role_arn
    import capo_comprehend.types.model_type
    import capo_comprehend.types.tag_list
    import capo_comprehend.types.task_config


class CreateFlywheelRequest(TypedDict, closed=True):
    flywheel_name: "capo_comprehend.types.comprehend_arn_name.ComprehendArnName"
    """<p>Name for the flywheel.</p>"""
    active_model_arn: NotRequired[
        "capo_comprehend.types.comprehend_model_arn.ComprehendModelArn"
    ]
    """<p>To associate an existing model with the flywheel, specify the Amazon Resource Number (ARN) of the model version. Do not set <code>TaskConfig</code> or <code>ModelType</code> if you specify an <code>ActiveModelArn</code>.</p>"""
    data_access_role_arn: "capo_comprehend.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend the permissions required to access the flywheel data in the data lake.</p>"""
    task_config: NotRequired["capo_comprehend.types.task_config.TaskConfig"]
    """<p>Configuration about the model associated with the flywheel. You need to set <code>TaskConfig</code> if you are creating a flywheel for a new model.</p>"""
    model_type: NotRequired["capo_comprehend.types.model_type.ModelType"]
    """<p>The model type. You need to set <code>ModelType</code> if you are creating a flywheel for a new model.</p>"""
    data_lake_s3_uri: "capo_comprehend.types.flywheel_s3_uri.FlywheelS3Uri"
    """<p>Enter the S3 location for the data lake. You can specify a new S3 bucket or a new folder of an existing S3 bucket. The flywheel creates the data lake at this location.</p>"""
    data_security_config: NotRequired[
        "capo_comprehend.types.data_security_config.DataSecurityConfig"
    ]
    """<p>Data security configurations.</p>"""
    client_request_token: NotRequired[
        "capo_comprehend.types.client_request_token_string.ClientRequestTokenString"
    ]
    """<p>A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.</p>"""
    tags: NotRequired["capo_comprehend.types.tag_list.TagList"]
    """<p>The tags to associate with this flywheel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFlywheelRequest) -> dict:
    out: dict = {}
    out["FlywheelName"] = value["flywheel_name"]
    if "active_model_arn" in value:
        out["ActiveModelArn"] = value["active_model_arn"]
    out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "task_config" in value:
        import capo_comprehend.types.task_config

        out["TaskConfig"] = capo_comprehend.types.task_config.serialize_aws_json_1_1(
            value["task_config"]
        )
    if "model_type" in value:
        import capo_comprehend.types.model_type

        out["ModelType"] = capo_comprehend.types.model_type.serialize_aws_json_1_1(
            value["model_type"]
        )
    out["DataLakeS3Uri"] = value["data_lake_s3_uri"]
    if "data_security_config" in value:
        import capo_comprehend.types.data_security_config

        out["DataSecurityConfig"] = (
            capo_comprehend.types.data_security_config.serialize_aws_json_1_1(
                value["data_security_config"]
            )
        )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import capo_comprehend.types.tag_list

        out["Tags"] = capo_comprehend.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFlywheelRequest:
    out: CreateFlywheelRequest = {}  # type: ignore[typeddict-item]
    if data.get("FlywheelName") is not None:
        out["flywheel_name"] = data["FlywheelName"]
    else:
        out["flywheel_name"] = ""
    if data.get("ActiveModelArn") is not None:
        out["active_model_arn"] = data["ActiveModelArn"]
    if data.get("DataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    else:
        out["data_access_role_arn"] = ""
    if data.get("TaskConfig") is not None:
        import capo_comprehend.types.task_config

        out["task_config"] = capo_comprehend.types.task_config.deserialize_aws_json_1_1(
            data["TaskConfig"]
        )
    if data.get("ModelType") is not None:
        import capo_comprehend.types.model_type

        out["model_type"] = capo_comprehend.types.model_type.deserialize_aws_json_1_1(
            data["ModelType"]
        )
    if data.get("DataLakeS3Uri") is not None:
        out["data_lake_s3_uri"] = data["DataLakeS3Uri"]
    else:
        out["data_lake_s3_uri"] = ""
    if data.get("DataSecurityConfig") is not None:
        import capo_comprehend.types.data_security_config

        out["data_security_config"] = (
            capo_comprehend.types.data_security_config.deserialize_aws_json_1_1(
                data["DataSecurityConfig"]
            )
        )
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("Tags") is not None:
        import capo_comprehend.types.tag_list

        out["tags"] = capo_comprehend.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
