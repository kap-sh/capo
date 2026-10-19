"""Generated from Smithy shape ``com.amazonaws.proton#ListServicePipelineProvisionedResourcesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.empty_next_token
    import capo_proton.types.provisioned_resource_list


class ListServicePipelineProvisionedResourcesOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_proton.types.empty_next_token.EmptyNextToken"]
    """<p>A token that indicates the location of the next provisioned resource in the array of provisioned resources, after the current requested list of provisioned resources.</p>"""
    provisioned_resources: (
        "capo_proton.types.provisioned_resource_list.ProvisionedResourceList"
    )
    """<p>An array of provisioned resources for a service and pipeline.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: ListServicePipelineProvisionedResourcesOutput,
) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_proton.types.provisioned_resource_list

    out["provisionedResources"] = (
        capo_proton.types.provisioned_resource_list.serialize_aws_json_1_0(
            value["provisioned_resources"]
        )
    )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> ListServicePipelineProvisionedResourcesOutput:
    out: ListServicePipelineProvisionedResourcesOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("provisionedResources") is not None:
        import capo_proton.types.provisioned_resource_list

        out["provisioned_resources"] = (
            capo_proton.types.provisioned_resource_list.deserialize_aws_json_1_0(
                data["provisionedResources"]
            )
        )
    else:
        out["provisioned_resources"] = []
    return out
