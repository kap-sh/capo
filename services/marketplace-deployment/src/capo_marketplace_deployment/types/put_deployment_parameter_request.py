"""Generated from Smithy shape ``com.amazonaws.marketplacedeployment#PutDeploymentParameterRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_marketplace_deployment.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_marketplace_deployment.types.catalog
    import capo_marketplace_deployment.types.client_token
    import capo_marketplace_deployment.types.deployment_parameter_input
    import capo_marketplace_deployment.types.resource_id
    import capo_marketplace_deployment.types.tags_map


class PutDeploymentParameterRequest(TypedDict, closed=True):
    catalog: "capo_marketplace_deployment.types.catalog.Catalog"
    """<p>The catalog related to the request. Fixed value: <code>AWSMarketplace</code> </p>"""
    product_id: "capo_marketplace_deployment.types.resource_id.ResourceId"
    """<p>The product for which AWS Marketplace will save secrets for the buyer’s account.</p>"""
    agreement_id: "capo_marketplace_deployment.types.resource_id.ResourceId"
    """<p>The unique identifier of the agreement.</p>"""
    deployment_parameter: "capo_marketplace_deployment.types.deployment_parameter_input.DeploymentParameterInput"
    """<p>The deployment parameter targeted to the acceptor of an agreement for which to create the AWS Secret Manager resource.</p>"""
    tags: NotRequired["capo_marketplace_deployment.types.tags_map.TagsMap"]
    """<p>A map of key-value pairs, where each pair represents a tag saved to the resource. Tags will only be applied for create operations, and they'll be ignored if the resource already exists.</p>"""
    expiration_date: NotRequired["datetime.datetime"]
    """<p>The date when deployment parameters expire and are scheduled for deletion.</p>"""
    client_token: NotRequired[
        "capo_marketplace_deployment.types.client_token.ClientToken"
    ]
    """<p>The idempotency token for deployment parameters. A unique identifier for the new version.</p> <note> <p>This field is not required if you're calling using an AWS SDK. Otherwise, a <code>clientToken</code> must be provided with the request.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutDeploymentParameterRequest) -> dict:
    out: dict = {}
    out["agreementId"] = value["agreement_id"]
    import capo_marketplace_deployment.types.deployment_parameter_input

    out["deploymentParameter"] = (
        capo_marketplace_deployment.types.deployment_parameter_input.serialize_json(
            value["deployment_parameter"]
        )
    )
    if "tags" in value:
        import capo_marketplace_deployment.types.tags_map

        out["tags"] = capo_marketplace_deployment.types.tags_map.serialize_json(
            value["tags"]
        )
    if "expiration_date" in value:
        import capo_marketplace_deployment._protocol.serialize

        out["expirationDate"] = (
            capo_marketplace_deployment._protocol.serialize.fmt_date_time(
                value["expiration_date"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> PutDeploymentParameterRequest:
    out: PutDeploymentParameterRequest = {}  # type: ignore[typeddict-item]
    if data.get("agreementId") is not None:
        out["agreement_id"] = data["agreementId"]
    else:
        out["agreement_id"] = ""
    if data.get("deploymentParameter") is not None:
        import capo_marketplace_deployment.types.deployment_parameter_input

        out["deployment_parameter"] = (
            capo_marketplace_deployment.types.deployment_parameter_input.deserialize_json(
                data["deploymentParameter"]
            )
        )
    else:
        raise DeserializationError(
            "PutDeploymentParameterRequest.deployment_parameter required"
        )
    if data.get("tags") is not None:
        import capo_marketplace_deployment.types.tags_map

        out["tags"] = capo_marketplace_deployment.types.tags_map.deserialize_json(
            data["tags"]
        )
    if data.get("expirationDate") is not None:
        import datetime

        out["expiration_date"] = datetime.datetime.fromisoformat(
            data["expirationDate"].replace("Z", "+00:00")
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: PutDeploymentParameterRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "deployment_parameter" in value:
        import capo_marketplace_deployment.types.deployment_parameter_input

        out["deployment_parameter"] = (
            capo_marketplace_deployment.types.deployment_parameter_input.redact_sensitive(
                value["deployment_parameter"]
            )
        )
    return out
