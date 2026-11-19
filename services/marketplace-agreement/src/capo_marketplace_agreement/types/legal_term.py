"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#LegalTerm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.document_list
    import capo_marketplace_agreement.types.term_id
    import capo_marketplace_agreement.types.unversioned_term_type


class LegalTerm(TypedDict, closed=True):
    type: NotRequired[
        "capo_marketplace_agreement.types.unversioned_term_type.UnversionedTermType"
    ]
    """<p>Category of the term being updated.</p>"""
    id: NotRequired["capo_marketplace_agreement.types.term_id.TermId"]
    """<p>The unique identifier for the term.</p>"""
    documents: NotRequired[
        "capo_marketplace_agreement.types.document_list.DocumentList"
    ]
    """<p>List of references to legal resources proposed to the buyers. An example is the EULA.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LegalTerm) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "id" in value:
        out["id"] = value["id"]
    if "documents" in value:
        import capo_marketplace_agreement.types.document_list

        out["documents"] = (
            capo_marketplace_agreement.types.document_list.serialize_aws_json_1_0(
                value["documents"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> LegalTerm:
    out: LegalTerm = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("documents") is not None:
        import capo_marketplace_agreement.types.document_list

        out["documents"] = (
            capo_marketplace_agreement.types.document_list.deserialize_aws_json_1_0(
                data["documents"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LegalTerm) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "id" in value:
        out["id"] = value["id"]
    if "documents" in value:
        import capo_marketplace_agreement.types.document_list

        out["documents"] = (
            capo_marketplace_agreement.types.document_list.serialize_cbor(
                value["documents"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> LegalTerm:
    out: LegalTerm = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("documents") is not None:
        import capo_marketplace_agreement.types.document_list

        out["documents"] = (
            capo_marketplace_agreement.types.document_list.deserialize_cbor(
                data["documents"]
            )
        )
    return out
