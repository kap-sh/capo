"""Generated from Smithy shape ``com.amazonaws.eks#UpdateClusterVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_eks.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eks.types.boolean
    import capo_eks.types.rollback_config
    import capo_eks.types.string


class UpdateClusterVersionRequest(TypedDict, closed=True):
    name: "capo_eks.types.string.String"
    """<p>The name of the Amazon EKS cluster to update.</p>"""
    version: "capo_eks.types.string.String"
    """<p>The desired Kubernetes version following a successful update.</p>"""
    client_request_token: NotRequired["capo_eks.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    force: NotRequired["capo_eks.types.boolean.Boolean"]
    """<p>Set this value to <code>true</code> to override upgrade-blocking or rollback-blocking readiness checks when updating a cluster.</p>"""
    rollback_config: NotRequired["capo_eks.types.rollback_config.RollbackConfig"]
    """<p>The rollback configuration for the cluster version rollback.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateClusterVersionRequest) -> dict:
    out: dict = {}
    out["version"] = value["version"]
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    if "force" in value:
        out["force"] = value["force"]
    if "rollback_config" in value:
        import capo_eks.types.rollback_config

        out["rollbackConfig"] = capo_eks.types.rollback_config.serialize_json(
            value["rollback_config"]
        )
    return out


def deserialize_json(data: dict) -> UpdateClusterVersionRequest:
    out: UpdateClusterVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        raise DeserializationError("UpdateClusterVersionRequest.version required")
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    if data.get("force") is not None:
        out["force"] = data["force"]
    if data.get("rollbackConfig") is not None:
        import capo_eks.types.rollback_config

        out["rollback_config"] = capo_eks.types.rollback_config.deserialize_json(
            data["rollbackConfig"]
        )
    return out
