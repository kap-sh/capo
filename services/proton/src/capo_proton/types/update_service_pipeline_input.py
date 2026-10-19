"""Generated from Smithy shape ``com.amazonaws.proton#UpdateServicePipelineInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.deployment_update_type
    import capo_proton.types.resource_name
    import capo_proton.types.spec_contents
    import capo_proton.types.template_version_part


class UpdateServicePipelineInput(TypedDict, closed=True):
    service_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the service to that the pipeline is associated with.</p>"""
    spec: "capo_proton.types.spec_contents.SpecContents"
    """<p>The spec for the service pipeline to update.</p>"""
    deployment_type: "capo_proton.types.deployment_update_type.DeploymentUpdateType"
    """<p>The deployment type.</p> <p>There are four modes for updating a service pipeline. The <code>deploymentType</code> field defines the mode.</p> <dl> <dt/> <dd> <p> <code>NONE</code> </p> <p>In this mode, a deployment <i>doesn't</i> occur. Only the requested metadata parameters are updated.</p> </dd> <dt/> <dd> <p> <code>CURRENT_VERSION</code> </p> <p>In this mode, the service pipeline is deployed and updated with the new spec that you provide. Only requested parameters are updated. <i>Don’t</i> include major or minor version parameters when you use this <code>deployment-type</code>.</p> </dd> <dt/> <dd> <p> <code>MINOR_VERSION</code> </p> <p>In this mode, the service pipeline is deployed and updated with the published, recommended (latest) minor version of the current major version in use, by default. You can specify a different minor version of the current major version in use.</p> </dd> <dt/> <dd> <p> <code>MAJOR_VERSION</code> </p> <p>In this mode, the service pipeline is deployed and updated with the published, recommended (latest) major and minor version of the current template, by default. You can specify a different major version that's higher than the major version in use and a minor version.</p> </dd> </dl>"""
    template_major_version: NotRequired[
        "capo_proton.types.template_version_part.TemplateVersionPart"
    ]
    """<p>The major version of the service template that was used to create the service that the pipeline is associated with.</p>"""
    template_minor_version: NotRequired[
        "capo_proton.types.template_version_part.TemplateVersionPart"
    ]
    """<p>The minor version of the service template that was used to create the service that the pipeline is associated with.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateServicePipelineInput) -> dict:
    out: dict = {}
    out["serviceName"] = value["service_name"]
    out["spec"] = value["spec"]
    out["deploymentType"] = value["deployment_type"]
    if "template_major_version" in value:
        out["templateMajorVersion"] = value["template_major_version"]
    if "template_minor_version" in value:
        out["templateMinorVersion"] = value["template_minor_version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateServicePipelineInput:
    out: UpdateServicePipelineInput = {}  # type: ignore[typeddict-item]
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    else:
        out["service_name"] = ""
    if data.get("spec") is not None:
        out["spec"] = data["spec"]
    else:
        out["spec"] = ""
    if data.get("deploymentType") is not None:
        out["deployment_type"] = data["deploymentType"]
    else:
        out["deployment_type"] = ""
    if data.get("templateMajorVersion") is not None:
        out["template_major_version"] = data["templateMajorVersion"]
    if data.get("templateMinorVersion") is not None:
        out["template_minor_version"] = data["templateMinorVersion"]
    return out


def redact_sensitive(value: UpdateServicePipelineInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "spec" in value:
        out["spec"] = "*** Sensitive Data Redacted ***"
    return out
