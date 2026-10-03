"""Generated from Smithy shape ``com.amazonaws.proton#ServiceTemplateVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_proton.types.compatible_environment_template_list
    import capo_proton.types.description
    import capo_proton.types.resource_name
    import capo_proton.types.service_template_supported_component_source_input_list
    import capo_proton.types.service_template_version_arn
    import capo_proton.types.status_message
    import capo_proton.types.template_schema
    import capo_proton.types.template_version_part
    import capo_proton.types.template_version_status


class ServiceTemplateVersion(TypedDict, closed=True):
    template_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the version of a service template.</p>"""
    major_version: "capo_proton.types.template_version_part.TemplateVersionPart"
    """<p>The latest major version that's associated with the version of a service template.</p>"""
    minor_version: "capo_proton.types.template_version_part.TemplateVersionPart"
    """<p>The minor version of a service template.</p>"""
    recommended_minor_version: NotRequired[
        "capo_proton.types.template_version_part.TemplateVersionPart"
    ]
    """<p>The recommended minor version of the service template.</p>"""
    status: "capo_proton.types.template_version_status.TemplateVersionStatus"
    """<p>The service template version status.</p>"""
    status_message: NotRequired["capo_proton.types.status_message.StatusMessage"]
    """<p>A service template version status message.</p>"""
    description: NotRequired["capo_proton.types.description.Description"]
    """<p>A description of the version of a service template.</p>"""
    arn: "capo_proton.types.service_template_version_arn.ServiceTemplateVersionArn"
    """<p>The Amazon Resource Name (ARN) of the version of a service template.</p>"""
    created_at: "datetime.datetime"
    """<p>The time when the version of a service template was created.</p>"""
    last_modified_at: "datetime.datetime"
    """<p>The time when the version of a service template was last modified.</p>"""
    compatible_environment_templates: "capo_proton.types.compatible_environment_template_list.CompatibleEnvironmentTemplateList"
    """<p>An array of compatible environment template names for the major version of a service template.</p>"""
    schema: NotRequired["capo_proton.types.template_schema.TemplateSchema"]
    """<p>The schema of the version of a service template.</p>"""
    supported_component_sources: NotRequired[
        "capo_proton.types.service_template_supported_component_source_input_list.ServiceTemplateSupportedComponentSourceInputList"
    ]
    """<p>An array of supported component sources. Components with supported sources can be attached to service instances based on this service template version.</p> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceTemplateVersion) -> dict:
    out: dict = {}
    out["templateName"] = value["template_name"]
    out["majorVersion"] = value["major_version"]
    out["minorVersion"] = value["minor_version"]
    if "recommended_minor_version" in value:
        out["recommendedMinorVersion"] = value["recommended_minor_version"]
    out["status"] = value["status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "description" in value:
        out["description"] = value["description"]
    out["arn"] = value["arn"]
    import capo_proton.types._prelude.timestamp

    out["createdAt"] = capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
        value["created_at"]
    )
    import capo_proton.types._prelude.timestamp

    out["lastModifiedAt"] = capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
        value["last_modified_at"]
    )
    import capo_proton.types.compatible_environment_template_list

    out["compatibleEnvironmentTemplates"] = (
        capo_proton.types.compatible_environment_template_list.serialize_aws_json_1_0(
            value["compatible_environment_templates"]
        )
    )
    if "schema" in value:
        out["schema"] = value["schema"]
    if "supported_component_sources" in value:
        import capo_proton.types.service_template_supported_component_source_input_list

        out["supportedComponentSources"] = (
            capo_proton.types.service_template_supported_component_source_input_list.serialize_aws_json_1_0(
                value["supported_component_sources"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ServiceTemplateVersion:
    out: ServiceTemplateVersion = {}  # type: ignore[typeddict-item]
    if data.get("templateName") is not None:
        out["template_name"] = data["templateName"]
    else:
        raise DeserializationError("ServiceTemplateVersion.template_name required")
    if data.get("majorVersion") is not None:
        out["major_version"] = data["majorVersion"]
    else:
        raise DeserializationError("ServiceTemplateVersion.major_version required")
    if data.get("minorVersion") is not None:
        out["minor_version"] = data["minorVersion"]
    else:
        raise DeserializationError("ServiceTemplateVersion.minor_version required")
    if data.get("recommendedMinorVersion") is not None:
        out["recommended_minor_version"] = data["recommendedMinorVersion"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        raise DeserializationError("ServiceTemplateVersion.status required")
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ServiceTemplateVersion.arn required")
    if data.get("createdAt") is not None:
        import capo_proton.types._prelude.timestamp

        out["created_at"] = (
            capo_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("ServiceTemplateVersion.created_at required")
    if data.get("lastModifiedAt") is not None:
        import capo_proton.types._prelude.timestamp

        out["last_modified_at"] = (
            capo_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["lastModifiedAt"]
            )
        )
    else:
        raise DeserializationError("ServiceTemplateVersion.last_modified_at required")
    if data.get("compatibleEnvironmentTemplates") is not None:
        import capo_proton.types.compatible_environment_template_list

        out["compatible_environment_templates"] = (
            capo_proton.types.compatible_environment_template_list.deserialize_aws_json_1_0(
                data["compatibleEnvironmentTemplates"]
            )
        )
    else:
        raise DeserializationError(
            "ServiceTemplateVersion.compatible_environment_templates required"
        )
    if data.get("schema") is not None:
        out["schema"] = data["schema"]
    if data.get("supportedComponentSources") is not None:
        import capo_proton.types.service_template_supported_component_source_input_list

        out["supported_component_sources"] = (
            capo_proton.types.service_template_supported_component_source_input_list.deserialize_aws_json_1_0(
                data["supportedComponentSources"]
            )
        )
    return out
