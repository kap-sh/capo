"""Generated from Smithy shape ``com.amazonaws.proton#UpdateComponentInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.client_token
    import capo_proton.types.component_deployment_update_type
    import capo_proton.types.description
    import capo_proton.types.resource_name
    import capo_proton.types.resource_name_or_empty
    import capo_proton.types.spec_contents
    import capo_proton.types.template_file_contents


class UpdateComponentInput(TypedDict, closed=True):
    name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the component to update.</p>"""
    deployment_type: "capo_proton.types.component_deployment_update_type.ComponentDeploymentUpdateType"
    """<p>The deployment type. It defines the mode for updating a component, as follows:</p> <dl> <dt/> <dd> <p> <code>NONE</code> </p> <p>In this mode, a deployment <i>doesn't</i> occur. Only the requested metadata parameters are updated. You can only specify <code>description</code> in this mode.</p> </dd> <dt/> <dd> <p> <code>CURRENT_VERSION</code> </p> <p>In this mode, the component is deployed and updated with the new <code>serviceSpec</code>, <code>templateSource</code>, and/or <code>type</code> that you provide. Only requested parameters are updated.</p> </dd> </dl>"""
    description: NotRequired["capo_proton.types.description.Description"]
    """<p>An optional customer-provided description of the component.</p>"""
    service_name: NotRequired[
        "capo_proton.types.resource_name_or_empty.ResourceNameOrEmpty"
    ]
    """<p>The name of the service that <code>serviceInstanceName</code> is associated with. Don't specify to keep the component's current service instance attachment. Specify an empty string to detach the component from the service instance it's attached to. Specify non-empty values for both <code>serviceInstanceName</code> and <code>serviceName</code> or for neither of them.</p>"""
    service_instance_name: NotRequired[
        "capo_proton.types.resource_name_or_empty.ResourceNameOrEmpty"
    ]
    """<p>The name of the service instance that you want to attach this component to. Don't specify to keep the component's current service instance attachment. Specify an empty string to detach the component from the service instance it's attached to. Specify non-empty values for both <code>serviceInstanceName</code> and <code>serviceName</code> or for neither of them.</p>"""
    service_spec: NotRequired["capo_proton.types.spec_contents.SpecContents"]
    """<p>The service spec that you want the component to use to access service inputs. Set this only when the component is attached to a service instance.</p>"""
    template_file: NotRequired[
        "capo_proton.types.template_file_contents.TemplateFileContents"
    ]
    """<p>A path to the Infrastructure as Code (IaC) file describing infrastructure that a custom component provisions.</p> <note> <p>Components support a single IaC file, even if you use Terraform as your template language.</p> </note>"""
    client_token: NotRequired["capo_proton.types.client_token.ClientToken"]
    """<p>The client token for the updated component.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateComponentInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["deploymentType"] = value["deployment_type"]
    if "description" in value:
        out["description"] = value["description"]
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    if "service_instance_name" in value:
        out["serviceInstanceName"] = value["service_instance_name"]
    if "service_spec" in value:
        out["serviceSpec"] = value["service_spec"]
    if "template_file" in value:
        out["templateFile"] = value["template_file"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateComponentInput:
    out: UpdateComponentInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("deploymentType") is not None:
        out["deployment_type"] = data["deploymentType"]
    else:
        out["deployment_type"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    if data.get("serviceInstanceName") is not None:
        out["service_instance_name"] = data["serviceInstanceName"]
    if data.get("serviceSpec") is not None:
        out["service_spec"] = data["serviceSpec"]
    if data.get("templateFile") is not None:
        out["template_file"] = data["templateFile"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: UpdateComponentInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "service_spec" in value:
        out["service_spec"] = "*** Sensitive Data Redacted ***"
    if "template_file" in value:
        out["template_file"] = "*** Sensitive Data Redacted ***"
    return out
