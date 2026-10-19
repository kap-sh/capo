"""Generated from Smithy shape ``com.amazonaws.datazone#ProjectGrantFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.domain_unit_filter_for_project


class _ProjectGrantFilter_domainUnitFilter(TypedDict, closed=True):
    domainUnitFilter: (
        "capo_datazone.types.domain_unit_filter_for_project.DomainUnitFilterForProject"
    )


ProjectGrantFilter: TypeAlias = (
    _ProjectGrantFilter_domainUnitFilter | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ProjectGrantFilter) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"ProjectGrantFilter: cannot serialize unknown variant {value.name!r}"
        )
    elif "domainUnitFilter" in value:
        import capo_datazone.types.domain_unit_filter_for_project

        return {
            "domainUnitFilter": capo_datazone.types.domain_unit_filter_for_project.serialize_json(
                value["domainUnitFilter"]
            )
        }
    else:
        raise SerializationError("ProjectGrantFilter: no variant present")


def deserialize_json(data: dict) -> ProjectGrantFilter:
    if data.get("domainUnitFilter") is not None:
        import capo_datazone.types.domain_unit_filter_for_project

        return {
            "domainUnitFilter": capo_datazone.types.domain_unit_filter_for_project.deserialize_json(
                data["domainUnitFilter"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("ProjectGrantFilter: no recognized variant key")
