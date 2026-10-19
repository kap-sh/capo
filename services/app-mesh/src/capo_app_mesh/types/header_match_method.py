"""Generated from Smithy shape ``com.amazonaws.appmesh#HeaderMatchMethod``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError, SerializationError
from capo_app_mesh.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_app_mesh.types.header_match
    import capo_app_mesh.types.match_range


class _HeaderMatchMethod_exact(TypedDict, closed=True):
    exact: "capo_app_mesh.types.header_match.HeaderMatch"


class _HeaderMatchMethod_regex(TypedDict, closed=True):
    regex: "capo_app_mesh.types.header_match.HeaderMatch"


class _HeaderMatchMethod_range(TypedDict, closed=True):
    range: "capo_app_mesh.types.match_range.MatchRange"


class _HeaderMatchMethod_prefix(TypedDict, closed=True):
    prefix: "capo_app_mesh.types.header_match.HeaderMatch"


class _HeaderMatchMethod_suffix(TypedDict, closed=True):
    suffix: "capo_app_mesh.types.header_match.HeaderMatch"


HeaderMatchMethod: TypeAlias = (
    _HeaderMatchMethod_exact
    | _HeaderMatchMethod_regex
    | _HeaderMatchMethod_range
    | _HeaderMatchMethod_prefix
    | _HeaderMatchMethod_suffix
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: HeaderMatchMethod) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"HeaderMatchMethod: cannot serialize unknown variant {value.name!r}"
        )
    elif "exact" in value:
        return {"exact": value["exact"]}
    elif "regex" in value:
        return {"regex": value["regex"]}
    elif "range" in value:
        import capo_app_mesh.types.match_range

        return {"range": capo_app_mesh.types.match_range.serialize_json(value["range"])}
    elif "prefix" in value:
        return {"prefix": value["prefix"]}
    elif "suffix" in value:
        return {"suffix": value["suffix"]}
    else:
        raise SerializationError("HeaderMatchMethod: no variant present")


def deserialize_json(data: dict) -> HeaderMatchMethod:
    if data.get("exact") is not None:
        return {"exact": data["exact"]}
    elif data.get("regex") is not None:
        return {"regex": data["regex"]}
    elif data.get("range") is not None:
        import capo_app_mesh.types.match_range

        return {
            "range": capo_app_mesh.types.match_range.deserialize_json(data["range"])
        }
    elif data.get("prefix") is not None:
        return {"prefix": data["prefix"]}
    elif data.get("suffix") is not None:
        return {"suffix": data["suffix"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("HeaderMatchMethod: no recognized variant key")
