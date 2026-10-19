"""Generated from Smithy shape ``com.amazonaws.datazone#GlossaryTermItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.created_at
    import capo_datazone.types.created_by
    import capo_datazone.types.domain_id
    import capo_datazone.types.glossary_id
    import capo_datazone.types.glossary_term_id
    import capo_datazone.types.glossary_term_item_additional_attributes
    import capo_datazone.types.glossary_term_name
    import capo_datazone.types.glossary_term_status
    import capo_datazone.types.glossary_usage_restrictions
    import capo_datazone.types.long_description
    import capo_datazone.types.short_description
    import capo_datazone.types.term_relations
    import capo_datazone.types.updated_at
    import capo_datazone.types.updated_by


class GlossaryTermItem(TypedDict, closed=True):
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which the business glossary exists.</p>"""
    glossary_id: "capo_datazone.types.glossary_id.GlossaryId"
    """<p>The identifier of the business glossary to which the term belongs.</p>"""
    id: "capo_datazone.types.glossary_term_id.GlossaryTermId"
    """<p>The identifier of the business glossary term.</p>"""
    name: "capo_datazone.types.glossary_term_name.GlossaryTermName"
    """<p>The name of the business glossary term.</p>"""
    short_description: NotRequired[
        "capo_datazone.types.short_description.ShortDescription"
    ]
    """<p>The short description of the business glossary term.</p>"""
    usage_restrictions: NotRequired[
        "capo_datazone.types.glossary_usage_restrictions.GlossaryUsageRestrictions"
    ]
    """<p>The usage restrictions associated with a goverened glossary term.</p>"""
    long_description: NotRequired[
        "capo_datazone.types.long_description.LongDescription"
    ]
    """<p>The long description of the business glossary term.</p>"""
    term_relations: NotRequired["capo_datazone.types.term_relations.TermRelations"]
    """<p>The relations of the business glossary term.</p>"""
    status: "capo_datazone.types.glossary_term_status.GlossaryTermStatus"
    """<p>The status of the business glossary term.</p>"""
    created_at: NotRequired["capo_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp of when a business glossary term was created.</p>"""
    created_by: NotRequired["capo_datazone.types.created_by.CreatedBy"]
    """<p>The Amazon DataZone user who created the business glossary.</p>"""
    updated_at: NotRequired["capo_datazone.types.updated_at.UpdatedAt"]
    """<p>The timestamp of when a business glossary term was updated.</p>"""
    updated_by: NotRequired["capo_datazone.types.updated_by.UpdatedBy"]
    """<p>The Amazon DataZone user who updated the business glossary term.</p>"""
    additional_attributes: NotRequired[
        "capo_datazone.types.glossary_term_item_additional_attributes.GlossaryTermItemAdditionalAttributes"
    ]
    """<p>The additional attributes of an Amazon DataZone glossary term.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GlossaryTermItem) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["glossaryId"] = value["glossary_id"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    if "short_description" in value:
        out["shortDescription"] = value["short_description"]
    if "usage_restrictions" in value:
        import capo_datazone.types.glossary_usage_restrictions

        out["usageRestrictions"] = (
            capo_datazone.types.glossary_usage_restrictions.serialize_json(
                value["usage_restrictions"]
            )
        )
    if "long_description" in value:
        out["longDescription"] = value["long_description"]
    if "term_relations" in value:
        import capo_datazone.types.term_relations

        out["termRelations"] = capo_datazone.types.term_relations.serialize_json(
            value["term_relations"]
        )
    import capo_datazone.types.glossary_term_status

    out["status"] = capo_datazone.types.glossary_term_status.serialize_json(
        value["status"]
    )
    if "created_at" in value:
        import capo_datazone.types.created_at

        out["createdAt"] = capo_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "updated_at" in value:
        import capo_datazone.types.updated_at

        out["updatedAt"] = capo_datazone.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    if "additional_attributes" in value:
        import capo_datazone.types.glossary_term_item_additional_attributes

        out["additionalAttributes"] = (
            capo_datazone.types.glossary_term_item_additional_attributes.serialize_json(
                value["additional_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> GlossaryTermItem:
    out: GlossaryTermItem = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
    if data.get("glossaryId") is not None:
        out["glossary_id"] = data["glossaryId"]
    else:
        out["glossary_id"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("shortDescription") is not None:
        out["short_description"] = data["shortDescription"]
    if data.get("usageRestrictions") is not None:
        import capo_datazone.types.glossary_usage_restrictions

        out["usage_restrictions"] = (
            capo_datazone.types.glossary_usage_restrictions.deserialize_json(
                data["usageRestrictions"]
            )
        )
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
    else:
        import typing

        out["status"] = typing.cast(
            "capo_datazone.types.glossary_term_status.GlossaryTermStatus", ""
        )
    if data.get("createdAt") is not None:
        import capo_datazone.types.created_at

        out["created_at"] = capo_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    if data.get("updatedAt") is not None:
        import capo_datazone.types.updated_at

        out["updated_at"] = capo_datazone.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if data.get("updatedBy") is not None:
        out["updated_by"] = data["updatedBy"]
    if data.get("additionalAttributes") is not None:
        import capo_datazone.types.glossary_term_item_additional_attributes

        out["additional_attributes"] = (
            capo_datazone.types.glossary_term_item_additional_attributes.deserialize_json(
                data["additionalAttributes"]
            )
        )
    return out


def redact_sensitive(value: GlossaryTermItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "short_description" in value:
        out["short_description"] = "*** Sensitive Data Redacted ***"
    if "long_description" in value:
        out["long_description"] = "*** Sensitive Data Redacted ***"
    return out
