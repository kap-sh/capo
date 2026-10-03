"""Generated from Smithy shape ``com.amazonaws.proton#UpdateServiceTemplateVersionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.compatible_environment_template_input_list
    import capo_proton.types.description
    import capo_proton.types.resource_name
    import capo_proton.types.service_template_supported_component_source_input_list
    import capo_proton.types.template_version_part
    import capo_proton.types.template_version_status


class UpdateServiceTemplateVersionInput(TypedDict, closed=True):
    template_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the service template.</p>"""
    major_version: "capo_proton.types.template_version_part.TemplateVersionPart"
    """<p>To update a major version of a service template, include <code>major Version</code>.</p>"""
    minor_version: "capo_proton.types.template_version_part.TemplateVersionPart"
    """<p>To update a minor version of a service template, include <code>minorVersion</code>.</p>"""
    description: NotRequired["capo_proton.types.description.Description"]
    """<p>A description of a service template version to update.</p>"""
    status: NotRequired[
        "capo_proton.types.template_version_status.TemplateVersionStatus"
    ]
    """<p>The status of the service template minor version to update.</p>"""
    compatible_environment_templates: NotRequired[
        "capo_proton.types.compatible_environment_template_input_list.CompatibleEnvironmentTemplateInputList"
    ]
    """<p>An array of environment template objects that are compatible with this service template version. A service instance based on this service template version can run in environments based on compatible templates.</p>"""
    supported_component_sources: NotRequired[
        "capo_proton.types.service_template_supported_component_source_input_list.ServiceTemplateSupportedComponentSourceInputList"
    ]
    """<p>An array of supported component sources. Components with supported sources can be attached to service instances based on this service template version.</p> <note> <p>A change to <code>supportedComponentSources</code> doesn't impact existing component attachments to instances based on this template version. A change only affects later associations.</p> </note> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateServiceTemplateVersionInput) -> dict:
    out: dict = {}
    out["templateName"] = value["template_name"]
    out["majorVersion"] = value["major_version"]
    out["minorVersion"] = value["minor_version"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        out["status"] = value["status"]
    if "compatible_environment_templates" in value:
        import capo_proton.types.compatible_environment_template_input_list

        out["compatibleEnvironmentTemplates"] = (
            capo_proton.types.compatible_environment_template_input_list.serialize_aws_json_1_0(
                value["compatible_environment_templates"]
            )
        )
    if "supported_component_sources" in value:
        import capo_proton.types.service_template_supported_component_source_input_list

        out["supportedComponentSources"] = (
            capo_proton.types.service_template_supported_component_source_input_list.serialize_aws_json_1_0(
                value["supported_component_sources"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateServiceTemplateVersionInput:
    out: UpdateServiceTemplateVersionInput = {}  # type: ignore[typeddict-item]
    if data.get("templateName") is not None:
        out["template_name"] = data["templateName"]
    else:
        raise DeserializationError(
            "UpdateServiceTemplateVersionInput.template_name required"
        )
    if data.get("majorVersion") is not None:
        out["major_version"] = data["majorVersion"]
    else:
        raise DeserializationError(
            "UpdateServiceTemplateVersionInput.major_version required"
        )
    if data.get("minorVersion") is not None:
        out["minor_version"] = data["minorVersion"]
    else:
        raise DeserializationError(
            "UpdateServiceTemplateVersionInput.minor_version required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("compatibleEnvironmentTemplates") is not None:
        import capo_proton.types.compatible_environment_template_input_list

        out["compatible_environment_templates"] = (
            capo_proton.types.compatible_environment_template_input_list.deserialize_aws_json_1_0(
                data["compatibleEnvironmentTemplates"]
            )
        )
    if data.get("supportedComponentSources") is not None:
        import capo_proton.types.service_template_supported_component_source_input_list

        out["supported_component_sources"] = (
            capo_proton.types.service_template_supported_component_source_input_list.deserialize_aws_json_1_0(
                data["supportedComponentSources"]
            )
        )
    return out
