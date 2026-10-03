"""Generated from Smithy shape ``com.amazonaws.connectcases#GetTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcases.types.created_time
    import capo_connectcases.types.deleted
    import capo_connectcases.types.last_modified_time
    import capo_connectcases.types.layout_configuration
    import capo_connectcases.types.required_field_list
    import capo_connectcases.types.tag_propagation_configuration_list
    import capo_connectcases.types.tags
    import capo_connectcases.types.template_arn
    import capo_connectcases.types.template_case_rule_list
    import capo_connectcases.types.template_description
    import capo_connectcases.types.template_id
    import capo_connectcases.types.template_name
    import capo_connectcases.types.template_status


class GetTemplateResponse(TypedDict, closed=True):
    template_id: "capo_connectcases.types.template_id.TemplateId"
    """<p>A unique identifier of a template.</p>"""
    template_arn: "capo_connectcases.types.template_arn.TemplateArn"
    """<p>The Amazon Resource Name (ARN) of the template.</p>"""
    name: "capo_connectcases.types.template_name.TemplateName"
    """<p>The name of the template.</p>"""
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
    tags: NotRequired["capo_connectcases.types.tags.Tags"]
    """<p>A map of of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.</p>"""
    status: "capo_connectcases.types.template_status.TemplateStatus"
    """<p>The status of the template.</p>"""
    deleted: "capo_connectcases.types.deleted.Deleted"
    """<p>Denotes whether or not the resource has been deleted.</p>"""
    created_time: NotRequired["capo_connectcases.types.created_time.CreatedTime"]
    """<p>Timestamp at which the resource was created.</p>"""
    last_modified_time: NotRequired[
        "capo_connectcases.types.last_modified_time.LastModifiedTime"
    ]
    """<p>Timestamp at which the resource was created or last modified.</p>"""
    rules: NotRequired[
        "capo_connectcases.types.template_case_rule_list.TemplateCaseRuleList"
    ]
    """<p>A list of case rules (also known as <a href="https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html">case field conditions</a>) on a template. </p>"""
    tag_propagation_configurations: NotRequired[
        "capo_connectcases.types.tag_propagation_configuration_list.TagPropagationConfigurationList"
    ]
    """<p>Defines tag propagation configuration for resources created within a domain. Tags specified here will be automatically applied to resources being created for the specified resource type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTemplateResponse) -> dict:
    out: dict = {}
    out["templateId"] = value["template_id"]
    out["templateArn"] = value["template_arn"]
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
    if "tags" in value:
        import capo_connectcases.types.tags

        out["tags"] = capo_connectcases.types.tags.serialize_json(value["tags"])
    out["status"] = value["status"]
    out["deleted"] = value.get("deleted", False)
    if "created_time" in value:
        import capo_connectcases.types.created_time

        out["createdTime"] = capo_connectcases.types.created_time.serialize_json(
            value["created_time"]
        )
    if "last_modified_time" in value:
        import capo_connectcases.types.last_modified_time

        out["lastModifiedTime"] = (
            capo_connectcases.types.last_modified_time.serialize_json(
                value["last_modified_time"]
            )
        )
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


def deserialize_json(data: dict) -> GetTemplateResponse:
    out: GetTemplateResponse = {}  # type: ignore[typeddict-item]
    if data.get("templateId") is not None:
        out["template_id"] = data["templateId"]
    else:
        raise DeserializationError("GetTemplateResponse.template_id required")
    if data.get("templateArn") is not None:
        out["template_arn"] = data["templateArn"]
    else:
        raise DeserializationError("GetTemplateResponse.template_arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetTemplateResponse.name required")
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
    if data.get("tags") is not None:
        import capo_connectcases.types.tags

        out["tags"] = capo_connectcases.types.tags.deserialize_json(data["tags"])
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        raise DeserializationError("GetTemplateResponse.status required")
    if data.get("deleted") is not None:
        out["deleted"] = data["deleted"]
    else:
        out["deleted"] = False
    if data.get("createdTime") is not None:
        import capo_connectcases.types.created_time

        out["created_time"] = capo_connectcases.types.created_time.deserialize_json(
            data["createdTime"]
        )
    if data.get("lastModifiedTime") is not None:
        import capo_connectcases.types.last_modified_time

        out["last_modified_time"] = (
            capo_connectcases.types.last_modified_time.deserialize_json(
                data["lastModifiedTime"]
            )
        )
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
