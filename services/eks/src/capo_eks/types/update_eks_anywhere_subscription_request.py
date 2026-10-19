"""Generated from Smithy shape ``com.amazonaws.eks#UpdateEksAnywhereSubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_eks.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eks.types.boolean
    import capo_eks.types.string


class UpdateEksAnywhereSubscriptionRequest(TypedDict, closed=True):
    id: "capo_eks.types.string.String"
    """<p>The ID of the subscription.</p>"""
    auto_renew: "capo_eks.types.boolean.Boolean"
    """<p>A boolean indicating whether or not to automatically renew the subscription.</p>"""
    client_request_token: NotRequired["capo_eks.types.string.String"]
    """<p>Unique, case-sensitive identifier to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEksAnywhereSubscriptionRequest) -> dict:
    out: dict = {}
    out["autoRenew"] = value["auto_renew"]
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> UpdateEksAnywhereSubscriptionRequest:
    out: UpdateEksAnywhereSubscriptionRequest = {}  # type: ignore[typeddict-item]
    if data.get("autoRenew") is not None:
        out["auto_renew"] = data["autoRenew"]
    else:
        raise DeserializationError(
            "UpdateEksAnywhereSubscriptionRequest.auto_renew required"
        )
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    return out
