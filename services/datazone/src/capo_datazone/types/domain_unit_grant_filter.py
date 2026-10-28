"""Generated from Smithy shape ``com.amazonaws.datazone#DomainUnitGrantFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.all_domain_units_grant_filter


class DomainUnitGrantFilterAllDomainUnitsGrantFilterMember(TypedDict, closed=True):
    allDomainUnitsGrantFilter: (
        "capo_datazone.types.all_domain_units_grant_filter.AllDomainUnitsGrantFilter"
    )


DomainUnitGrantFilter: TypeAlias = (
    DomainUnitGrantFilterAllDomainUnitsGrantFilterMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: DomainUnitGrantFilter) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"DomainUnitGrantFilter: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "allDomainUnitsGrantFilter" in value:
        import capo_datazone.types.all_domain_units_grant_filter

        return {
            "allDomainUnitsGrantFilter": capo_datazone.types.all_domain_units_grant_filter.serialize_json(
                value["allDomainUnitsGrantFilter"]
            )
        }
    else:
        raise SerializationError("DomainUnitGrantFilter: no variant present")


def deserialize_json(data: dict) -> DomainUnitGrantFilter:
    if data.get("allDomainUnitsGrantFilter") is not None:
        import capo_datazone.types.all_domain_units_grant_filter

        return {
            "allDomainUnitsGrantFilter": capo_datazone.types.all_domain_units_grant_filter.deserialize_json(
                data["allDomainUnitsGrantFilter"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("DomainUnitGrantFilter: no recognized variant key")
