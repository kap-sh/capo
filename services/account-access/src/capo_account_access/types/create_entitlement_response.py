"""Generated from Smithy shape ``com.amazonaws.accountaccess#CreateEntitlementResponse``."""

from typing_extensions import TypedDict

from capo_account_access.errors import DeserializationError


class CreateEntitlementResponse(TypedDict, closed=True):
    entitlement_id: "str"
    """<p>The unique identifier of the created entitlement.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEntitlementResponse) -> dict:
    out: dict = {}
    out["entitlementId"] = value["entitlement_id"]
    return out


def deserialize_json(data: dict) -> CreateEntitlementResponse:
    out: CreateEntitlementResponse = {}  # type: ignore[typeddict-item]
    if data.get("entitlementId") is not None:
        out["entitlement_id"] = data["entitlementId"]
    else:
        raise DeserializationError("CreateEntitlementResponse.entitlement_id required")
    return out
