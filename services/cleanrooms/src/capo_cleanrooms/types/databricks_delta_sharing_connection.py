"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DatabricksDeltaSharingConnection``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.databricks_endpoint_url
    import capo_cleanrooms.types.databricks_object


class DatabricksDeltaSharingConnection(TypedDict, closed=True):
    delta_share_endpoint: (
        "capo_cleanrooms.types.databricks_endpoint_url.DatabricksEndpointUrl"
    )
    """<p>The base URL of a Delta Sharing server that hosts shared datasets.</p>"""
    share_name: "capo_cleanrooms.types.databricks_object.DatabricksObject"
    """<p>Name of the Share used for OpenSharing (Delta Sharing) the Databricks Table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatabricksDeltaSharingConnection) -> dict:
    out: dict = {}
    out["deltaShareEndpoint"] = value["delta_share_endpoint"]
    out["shareName"] = value["share_name"]
    return out


def deserialize_json(data: dict) -> DatabricksDeltaSharingConnection:
    out: DatabricksDeltaSharingConnection = {}  # type: ignore[typeddict-item]
    if data.get("deltaShareEndpoint") is not None:
        out["delta_share_endpoint"] = data["deltaShareEndpoint"]
    else:
        out["delta_share_endpoint"] = ""
    if data.get("shareName") is not None:
        out["share_name"] = data["shareName"]
    else:
        out["share_name"] = ""
    return out
