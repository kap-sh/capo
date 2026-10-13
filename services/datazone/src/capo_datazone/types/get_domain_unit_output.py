"""Generated from Smithy shape ``com.amazonaws.datazone#GetDomainUnitOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.created_at
    import capo_datazone.types.created_by
    import capo_datazone.types.domain_id
    import capo_datazone.types.domain_unit_description
    import capo_datazone.types.domain_unit_id
    import capo_datazone.types.domain_unit_name
    import capo_datazone.types.domain_unit_owners
    import capo_datazone.types.updated_at
    import capo_datazone.types.updated_by


class GetDomainUnitOutput(TypedDict, closed=True):
    id: "capo_datazone.types.domain_unit_id.DomainUnitId"
    """<p>The ID of the domain unit.</p>"""
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain in which the domain unit lives.</p>"""
    name: "capo_datazone.types.domain_unit_name.DomainUnitName"
    """<p>The name of the domain unit.</p>"""
    parent_domain_unit_id: NotRequired[
        "capo_datazone.types.domain_unit_id.DomainUnitId"
    ]
    """<p>The ID of the parent domain unit.</p>"""
    description: NotRequired[
        "capo_datazone.types.domain_unit_description.DomainUnitDescription"
    ]
    """<p>The description of the domain unit.</p>"""
    owners: "capo_datazone.types.domain_unit_owners.DomainUnitOwners"
    """<p>The owners of the domain unit.</p>"""
    created_at: NotRequired["capo_datazone.types.created_at.CreatedAt"]
    """<p>The time stamp at which the domain unit was created.</p>"""
    last_updated_at: NotRequired["capo_datazone.types.updated_at.UpdatedAt"]
    """<p>The timestamp at which the domain unit was last updated.</p>"""
    created_by: NotRequired["capo_datazone.types.created_by.CreatedBy"]
    """<p>The user who created the domain unit.</p>"""
    last_updated_by: NotRequired["capo_datazone.types.updated_by.UpdatedBy"]
    """<p>The user who last updated the domain unit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDomainUnitOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["domainId"] = value["domain_id"]
    out["name"] = value["name"]
    if "parent_domain_unit_id" in value:
        out["parentDomainUnitId"] = value["parent_domain_unit_id"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_datazone.types.domain_unit_owners

    out["owners"] = capo_datazone.types.domain_unit_owners.serialize_json(
        value["owners"]
    )
    if "created_at" in value:
        import capo_datazone.types.created_at

        out["createdAt"] = capo_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import capo_datazone.types.updated_at

        out["lastUpdatedAt"] = capo_datazone.types.updated_at.serialize_json(
            value["last_updated_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "last_updated_by" in value:
        out["lastUpdatedBy"] = value["last_updated_by"]
    return out


def deserialize_json(data: dict) -> GetDomainUnitOutput:
    out: GetDomainUnitOutput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetDomainUnitOutput.id required")
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("GetDomainUnitOutput.domain_id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetDomainUnitOutput.name required")
    if data.get("parentDomainUnitId") is not None:
        out["parent_domain_unit_id"] = data["parentDomainUnitId"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("owners") is not None:
        import capo_datazone.types.domain_unit_owners

        out["owners"] = capo_datazone.types.domain_unit_owners.deserialize_json(
            data["owners"]
        )
    else:
        raise DeserializationError("GetDomainUnitOutput.owners required")
    if data.get("createdAt") is not None:
        import capo_datazone.types.created_at

        out["created_at"] = capo_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if data.get("lastUpdatedAt") is not None:
        import capo_datazone.types.updated_at

        out["last_updated_at"] = capo_datazone.types.updated_at.deserialize_json(
            data["lastUpdatedAt"]
        )
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    if data.get("lastUpdatedBy") is not None:
        out["last_updated_by"] = data["lastUpdatedBy"]
    return out


def redact_sensitive(value: GetDomainUnitOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
