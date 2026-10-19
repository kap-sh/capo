"""Generated from Smithy shape ``com.amazonaws.applicationinsights#UpdateComponentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_insights.types.custom_component_name
    import capo_application_insights.types.resource_group_name
    import capo_application_insights.types.resource_list


class UpdateComponentRequest(TypedDict, closed=True):
    resource_group_name: (
        "capo_application_insights.types.resource_group_name.ResourceGroupName"
    )
    """<p>The name of the resource group.</p>"""
    component_name: (
        "capo_application_insights.types.custom_component_name.CustomComponentName"
    )
    """<p>The name of the component.</p>"""
    new_component_name: NotRequired[
        "capo_application_insights.types.custom_component_name.CustomComponentName"
    ]
    """<p>The new name of the component.</p>"""
    resource_list: NotRequired[
        "capo_application_insights.types.resource_list.ResourceList"
    ]
    """<p>The list of resource ARNs that belong to the component.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateComponentRequest) -> dict:
    out: dict = {}
    out["ResourceGroupName"] = value["resource_group_name"]
    out["ComponentName"] = value["component_name"]
    if "new_component_name" in value:
        out["NewComponentName"] = value["new_component_name"]
    if "resource_list" in value:
        import capo_application_insights.types.resource_list

        out["ResourceList"] = (
            capo_application_insights.types.resource_list.serialize_aws_json_1_1(
                value["resource_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateComponentRequest:
    out: UpdateComponentRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceGroupName") is not None:
        out["resource_group_name"] = data["ResourceGroupName"]
    else:
        out["resource_group_name"] = ""
    if data.get("ComponentName") is not None:
        out["component_name"] = data["ComponentName"]
    else:
        out["component_name"] = ""
    if data.get("NewComponentName") is not None:
        out["new_component_name"] = data["NewComponentName"]
    if data.get("ResourceList") is not None:
        import capo_application_insights.types.resource_list

        out["resource_list"] = (
            capo_application_insights.types.resource_list.deserialize_aws_json_1_1(
                data["ResourceList"]
            )
        )
    return out
