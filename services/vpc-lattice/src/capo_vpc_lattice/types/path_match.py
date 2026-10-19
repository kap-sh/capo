"""Generated from Smithy shape ``com.amazonaws.vpclattice#PathMatch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.boolean
    import capo_vpc_lattice.types.path_match_type


class PathMatch(TypedDict, closed=True):
    match: "capo_vpc_lattice.types.path_match_type.PathMatchType"
    """<p>The type of path match.</p>"""
    case_sensitive: NotRequired["capo_vpc_lattice.types.boolean.Boolean"]
    """<p>Indicates whether the match is case sensitive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PathMatch) -> dict:
    out: dict = {}
    import capo_vpc_lattice.types.path_match_type

    out["match"] = capo_vpc_lattice.types.path_match_type.serialize_json(value["match"])
    if "case_sensitive" in value:
        out["caseSensitive"] = value["case_sensitive"]
    return out


def deserialize_json(data: dict) -> PathMatch:
    out: PathMatch = {}  # type: ignore[typeddict-item]
    if data.get("match") is not None:
        import capo_vpc_lattice.types.path_match_type

        out["match"] = capo_vpc_lattice.types.path_match_type.deserialize_json(
            data["match"]
        )
    else:
        import capo_vpc_lattice.types._unknown

        out["match"] = capo_vpc_lattice.types._unknown.UnknownUnionMember("")
    if data.get("caseSensitive") is not None:
        out["case_sensitive"] = data["caseSensitive"]
    return out
