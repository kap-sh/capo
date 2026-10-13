"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateGlossaryTermInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.glossary_term_id
    import capo_datazone.types.glossary_term_name
    import capo_datazone.types.glossary_term_status
    import capo_datazone.types.long_description
    import capo_datazone.types.short_description
    import capo_datazone.types.term_relations


class UpdateGlossaryTermInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which a business glossary term is to be updated.</p>"""
    glossary_identifier: NotRequired[
        "capo_datazone.types.glossary_term_id.GlossaryTermId"
    ]
    """<p>The identifier of the business glossary in which a term is to be updated.</p>"""
    identifier: "capo_datazone.types.glossary_term_id.GlossaryTermId"
    """<p>The identifier of the business glossary term that is to be updated.</p>"""
    name: NotRequired["capo_datazone.types.glossary_term_name.GlossaryTermName"]
    """<p>The name to be updated as part of the <code>UpdateGlossaryTerm</code> action.</p>"""
    short_description: NotRequired[
        "capo_datazone.types.short_description.ShortDescription"
    ]
    """<p>The short description to be updated as part of the <code>UpdateGlossaryTerm</code> action.</p>"""
    long_description: NotRequired[
        "capo_datazone.types.long_description.LongDescription"
    ]
    """<p>The long description to be updated as part of the <code>UpdateGlossaryTerm</code> action.</p>"""
    term_relations: NotRequired["capo_datazone.types.term_relations.TermRelations"]
    """<p>The term relations to be updated as part of the <code>UpdateGlossaryTerm</code> action.</p>"""
    status: NotRequired["capo_datazone.types.glossary_term_status.GlossaryTermStatus"]
    """<p>The status to be updated as part of the <code>UpdateGlossaryTerm</code> action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGlossaryTermInput) -> dict:
    out: dict = {}
    if "glossary_identifier" in value:
        out["glossaryIdentifier"] = value["glossary_identifier"]
    if "name" in value:
        out["name"] = value["name"]
    if "short_description" in value:
        out["shortDescription"] = value["short_description"]
    if "long_description" in value:
        out["longDescription"] = value["long_description"]
    if "term_relations" in value:
        import capo_datazone.types.term_relations

        out["termRelations"] = capo_datazone.types.term_relations.serialize_json(
            value["term_relations"]
        )
    if "status" in value:
        import capo_datazone.types.glossary_term_status

        out["status"] = capo_datazone.types.glossary_term_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> UpdateGlossaryTermInput:
    out: UpdateGlossaryTermInput = {}  # type: ignore[typeddict-item]
    if data.get("glossaryIdentifier") is not None:
        out["glossary_identifier"] = data["glossaryIdentifier"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("shortDescription") is not None:
        out["short_description"] = data["shortDescription"]
    if data.get("longDescription") is not None:
        out["long_description"] = data["longDescription"]
    if data.get("termRelations") is not None:
        import capo_datazone.types.term_relations

        out["term_relations"] = capo_datazone.types.term_relations.deserialize_json(
            data["termRelations"]
        )
    if data.get("status") is not None:
        import capo_datazone.types.glossary_term_status

        out["status"] = capo_datazone.types.glossary_term_status.deserialize_json(
            data["status"]
        )
    return out


def redact_sensitive(value: UpdateGlossaryTermInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "short_description" in value:
        out["short_description"] = "*** Sensitive Data Redacted ***"
    if "long_description" in value:
        out["long_description"] = "*** Sensitive Data Redacted ***"
    return out
