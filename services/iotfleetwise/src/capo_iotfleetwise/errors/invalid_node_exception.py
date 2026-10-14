"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#InvalidNodeException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_iotfleetwise.errors import ServiceError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.nodes
    import capo_iotfleetwise.types.string


class InvalidNodeException_(TypedDict, closed=True):
    invalid_nodes: NotRequired["capo_iotfleetwise.types.nodes.Nodes"]
    """<p>The specified node type isn't valid.</p>"""
    reason: NotRequired["capo_iotfleetwise.types.string.string"]
    """<p>The reason the node validation failed.</p>"""
    message: NotRequired["capo_iotfleetwise.types.string.string"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvalidNodeException_) -> dict:
    out: dict = {}
    if "invalid_nodes" in value:
        import capo_iotfleetwise.types.nodes

        out["invalidNodes"] = capo_iotfleetwise.types.nodes.serialize_aws_json_1_0(
            value["invalid_nodes"]
        )
    if "reason" in value:
        out["reason"] = value["reason"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InvalidNodeException_:
    out: InvalidNodeException_ = {}  # type: ignore[typeddict-item]
    if data.get("invalidNodes") is not None:
        import capo_iotfleetwise.types.nodes

        out["invalid_nodes"] = capo_iotfleetwise.types.nodes.deserialize_aws_json_1_0(
            data["invalidNodes"]
        )
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InvalidNodeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotfleetwise#InvalidNodeException``."""

    code: str | None = "InvalidNodeException"

    def __init__(
        self,
        data: InvalidNodeException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidNodeException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidNodeException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
