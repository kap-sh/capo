"""Generated from Smithy shape ``com.amazonaws.datazone#CreateDomainUnitOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.created_at
    import capo_datazone.types.created_by
    import capo_datazone.types.domain_id
    import capo_datazone.types.domain_unit_description
    import capo_datazone.types.domain_unit_id
    import capo_datazone.types.domain_unit_ids
    import capo_datazone.types.domain_unit_name
    import capo_datazone.types.domain_unit_owners


class CreateDomainUnitOutput(TypedDict, closed=True):
    id: "capo_datazone.types.domain_unit_id.DomainUnitId"
    """<p>The ID of the domain unit.</p>"""
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where the domain unit was created.</p>"""
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
    ancestor_domain_unit_ids: "capo_datazone.types.domain_unit_ids.DomainUnitIds"
    """<p>The IDs of the ancestor domain units.</p>"""
    created_at: NotRequired["capo_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp at which the domain unit was created.</p>"""
    created_by: NotRequired["capo_datazone.types.created_by.CreatedBy"]
    """<p>The user who created the domain unit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDomainUnitOutput) -> dict:
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
    import capo_datazone.types.domain_unit_ids

    out["ancestorDomainUnitIds"] = capo_datazone.types.domain_unit_ids.serialize_json(
        value["ancestor_domain_unit_ids"]
    )
    if "created_at" in value:
        import capo_datazone.types.created_at

        out["createdAt"] = capo_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    return out


def deserialize_json(data: dict) -> CreateDomainUnitOutput:
    out: CreateDomainUnitOutput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
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
        out["owners"] = []
    if data.get("ancestorDomainUnitIds") is not None:
        import capo_datazone.types.domain_unit_ids

        out["ancestor_domain_unit_ids"] = (
            capo_datazone.types.domain_unit_ids.deserialize_json(
                data["ancestorDomainUnitIds"]
            )
        )
    else:
        out["ancestor_domain_unit_ids"] = []
    if data.get("createdAt") is not None:
        import capo_datazone.types.created_at

        out["created_at"] = capo_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    return out


def redact_sensitive(value: CreateDomainUnitOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
