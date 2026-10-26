"""Generated from Smithy shape ``com.amazonaws.vpclattice#HeaderMatch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.boolean
    import capo_vpc_lattice.types.header_match_name
    import capo_vpc_lattice.types.header_match_type


class HeaderMatch(TypedDict, closed=True):
    name: "capo_vpc_lattice.types.header_match_name.HeaderMatchName"
    """<p>The name of the header.</p>"""
    match: "capo_vpc_lattice.types.header_match_type.HeaderMatchType"
    """<p>The header match type.</p>"""
    case_sensitive: NotRequired["capo_vpc_lattice.types.boolean.Boolean"]
    """<p>Indicates whether the match is case sensitive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HeaderMatch) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_vpc_lattice.types.header_match_type

    out["match"] = capo_vpc_lattice.types.header_match_type.serialize_json(
        value["match"]
    )
    if "case_sensitive" in value:
        out["caseSensitive"] = value["case_sensitive"]
    return out


def deserialize_json(data: dict) -> HeaderMatch:
    out: HeaderMatch = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("match") is not None:
        import capo_vpc_lattice.types.header_match_type

        out["match"] = capo_vpc_lattice.types.header_match_type.deserialize_json(
            data["match"]
        )
    else:
        out["match"] = {"$unknown": {"name": ""}}
    if data.get("caseSensitive") is not None:
        out["case_sensitive"] = data["caseSensitive"]
    return out
