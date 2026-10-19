"""Generated from Smithy shape ``com.amazonaws.resourcegroups#Group``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups.types.application_tag
    import capo_resource_groups.types.criticality
    import capo_resource_groups.types.description
    import capo_resource_groups.types.display_name
    import capo_resource_groups.types.group_arn_v2
    import capo_resource_groups.types.group_name
    import capo_resource_groups.types.owner


class Group(TypedDict, closed=True):
    group_arn: "capo_resource_groups.types.group_arn_v2.GroupArnV2"
    """<p>The Amazon resource name (ARN) of the resource group.</p>"""
    name: "capo_resource_groups.types.group_name.GroupName"
    """<p>The name of the resource group.</p>"""
    description: NotRequired["capo_resource_groups.types.description.Description"]
    """<p>The description of the resource group.</p>"""
    criticality: NotRequired["capo_resource_groups.types.criticality.Criticality"]
    """<p>The critical rank of the application group on a scale of 1 to 10, with a rank of 1 being the most critical, and a rank of 10 being least critical.</p>"""
    owner: NotRequired["capo_resource_groups.types.owner.Owner"]
    """<p>A name, email address or other identifier for the person or group who is considered as the owner of this application group within your organization. </p>"""
    display_name: NotRequired["capo_resource_groups.types.display_name.DisplayName"]
    """<p>The name of the application group, which you can change at any time. </p>"""
    application_tag: NotRequired[
        "capo_resource_groups.types.application_tag.ApplicationTag"
    ]
    """<p>A tag that defines the application group membership. This tag is only supported for application groups. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Group) -> dict:
    out: dict = {}
    out["GroupArn"] = value["group_arn"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "criticality" in value:
        out["Criticality"] = value["criticality"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "application_tag" in value:
        import capo_resource_groups.types.application_tag

        out["ApplicationTag"] = (
            capo_resource_groups.types.application_tag.serialize_json(
                value["application_tag"]
            )
        )
    return out


def deserialize_json(data: dict) -> Group:
    out: Group = {}  # type: ignore[typeddict-item]
    if data.get("GroupArn") is not None:
        out["group_arn"] = data["GroupArn"]
    else:
        out["group_arn"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Criticality") is not None:
        out["criticality"] = data["Criticality"]
    if data.get("Owner") is not None:
        out["owner"] = data["Owner"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("ApplicationTag") is not None:
        import capo_resource_groups.types.application_tag

        out["application_tag"] = (
            capo_resource_groups.types.application_tag.deserialize_json(
                data["ApplicationTag"]
            )
        )
    return out
