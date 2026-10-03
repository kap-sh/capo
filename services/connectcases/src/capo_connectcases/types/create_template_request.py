"""Generated from Smithy shape ``com.amazonaws.connectcases#CreateTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcases.types.domain_id
    import capo_connectcases.types.layout_configuration
    import capo_connectcases.types.required_field_list
    import capo_connectcases.types.tag_propagation_configuration_list
    import capo_connectcases.types.template_case_rule_list
    import capo_connectcases.types.template_description
    import capo_connectcases.types.template_name
    import capo_connectcases.types.template_status


class CreateTemplateRequest(TypedDict, closed=True):
    domain_id: "capo_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    name: "capo_connectcases.types.template_name.TemplateName"
    """<p>A name for the template. It must be unique per domain.</p>"""
    description: NotRequired[
        "capo_connectcases.types.template_description.TemplateDescription"
    ]
    """<p>A brief description of the template.</p>"""
    layout_configuration: NotRequired[
        "capo_connectcases.types.layout_configuration.LayoutConfiguration"
    ]
    """<p>Configuration of layouts associated to the template.</p>"""
    required_fields: NotRequired[
        "capo_connectcases.types.required_field_list.RequiredFieldList"
    ]
    """<p>A list of fields that must contain a value for a case to be successfully created with this template.</p>"""
    status: NotRequired["capo_connectcases.types.template_status.TemplateStatus"]
    """<p>The status of the template.</p>"""
    rules: NotRequired[
        "capo_connectcases.types.template_case_rule_list.TemplateCaseRuleList"
    ]
    """<p>A list of case rules (also known as <a href="https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html">case field conditions</a>) on a template. </p>"""
    tag_propagation_configurations: NotRequired[
        "capo_connectcases.types.tag_propagation_configuration_list.TagPropagationConfigurationList"
    ]
    """<p>Defines tag propagation configuration for resources created within a domain. Tags specified here will be automatically applied to resources being created for the specified resource type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTemplateRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "layout_configuration" in value:
        import capo_connectcases.types.layout_configuration

        out["layoutConfiguration"] = (
            capo_connectcases.types.layout_configuration.serialize_json(
                value["layout_configuration"]
            )
        )
    if "required_fields" in value:
        import capo_connectcases.types.required_field_list

        out["requiredFields"] = (
            capo_connectcases.types.required_field_list.serialize_json(
                value["required_fields"]
            )
        )
    if "status" in value:
        out["status"] = value["status"]
    if "rules" in value:
        import capo_connectcases.types.template_case_rule_list

        out["rules"] = capo_connectcases.types.template_case_rule_list.serialize_json(
            value["rules"]
        )
    if "tag_propagation_configurations" in value:
        import capo_connectcases.types.tag_propagation_configuration_list

        out["tagPropagationConfigurations"] = (
            capo_connectcases.types.tag_propagation_configuration_list.serialize_json(
                value["tag_propagation_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateTemplateRequest:
    out: CreateTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateTemplateRequest.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("layoutConfiguration") is not None:
        import capo_connectcases.types.layout_configuration

        out["layout_configuration"] = (
            capo_connectcases.types.layout_configuration.deserialize_json(
                data["layoutConfiguration"]
            )
        )
    if data.get("requiredFields") is not None:
        import capo_connectcases.types.required_field_list

        out["required_fields"] = (
            capo_connectcases.types.required_field_list.deserialize_json(
                data["requiredFields"]
            )
        )
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("rules") is not None:
        import capo_connectcases.types.template_case_rule_list

        out["rules"] = capo_connectcases.types.template_case_rule_list.deserialize_json(
            data["rules"]
        )
    if data.get("tagPropagationConfigurations") is not None:
        import capo_connectcases.types.tag_propagation_configuration_list

        out["tag_propagation_configurations"] = (
            capo_connectcases.types.tag_propagation_configuration_list.deserialize_json(
                data["tagPropagationConfigurations"]
            )
        )
    return out
