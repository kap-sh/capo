"""Generated from Smithy shape ``com.amazonaws.resourcegroups#UngroupResourcesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resource_groups.types.group_string_v2
    import capo_resource_groups.types.resource_arn_list


class UngroupResourcesInput(TypedDict, closed=True):
    group: "capo_resource_groups.types.group_string_v2.GroupStringV2"
    """<p>The name or the Amazon resource name (ARN) of the resource group from which to remove the resources.</p>"""
    resource_arns: "capo_resource_groups.types.resource_arn_list.ResourceArnList"
    """<p>The Amazon resource names (ARNs) of the resources to be removed from the group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UngroupResourcesInput) -> dict:
    out: dict = {}
    out["Group"] = value["group"]
    import capo_resource_groups.types.resource_arn_list

    out["ResourceArns"] = capo_resource_groups.types.resource_arn_list.serialize_json(
        value["resource_arns"]
    )
    return out


def deserialize_json(data: dict) -> UngroupResourcesInput:
    out: UngroupResourcesInput = {}  # type: ignore[typeddict-item]
    if data.get("Group") is not None:
        out["group"] = data["Group"]
    else:
        out["group"] = ""
    if data.get("ResourceArns") is not None:
        import capo_resource_groups.types.resource_arn_list

        out["resource_arns"] = (
            capo_resource_groups.types.resource_arn_list.deserialize_json(
                data["ResourceArns"]
            )
        )
    else:
        out["resource_arns"] = []
    return out
