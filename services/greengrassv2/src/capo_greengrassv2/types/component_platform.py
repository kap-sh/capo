"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ComponentPlatform``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.non_empty_string
    import capo_greengrassv2.types.platform_attributes_map


class ComponentPlatform(TypedDict, closed=True):
    name: NotRequired["capo_greengrassv2.types.non_empty_string.NonEmptyString"]
    """<p>The friendly name of the platform. This name helps you identify the platform.</p> <p>If you omit this parameter, IoT Greengrass creates a friendly name from the <code>os</code> and <code>architecture</code> of the platform.</p>"""
    attributes: NotRequired[
        "capo_greengrassv2.types.platform_attributes_map.PlatformAttributesMap"
    ]
    """<p>A dictionary of attributes for the platform. The IoT Greengrass Core software defines the <code>os</code> and <code>architecture</code> by default. You can specify additional platform attributes for a core device when you deploy the Greengrass nucleus component. For more information, see the <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-component.html">Greengrass nucleus component</a> in the <i>IoT Greengrass V2 Developer Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentPlatform) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "attributes" in value:
        import capo_greengrassv2.types.platform_attributes_map

        out["attributes"] = (
            capo_greengrassv2.types.platform_attributes_map.serialize_json(
                value["attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> ComponentPlatform:
    out: ComponentPlatform = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("attributes") is not None:
        import capo_greengrassv2.types.platform_attributes_map

        out["attributes"] = (
            capo_greengrassv2.types.platform_attributes_map.deserialize_json(
                data["attributes"]
            )
        )
    return out
