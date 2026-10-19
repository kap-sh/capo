"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ServiceActionAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.id


class ServiceActionAssociation(TypedDict, closed=True):
    service_action_id: "capo_service_catalog.types.id.Id"
    """<p>The self-service action identifier. For example, <code>act-fs7abcd89wxyz</code>.</p>"""
    product_id: "capo_service_catalog.types.id.Id"
    """<p>The product identifier. For example, <code>prod-abcdzk7xy33qa</code>.</p>"""
    provisioning_artifact_id: "capo_service_catalog.types.id.Id"
    """<p>The identifier of the provisioning artifact. For example, <code>pa-4abcdjnxjj6ne</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceActionAssociation) -> dict:
    out: dict = {}
    out["ServiceActionId"] = value["service_action_id"]
    out["ProductId"] = value["product_id"]
    out["ProvisioningArtifactId"] = value["provisioning_artifact_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceActionAssociation:
    out: ServiceActionAssociation = {}  # type: ignore[typeddict-item]
    if data.get("ServiceActionId") is not None:
        out["service_action_id"] = data["ServiceActionId"]
    else:
        out["service_action_id"] = ""
    if data.get("ProductId") is not None:
        out["product_id"] = data["ProductId"]
    else:
        out["product_id"] = ""
    if data.get("ProvisioningArtifactId") is not None:
        out["provisioning_artifact_id"] = data["ProvisioningArtifactId"]
    else:
        out["provisioning_artifact_id"] = ""
    return out
