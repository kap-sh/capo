"""Generated from Smithy shape ``com.amazonaws.continuum#DomainNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_continuum.types.domain_name

DomainNames: TypeAlias = list["capo_continuum.types.domain_name.DomainName"]


# --- restJson1 ser/de ---
def serialize_json(value: DomainNames) -> list:
    return list(value)


def deserialize_json(data: list) -> DomainNames:
    return [item for item in data if item is not None]
