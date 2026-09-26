"""Generated from Smithy shape ``com.amazonaws.accountaccess#CreateEntitlementRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_account_access.errors import DeserializationError

if TYPE_CHECKING:
    import capo_account_access.types.application_arn
    import capo_account_access.types.entitlement


class CreateEntitlementRequest(TypedDict, closed=True):
    application_arn: "capo_account_access.types.application_arn.ApplicationArn"
    """<p>Specifies the ARN of the application to create the entitlement for.</p>"""
    entitlement: "capo_account_access.types.entitlement.Entitlement"
    """<p>Specifies the entitlement configuration, including the principal and the IAM role to grant access to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEntitlementRequest) -> dict:
    out: dict = {}
    out["applicationArn"] = value["application_arn"]
    import capo_account_access.types.entitlement

    out["entitlement"] = capo_account_access.types.entitlement.serialize_json(
        value["entitlement"]
    )
    return out


def deserialize_json(data: dict) -> CreateEntitlementRequest:
    out: CreateEntitlementRequest = {}  # type: ignore[typeddict-item]
    if data.get("applicationArn") is not None:
        out["application_arn"] = data["applicationArn"]
    else:
        raise DeserializationError("CreateEntitlementRequest.application_arn required")
    if data.get("entitlement") is not None:
        import capo_account_access.types.entitlement

        out["entitlement"] = capo_account_access.types.entitlement.deserialize_json(
            data["entitlement"]
        )
    else:
        raise DeserializationError("CreateEntitlementRequest.entitlement required")
    return out
