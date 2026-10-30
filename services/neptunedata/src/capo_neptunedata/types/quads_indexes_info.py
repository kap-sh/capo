"""Generated from Smithy shape ``com.amazonaws.neptunedata#QuadsIndexesInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptunedata.types.quads_info


class QuadsIndexesInfo(TypedDict, closed=True):
    rdf: NotRequired["capo_neptunedata.types.quads_info.QuadsInfo"]
    """<p>Contains quad index information for the RDF (SPARQL) data model.</p>"""
    pg: NotRequired["capo_neptunedata.types.quads_info.QuadsInfo"]
    """<p>Contains quad index information for the Property Graph (Gremlin/openCypher) data model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuadsIndexesInfo) -> dict:
    out: dict = {}
    if "rdf" in value:
        import capo_neptunedata.types.quads_info

        out["RDF"] = capo_neptunedata.types.quads_info.serialize_json(value["rdf"])
    if "pg" in value:
        import capo_neptunedata.types.quads_info

        out["PG"] = capo_neptunedata.types.quads_info.serialize_json(value["pg"])
    return out


def deserialize_json(data: dict) -> QuadsIndexesInfo:
    out: QuadsIndexesInfo = {}  # type: ignore[typeddict-item]
    if data.get("RDF") is not None:
        import capo_neptunedata.types.quads_info

        out["rdf"] = capo_neptunedata.types.quads_info.deserialize_json(data["RDF"])
    if data.get("PG") is not None:
        import capo_neptunedata.types.quads_info

        out["pg"] = capo_neptunedata.types.quads_info.deserialize_json(data["PG"])
    return out
