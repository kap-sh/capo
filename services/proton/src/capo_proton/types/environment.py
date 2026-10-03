"""Generated from Smithy shape ``com.amazonaws.proton#Environment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_proton.types.arn
    import capo_proton.types.aws_account_id
    import capo_proton.types.deployment_id
    import capo_proton.types.deployment_status
    import capo_proton.types.description
    import capo_proton.types.environment_account_connection_id
    import capo_proton.types.environment_arn
    import capo_proton.types.provisioning
    import capo_proton.types.repository_branch
    import capo_proton.types.resource_name
    import capo_proton.types.role_arn
    import capo_proton.types.spec_contents
    import capo_proton.types.status_message
    import capo_proton.types.template_version_part


class Environment(TypedDict, closed=True):
    name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the environment.</p>"""
    description: NotRequired["capo_proton.types.description.Description"]
    """<p>The description of the environment.</p>"""
    created_at: "datetime.datetime"
    """<p>The time when the environment was created.</p>"""
    last_deployment_attempted_at: "datetime.datetime"
    """<p>The time when a deployment of the environment was last attempted.</p>"""
    last_deployment_succeeded_at: "datetime.datetime"
    """<p>The time when the environment was last deployed successfully.</p>"""
    arn: "capo_proton.types.environment_arn.EnvironmentArn"
    """<p>The Amazon Resource Name (ARN) of the environment.</p>"""
    template_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The Amazon Resource Name (ARN) of the environment template.</p>"""
    template_major_version: (
        "capo_proton.types.template_version_part.TemplateVersionPart"
    )
    """<p>The major version of the environment template.</p>"""
    template_minor_version: (
        "capo_proton.types.template_version_part.TemplateVersionPart"
    )
    """<p>The minor version of the environment template.</p>"""
    deployment_status: "capo_proton.types.deployment_status.DeploymentStatus"
    """<p>The environment deployment status.</p>"""
    deployment_status_message: NotRequired[
        "capo_proton.types.status_message.StatusMessage"
    ]
    """<p>An environment deployment status message.</p>"""
    proton_service_role_arn: NotRequired["capo_proton.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the Proton service role that allows Proton to make calls to other services on your behalf.</p>"""
    environment_account_connection_id: NotRequired[
        "capo_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId"
    ]
    """<p>The ID of the environment account connection that's used to provision infrastructure resources in an environment account.</p>"""
    environment_account_id: NotRequired["capo_proton.types.aws_account_id.AwsAccountId"]
    """<p>The ID of the environment account that the environment infrastructure resources are provisioned in.</p>"""
    spec: NotRequired["capo_proton.types.spec_contents.SpecContents"]
    """<p>The environment spec.</p>"""
    provisioning: NotRequired["capo_proton.types.provisioning.Provisioning"]
    """<p>When included, indicates that the environment template is for customer provisioned and managed infrastructure.</p>"""
    provisioning_repository: NotRequired[
        "capo_proton.types.repository_branch.RepositoryBranch"
    ]
    """<p>The linked repository that you use to host your rendered infrastructure templates for self-managed provisioning. A linked repository is a repository that has been registered with Proton. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/APIReference/API_CreateRepository.html">CreateRepository</a>.</p>"""
    component_role_arn: NotRequired["capo_proton.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM service role that Proton uses when provisioning directly defined components in this environment. It determines the scope of infrastructure that a component can provision.</p> <p>The environment must have a <code>componentRoleArn</code> to allow directly defined components to be associated with the environment.</p> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>"""
    codebuild_role_arn: NotRequired["capo_proton.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM service role that allows Proton to provision infrastructure using CodeBuild-based provisioning on your behalf.</p>"""
    last_attempted_deployment_id: NotRequired[
        "capo_proton.types.deployment_id.DeploymentId"
    ]
    """<p>The ID of the last attempted deployment of this environment.</p>"""
    last_succeeded_deployment_id: NotRequired[
        "capo_proton.types.deployment_id.DeploymentId"
    ]
    """<p>The ID of the last successful deployment of this environment.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Environment) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_proton.types._prelude.timestamp

    out["createdAt"] = capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
        value["created_at"]
    )
    import capo_proton.types._prelude.timestamp

    out["lastDeploymentAttemptedAt"] = (
        capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
            value["last_deployment_attempted_at"]
        )
    )
    import capo_proton.types._prelude.timestamp

    out["lastDeploymentSucceededAt"] = (
        capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
            value["last_deployment_succeeded_at"]
        )
    )
    out["arn"] = value["arn"]
    out["templateName"] = value["template_name"]
    out["templateMajorVersion"] = value["template_major_version"]
    out["templateMinorVersion"] = value["template_minor_version"]
    out["deploymentStatus"] = value["deployment_status"]
    if "deployment_status_message" in value:
        out["deploymentStatusMessage"] = value["deployment_status_message"]
    if "proton_service_role_arn" in value:
        out["protonServiceRoleArn"] = value["proton_service_role_arn"]
    if "environment_account_connection_id" in value:
        out["environmentAccountConnectionId"] = value[
            "environment_account_connection_id"
        ]
    if "environment_account_id" in value:
        out["environmentAccountId"] = value["environment_account_id"]
    if "spec" in value:
        out["spec"] = value["spec"]
    if "provisioning" in value:
        out["provisioning"] = value["provisioning"]
    if "provisioning_repository" in value:
        import capo_proton.types.repository_branch

        out["provisioningRepository"] = (
            capo_proton.types.repository_branch.serialize_aws_json_1_0(
                value["provisioning_repository"]
            )
        )
    if "component_role_arn" in value:
        out["componentRoleArn"] = value["component_role_arn"]
    if "codebuild_role_arn" in value:
        out["codebuildRoleArn"] = value["codebuild_role_arn"]
    if "last_attempted_deployment_id" in value:
        out["lastAttemptedDeploymentId"] = value["last_attempted_deployment_id"]
    if "last_succeeded_deployment_id" in value:
        out["lastSucceededDeploymentId"] = value["last_succeeded_deployment_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Environment:
    out: Environment = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Environment.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("createdAt") is not None:
        import capo_proton.types._prelude.timestamp

        out["created_at"] = (
            capo_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("Environment.created_at required")
    if data.get("lastDeploymentAttemptedAt") is not None:
        import capo_proton.types._prelude.timestamp

        out["last_deployment_attempted_at"] = (
            capo_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["lastDeploymentAttemptedAt"]
            )
        )
    else:
        raise DeserializationError("Environment.last_deployment_attempted_at required")
    if data.get("lastDeploymentSucceededAt") is not None:
        import capo_proton.types._prelude.timestamp

        out["last_deployment_succeeded_at"] = (
            capo_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["lastDeploymentSucceededAt"]
            )
        )
    else:
        raise DeserializationError("Environment.last_deployment_succeeded_at required")
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("Environment.arn required")
    if data.get("templateName") is not None:
        out["template_name"] = data["templateName"]
    else:
        raise DeserializationError("Environment.template_name required")
    if data.get("templateMajorVersion") is not None:
        out["template_major_version"] = data["templateMajorVersion"]
    else:
        raise DeserializationError("Environment.template_major_version required")
    if data.get("templateMinorVersion") is not None:
        out["template_minor_version"] = data["templateMinorVersion"]
    else:
        raise DeserializationError("Environment.template_minor_version required")
    if data.get("deploymentStatus") is not None:
        out["deployment_status"] = data["deploymentStatus"]
    else:
        raise DeserializationError("Environment.deployment_status required")
    if data.get("deploymentStatusMessage") is not None:
        out["deployment_status_message"] = data["deploymentStatusMessage"]
    if data.get("protonServiceRoleArn") is not None:
        out["proton_service_role_arn"] = data["protonServiceRoleArn"]
    if data.get("environmentAccountConnectionId") is not None:
        out["environment_account_connection_id"] = data[
            "environmentAccountConnectionId"
        ]
    if data.get("environmentAccountId") is not None:
        out["environment_account_id"] = data["environmentAccountId"]
    if data.get("spec") is not None:
        out["spec"] = data["spec"]
    if data.get("provisioning") is not None:
        out["provisioning"] = data["provisioning"]
    if data.get("provisioningRepository") is not None:
        import capo_proton.types.repository_branch

        out["provisioning_repository"] = (
            capo_proton.types.repository_branch.deserialize_aws_json_1_0(
                data["provisioningRepository"]
            )
        )
    if data.get("componentRoleArn") is not None:
        out["component_role_arn"] = data["componentRoleArn"]
    if data.get("codebuildRoleArn") is not None:
        out["codebuild_role_arn"] = data["codebuildRoleArn"]
    if data.get("lastAttemptedDeploymentId") is not None:
        out["last_attempted_deployment_id"] = data["lastAttemptedDeploymentId"]
    if data.get("lastSucceededDeploymentId") is not None:
        out["last_succeeded_deployment_id"] = data["lastSucceededDeploymentId"]
    return out
