"""Generated from Smithy shape ``com.amazonaws.appmesh#GrpcRouteMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.grpc_route_metadata_match_method
    import capo_app_mesh.types.header_name


class GrpcRouteMetadata(TypedDict, closed=True):
    name: "capo_app_mesh.types.header_name.HeaderName"
    """<p>The name of the route.</p>"""
    invert: NotRequired["bool"]
    """<p>Specify <code>True</code> to match anything except the match criteria. The default value is <code>False</code>.</p>"""
    match: NotRequired[
        "capo_app_mesh.types.grpc_route_metadata_match_method.GrpcRouteMetadataMatchMethod"
    ]
    """<p>An object that represents the data to match from the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GrpcRouteMetadata) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "invert" in value:
        out["invert"] = value["invert"]
    if "match" in value:
        import capo_app_mesh.types.grpc_route_metadata_match_method

        out["match"] = (
            capo_app_mesh.types.grpc_route_metadata_match_method.serialize_json(
                value["match"]
            )
        )
    return out


def deserialize_json(data: dict) -> GrpcRouteMetadata:
    out: GrpcRouteMetadata = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("invert") is not None:
        out["invert"] = data["invert"]
    if data.get("match") is not None:
        import capo_app_mesh.types.grpc_route_metadata_match_method

        out["match"] = (
            capo_app_mesh.types.grpc_route_metadata_match_method.deserialize_json(
                data["match"]
            )
        )
    return out
