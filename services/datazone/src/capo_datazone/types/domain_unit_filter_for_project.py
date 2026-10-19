"""Generated from Smithy shape ``com.amazonaws.datazone#DomainUnitFilterForProject``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_unit_id


class DomainUnitFilterForProject(TypedDict, closed=True):
    domain_unit: "capo_datazone.types.domain_unit_id.DomainUnitId"
    """<p>The domain unit ID to use in the filter.</p>"""
    include_child_domain_units: "bool"
    """<p>Specifies whether to include child domain units.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainUnitFilterForProject) -> dict:
    out: dict = {}
    out["domainUnit"] = value["domain_unit"]
    out["includeChildDomainUnits"] = value.get("include_child_domain_units", False)
    return out


def deserialize_json(data: dict) -> DomainUnitFilterForProject:
    out: DomainUnitFilterForProject = {}  # type: ignore[typeddict-item]
    if data.get("domainUnit") is not None:
        out["domain_unit"] = data["domainUnit"]
    else:
        out["domain_unit"] = ""
    if data.get("includeChildDomainUnits") is not None:
        out["include_child_domain_units"] = data["includeChildDomainUnits"]
    else:
        out["include_child_domain_units"] = False
    return out
