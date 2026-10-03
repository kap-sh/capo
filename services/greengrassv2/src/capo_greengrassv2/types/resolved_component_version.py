"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ResolvedComponentVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.component_name_string
    import capo_greengrassv2.types.component_version_arn
    import capo_greengrassv2.types.component_version_string
    import capo_greengrassv2.types.non_empty_string
    import capo_greengrassv2.types.recipe_blob
    import capo_greengrassv2.types.vendor_guidance


class ResolvedComponentVersion(TypedDict, closed=True):
    arn: NotRequired[
        "capo_greengrassv2.types.component_version_arn.ComponentVersionARN"
    ]
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the component version.</p>"""
    component_name: NotRequired[
        "capo_greengrassv2.types.component_name_string.ComponentNameString"
    ]
    """<p>The name of the component.</p>"""
    component_version: NotRequired[
        "capo_greengrassv2.types.component_version_string.ComponentVersionString"
    ]
    """<p>The version of the component.</p>"""
    recipe: NotRequired["capo_greengrassv2.types.recipe_blob.RecipeBlob"]
    """<p>The recipe of the component version.</p>"""
    vendor_guidance: NotRequired[
        "capo_greengrassv2.types.vendor_guidance.VendorGuidance"
    ]
    """<p>The vendor guidance state for the component version. This state indicates whether the component version has any issues that you should consider before you deploy it. The vendor guidance state can be:</p> <ul> <li> <p> <code>ACTIVE</code> – This component version is available and recommended for use.</p> </li> <li> <p> <code>DISCONTINUED</code> – This component version has been discontinued by its publisher. You can deploy this component version, but we recommend that you use a different version of this component.</p> </li> <li> <p> <code>DELETED</code> – This component version has been deleted by its publisher, so you can't deploy it. If you have any existing deployments that specify this component version, those deployments will fail.</p> </li> </ul>"""
    message: NotRequired["capo_greengrassv2.types.non_empty_string.NonEmptyString"]
    """<p>A message that communicates details about the vendor guidance state of the component version. This message communicates why a component version is discontinued or deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResolvedComponentVersion) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "component_name" in value:
        out["componentName"] = value["component_name"]
    if "component_version" in value:
        out["componentVersion"] = value["component_version"]
    if "recipe" in value:
        import capo_greengrassv2.types.recipe_blob

        out["recipe"] = capo_greengrassv2.types.recipe_blob.serialize_json(
            value["recipe"]
        )
    if "vendor_guidance" in value:
        import capo_greengrassv2.types.vendor_guidance

        out["vendorGuidance"] = capo_greengrassv2.types.vendor_guidance.serialize_json(
            value["vendor_guidance"]
        )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResolvedComponentVersion:
    out: ResolvedComponentVersion = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("componentName") is not None:
        out["component_name"] = data["componentName"]
    if data.get("componentVersion") is not None:
        out["component_version"] = data["componentVersion"]
    if data.get("recipe") is not None:
        import capo_greengrassv2.types.recipe_blob

        out["recipe"] = capo_greengrassv2.types.recipe_blob.deserialize_json(
            data["recipe"]
        )
    if data.get("vendorGuidance") is not None:
        import capo_greengrassv2.types.vendor_guidance

        out["vendor_guidance"] = (
            capo_greengrassv2.types.vendor_guidance.deserialize_json(
                data["vendorGuidance"]
            )
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
