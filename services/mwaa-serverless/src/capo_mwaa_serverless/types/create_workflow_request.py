"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#CreateWorkflowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mwaa_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.code
    import capo_mwaa_serverless.types.definition_s3_location
    import capo_mwaa_serverless.types.description_string
    import capo_mwaa_serverless.types.encryption_configuration
    import capo_mwaa_serverless.types.engine_version
    import capo_mwaa_serverless.types.generic_string
    import capo_mwaa_serverless.types.idempotency_token_string
    import capo_mwaa_serverless.types.logging_configuration
    import capo_mwaa_serverless.types.name_string
    import capo_mwaa_serverless.types.network_configuration
    import capo_mwaa_serverless.types.role_arn
    import capo_mwaa_serverless.types.tags


class CreateWorkflowRequest(TypedDict, closed=True):
    name: "capo_mwaa_serverless.types.name_string.NameString"
    """<p>The name of the workflow. You must use unique workflow names within your Amazon Web Services account. The service generates a unique identifier that is appended to ensure temporal uniqueness across the account lifecycle.</p>"""
    client_token: NotRequired[
        "capo_mwaa_serverless.types.idempotency_token_string.IdempotencyTokenString"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This token prevents duplicate workflow creation requests.</p>"""
    definition_s3_location: (
        "capo_mwaa_serverless.types.definition_s3_location.DefinitionS3Location"
    )
    """<p>The Amazon S3 location where the workflow definition file is stored. This must point to a valid YAML file that defines the workflow structure using supported Amazon Web Services operators and tasks. Amazon Managed Workflows for Apache Airflow Serverless takes a snapshot of the definition at creation time, so subsequent changes to the Amazon S3 object will not affect the workflow unless you create a new version. In your YAML definition, include task dependencies, scheduling information, and operator configurations that are compatible with the Amazon Managed Workflows for Apache Airflow Serverless execution environment.</p>"""
    code: NotRequired["capo_mwaa_serverless.types.code.Code"]
    """<p>The location of code artifacts in Amazon S3 for the workflow. The service copies the code from this location at the time of the request.</p>"""
    role_arn: "capo_mwaa_serverless.types.role_arn.RoleARN"
    """<p>The Amazon Resource Name (ARN) of the IAM role that Amazon Managed Workflows for Apache Airflow Serverless assumes when executing the workflow. This role must have the necessary permissions to access the required Amazon Web Services services and resources that your workflow tasks will interact with. The role is used for task execution in the isolated, multi-tenant environment and should follow the principle of least privilege. Amazon Managed Workflows for Apache Airflow Serverless validates role access during workflow creation but runtime permission checks are performed by the target services.</p>"""
    description: NotRequired[
        "capo_mwaa_serverless.types.description_string.DescriptionString"
    ]
    """<p>An optional description of the workflow that you can use to provide additional context about the workflow's purpose and functionality.</p>"""
    encryption_configuration: NotRequired[
        "capo_mwaa_serverless.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>The configuration for encrypting workflow data at rest and in transit. Specifies the encryption type and optional KMS key for customer-managed encryption.</p>"""
    logging_configuration: NotRequired[
        "capo_mwaa_serverless.types.logging_configuration.LoggingConfiguration"
    ]
    """<p>The configuration for workflow logging. Specifies the CloudWatch log group where workflow execution logs are stored. Amazon Managed Workflows for Apache Airflow Serverless automatically exports worker logs and task-level information to the specified log group in your account using remote logging functionality. This provides comprehensive observability for debugging and monitoring workflow execution across the distributed, serverless environment.</p>"""
    engine_version: NotRequired[
        "capo_mwaa_serverless.types.engine_version.EngineVersion"
    ]
    """<p>The version of the Amazon Managed Workflows for Apache Airflow Serverless engine that you want to use for this workflow. This determines the feature set, supported operators, and execution environment capabilities available to your workflow. Amazon Managed Workflows for Apache Airflow Serverless maintains backward compatibility across versions while introducing new features and improvements. Currently supports version 1 with plans for additional versions as the service evolves.</p>"""
    network_configuration: NotRequired[
        "capo_mwaa_serverless.types.network_configuration.NetworkConfiguration"
    ]
    """<p>Network configuration for the workflow execution environment, including VPC security groups and subnets for secure network access. When specified, Amazon Managed Workflows for Apache Airflow Serverless deploys ECS worker tasks in your customer VPC to provide secure connectivity to your resources. If not specified, tasks run in the service's default worker VPC with network isolation from other customers. This configuration enables secure access to VPC-only resources like RDS databases or private endpoints.</p>"""
    tags: NotRequired["capo_mwaa_serverless.types.tags.Tags"]
    """<p>A map of tags to assign to the workflow resource. Tags are key-value pairs that are used for resource organization and cost allocation.</p>"""
    trigger_mode: NotRequired["capo_mwaa_serverless.types.generic_string.GenericString"]
    """<p>The trigger mode for the workflow execution.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateWorkflowRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
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
    if "encryption_configuration" in value:
        import capo_mwaa_serverless.types.encryption_configuration

        out["EncryptionConfiguration"] = (
            capo_mwaa_serverless.types.encryption_configuration.serialize_aws_json_1_0(
                value["encryption_configuration"]
            )
        )
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
    if "tags" in value:
        import capo_mwaa_serverless.types.tags

        out["Tags"] = capo_mwaa_serverless.types.tags.serialize_aws_json_1_0(
            value["tags"]
        )
    if "trigger_mode" in value:
        out["TriggerMode"] = value["trigger_mode"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateWorkflowRequest:
    out: CreateWorkflowRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("DefinitionS3Location") is not None:
        import capo_mwaa_serverless.types.definition_s3_location

        out["definition_s3_location"] = (
            capo_mwaa_serverless.types.definition_s3_location.deserialize_aws_json_1_0(
                data["DefinitionS3Location"]
            )
        )
    else:
        raise DeserializationError(
            "CreateWorkflowRequest.definition_s3_location required"
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
    if data.get("EncryptionConfiguration") is not None:
        import capo_mwaa_serverless.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_mwaa_serverless.types.encryption_configuration.deserialize_aws_json_1_0(
                data["EncryptionConfiguration"]
            )
        )
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
    if data.get("Tags") is not None:
        import capo_mwaa_serverless.types.tags

        out["tags"] = capo_mwaa_serverless.types.tags.deserialize_aws_json_1_0(
            data["Tags"]
        )
    if data.get("TriggerMode") is not None:
        out["trigger_mode"] = data["TriggerMode"]
    return out
