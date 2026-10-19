"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.plan_arn
    import capo_arc_region_switch.types.tags


class TagResourceRequest(TypedDict, closed=True):
    arn: "capo_arc_region_switch.types.plan_arn.PlanArn"
    """<p>The Amazon Resource Name (ARN) for a tag that you add to a resource.</p>"""
    tags: "capo_arc_region_switch.types.tags.Tags"
    """<p>Tags that you add to a resource. You can add a maximum of 50 tags in Region switch.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    import capo_arc_region_switch.types.tags

    out["tags"] = capo_arc_region_switch.types.tags.serialize_aws_json_1_0(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("tags") is not None:
        import capo_arc_region_switch.types.tags

        out["tags"] = capo_arc_region_switch.types.tags.deserialize_aws_json_1_0(
            data["tags"]
        )
    else:
        out["tags"] = {}
    return out
