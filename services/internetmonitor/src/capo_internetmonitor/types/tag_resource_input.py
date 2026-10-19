"""Generated from Smithy shape ``com.amazonaws.internetmonitor#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_internetmonitor.types.monitor_arn
    import capo_internetmonitor.types.tag_map


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_internetmonitor.types.monitor_arn.MonitorArn"
    """<p>The Amazon Resource Name (ARN) for a tag that you add to a resource. Tags are supported only for monitors in Amazon CloudWatch Internet Monitor.</p>"""
    tags: "capo_internetmonitor.types.tag_map.TagMap"
    """<p>Tags that you add to a resource. You can add a maximum of 50 tags in Internet Monitor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    import capo_internetmonitor.types.tag_map

    out["Tags"] = capo_internetmonitor.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_internetmonitor.types.tag_map

        out["tags"] = capo_internetmonitor.types.tag_map.deserialize_json(data["Tags"])
    else:
        out["tags"] = {}
    return out
