"""Generated from Smithy shape ``com.amazonaws.vpclattice#Matcher``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_vpc_lattice.errors import DeserializationError, SerializationError
from capo_vpc_lattice.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_vpc_lattice.types.http_code_matcher


class MatcherHttpCodeMember(TypedDict, closed=True):
    httpCode: "capo_vpc_lattice.types.http_code_matcher.HttpCodeMatcher"


Matcher: TypeAlias = MatcherHttpCodeMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: Matcher) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Matcher: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "httpCode" in value:
        return {"httpCode": value["httpCode"]}
    else:
        raise SerializationError("Matcher: no variant present")


def deserialize_json(data: dict) -> Matcher:
    if data.get("httpCode") is not None:
        return {"httpCode": data["httpCode"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Matcher: no recognized variant key")
