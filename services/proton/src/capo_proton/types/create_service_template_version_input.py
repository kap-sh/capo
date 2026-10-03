"""Generated from Smithy shape ``com.amazonaws.proton#CreateServiceTemplateVersionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.client_token
    import capo_proton.types.compatible_environment_template_input_list
    import capo_proton.types.description
    import capo_proton.types.resource_name
    import capo_proton.types.service_template_supported_component_source_input_list
    import capo_proton.types.tag_list
    import capo_proton.types.template_version_part
    import capo_proton.types.template_version_source_input


class CreateServiceTemplateVersionInput(TypedDict, closed=True):
    client_token: NotRequired["capo_proton.types.client_token.ClientToken"]
    """<p>When included, if two identical requests are made with the same client token, Proton returns the service template version that the first request created.</p>"""
    template_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the service template.</p>"""
    description: NotRequired["capo_proton.types.description.Description"]
    """<p>A description of the new version of a service template.</p>"""
    major_version: NotRequired[
        "capo_proton.types.template_version_part.TemplateVersionPart"
    ]
    """<p>To create a new minor version of the service template, include a <code>major Version</code>.</p> <p>To create a new major and minor version of the service template, <i>exclude</i> <code>major Version</code>.</p>"""
    source: "capo_proton.types.template_version_source_input.TemplateVersionSourceInput"
    """<p>An object that includes the template bundle S3 bucket path and name for the new version of a service template.</p>"""
    compatible_environment_templates: "capo_proton.types.compatible_environment_template_input_list.CompatibleEnvironmentTemplateInputList"
    """<p>An array of environment template objects that are compatible with the new service template version. A service instance based on this service template version can run in environments based on compatible templates.</p>"""
    tags: NotRequired["capo_proton.types.tag_list.TagList"]
    """<p>An optional list of metadata items that you can associate with the Proton service template version. A tag is a key-value pair.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>"""
    supported_component_sources: NotRequired[
        "capo_proton.types.service_template_supported_component_source_input_list.ServiceTemplateSupportedComponentSourceInputList"
    ]
    """<p>An array of supported component sources. Components with supported sources can be attached to service instances based on this service template version.</p> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateServiceTemplateVersionInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["templateName"] = value["template_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "major_version" in value:
        out["majorVersion"] = value["major_version"]
    import capo_proton.types.template_version_source_input

    out["source"] = (
        capo_proton.types.template_version_source_input.serialize_aws_json_1_0(
            value["source"]
        )
    )
    import capo_proton.types.compatible_environment_template_input_list

    out["compatibleEnvironmentTemplates"] = (
        capo_proton.types.compatible_environment_template_input_list.serialize_aws_json_1_0(
            value["compatible_environment_templates"]
        )
    )
    if "tags" in value:
        import capo_proton.types.tag_list

        out["tags"] = capo_proton.types.tag_list.serialize_aws_json_1_0(value["tags"])
    if "supported_component_sources" in value:
        import capo_proton.types.service_template_supported_component_source_input_list

        out["supportedComponentSources"] = (
            capo_proton.types.service_template_supported_component_source_input_list.serialize_aws_json_1_0(
                value["supported_component_sources"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateServiceTemplateVersionInput:
    out: CreateServiceTemplateVersionInput = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("templateName") is not None:
        out["template_name"] = data["templateName"]
    else:
        raise DeserializationError(
            "CreateServiceTemplateVersionInput.template_name required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("majorVersion") is not None:
        out["major_version"] = data["majorVersion"]
    if data.get("source") is not None:
        import capo_proton.types.template_version_source_input

        out["source"] = (
            capo_proton.types.template_version_source_input.deserialize_aws_json_1_0(
                data["source"]
            )
        )
    else:
        raise DeserializationError("CreateServiceTemplateVersionInput.source required")
    if data.get("compatibleEnvironmentTemplates") is not None:
        import capo_proton.types.compatible_environment_template_input_list

        out["compatible_environment_templates"] = (
            capo_proton.types.compatible_environment_template_input_list.deserialize_aws_json_1_0(
                data["compatibleEnvironmentTemplates"]
            )
        )
    else:
        raise DeserializationError(
            "CreateServiceTemplateVersionInput.compatible_environment_templates required"
        )
    if data.get("tags") is not None:
        import capo_proton.types.tag_list

        out["tags"] = capo_proton.types.tag_list.deserialize_aws_json_1_0(data["tags"])
    if data.get("supportedComponentSources") is not None:
        import capo_proton.types.service_template_supported_component_source_input_list

        out["supported_component_sources"] = (
            capo_proton.types.service_template_supported_component_source_input_list.deserialize_aws_json_1_0(
                data["supportedComponentSources"]
            )
        )
    return out
