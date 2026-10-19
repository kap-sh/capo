"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ResolvedTargetResource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.resolved_target_information


class ResolvedTargetResource(TypedDict, closed=True):
    resource_type: "str"
    """<p>The AWS FIS resource type the target belongs to, such as aws:ec2:instance, aws:ecs:task, or aws:eks:pod.</p>"""
    target_name: "str"
    """<p>The name of the target in the AWS FIS experiment template.</p>"""
    target_information: "capo_resiliencehubv2.types.resolved_target_information.ResolvedTargetInformation"
    """<p>The raw target information map as returned by AWS FIS.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResolvedTargetResource) -> dict:
    out: dict = {}
    out["resourceType"] = value["resource_type"]
    out["targetName"] = value["target_name"]
    import capo_resiliencehubv2.types.resolved_target_information

    out["targetInformation"] = (
        capo_resiliencehubv2.types.resolved_target_information.serialize_json(
            value["target_information"]
        )
    )
    return out


def deserialize_json(data: dict) -> ResolvedTargetResource:
    out: ResolvedTargetResource = {}  # type: ignore[typeddict-item]
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    else:
        out["resource_type"] = ""
    if data.get("targetName") is not None:
        out["target_name"] = data["targetName"]
    else:
        out["target_name"] = ""
    if data.get("targetInformation") is not None:
        import capo_resiliencehubv2.types.resolved_target_information

        out["target_information"] = (
            capo_resiliencehubv2.types.resolved_target_information.deserialize_json(
                data["targetInformation"]
            )
        )
    else:
        out["target_information"] = {}
    return out
