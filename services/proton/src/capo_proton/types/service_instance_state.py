"""Generated from Smithy shape ``com.amazonaws.proton#ServiceInstanceState``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.component_deployment_id_list
    import capo_proton.types.deployment_id
    import capo_proton.types.resource_name
    import capo_proton.types.spec_contents
    import capo_proton.types.template_version_part


class ServiceInstanceState(TypedDict, closed=True):
    spec: "capo_proton.types.spec_contents.SpecContents"
    """<p>The service spec that was used to create the service instance.</p>"""
    template_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the service template that was used to create the service instance.</p>"""
    template_major_version: (
        "capo_proton.types.template_version_part.TemplateVersionPart"
    )
    """<p>The major version of the service template that was used to create the service pipeline.</p>"""
    template_minor_version: (
        "capo_proton.types.template_version_part.TemplateVersionPart"
    )
    """<p>The minor version of the service template that was used to create the service pipeline.</p>"""
    last_successful_component_deployment_ids: NotRequired[
        "capo_proton.types.component_deployment_id_list.ComponentDeploymentIdList"
    ]
    """<p>The IDs for the last successful components deployed for this service instance.</p>"""
    last_successful_environment_deployment_id: NotRequired[
        "capo_proton.types.deployment_id.DeploymentId"
    ]
    """<p>The ID for the last successful environment deployed for this service instance.</p>"""
    last_successful_service_pipeline_deployment_id: NotRequired[
        "capo_proton.types.deployment_id.DeploymentId"
    ]
    """<p>The ID for the last successful service pipeline deployed for this service instance.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceInstanceState) -> dict:
    out: dict = {}
    out["spec"] = value["spec"]
    out["templateName"] = value["template_name"]
    out["templateMajorVersion"] = value["template_major_version"]
    out["templateMinorVersion"] = value["template_minor_version"]
    if "last_successful_component_deployment_ids" in value:
        import capo_proton.types.component_deployment_id_list

        out["lastSuccessfulComponentDeploymentIds"] = (
            capo_proton.types.component_deployment_id_list.serialize_aws_json_1_0(
                value["last_successful_component_deployment_ids"]
            )
        )
    if "last_successful_environment_deployment_id" in value:
        out["lastSuccessfulEnvironmentDeploymentId"] = value[
            "last_successful_environment_deployment_id"
        ]
    if "last_successful_service_pipeline_deployment_id" in value:
        out["lastSuccessfulServicePipelineDeploymentId"] = value[
            "last_successful_service_pipeline_deployment_id"
        ]
    return out


def deserialize_aws_json_1_0(data: dict) -> ServiceInstanceState:
    out: ServiceInstanceState = {}  # type: ignore[typeddict-item]
    if data.get("spec") is not None:
        out["spec"] = data["spec"]
    else:
        out["spec"] = ""
    if data.get("templateName") is not None:
        out["template_name"] = data["templateName"]
    else:
        out["template_name"] = ""
    if data.get("templateMajorVersion") is not None:
        out["template_major_version"] = data["templateMajorVersion"]
    else:
        out["template_major_version"] = ""
    if data.get("templateMinorVersion") is not None:
        out["template_minor_version"] = data["templateMinorVersion"]
    else:
        out["template_minor_version"] = ""
    if data.get("lastSuccessfulComponentDeploymentIds") is not None:
        import capo_proton.types.component_deployment_id_list

        out["last_successful_component_deployment_ids"] = (
            capo_proton.types.component_deployment_id_list.deserialize_aws_json_1_0(
                data["lastSuccessfulComponentDeploymentIds"]
            )
        )
    if data.get("lastSuccessfulEnvironmentDeploymentId") is not None:
        out["last_successful_environment_deployment_id"] = data[
            "lastSuccessfulEnvironmentDeploymentId"
        ]
    if data.get("lastSuccessfulServicePipelineDeploymentId") is not None:
        out["last_successful_service_pipeline_deployment_id"] = data[
            "lastSuccessfulServicePipelineDeploymentId"
        ]
    return out


def redact_sensitive(value: ServiceInstanceState) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "spec" in value:
        out["spec"] = "*** Sensitive Data Redacted ***"
    return out
