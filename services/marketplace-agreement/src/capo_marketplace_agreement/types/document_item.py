"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#DocumentItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.bounded_string


class DocumentItem(TypedDict, closed=True):
    type: NotRequired["capo_marketplace_agreement.types.bounded_string.BoundedString"]
    """<p>Category of the document. Document types include:</p> <ul> <li> <p> <code>CustomEula</code> – A custom EULA provided by you as seller. A URL for a EULA stored in an accessible Amazon S3 bucket is required for this document type.</p> </li> <li> <p> <code>CustomDsa</code> – A custom Data Subscription Agreement (DSA) provided by you as seller. A URL for a DSA stored in an accessible Amazon S3 bucket is required for this document type.</p> </li> <li> <p> <code>StandardEula</code> – The Standard Contract for AWS Marketplace (SCMP). For more information about SCMP, see the AWS Marketplace Seller Guide. You don't provide a URL for this type because it's managed by AWS Marketplace.</p> </li> <li> <p> <code>StandardDsa</code> – DSA for AWS Marketplace. For more information about the DSA, see the AWS Data Exchange User Guide. You don't provide a URL for this type because it's managed by AWS Marketplace.</p> </li> </ul>"""
    url: NotRequired["capo_marketplace_agreement.types.bounded_string.BoundedString"]
    """<p>A URL to the legal document for buyers to read. Required when <code>Type</code> is <code>CustomEula</code>.</p>"""
    version: NotRequired[
        "capo_marketplace_agreement.types.bounded_string.BoundedString"
    ]
    """<p>Version of standard contracts provided by AWS Marketplace. Required when Type is <code>StandardEula</code> or <code>StandardDsa</code>. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DocumentItem) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "url" in value:
        out["url"] = value["url"]
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DocumentItem:
    out: DocumentItem = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("url") is not None:
        out["url"] = data["url"]
    if data.get("version") is not None:
        out["version"] = data["version"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DocumentItem) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "url" in value:
        out["url"] = value["url"]
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_cbor(data: dict) -> DocumentItem:
    out: DocumentItem = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("url") is not None:
        out["url"] = data["url"]
    if data.get("version") is not None:
        out["version"] = data["version"]
    return out
