"""Generated from Smithy shape ``com.amazonaws.appmesh#GrpcGatewayRouteMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.grpc_metadata_match_method
    import capo_app_mesh.types.header_name


class GrpcGatewayRouteMetadata(TypedDict, closed=True):
    name: "capo_app_mesh.types.header_name.HeaderName"
    """<p>A name for the gateway route metadata.</p>"""
    invert: NotRequired["bool"]
    """<p>Specify <code>True</code> to match anything except the match criteria. The default value is <code>False</code>.</p>"""
    match: NotRequired[
        "capo_app_mesh.types.grpc_metadata_match_method.GrpcMetadataMatchMethod"
    ]
    """<p>The criteria for determining a metadata match.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GrpcGatewayRouteMetadata) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "invert" in value:
        out["invert"] = value["invert"]
    if "match" in value:
        import capo_app_mesh.types.grpc_metadata_match_method

        out["match"] = capo_app_mesh.types.grpc_metadata_match_method.serialize_json(
            value["match"]
        )
    return out


def deserialize_json(data: dict) -> GrpcGatewayRouteMetadata:
    out: GrpcGatewayRouteMetadata = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("invert") is not None:
        out["invert"] = data["invert"]
    if data.get("match") is not None:
        import capo_app_mesh.types.grpc_metadata_match_method

        out["match"] = capo_app_mesh.types.grpc_metadata_match_method.deserialize_json(
            data["match"]
        )
    return out
