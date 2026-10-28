"""Generated from Smithy shape ``com.amazonaws.vpclattice#HeaderMatchType``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_vpc_lattice.errors import DeserializationError, SerializationError
from capo_vpc_lattice.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_vpc_lattice.types.header_match_contains
    import capo_vpc_lattice.types.header_match_exact
    import capo_vpc_lattice.types.header_match_prefix


class HeaderMatchTypeExactMember(TypedDict, closed=True):
    exact: "capo_vpc_lattice.types.header_match_exact.HeaderMatchExact"


class HeaderMatchTypePrefixMember(TypedDict, closed=True):
    prefix: "capo_vpc_lattice.types.header_match_prefix.HeaderMatchPrefix"


class HeaderMatchTypeContainsMember(TypedDict, closed=True):
    contains: "capo_vpc_lattice.types.header_match_contains.HeaderMatchContains"


HeaderMatchType: TypeAlias = (
    HeaderMatchTypeExactMember
    | HeaderMatchTypePrefixMember
    | HeaderMatchTypeContainsMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: HeaderMatchType) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"HeaderMatchType: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "exact" in value:
        return {"exact": value["exact"]}
    elif "prefix" in value:
        return {"prefix": value["prefix"]}
    elif "contains" in value:
        return {"contains": value["contains"]}
    else:
        raise SerializationError("HeaderMatchType: no variant present")


def deserialize_json(data: dict) -> HeaderMatchType:
    if data.get("exact") is not None:
        return {"exact": data["exact"]}
    elif data.get("prefix") is not None:
        return {"prefix": data["prefix"]}
    elif data.get("contains") is not None:
        return {"contains": data["contains"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("HeaderMatchType: no recognized variant key")
