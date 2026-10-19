"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_snow_device_management.types.tag_map


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the device or task.</p>"""
    tags: "capo_snow_device_management.types.tag_map.TagMap"
    """<p>Optional metadata that you assign to a resource. You can use tags to categorize a resource in different ways, such as by purpose, owner, or environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    import capo_snow_device_management.types.tag_map

    out["tags"] = capo_snow_device_management.types.tag_map.serialize_json(
        value["tags"]
    )
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_snow_device_management.types.tag_map

        out["tags"] = capo_snow_device_management.types.tag_map.deserialize_json(
            data["tags"]
        )
    else:
        out["tags"] = {}
    return out
