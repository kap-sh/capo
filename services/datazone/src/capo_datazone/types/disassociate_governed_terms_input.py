"""Generated from Smithy shape ``com.amazonaws.datazone#DisassociateGovernedTermsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.entity_identifier
    import capo_datazone.types.governed_entity_type
    import capo_datazone.types.governed_glossary_terms


class DisassociateGovernedTermsInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where you want to disassociate restricted terms from an asset.</p>"""
    entity_identifier: "capo_datazone.types.entity_identifier.EntityIdentifier"
    """<p>The ID of an asset from which you want to disassociate restricted terms.</p>"""
    entity_type: "capo_datazone.types.governed_entity_type.GovernedEntityType"
    """<p>The type of the asset from which you want to disassociate restricted terms.</p>"""
    governed_glossary_terms: (
        "capo_datazone.types.governed_glossary_terms.GovernedGlossaryTerms"
    )
    """<p>The restricted glossary terms that you want to disassociate from an asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateGovernedTermsInput) -> dict:
    out: dict = {}
    import capo_datazone.types.governed_glossary_terms

    out["governedGlossaryTerms"] = (
        capo_datazone.types.governed_glossary_terms.serialize_json(
            value["governed_glossary_terms"]
        )
    )
    return out


def deserialize_json(data: dict) -> DisassociateGovernedTermsInput:
    out: DisassociateGovernedTermsInput = {}  # type: ignore[typeddict-item]
    if data.get("governedGlossaryTerms") is not None:
        import capo_datazone.types.governed_glossary_terms

        out["governed_glossary_terms"] = (
            capo_datazone.types.governed_glossary_terms.deserialize_json(
                data["governedGlossaryTerms"]
            )
        )
    else:
        out["governed_glossary_terms"] = []
    return out
