"""Generated from Smithy shape ``com.amazonaws.proton#ListEnvironmentProvisionedResourcesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.empty_next_token
    import capo_proton.types.resource_name


class ListEnvironmentProvisionedResourcesInput(TypedDict, closed=True):
    environment_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The environment name.</p>"""
    next_token: NotRequired["capo_proton.types.empty_next_token.EmptyNextToken"]
    """<p>A token that indicates the location of the next environment provisioned resource in the array of environment provisioned resources, after the list of environment provisioned resources that was previously requested.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEnvironmentProvisionedResourcesInput) -> dict:
    out: dict = {}
    out["environmentName"] = value["environment_name"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEnvironmentProvisionedResourcesInput:
    out: ListEnvironmentProvisionedResourcesInput = {}  # type: ignore[typeddict-item]
    if data.get("environmentName") is not None:
        out["environment_name"] = data["environmentName"]
    else:
        out["environment_name"] = ""
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
