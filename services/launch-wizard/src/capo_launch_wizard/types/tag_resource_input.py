"""Generated from Smithy shape ``com.amazonaws.launchwizard#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_launch_wizard.types.tags


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tags: "capo_launch_wizard.types.tags.Tags"
    """<p>One or more tags to attach to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    import capo_launch_wizard.types.tags

    out["tags"] = capo_launch_wizard.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_launch_wizard.types.tags

        out["tags"] = capo_launch_wizard.types.tags.deserialize_json(data["tags"])
    else:
        out["tags"] = {}
    return out
