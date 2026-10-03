"""Generated from Smithy shape ``com.amazonaws.proton#CreateComponentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.client_token
    import capo_proton.types.description
    import capo_proton.types.resource_name
    import capo_proton.types.spec_contents
    import capo_proton.types.tag_list
    import capo_proton.types.template_file_contents
    import capo_proton.types.template_manifest_contents


class CreateComponentInput(TypedDict, closed=True):
    name: "capo_proton.types.resource_name.ResourceName"
    """<p>The customer-provided name of the component.</p>"""
    description: NotRequired["capo_proton.types.description.Description"]
    """<p>An optional customer-provided description of the component.</p>"""
    service_name: NotRequired["capo_proton.types.resource_name.ResourceName"]
    """<p>The name of the service that <code>serviceInstanceName</code> is associated with. If you don't specify this, the component isn't attached to any service instance. Specify both <code>serviceInstanceName</code> and <code>serviceName</code> or neither of them.</p>"""
    service_instance_name: NotRequired["capo_proton.types.resource_name.ResourceName"]
    """<p>The name of the service instance that you want to attach this component to. If you don't specify this, the component isn't attached to any service instance. Specify both <code>serviceInstanceName</code> and <code>serviceName</code> or neither of them.</p>"""
    environment_name: NotRequired["capo_proton.types.resource_name.ResourceName"]
    """<p>The name of the Proton environment that you want to associate this component with. You must specify this when you don't specify <code>serviceInstanceName</code> and <code>serviceName</code>.</p>"""
    template_file: "capo_proton.types.template_file_contents.TemplateFileContents"
    """<p>A path to the Infrastructure as Code (IaC) file describing infrastructure that a custom component provisions.</p> <note> <p>Components support a single IaC file, even if you use Terraform as your template language.</p> </note>"""
    manifest: "capo_proton.types.template_manifest_contents.TemplateManifestContents"
    """<p>A path to a manifest file that lists the Infrastructure as Code (IaC) file, template language, and rendering engine for infrastructure that a custom component provisions.</p>"""
    service_spec: NotRequired["capo_proton.types.spec_contents.SpecContents"]
    """<p>The service spec that you want the component to use to access service inputs. Set this only when you attach the component to a service instance.</p>"""
    tags: NotRequired["capo_proton.types.tag_list.TagList"]
    """<p>An optional list of metadata items that you can associate with the Proton component. A tag is a key-value pair.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>"""
    client_token: NotRequired["capo_proton.types.client_token.ClientToken"]
    """<p>The client token for the created component.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateComponentInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    if "service_instance_name" in value:
        out["serviceInstanceName"] = value["service_instance_name"]
    if "environment_name" in value:
        out["environmentName"] = value["environment_name"]
    out["templateFile"] = value["template_file"]
    out["manifest"] = value["manifest"]
    if "service_spec" in value:
        out["serviceSpec"] = value["service_spec"]
    if "tags" in value:
        import capo_proton.types.tag_list

        out["tags"] = capo_proton.types.tag_list.serialize_aws_json_1_0(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateComponentInput:
    out: CreateComponentInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateComponentInput.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    if data.get("serviceInstanceName") is not None:
        out["service_instance_name"] = data["serviceInstanceName"]
    if data.get("environmentName") is not None:
        out["environment_name"] = data["environmentName"]
    if data.get("templateFile") is not None:
        out["template_file"] = data["templateFile"]
    else:
        raise DeserializationError("CreateComponentInput.template_file required")
    if data.get("manifest") is not None:
        out["manifest"] = data["manifest"]
    else:
        raise DeserializationError("CreateComponentInput.manifest required")
    if data.get("serviceSpec") is not None:
        out["service_spec"] = data["serviceSpec"]
    if data.get("tags") is not None:
        import capo_proton.types.tag_list

        out["tags"] = capo_proton.types.tag_list.deserialize_aws_json_1_0(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
