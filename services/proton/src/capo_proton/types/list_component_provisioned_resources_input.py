"""Generated from Smithy shape ``com.amazonaws.proton#ListComponentProvisionedResourcesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.empty_next_token
    import capo_proton.types.resource_name


class ListComponentProvisionedResourcesInput(TypedDict, closed=True):
    component_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the component whose provisioned resources you want.</p>"""
    next_token: NotRequired["capo_proton.types.empty_next_token.EmptyNextToken"]
    """<p>A token that indicates the location of the next provisioned resource in the array of provisioned resources, after the list of provisioned resources that was previously requested.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListComponentProvisionedResourcesInput) -> dict:
    out: dict = {}
    out["componentName"] = value["component_name"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListComponentProvisionedResourcesInput:
    out: ListComponentProvisionedResourcesInput = {}  # type: ignore[typeddict-item]
    if data.get("componentName") is not None:
        out["component_name"] = data["componentName"]
    else:
        out["component_name"] = ""
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
