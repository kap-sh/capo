"""Generated from Smithy shape ``com.amazonaws.eks#ServerException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_eks.errors import ServiceError

if TYPE_CHECKING:
    import capo_eks.types.string


class ServerException_(TypedDict, closed=True):
    cluster_name: NotRequired["capo_eks.types.string.String"]
    """<p>The Amazon EKS cluster associated with the exception.</p>"""
    nodegroup_name: NotRequired["capo_eks.types.string.String"]
    """<p>The Amazon EKS managed node group associated with the exception.</p>"""
    addon_name: NotRequired["capo_eks.types.string.String"]
    """<p>The Amazon EKS add-on name associated with the exception.</p>"""
    subscription_id: NotRequired["capo_eks.types.string.String"]
    """<p>The Amazon EKS subscription ID with the exception.</p>"""
    message: NotRequired["capo_eks.types.string.String"]
    """<p>These errors are usually caused by a server-side issue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServerException_) -> dict:
    out: dict = {}
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    if "nodegroup_name" in value:
        out["nodegroupName"] = value["nodegroup_name"]
    if "addon_name" in value:
        out["addonName"] = value["addon_name"]
    if "subscription_id" in value:
        out["subscriptionId"] = value["subscription_id"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ServerException_:
    out: ServerException_ = {}  # type: ignore[typeddict-item]
    if data.get("clusterName") is not None:
        out["cluster_name"] = data["clusterName"]
    if data.get("nodegroupName") is not None:
        out["nodegroup_name"] = data["nodegroupName"]
    if data.get("addonName") is not None:
        out["addon_name"] = data["addonName"]
    if data.get("subscriptionId") is not None:
        out["subscription_id"] = data["subscriptionId"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.eks#ServerException``."""

    code: str | None = "ServerException"

    def __init__(
        self,
        data: ServerException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ServerException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ServerException":
        return cls(deserialize_json(data), message, response=response)
