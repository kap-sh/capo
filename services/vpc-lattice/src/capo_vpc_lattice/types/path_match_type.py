"""Generated from Smithy shape ``com.amazonaws.vpclattice#PathMatchType``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_vpc_lattice.errors import DeserializationError, SerializationError
from capo_vpc_lattice.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_vpc_lattice.types.path_match_exact
    import capo_vpc_lattice.types.path_match_prefix


class PathMatchTypeExactMember(TypedDict, closed=True):
    exact: "capo_vpc_lattice.types.path_match_exact.PathMatchExact"


class PathMatchTypePrefixMember(TypedDict, closed=True):
    prefix: "capo_vpc_lattice.types.path_match_prefix.PathMatchPrefix"


PathMatchType: TypeAlias = (
    PathMatchTypeExactMember | PathMatchTypePrefixMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: PathMatchType) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"PathMatchType: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "exact" in value:
        return {"exact": value["exact"]}
    elif "prefix" in value:
        return {"prefix": value["prefix"]}
    else:
        raise SerializationError("PathMatchType: no variant present")


def deserialize_json(data: dict) -> PathMatchType:
    if data.get("exact") is not None:
        return {"exact": data["exact"]}
    elif data.get("prefix") is not None:
        return {"prefix": data["prefix"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("PathMatchType: no recognized variant key")
