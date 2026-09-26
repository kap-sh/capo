"""Generated from Smithy shape ``com.amazonaws.accountaccess#GetEntitlementResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_account_access.errors import DeserializationError

if TYPE_CHECKING:
    import capo_account_access.types.application_arn
    import capo_account_access.types.date_time
    import capo_account_access.types.entitlement_details


class GetEntitlementResponse(TypedDict, closed=True):
    application_arn: "capo_account_access.types.application_arn.ApplicationArn"
    """<p>The ARN of the application that the entitlement belongs to.</p>"""
    entitlement_id: "str"
    """<p>The unique identifier of the entitlement.</p>"""
    entitlement: "capo_account_access.types.entitlement_details.EntitlementDetails"
    """<p>The entitlement details, including the principal, IAM role, and target account.</p>"""
    created_at: "capo_account_access.types.date_time.DateTime"
    """<p>The date and time when the entitlement was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEntitlementResponse) -> dict:
    out: dict = {}
    out["applicationArn"] = value["application_arn"]
    out["entitlementId"] = value["entitlement_id"]
    import capo_account_access.types.entitlement_details

    out["entitlement"] = capo_account_access.types.entitlement_details.serialize_json(
        value["entitlement"]
    )
    import capo_account_access.types.date_time

    out["createdAt"] = capo_account_access.types.date_time.serialize_json(
        value["created_at"]
    )
    return out


def deserialize_json(data: dict) -> GetEntitlementResponse:
    out: GetEntitlementResponse = {}  # type: ignore[typeddict-item]
    if data.get("applicationArn") is not None:
        out["application_arn"] = data["applicationArn"]
    else:
        raise DeserializationError("GetEntitlementResponse.application_arn required")
    if data.get("entitlementId") is not None:
        out["entitlement_id"] = data["entitlementId"]
    else:
        raise DeserializationError("GetEntitlementResponse.entitlement_id required")
    if data.get("entitlement") is not None:
        import capo_account_access.types.entitlement_details

        out["entitlement"] = (
            capo_account_access.types.entitlement_details.deserialize_json(
                data["entitlement"]
            )
        )
    else:
        raise DeserializationError("GetEntitlementResponse.entitlement required")
    if data.get("createdAt") is not None:
        import capo_account_access.types.date_time

        out["created_at"] = capo_account_access.types.date_time.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GetEntitlementResponse.created_at required")
    return out
