"""Generated from Smithy shape ``com.amazonaws.datazone#CreateGlossaryTermOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.glossary_id
    import capo_datazone.types.glossary_term_id
    import capo_datazone.types.glossary_term_name
    import capo_datazone.types.glossary_term_status
    import capo_datazone.types.glossary_usage_restrictions
    import capo_datazone.types.long_description
    import capo_datazone.types.short_description
    import capo_datazone.types.term_relations


class CreateGlossaryTermOutput(TypedDict, closed=True):
    id: "capo_datazone.types.glossary_term_id.GlossaryTermId"
    """<p>The ID of this business glossary term.</p>"""
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which this business glossary term is created.</p>"""
    glossary_id: "capo_datazone.types.glossary_id.GlossaryId"
    """<p>The ID of the business glossary in which this term is created.</p>"""
    name: "capo_datazone.types.glossary_term_name.GlossaryTermName"
    """<p>The name of this business glossary term.</p>"""
    status: "capo_datazone.types.glossary_term_status.GlossaryTermStatus"
    """<p>The status of this business glossary term.</p>"""
    short_description: NotRequired[
        "capo_datazone.types.short_description.ShortDescription"
    ]
    """<p>The short description of this business glossary term.</p>"""
    long_description: NotRequired[
        "capo_datazone.types.long_description.LongDescription"
    ]
    """<p>The long description of this business glossary term.</p>"""
    term_relations: NotRequired["capo_datazone.types.term_relations.TermRelations"]
    """<p>The term relations of this business glossary term.</p>"""
    usage_restrictions: NotRequired[
        "capo_datazone.types.glossary_usage_restrictions.GlossaryUsageRestrictions"
    ]
    """<p>The usage restriction of the restricted glossary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGlossaryTermOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["domainId"] = value["domain_id"]
    out["glossaryId"] = value["glossary_id"]
    out["name"] = value["name"]
    import capo_datazone.types.glossary_term_status

    out["status"] = capo_datazone.types.glossary_term_status.serialize_json(
        value["status"]
    )
    if "short_description" in value:
        out["shortDescription"] = value["short_description"]
    if "long_description" in value:
        out["longDescription"] = value["long_description"]
    if "term_relations" in value:
        import capo_datazone.types.term_relations

        out["termRelations"] = capo_datazone.types.term_relations.serialize_json(
            value["term_relations"]
        )
    if "usage_restrictions" in value:
        import capo_datazone.types.glossary_usage_restrictions

        out["usageRestrictions"] = (
            capo_datazone.types.glossary_usage_restrictions.serialize_json(
                value["usage_restrictions"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateGlossaryTermOutput:
    out: CreateGlossaryTermOutput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
    if data.get("glossaryId") is not None:
        out["glossary_id"] = data["glossaryId"]
    else:
        out["glossary_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("status") is not None:
        import capo_datazone.types.glossary_term_status

        out["status"] = capo_datazone.types.glossary_term_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_datazone.types.glossary_term_status.GlossaryTermStatus", ""
        )
    if data.get("shortDescription") is not None:
        out["short_description"] = data["shortDescription"]
    if data.get("longDescription") is not None:
        out["long_description"] = data["longDescription"]
    if data.get("termRelations") is not None:
        import capo_datazone.types.term_relations

        out["term_relations"] = capo_datazone.types.term_relations.deserialize_json(
            data["termRelations"]
        )
    if data.get("usageRestrictions") is not None:
        import capo_datazone.types.glossary_usage_restrictions

        out["usage_restrictions"] = (
            capo_datazone.types.glossary_usage_restrictions.deserialize_json(
                data["usageRestrictions"]
            )
        )
    return out


def redact_sensitive(value: CreateGlossaryTermOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "short_description" in value:
        out["short_description"] = "*** Sensitive Data Redacted ***"
    if "long_description" in value:
        out["long_description"] = "*** Sensitive Data Redacted ***"
    return out
