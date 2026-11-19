"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#Resource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_resource_type
    import capo_marketplace_agreement.types.resource_id


class Resource(TypedDict, closed=True):
    id: NotRequired["capo_marketplace_agreement.types.resource_id.ResourceId"]
    """<p>The unique identifier of the resource.</p> <note> <p>We mention the term resource, which is most commonly a product, so a <code>resourceId</code> is also a <code>productId</code>.</p> </note>"""
    type: NotRequired[
        "capo_marketplace_agreement.types.agreement_resource_type.AgreementResourceType"
    ]
    """<p>Type of the resource, which is the product (for example, <code>SaaSProduct</code>, <code>AmiProduct</code>, <code>ContainerProduct</code>).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Resource) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "type" in value:
        out["type"] = value["type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Resource:
    out: Resource = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("type") is not None:
        out["type"] = data["type"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Resource) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "type" in value:
        out["type"] = value["type"]
    return out


def deserialize_cbor(data: dict) -> Resource:
    out: Resource = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("type") is not None:
        out["type"] = data["type"]
    return out
