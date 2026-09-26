"""Generated from Smithy shape ``com.amazonaws.accountaccess#DeleteEntitlementRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_account_access.types.application_arn


class DeleteEntitlementRequest(TypedDict, closed=True):
    application_arn: "capo_account_access.types.application_arn.ApplicationArn"
    """<p>Specifies the ARN of the application that the entitlement belongs to.</p>"""
    entitlement_id: "str"
    """<p>Specifies the unique identifier of the entitlement to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEntitlementRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEntitlementRequest:
    out: DeleteEntitlementRequest = {}  # type: ignore[typeddict-item]
    return out
