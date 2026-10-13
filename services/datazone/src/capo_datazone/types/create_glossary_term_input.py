"""Generated from Smithy shape ``com.amazonaws.datazone#CreateGlossaryTermInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.client_token
    import capo_datazone.types.domain_id
    import capo_datazone.types.glossary_term_id
    import capo_datazone.types.glossary_term_name
    import capo_datazone.types.glossary_term_status
    import capo_datazone.types.long_description
    import capo_datazone.types.short_description
    import capo_datazone.types.term_relations


class CreateGlossaryTermInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which this business glossary term is created.</p>"""
    glossary_identifier: "capo_datazone.types.glossary_term_id.GlossaryTermId"
    """<p>The ID of the business glossary in which this term is created.</p>"""
    name: "capo_datazone.types.glossary_term_name.GlossaryTermName"
    """<p>The name of this business glossary term.</p>"""
    status: NotRequired["capo_datazone.types.glossary_term_status.GlossaryTermStatus"]
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
    client_token: NotRequired["capo_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGlossaryTermInput) -> dict:
    out: dict = {}
    out["glossaryIdentifier"] = value["glossary_identifier"]
    out["name"] = value["name"]
    if "status" in value:
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
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateGlossaryTermInput:
    out: CreateGlossaryTermInput = {}  # type: ignore[typeddict-item]
    if data.get("glossaryIdentifier") is not None:
        out["glossary_identifier"] = data["glossaryIdentifier"]
    else:
        raise DeserializationError(
            "CreateGlossaryTermInput.glossary_identifier required"
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateGlossaryTermInput.name required")
    if data.get("status") is not None:
        import capo_datazone.types.glossary_term_status

        out["status"] = capo_datazone.types.glossary_term_status.deserialize_json(
            data["status"]
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
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: CreateGlossaryTermInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "short_description" in value:
        out["short_description"] = "*** Sensitive Data Redacted ***"
    if "long_description" in value:
        out["long_description"] = "*** Sensitive Data Redacted ***"
    return out
