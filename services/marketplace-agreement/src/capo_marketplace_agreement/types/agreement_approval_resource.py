"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementApprovalResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_approval_deployed_on_aws
    import capo_marketplace_agreement.types.agreement_approval_resource_id
    import capo_marketplace_agreement.types.agreement_approval_resource_name
    import capo_marketplace_agreement.types.agreement_approval_resource_type


class AgreementApprovalResource(TypedDict, closed=True):
    id: "capo_marketplace_agreement.types.agreement_approval_resource_id.AgreementApprovalResourceId"
    """<p>The unique identifier of the resource.</p>"""
    type: "capo_marketplace_agreement.types.agreement_approval_resource_type.AgreementApprovalResourceType"
    """<p>Type of the resource, which is the product (for example, <code>SaaSProduct</code>, <code>AmiProduct</code>, <code>ContainerProduct</code>).</p>"""
    name: "capo_marketplace_agreement.types.agreement_approval_resource_name.AgreementApprovalResourceName"
    """<p>The name of the product.</p>"""
    deployed_on_aws: NotRequired[
        "capo_marketplace_agreement.types.agreement_approval_deployed_on_aws.AgreementApprovalDeployedOnAws"
    ]
    """<p>Whether the product is deployed on AWS (for example, <code>DEPLOYED</code>).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementApprovalResource) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["type"] = value["type"]
    out["name"] = value["name"]
    if "deployed_on_aws" in value:
        out["deployedOnAws"] = value["deployed_on_aws"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AgreementApprovalResource:
    out: AgreementApprovalResource = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("deployedOnAws") is not None:
        out["deployed_on_aws"] = data["deployedOnAws"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AgreementApprovalResource) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["type"] = value["type"]
    out["name"] = value["name"]
    if "deployed_on_aws" in value:
        out["deployedOnAws"] = value["deployed_on_aws"]
    return out


def deserialize_cbor(data: dict) -> AgreementApprovalResource:
    out: AgreementApprovalResource = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("deployedOnAws") is not None:
        out["deployed_on_aws"] = data["deployedOnAws"]
    return out
