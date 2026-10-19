"""Generated from Smithy shape ``com.amazonaws.datazone#DomainUnitTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_unit_id


class DomainUnitTarget(TypedDict, closed=True):
    domain_unit_id: "capo_datazone.types.domain_unit_id.DomainUnitId"
    """<p>The ID of the domain unit.</p>"""
    include_child_domain_units: NotRequired["bool"]
    """<p>Specifies whether to apply a rule to the child domain units.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainUnitTarget) -> dict:
    out: dict = {}
    out["domainUnitId"] = value["domain_unit_id"]
    if "include_child_domain_units" in value:
        out["includeChildDomainUnits"] = value["include_child_domain_units"]
    return out


def deserialize_json(data: dict) -> DomainUnitTarget:
    out: DomainUnitTarget = {}  # type: ignore[typeddict-item]
    if data.get("domainUnitId") is not None:
        out["domain_unit_id"] = data["domainUnitId"]
    else:
        out["domain_unit_id"] = ""
    if data.get("includeChildDomainUnits") is not None:
        out["include_child_domain_units"] = data["includeChildDomainUnits"]
    return out
