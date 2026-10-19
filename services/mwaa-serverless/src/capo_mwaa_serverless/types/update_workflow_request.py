"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#UpdateWorkflowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mwaa_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.code
    import capo_mwaa_serverless.types.definition_s3_location
    import capo_mwaa_serverless.types.description_string
    import capo_mwaa_serverless.types.engine_version
    import capo_mwaa_serverless.types.generic_string
    import capo_mwaa_serverless.types.logging_configuration
    import capo_mwaa_serverless.types.network_configuration
    import capo_mwaa_serverless.types.role_arn
    import capo_mwaa_serverless.types.workflow_arn


class UpdateWorkflowRequest(TypedDict, closed=True):
    workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn"
    """<p>The Amazon Resource Name (ARN) of the workflow you want to update.</p>"""
    definition_s3_location: (
        "capo_mwaa_serverless.types.definition_s3_location.DefinitionS3Location"
    )
    """<p>The Amazon S3 location where the updated workflow definition file is stored.</p>"""
    code: NotRequired["capo_mwaa_serverless.types.code.Code"]
    """<p>The location of code artifacts in Amazon S3 for the updated workflow. The service copies the code from this location at the time of the request.</p>"""
    role_arn: "capo_mwaa_serverless.types.role_arn.RoleARN"
    """<p>The Amazon Resource Name (ARN) of the IAM role that Amazon Managed Workflows for Apache Airflow Serverless assumes when it executes the updated workflow.</p>"""
    description: NotRequired[
        "capo_mwaa_serverless.types.description_string.DescriptionString"
    ]
    """<p>An updated description for the workflow.</p>"""
    logging_configuration: NotRequired[
        "capo_mwaa_serverless.types.logging_configuration.LoggingConfiguration"
    ]
    """<p>Updated logging configuration for the workflow.</p>"""
    engine_version: NotRequired[
        "capo_mwaa_serverless.types.engine_version.EngineVersion"
    ]
    """<p>The version of the Amazon Managed Workflows for Apache Airflow Serverless engine that you want to use for the updated workflow.</p>"""
    network_configuration: NotRequired[
        "capo_mwaa_serverless.types.network_configuration.NetworkConfiguration"
    ]
    """<p>Updated network configuration for the workflow execution environment.</p>"""
    trigger_mode: NotRequired["capo_mwaa_serverless.types.generic_string.GenericString"]
    """<p>The trigger mode for the workflow execution.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateWorkflowRequest) -> dict:
    out: dict = {}
    out["WorkflowArn"] = value["workflow_arn"]
    import capo_mwaa_serverless.types.definition_s3_location

    out["DefinitionS3Location"] = (
        capo_mwaa_serverless.types.definition_s3_location.serialize_aws_json_1_0(
            value["definition_s3_location"]
        )
    )
    if "code" in value:
        import capo_mwaa_serverless.types.code

        out["Code"] = capo_mwaa_serverless.types.code.serialize_aws_json_1_0(
            value["code"]
        )
    out["RoleArn"] = value["role_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "logging_configuration" in value:
        import capo_mwaa_serverless.types.logging_configuration

        out["LoggingConfiguration"] = (
            capo_mwaa_serverless.types.logging_configuration.serialize_aws_json_1_0(
                value["logging_configuration"]
            )
        )
    if "engine_version" in value:
        import capo_mwaa_serverless.types.engine_version

        out["EngineVersion"] = (
            capo_mwaa_serverless.types.engine_version.serialize_aws_json_1_0(
                value["engine_version"]
            )
        )
    if "network_configuration" in value:
        import capo_mwaa_serverless.types.network_configuration

        out["NetworkConfiguration"] = (
            capo_mwaa_serverless.types.network_configuration.serialize_aws_json_1_0(
                value["network_configuration"]
            )
        )
    if "trigger_mode" in value:
        out["TriggerMode"] = value["trigger_mode"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateWorkflowRequest:
    out: UpdateWorkflowRequest = {}  # type: ignore[typeddict-item]
    if data.get("WorkflowArn") is not None:
        out["workflow_arn"] = data["WorkflowArn"]
    else:
        out["workflow_arn"] = ""
    if data.get("DefinitionS3Location") is not None:
        import capo_mwaa_serverless.types.definition_s3_location

        out["definition_s3_location"] = (
            capo_mwaa_serverless.types.definition_s3_location.deserialize_aws_json_1_0(
                data["DefinitionS3Location"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateWorkflowRequest.definition_s3_location required"
        )
    if data.get("Code") is not None:
        import capo_mwaa_serverless.types.code

        out["code"] = capo_mwaa_serverless.types.code.deserialize_aws_json_1_0(
            data["Code"]
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        out["role_arn"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("LoggingConfiguration") is not None:
        import capo_mwaa_serverless.types.logging_configuration

        out["logging_configuration"] = (
            capo_mwaa_serverless.types.logging_configuration.deserialize_aws_json_1_0(
                data["LoggingConfiguration"]
            )
        )
    if data.get("EngineVersion") is not None:
        import capo_mwaa_serverless.types.engine_version

        out["engine_version"] = (
            capo_mwaa_serverless.types.engine_version.deserialize_aws_json_1_0(
                data["EngineVersion"]
            )
        )
    if data.get("NetworkConfiguration") is not None:
        import capo_mwaa_serverless.types.network_configuration

        out["network_configuration"] = (
            capo_mwaa_serverless.types.network_configuration.deserialize_aws_json_1_0(
                data["NetworkConfiguration"]
            )
        )
    if data.get("TriggerMode") is not None:
        out["trigger_mode"] = data["TriggerMode"]
    return out
