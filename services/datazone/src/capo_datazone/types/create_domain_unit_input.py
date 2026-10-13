"""Generated from Smithy shape ``com.amazonaws.datazone#CreateDomainUnitInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.client_token
    import capo_datazone.types.domain_id
    import capo_datazone.types.domain_unit_description
    import capo_datazone.types.domain_unit_id
    import capo_datazone.types.domain_unit_name


class CreateDomainUnitInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where you want to crate a domain unit.</p>"""
    name: "capo_datazone.types.domain_unit_name.DomainUnitName"
    """<p>The name of the domain unit.</p>"""
    parent_domain_unit_identifier: "capo_datazone.types.domain_unit_id.DomainUnitId"
    """<p>The ID of the parent domain unit.</p>"""
    description: NotRequired[
        "capo_datazone.types.domain_unit_description.DomainUnitDescription"
    ]
    """<p>The description of the domain unit.</p>"""
    client_token: NotRequired["capo_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDomainUnitInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["parentDomainUnitIdentifier"] = value["parent_domain_unit_identifier"]
    if "description" in value:
        out["description"] = value["description"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateDomainUnitInput:
    out: CreateDomainUnitInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateDomainUnitInput.name required")
    if data.get("parentDomainUnitIdentifier") is not None:
        out["parent_domain_unit_identifier"] = data["parentDomainUnitIdentifier"]
    else:
        raise DeserializationError(
            "CreateDomainUnitInput.parent_domain_unit_identifier required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: CreateDomainUnitInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
