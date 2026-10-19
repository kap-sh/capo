"""Generated from Smithy shape ``com.amazonaws.connectcases#TemplateSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.tag_propagation_configuration_list
    import capo_connectcases.types.template_arn
    import capo_connectcases.types.template_id
    import capo_connectcases.types.template_name
    import capo_connectcases.types.template_status


class TemplateSummary(TypedDict, closed=True):
    template_id: "capo_connectcases.types.template_id.TemplateId"
    """<p>The unique identifier for the template.</p>"""
    template_arn: "capo_connectcases.types.template_arn.TemplateArn"
    """<p>The Amazon Resource Name (ARN) of the template.</p>"""
    name: "capo_connectcases.types.template_name.TemplateName"
    """<p>The template name.</p>"""
    status: "capo_connectcases.types.template_status.TemplateStatus"
    """<p>The status of the template.</p>"""
    tag_propagation_configurations: NotRequired[
        "capo_connectcases.types.tag_propagation_configuration_list.TagPropagationConfigurationList"
    ]
    """<p>Defines tag propagation configuration for resources created within a domain. Tags specified here will be automatically applied to resources being created for the specified resource type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateSummary) -> dict:
    out: dict = {}
    out["templateId"] = value["template_id"]
    out["templateArn"] = value["template_arn"]
    out["name"] = value["name"]
    out["status"] = value["status"]
    if "tag_propagation_configurations" in value:
        import capo_connectcases.types.tag_propagation_configuration_list

        out["tagPropagationConfigurations"] = (
            capo_connectcases.types.tag_propagation_configuration_list.serialize_json(
                value["tag_propagation_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> TemplateSummary:
    out: TemplateSummary = {}  # type: ignore[typeddict-item]
    if data.get("templateId") is not None:
        out["template_id"] = data["templateId"]
    else:
        out["template_id"] = ""
    if data.get("templateArn") is not None:
        out["template_arn"] = data["templateArn"]
    else:
        out["template_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("tagPropagationConfigurations") is not None:
        import capo_connectcases.types.tag_propagation_configuration_list

        out["tag_propagation_configurations"] = (
            capo_connectcases.types.tag_propagation_configuration_list.deserialize_json(
                data["tagPropagationConfigurations"]
            )
        )
    return out
