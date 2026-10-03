"""Generated from Smithy shape ``com.amazonaws.rtbfabric#UpdateRequesterGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rtbfabric.types.gateway_id


class UpdateRequesterGatewayRequest(TypedDict, closed=True):
    client_token: "str"
    """<p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>clientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>"""
    gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    description: NotRequired["str"]
    """<p>An optional description for the requester gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRequesterGatewayRequest) -> dict:
    out: dict = {}
    out["clientToken"] = value["client_token"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateRequesterGatewayRequest:
    out: UpdateRequesterGatewayRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError(
            "UpdateRequesterGatewayRequest.client_token required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
