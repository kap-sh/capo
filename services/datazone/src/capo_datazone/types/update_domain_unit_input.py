"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateDomainUnitInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.domain_unit_description
    import capo_datazone.types.domain_unit_id
    import capo_datazone.types.domain_unit_name


class UpdateDomainUnitInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where you want to update a domain unit.</p>"""
    identifier: "capo_datazone.types.domain_unit_id.DomainUnitId"
    """<p>The ID of the domain unit that you want to update.</p>"""
    description: NotRequired[
        "capo_datazone.types.domain_unit_description.DomainUnitDescription"
    ]
    """<p>The description of the domain unit that you want to update.</p>"""
    name: NotRequired["capo_datazone.types.domain_unit_name.DomainUnitName"]
    """<p>The name of the domain unit that you want to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDomainUnitInput) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateDomainUnitInput:
    out: UpdateDomainUnitInput = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    return out


def redact_sensitive(value: UpdateDomainUnitInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
