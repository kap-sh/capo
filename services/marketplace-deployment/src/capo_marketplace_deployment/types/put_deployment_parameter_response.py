"""Generated from Smithy shape ``com.amazonaws.marketplacedeployment#PutDeploymentParameterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_deployment.types.deployment_parameter_resource_identifier
    import capo_marketplace_deployment.types.resource_arn
    import capo_marketplace_deployment.types.resource_id
    import capo_marketplace_deployment.types.tags_map


class PutDeploymentParameterResponse(TypedDict, closed=True):
    resource_arn: "capo_marketplace_deployment.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) associated with the deployment parameter resource you want to create or update.</p>"""
    agreement_id: "capo_marketplace_deployment.types.resource_id.ResourceId"
    """<p>The unique identifier of the agreement.</p>"""
    deployment_parameter_id: "capo_marketplace_deployment.types.deployment_parameter_resource_identifier.DeploymentParameterResourceIdentifier"
    """<p>The unique identifier of the deployment parameter.</p>"""
    tags: NotRequired["capo_marketplace_deployment.types.tags_map.TagsMap"]
    """<p>A map of key-value pairs, where each pair represents a tag saved to the resource. Tags will only be applied for create operations, and they'll be ignored if the resource already exists.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutDeploymentParameterResponse) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["agreementId"] = value["agreement_id"]
    out["deploymentParameterId"] = value["deployment_parameter_id"]
    if "tags" in value:
        import capo_marketplace_deployment.types.tags_map

        out["tags"] = capo_marketplace_deployment.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> PutDeploymentParameterResponse:
    out: PutDeploymentParameterResponse = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("agreementId") is not None:
        out["agreement_id"] = data["agreementId"]
    else:
        out["agreement_id"] = ""
    if data.get("deploymentParameterId") is not None:
        out["deployment_parameter_id"] = data["deploymentParameterId"]
    else:
        out["deployment_parameter_id"] = ""
    if data.get("tags") is not None:
        import capo_marketplace_deployment.types.tags_map

        out["tags"] = capo_marketplace_deployment.types.tags_map.deserialize_json(
            data["tags"]
        )
    return out
