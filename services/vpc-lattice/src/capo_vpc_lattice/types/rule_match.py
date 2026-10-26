"""Generated from Smithy shape ``com.amazonaws.vpclattice#RuleMatch``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_vpc_lattice.errors import DeserializationError, SerializationError
from capo_vpc_lattice.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_vpc_lattice.types.http_match


class _RuleMatch_httpMatch(TypedDict, closed=True):
    httpMatch: "capo_vpc_lattice.types.http_match.HttpMatch"


RuleMatch: TypeAlias = _RuleMatch_httpMatch | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: RuleMatch) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RuleMatch: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "httpMatch" in value:
        import capo_vpc_lattice.types.http_match

        return {
            "httpMatch": capo_vpc_lattice.types.http_match.serialize_json(
                value["httpMatch"]
            )
        }
    else:
        raise SerializationError("RuleMatch: no variant present")


def deserialize_json(data: dict) -> RuleMatch:
    if data.get("httpMatch") is not None:
        import capo_vpc_lattice.types.http_match

        return {
            "httpMatch": capo_vpc_lattice.types.http_match.deserialize_json(
                data["httpMatch"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("RuleMatch: no recognized variant key")
