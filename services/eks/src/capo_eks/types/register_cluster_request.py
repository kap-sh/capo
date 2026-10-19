"""Generated from Smithy shape ``com.amazonaws.eks#RegisterClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_eks.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eks.types.cluster_name
    import capo_eks.types.connector_config_request
    import capo_eks.types.string
    import capo_eks.types.tag_map


class RegisterClusterRequest(TypedDict, closed=True):
    name: "capo_eks.types.cluster_name.ClusterName"
    """<p>A unique name for this cluster in your Amazon Web Services Region.</p>"""
    connector_config: "capo_eks.types.connector_config_request.ConnectorConfigRequest"
    """<p>The configuration settings required to connect the Kubernetes cluster to the Amazon EKS control plane.</p>"""
    client_request_token: NotRequired["capo_eks.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    tags: NotRequired["capo_eks.types.tag_map.TagMap"]
    """<p>Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or Amazon Web Services resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterClusterRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_eks.types.connector_config_request

    out["connectorConfig"] = capo_eks.types.connector_config_request.serialize_json(
        value["connector_config"]
    )
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import capo_eks.types.tag_map

        out["tags"] = capo_eks.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> RegisterClusterRequest:
    out: RegisterClusterRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("connectorConfig") is not None:
        import capo_eks.types.connector_config_request

        out["connector_config"] = (
            capo_eks.types.connector_config_request.deserialize_json(
                data["connectorConfig"]
            )
        )
    else:
        raise DeserializationError("RegisterClusterRequest.connector_config required")
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    if data.get("tags") is not None:
        import capo_eks.types.tag_map

        out["tags"] = capo_eks.types.tag_map.deserialize_json(data["tags"])
    return out
