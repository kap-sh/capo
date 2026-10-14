"""Generated from Smithy shape ``com.amazonaws.eks#UnsupportedAvailabilityZoneException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_eks.errors import ServiceError

if TYPE_CHECKING:
    import capo_eks.types.string
    import capo_eks.types.string_list


class UnsupportedAvailabilityZoneException_(TypedDict, closed=True):
    message: NotRequired["capo_eks.types.string.String"]
    """<p>At least one of your specified cluster subnets is in an Availability Zone that does not support Amazon EKS. The exception output specifies the supported Availability Zones for your account, from which you can choose subnets for your cluster.</p>"""
    cluster_name: NotRequired["capo_eks.types.string.String"]
    """<p>The Amazon EKS cluster associated with the exception.</p>"""
    nodegroup_name: NotRequired["capo_eks.types.string.String"]
    """<p>The Amazon EKS managed node group associated with the exception.</p>"""
    valid_zones: NotRequired["capo_eks.types.string_list.StringList"]
    """<p>The supported Availability Zones for your account. Choose subnets in these Availability Zones for your cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnsupportedAvailabilityZoneException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    if "nodegroup_name" in value:
        out["nodegroupName"] = value["nodegroup_name"]
    if "valid_zones" in value:
        import capo_eks.types.string_list

        out["validZones"] = capo_eks.types.string_list.serialize_json(
            value["valid_zones"]
        )
    return out


def deserialize_json(data: dict) -> UnsupportedAvailabilityZoneException_:
    out: UnsupportedAvailabilityZoneException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("clusterName") is not None:
        out["cluster_name"] = data["clusterName"]
    if data.get("nodegroupName") is not None:
        out["nodegroup_name"] = data["nodegroupName"]
    if data.get("validZones") is not None:
        import capo_eks.types.string_list

        out["valid_zones"] = capo_eks.types.string_list.deserialize_json(
            data["validZones"]
        )
    return out


class UnsupportedAvailabilityZoneException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.eks#UnsupportedAvailabilityZoneException``."""

    code: str | None = "UnsupportedAvailabilityZoneException"

    def __init__(
        self,
        data: UnsupportedAvailabilityZoneException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedAvailabilityZoneException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "UnsupportedAvailabilityZoneException":
        return cls(deserialize_json(data), message, response=response)
