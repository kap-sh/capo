"""Generated from Smithy shape ``com.amazonaws.datazone#AssetItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.asset_identifier
    import capo_datazone.types.asset_item_additional_attributes
    import capo_datazone.types.asset_name
    import capo_datazone.types.asset_type_identifier
    import capo_datazone.types.created_at
    import capo_datazone.types.created_by
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.external_identifier
    import capo_datazone.types.glossary_terms
    import capo_datazone.types.governed_glossary_terms
    import capo_datazone.types.project_id
    import capo_datazone.types.revision


class AssetItem(TypedDict, closed=True):
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which the inventory asset exists.</p>"""
    identifier: "capo_datazone.types.asset_identifier.AssetIdentifier"
    """<p>the identifier of the Amazon DataZone inventory asset.</p>"""
    name: "capo_datazone.types.asset_name.AssetName"
    """<p>The name of the Amazon DataZone inventory asset.</p>"""
    type_identifier: "capo_datazone.types.asset_type_identifier.AssetTypeIdentifier"
    """<p>The identifier of the asset type of the specified Amazon DataZone inventory asset.</p>"""
    type_revision: "capo_datazone.types.revision.Revision"
    """<p>The revision of the inventory asset type.</p>"""
    external_identifier: NotRequired[
        "capo_datazone.types.external_identifier.ExternalIdentifier"
    ]
    """<p>The external identifier of the Amazon DataZone inventory asset.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of an Amazon DataZone inventory asset.</p>"""
    created_at: NotRequired["capo_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp of when the Amazon DataZone inventory asset was created.</p>"""
    created_by: NotRequired["capo_datazone.types.created_by.CreatedBy"]
    """<p>The Amazon DataZone user who created the inventory asset.</p>"""
    first_revision_created_at: NotRequired["capo_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp of when the first revision of the inventory asset was created.</p>"""
    first_revision_created_by: NotRequired["capo_datazone.types.created_by.CreatedBy"]
    """<p>The Amazon DataZone user who created the first revision of the inventory asset.</p>"""
    glossary_terms: NotRequired["capo_datazone.types.glossary_terms.GlossaryTerms"]
    """<p>The glossary terms attached to the Amazon DataZone inventory asset.</p>"""
    owning_project_id: "capo_datazone.types.project_id.ProjectId"
    """<p>The identifier of the Amazon DataZone project that owns the inventory asset.</p>"""
    additional_attributes: NotRequired[
        "capo_datazone.types.asset_item_additional_attributes.AssetItemAdditionalAttributes"
    ]
    """<p>The additional attributes of a Amazon DataZone inventory asset. </p>"""
    governed_glossary_terms: NotRequired[
        "capo_datazone.types.governed_glossary_terms.GovernedGlossaryTerms"
    ]
    """<p>The restricted glossary terms accociated with an asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetItem) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["identifier"] = value["identifier"]
    out["name"] = value["name"]
    out["typeIdentifier"] = value["type_identifier"]
    out["typeRevision"] = value["type_revision"]
    if "external_identifier" in value:
        out["externalIdentifier"] = value["external_identifier"]
    if "description" in value:
        out["description"] = value["description"]
    if "created_at" in value:
        import capo_datazone.types.created_at

        out["createdAt"] = capo_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "first_revision_created_at" in value:
        import capo_datazone.types.created_at

        out["firstRevisionCreatedAt"] = capo_datazone.types.created_at.serialize_json(
            value["first_revision_created_at"]
        )
    if "first_revision_created_by" in value:
        out["firstRevisionCreatedBy"] = value["first_revision_created_by"]
    if "glossary_terms" in value:
        import capo_datazone.types.glossary_terms

        out["glossaryTerms"] = capo_datazone.types.glossary_terms.serialize_json(
            value["glossary_terms"]
        )
    out["owningProjectId"] = value["owning_project_id"]
    if "additional_attributes" in value:
        import capo_datazone.types.asset_item_additional_attributes

        out["additionalAttributes"] = (
            capo_datazone.types.asset_item_additional_attributes.serialize_json(
                value["additional_attributes"]
            )
        )
    if "governed_glossary_terms" in value:
        import capo_datazone.types.governed_glossary_terms

        out["governedGlossaryTerms"] = (
            capo_datazone.types.governed_glossary_terms.serialize_json(
                value["governed_glossary_terms"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssetItem:
    out: AssetItem = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("AssetItem.domain_id required")
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("AssetItem.identifier required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AssetItem.name required")
    if data.get("typeIdentifier") is not None:
        out["type_identifier"] = data["typeIdentifier"]
    else:
        raise DeserializationError("AssetItem.type_identifier required")
    if data.get("typeRevision") is not None:
        out["type_revision"] = data["typeRevision"]
    else:
        raise DeserializationError("AssetItem.type_revision required")
    if data.get("externalIdentifier") is not None:
        out["external_identifier"] = data["externalIdentifier"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("createdAt") is not None:
        import capo_datazone.types.created_at

        out["created_at"] = capo_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    if data.get("firstRevisionCreatedAt") is not None:
        import capo_datazone.types.created_at

        out["first_revision_created_at"] = (
            capo_datazone.types.created_at.deserialize_json(
                data["firstRevisionCreatedAt"]
            )
        )
    if data.get("firstRevisionCreatedBy") is not None:
        out["first_revision_created_by"] = data["firstRevisionCreatedBy"]
    if data.get("glossaryTerms") is not None:
        import capo_datazone.types.glossary_terms

        out["glossary_terms"] = capo_datazone.types.glossary_terms.deserialize_json(
            data["glossaryTerms"]
        )
    if data.get("owningProjectId") is not None:
        out["owning_project_id"] = data["owningProjectId"]
    else:
        raise DeserializationError("AssetItem.owning_project_id required")
    if data.get("additionalAttributes") is not None:
        import capo_datazone.types.asset_item_additional_attributes

        out["additional_attributes"] = (
            capo_datazone.types.asset_item_additional_attributes.deserialize_json(
                data["additionalAttributes"]
            )
        )
    if data.get("governedGlossaryTerms") is not None:
        import capo_datazone.types.governed_glossary_terms

        out["governed_glossary_terms"] = (
            capo_datazone.types.governed_glossary_terms.deserialize_json(
                data["governedGlossaryTerms"]
            )
        )
    return out


def redact_sensitive(value: AssetItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "additional_attributes" in value:
        import capo_datazone.types.asset_item_additional_attributes

        out["additional_attributes"] = (
            capo_datazone.types.asset_item_additional_attributes.redact_sensitive(
                value["additional_attributes"]
            )
        )
    return out
