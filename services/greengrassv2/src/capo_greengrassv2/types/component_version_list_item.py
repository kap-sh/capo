"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ComponentVersionListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.component_name_string
    import capo_greengrassv2.types.component_version_string
    import capo_greengrassv2.types.non_empty_string


class ComponentVersionListItem(TypedDict, closed=True):
    component_name: NotRequired[
        "capo_greengrassv2.types.component_name_string.ComponentNameString"
    ]
    """<p>The name of the component.</p>"""
    component_version: NotRequired[
        "capo_greengrassv2.types.component_version_string.ComponentVersionString"
    ]
    """<p>The version of the component.</p>"""
    arn: NotRequired["capo_greengrassv2.types.non_empty_string.NonEmptyString"]
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the component version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentVersionListItem) -> dict:
    out: dict = {}
    if "component_name" in value:
        out["componentName"] = value["component_name"]
    if "component_version" in value:
        out["componentVersion"] = value["component_version"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> ComponentVersionListItem:
    out: ComponentVersionListItem = {}  # type: ignore[typeddict-item]
    if data.get("componentName") is not None:
        out["component_name"] = data["componentName"]
    if data.get("componentVersion") is not None:
        out["component_version"] = data["componentVersion"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    return out
