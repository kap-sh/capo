"""Generated from Smithy shape ``com.amazonaws.datazone#GlossaryItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.created_at
    import capo_datazone.types.created_by
    import capo_datazone.types.domain_id
    import capo_datazone.types.glossary_description
    import capo_datazone.types.glossary_id
    import capo_datazone.types.glossary_item_additional_attributes
    import capo_datazone.types.glossary_name
    import capo_datazone.types.glossary_status
    import capo_datazone.types.glossary_usage_restrictions
    import capo_datazone.types.project_id
    import capo_datazone.types.updated_at
    import capo_datazone.types.updated_by


class GlossaryItem(TypedDict, closed=True):
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which the business glossary exists.</p>"""
    id: "capo_datazone.types.glossary_id.GlossaryId"
    """<p>The identifier of the glossary.</p>"""
    name: "capo_datazone.types.glossary_name.GlossaryName"
    """<p>The name of the glossary.</p>"""
    owning_project_id: "capo_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project that owns the business glosary.</p>"""
    description: NotRequired[
        "capo_datazone.types.glossary_description.GlossaryDescription"
    ]
    """<p>The business glossary description.</p>"""
    status: "capo_datazone.types.glossary_status.GlossaryStatus"
    """<p>The business glossary status.</p>"""
    usage_restrictions: NotRequired[
        "capo_datazone.types.glossary_usage_restrictions.GlossaryUsageRestrictions"
    ]
    """<p>The usage restrictions associated with a goverened glossary term.</p>"""
    created_at: NotRequired["capo_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp of when the glossary was created.</p>"""
    created_by: NotRequired["capo_datazone.types.created_by.CreatedBy"]
    """<p>The Amazon DataZone user who created the glossary.</p>"""
    updated_at: NotRequired["capo_datazone.types.updated_at.UpdatedAt"]
    """<p>The timestamp of when the business glossary was updated.</p>"""
    updated_by: NotRequired["capo_datazone.types.updated_by.UpdatedBy"]
    """<p>The Amazon DataZone user who updated the business glossary.</p>"""
    additional_attributes: NotRequired[
        "capo_datazone.types.glossary_item_additional_attributes.GlossaryItemAdditionalAttributes"
    ]
    """<p>The additional attributes of an Amazon DataZone glossary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GlossaryItem) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["owningProjectId"] = value["owning_project_id"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_datazone.types.glossary_status

    out["status"] = capo_datazone.types.glossary_status.serialize_json(value["status"])
    if "usage_restrictions" in value:
        import capo_datazone.types.glossary_usage_restrictions

        out["usageRestrictions"] = (
            capo_datazone.types.glossary_usage_restrictions.serialize_json(
                value["usage_restrictions"]
            )
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
        import capo_datazone.types.glossary_item_additional_attributes

        out["additionalAttributes"] = (
            capo_datazone.types.glossary_item_additional_attributes.serialize_json(
                value["additional_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> GlossaryItem:
    out: GlossaryItem = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("GlossaryItem.domain_id required")
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GlossaryItem.id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GlossaryItem.name required")
    if data.get("owningProjectId") is not None:
        out["owning_project_id"] = data["owningProjectId"]
    else:
        raise DeserializationError("GlossaryItem.owning_project_id required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("status") is not None:
        import capo_datazone.types.glossary_status

        out["status"] = capo_datazone.types.glossary_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GlossaryItem.status required")
    if data.get("usageRestrictions") is not None:
        import capo_datazone.types.glossary_usage_restrictions

        out["usage_restrictions"] = (
            capo_datazone.types.glossary_usage_restrictions.deserialize_json(
                data["usageRestrictions"]
            )
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
        import capo_datazone.types.glossary_item_additional_attributes

        out["additional_attributes"] = (
            capo_datazone.types.glossary_item_additional_attributes.deserialize_json(
                data["additionalAttributes"]
            )
        )
    return out


def redact_sensitive(value: GlossaryItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
