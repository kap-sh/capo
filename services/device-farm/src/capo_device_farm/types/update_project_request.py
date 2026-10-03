"""Generated from Smithy shape ``com.amazonaws.devicefarm#UpdateProjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_device_farm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_device_farm.types.amazon_resource_name
    import capo_device_farm.types.amazon_role_resource_name
    import capo_device_farm.types.environment_variables
    import capo_device_farm.types.job_timeout_minutes
    import capo_device_farm.types.name
    import capo_device_farm.types.vpc_config


class UpdateProjectRequest(TypedDict, closed=True):
    arn: "capo_device_farm.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the project whose name to update.</p>"""
    name: NotRequired["capo_device_farm.types.name.Name"]
    """<p>A string that represents the new name of the project that you are updating.</p>"""
    default_job_timeout_minutes: NotRequired[
        "capo_device_farm.types.job_timeout_minutes.JobTimeoutMinutes"
    ]
    """<p>The number of minutes a test run in the project executes before it times out.</p>"""
    vpc_config: NotRequired["capo_device_farm.types.vpc_config.VpcConfig"]
    """<p>The VPC security groups and subnets that are attached to a project.</p>"""
    environment_variables: NotRequired[
        "capo_device_farm.types.environment_variables.EnvironmentVariables"
    ]
    """<p> A set of environment variables which are used by default for all runs in the project. These environment variables are applied to the test run during the execution of a test spec file. </p> <p> For more information about using test spec files, please see <a href="https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environments.html">Custom test environments </a> in <i>AWS Device Farm.</i> </p>"""
    execution_role_arn: NotRequired[
        "capo_device_farm.types.amazon_role_resource_name.AmazonRoleResourceName"
    ]
    """<p>An IAM role to be assumed by the test host for all runs in the project.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateProjectRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "default_job_timeout_minutes" in value:
        out["defaultJobTimeoutMinutes"] = value["default_job_timeout_minutes"]
    if "vpc_config" in value:
        import capo_device_farm.types.vpc_config

        out["vpcConfig"] = capo_device_farm.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "environment_variables" in value:
        import capo_device_farm.types.environment_variables

        out["environmentVariables"] = (
            capo_device_farm.types.environment_variables.serialize_aws_json_1_1(
                value["environment_variables"]
            )
        )
    if "execution_role_arn" in value:
        out["executionRoleArn"] = value["execution_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateProjectRequest:
    out: UpdateProjectRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("UpdateProjectRequest.arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("defaultJobTimeoutMinutes") is not None:
        out["default_job_timeout_minutes"] = data["defaultJobTimeoutMinutes"]
    if data.get("vpcConfig") is not None:
        import capo_device_farm.types.vpc_config

        out["vpc_config"] = capo_device_farm.types.vpc_config.deserialize_aws_json_1_1(
            data["vpcConfig"]
        )
    if data.get("environmentVariables") is not None:
        import capo_device_farm.types.environment_variables

        out["environment_variables"] = (
            capo_device_farm.types.environment_variables.deserialize_aws_json_1_1(
                data["environmentVariables"]
            )
        )
    if data.get("executionRoleArn") is not None:
        out["execution_role_arn"] = data["executionRoleArn"]
    return out
