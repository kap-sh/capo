"""Generated from Smithy shape ``com.amazonaws.proton#CreateServiceInstanceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.client_token
    import capo_proton.types.resource_name
    import capo_proton.types.spec_contents
    import capo_proton.types.tag_list
    import capo_proton.types.template_version_part


class CreateServiceInstanceInput(TypedDict, closed=True):
    name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the service instance to create.</p>"""
    service_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the service the service instance is added to.</p>"""
    spec: "capo_proton.types.spec_contents.SpecContents"
    """<p>The spec for the service instance you want to create.</p>"""
    template_major_version: NotRequired[
        "capo_proton.types.template_version_part.TemplateVersionPart"
    ]
    """<p>To create a new major and minor version of the service template, <i>exclude</i> <code>major Version</code>.</p>"""
    template_minor_version: NotRequired[
        "capo_proton.types.template_version_part.TemplateVersionPart"
    ]
    """<p>To create a new minor version of the service template, include a <code>major Version</code>.</p>"""
    tags: NotRequired["capo_proton.types.tag_list.TagList"]
    """<p>An optional list of metadata items that you can associate with the Proton service instance. A tag is a key-value pair.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>"""
    client_token: NotRequired["capo_proton.types.client_token.ClientToken"]
    """<p>The client token of the service instance to create.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateServiceInstanceInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["serviceName"] = value["service_name"]
    out["spec"] = value["spec"]
    if "template_major_version" in value:
        out["templateMajorVersion"] = value["template_major_version"]
    if "template_minor_version" in value:
        out["templateMinorVersion"] = value["template_minor_version"]
    if "tags" in value:
        import capo_proton.types.tag_list

        out["tags"] = capo_proton.types.tag_list.serialize_aws_json_1_0(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateServiceInstanceInput:
    out: CreateServiceInstanceInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateServiceInstanceInput.name required")
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    else:
        raise DeserializationError("CreateServiceInstanceInput.service_name required")
    if data.get("spec") is not None:
        out["spec"] = data["spec"]
    else:
        raise DeserializationError("CreateServiceInstanceInput.spec required")
    if data.get("templateMajorVersion") is not None:
        out["template_major_version"] = data["templateMajorVersion"]
    if data.get("templateMinorVersion") is not None:
        out["template_minor_version"] = data["templateMinorVersion"]
    if data.get("tags") is not None:
        import capo_proton.types.tag_list

        out["tags"] = capo_proton.types.tag_list.deserialize_aws_json_1_0(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
