"""Generated from Smithy shape ``com.amazonaws.datazone#GetEnvironmentOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_datazone.types.aws_account_id
    import capo_datazone.types.aws_region
    import capo_datazone.types.custom_parameter_list
    import capo_datazone.types.deployment
    import capo_datazone.types.deployment_properties
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.environment_action_list
    import capo_datazone.types.environment_blueprint_id
    import capo_datazone.types.environment_configuration_id
    import capo_datazone.types.environment_configuration_name
    import capo_datazone.types.environment_id
    import capo_datazone.types.environment_name
    import capo_datazone.types.environment_profile_id
    import capo_datazone.types.environment_status
    import capo_datazone.types.glossary_terms
    import capo_datazone.types.project_id
    import capo_datazone.types.provisioning_properties
    import capo_datazone.types.resource_list


class GetEnvironmentOutput(TypedDict, closed=True):
    project_id: "capo_datazone.types.project_id.ProjectId"
    """<p>The ID of the Amazon DataZone project in which this environment is created.</p>"""
    id: NotRequired["capo_datazone.types.environment_id.EnvironmentId"]
    """<p>The ID of the environment.</p>"""
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain where the environment exists.</p>"""
    created_by: "str"
    """<p>The Amazon DataZone user who created the environment.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the environment was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when this environment was updated.</p>"""
    name: "capo_datazone.types.environment_name.EnvironmentName"
    """<p>The name of the environment.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of the environment.</p>"""
    environment_profile_id: (
        "capo_datazone.types.environment_profile_id.EnvironmentProfileId"
    )
    """<p>The ID of the environment profile with which the environment is created.</p>"""
    aws_account_id: NotRequired["capo_datazone.types.aws_account_id.AwsAccountId"]
    """<p>The ID of the Amazon Web Services account where the environment exists.</p>"""
    aws_account_region: NotRequired["capo_datazone.types.aws_region.AwsRegion"]
    """<p>The Amazon Web Services region where the environment exists.</p>"""
    provider: "str"
    """<p>The provider of this Amazon DataZone environment.</p>"""
    provisioned_resources: NotRequired["capo_datazone.types.resource_list.ResourceList"]
    """<p>The provisioned resources of this Amazon DataZone environment.</p>"""
    status: NotRequired["capo_datazone.types.environment_status.EnvironmentStatus"]
    """<p>The status of this Amazon DataZone environment.</p>"""
    environment_actions: NotRequired[
        "capo_datazone.types.environment_action_list.EnvironmentActionList"
    ]
    """<p>The actions of the environment.</p>"""
    glossary_terms: NotRequired["capo_datazone.types.glossary_terms.GlossaryTerms"]
    """<p>The business glossary terms that can be used in this environment.</p>"""
    user_parameters: NotRequired[
        "capo_datazone.types.custom_parameter_list.CustomParameterList"
    ]
    """<p>The user parameters of this Amazon DataZone environment.</p>"""
    last_deployment: NotRequired["capo_datazone.types.deployment.Deployment"]
    """<p>The details of the last deployment of the environment.</p>"""
    provisioning_properties: NotRequired[
        "capo_datazone.types.provisioning_properties.ProvisioningProperties"
    ]
    """<p>The provisioning properties of this Amazon DataZone environment.</p>"""
    deployment_properties: NotRequired[
        "capo_datazone.types.deployment_properties.DeploymentProperties"
    ]
    """<p>The deployment properties of the environment.</p>"""
    environment_blueprint_id: NotRequired[
        "capo_datazone.types.environment_blueprint_id.EnvironmentBlueprintId"
    ]
    """<p>The blueprint with which the environment is created.</p>"""
    environment_configuration_id: NotRequired[
        "capo_datazone.types.environment_configuration_id.EnvironmentConfigurationId"
    ]
    """<p>The configuration ID that is used to create the environment.</p>"""
    environment_configuration_name: NotRequired[
        "capo_datazone.types.environment_configuration_name.EnvironmentConfigurationName"
    ]
    """<p>The configuration name that is used to create the environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEnvironmentOutput) -> dict:
    out: dict = {}
    out["projectId"] = value["project_id"]
    if "id" in value:
        out["id"] = value["id"]
    out["domainId"] = value["domain_id"]
    out["createdBy"] = value["created_by"]
    if "created_at" in value:
        import capo_datazone._protocol.serialize

        out["createdAt"] = capo_datazone._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_datazone._protocol.serialize

        out["updatedAt"] = capo_datazone._protocol.serialize.fmt_date_time(
            value["updated_at"]
        )
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["environmentProfileId"] = value.get("environment_profile_id", "")
    if "aws_account_id" in value:
        out["awsAccountId"] = value["aws_account_id"]
    if "aws_account_region" in value:
        out["awsAccountRegion"] = value["aws_account_region"]
    out["provider"] = value["provider"]
    if "provisioned_resources" in value:
        import capo_datazone.types.resource_list

        out["provisionedResources"] = capo_datazone.types.resource_list.serialize_json(
            value["provisioned_resources"]
        )
    if "status" in value:
        import capo_datazone.types.environment_status

        out["status"] = capo_datazone.types.environment_status.serialize_json(
            value["status"]
        )
    if "environment_actions" in value:
        import capo_datazone.types.environment_action_list

        out["environmentActions"] = (
            capo_datazone.types.environment_action_list.serialize_json(
                value["environment_actions"]
            )
        )
    if "glossary_terms" in value:
        import capo_datazone.types.glossary_terms

        out["glossaryTerms"] = capo_datazone.types.glossary_terms.serialize_json(
            value["glossary_terms"]
        )
    if "user_parameters" in value:
        import capo_datazone.types.custom_parameter_list

        out["userParameters"] = (
            capo_datazone.types.custom_parameter_list.serialize_json(
                value["user_parameters"]
            )
        )
    if "last_deployment" in value:
        import capo_datazone.types.deployment

        out["lastDeployment"] = capo_datazone.types.deployment.serialize_json(
            value["last_deployment"]
        )
    if "provisioning_properties" in value:
        import capo_datazone.types.provisioning_properties

        out["provisioningProperties"] = (
            capo_datazone.types.provisioning_properties.serialize_json(
                value["provisioning_properties"]
            )
        )
    if "deployment_properties" in value:
        import capo_datazone.types.deployment_properties

        out["deploymentProperties"] = (
            capo_datazone.types.deployment_properties.serialize_json(
                value["deployment_properties"]
            )
        )
    if "environment_blueprint_id" in value:
        out["environmentBlueprintId"] = value["environment_blueprint_id"]
    if "environment_configuration_id" in value:
        out["environmentConfigurationId"] = value["environment_configuration_id"]
    if "environment_configuration_name" in value:
        out["environmentConfigurationName"] = value["environment_configuration_name"]
    return out


def deserialize_json(data: dict) -> GetEnvironmentOutput:
    out: GetEnvironmentOutput = {}  # type: ignore[typeddict-item]
    if data.get("projectId") is not None:
        out["project_id"] = data["projectId"]
    else:
        out["project_id"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        out["created_by"] = ""
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("environmentProfileId") is not None:
        out["environment_profile_id"] = data["environmentProfileId"]
    else:
        out["environment_profile_id"] = ""
    if data.get("awsAccountId") is not None:
        out["aws_account_id"] = data["awsAccountId"]
    if data.get("awsAccountRegion") is not None:
        out["aws_account_region"] = data["awsAccountRegion"]
    if data.get("provider") is not None:
        out["provider"] = data["provider"]
    else:
        out["provider"] = ""
    if data.get("provisionedResources") is not None:
        import capo_datazone.types.resource_list

        out["provisioned_resources"] = (
            capo_datazone.types.resource_list.deserialize_json(
                data["provisionedResources"]
            )
        )
    if data.get("status") is not None:
        import capo_datazone.types.environment_status

        out["status"] = capo_datazone.types.environment_status.deserialize_json(
            data["status"]
        )
    if data.get("environmentActions") is not None:
        import capo_datazone.types.environment_action_list

        out["environment_actions"] = (
            capo_datazone.types.environment_action_list.deserialize_json(
                data["environmentActions"]
            )
        )
    if data.get("glossaryTerms") is not None:
        import capo_datazone.types.glossary_terms

        out["glossary_terms"] = capo_datazone.types.glossary_terms.deserialize_json(
            data["glossaryTerms"]
        )
    if data.get("userParameters") is not None:
        import capo_datazone.types.custom_parameter_list

        out["user_parameters"] = (
            capo_datazone.types.custom_parameter_list.deserialize_json(
                data["userParameters"]
            )
        )
    if data.get("lastDeployment") is not None:
        import capo_datazone.types.deployment

        out["last_deployment"] = capo_datazone.types.deployment.deserialize_json(
            data["lastDeployment"]
        )
    if data.get("provisioningProperties") is not None:
        import capo_datazone.types.provisioning_properties

        out["provisioning_properties"] = (
            capo_datazone.types.provisioning_properties.deserialize_json(
                data["provisioningProperties"]
            )
        )
    if data.get("deploymentProperties") is not None:
        import capo_datazone.types.deployment_properties

        out["deployment_properties"] = (
            capo_datazone.types.deployment_properties.deserialize_json(
                data["deploymentProperties"]
            )
        )
    if data.get("environmentBlueprintId") is not None:
        out["environment_blueprint_id"] = data["environmentBlueprintId"]
    if data.get("environmentConfigurationId") is not None:
        out["environment_configuration_id"] = data["environmentConfigurationId"]
    if data.get("environmentConfigurationName") is not None:
        out["environment_configuration_name"] = data["environmentConfigurationName"]
    return out


def redact_sensitive(value: GetEnvironmentOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "user_parameters" in value:
        import capo_datazone.types.custom_parameter_list

        out["user_parameters"] = (
            capo_datazone.types.custom_parameter_list.redact_sensitive(
                value["user_parameters"]
            )
        )
    if "environment_configuration_id" in value:
        out["environment_configuration_id"] = "*** Sensitive Data Redacted ***"
    if "environment_configuration_name" in value:
        out["environment_configuration_name"] = "*** Sensitive Data Redacted ***"
    return out
