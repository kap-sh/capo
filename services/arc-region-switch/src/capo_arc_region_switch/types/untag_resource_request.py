"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.plan_arn
    import capo_arc_region_switch.types.tag_keys


class UntagResourceRequest(TypedDict, closed=True):
    arn: "capo_arc_region_switch.types.plan_arn.PlanArn"
    """<p>The Amazon Resource Name (ARN) for a tag you remove a resource from.</p>"""
    resource_tag_keys: "capo_arc_region_switch.types.tag_keys.TagKeys"
    """<p>Tag keys that you remove from a resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    import capo_arc_region_switch.types.tag_keys

    out["resourceTagKeys"] = (
        capo_arc_region_switch.types.tag_keys.serialize_aws_json_1_0(
            value["resource_tag_keys"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("resourceTagKeys") is not None:
        import capo_arc_region_switch.types.tag_keys

        out["resource_tag_keys"] = (
            capo_arc_region_switch.types.tag_keys.deserialize_aws_json_1_0(
                data["resourceTagKeys"]
            )
        )
    else:
        out["resource_tag_keys"] = []
    return out
