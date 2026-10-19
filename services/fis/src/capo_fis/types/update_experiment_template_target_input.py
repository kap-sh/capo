"""Generated from Smithy shape ``com.amazonaws.fis#UpdateExperimentTemplateTargetInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.experiment_template_target_filter_input_list
    import capo_fis.types.experiment_template_target_parameter_map
    import capo_fis.types.experiment_template_target_selection_mode
    import capo_fis.types.resource_arn_list
    import capo_fis.types.tag_map
    import capo_fis.types.target_resource_type_id


class UpdateExperimentTemplateTargetInput(TypedDict, closed=True):
    resource_type: "capo_fis.types.target_resource_type_id.TargetResourceTypeId"
    """<p>The resource type. The resource type must be supported for the specified action.</p>"""
    resource_arns: NotRequired["capo_fis.types.resource_arn_list.ResourceArnList"]
    """<p>The Amazon Resource Names (ARNs) of the targets.</p>"""
    resource_tags: NotRequired["capo_fis.types.tag_map.TagMap"]
    """<p>The tags for the target resources.</p>"""
    filters: NotRequired[
        "capo_fis.types.experiment_template_target_filter_input_list.ExperimentTemplateTargetFilterInputList"
    ]
    """<p>The filters to apply to identify target resources using specific attributes.</p>"""
    selection_mode: "capo_fis.types.experiment_template_target_selection_mode.ExperimentTemplateTargetSelectionMode"
    """<p>Scopes the identified resources to a specific count or percentage.</p>"""
    parameters: NotRequired[
        "capo_fis.types.experiment_template_target_parameter_map.ExperimentTemplateTargetParameterMap"
    ]
    """<p>The resource type parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateExperimentTemplateTargetInput) -> dict:
    out: dict = {}
    out["resourceType"] = value["resource_type"]
    if "resource_arns" in value:
        import capo_fis.types.resource_arn_list

        out["resourceArns"] = capo_fis.types.resource_arn_list.serialize_json(
            value["resource_arns"]
        )
    if "resource_tags" in value:
        import capo_fis.types.tag_map

        out["resourceTags"] = capo_fis.types.tag_map.serialize_json(
            value["resource_tags"]
        )
    if "filters" in value:
        import capo_fis.types.experiment_template_target_filter_input_list

        out["filters"] = (
            capo_fis.types.experiment_template_target_filter_input_list.serialize_json(
                value["filters"]
            )
        )
    out["selectionMode"] = value["selection_mode"]
    if "parameters" in value:
        import capo_fis.types.experiment_template_target_parameter_map

        out["parameters"] = (
            capo_fis.types.experiment_template_target_parameter_map.serialize_json(
                value["parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateExperimentTemplateTargetInput:
    out: UpdateExperimentTemplateTargetInput = {}  # type: ignore[typeddict-item]
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    else:
        out["resource_type"] = ""
    if data.get("resourceArns") is not None:
        import capo_fis.types.resource_arn_list

        out["resource_arns"] = capo_fis.types.resource_arn_list.deserialize_json(
            data["resourceArns"]
        )
    if data.get("resourceTags") is not None:
        import capo_fis.types.tag_map

        out["resource_tags"] = capo_fis.types.tag_map.deserialize_json(
            data["resourceTags"]
        )
    if data.get("filters") is not None:
        import capo_fis.types.experiment_template_target_filter_input_list

        out["filters"] = (
            capo_fis.types.experiment_template_target_filter_input_list.deserialize_json(
                data["filters"]
            )
        )
    if data.get("selectionMode") is not None:
        out["selection_mode"] = data["selectionMode"]
    else:
        out["selection_mode"] = ""
    if data.get("parameters") is not None:
        import capo_fis.types.experiment_template_target_parameter_map

        out["parameters"] = (
            capo_fis.types.experiment_template_target_parameter_map.deserialize_json(
                data["parameters"]
            )
        )
    return out
