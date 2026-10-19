"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#LegalTerm``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.document_list
    import capo_marketplace_discovery.types.term_id
    import capo_marketplace_discovery.types.term_type


class LegalTerm(TypedDict, closed=True):
    id: "capo_marketplace_discovery.types.term_id.TermId"
    """<p>The unique identifier of the term.</p>"""
    type: "capo_marketplace_discovery.types.term_type.TermType"
    """<p>The category of the term.</p>"""
    documents: "capo_marketplace_discovery.types.document_list.DocumentList"
    """<p>The legal documents proposed to the buyer as part of this term.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LegalTerm) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import capo_marketplace_discovery.types.term_type

    out["type"] = capo_marketplace_discovery.types.term_type.serialize_json(
        value["type"]
    )
    import capo_marketplace_discovery.types.document_list

    out["documents"] = capo_marketplace_discovery.types.document_list.serialize_json(
        value["documents"]
    )
    return out


def deserialize_json(data: dict) -> LegalTerm:
    out: LegalTerm = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("type") is not None:
        import capo_marketplace_discovery.types.term_type

        out["type"] = capo_marketplace_discovery.types.term_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_marketplace_discovery.types.term_type.TermType", ""
        )
    if data.get("documents") is not None:
        import capo_marketplace_discovery.types.document_list

        out["documents"] = (
            capo_marketplace_discovery.types.document_list.deserialize_json(
                data["documents"]
            )
        )
    else:
        out["documents"] = []
    return out
