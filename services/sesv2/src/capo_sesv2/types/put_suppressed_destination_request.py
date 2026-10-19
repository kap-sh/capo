"""Generated from Smithy shape ``com.amazonaws.sesv2#PutSuppressedDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.email_address
    import capo_sesv2.types.suppression_list_reason
    import capo_sesv2.types.tenant_name


class PutSuppressedDestinationRequest(TypedDict, closed=True):
    email_address: "capo_sesv2.types.email_address.EmailAddress"
    """<p>The email address that should be added to the suppression list for your account or for the specified tenant.</p>"""
    reason: "capo_sesv2.types.suppression_list_reason.SuppressionListReason"
    """<p>The factors that should cause the email address to be added to the suppression list for your account or for the specified tenant.</p>"""
    tenant_name: NotRequired["capo_sesv2.types.tenant_name.TenantName"]
    """<p>The name of the tenant whose suppression list you want to add the address to. If you omit this parameter, the address is added to the account-level suppression list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutSuppressedDestinationRequest) -> dict:
    out: dict = {}
    out["EmailAddress"] = value["email_address"]
    import capo_sesv2.types.suppression_list_reason

    out["Reason"] = capo_sesv2.types.suppression_list_reason.serialize_json(
        value["reason"]
    )
    if "tenant_name" in value:
        out["TenantName"] = value["tenant_name"]
    return out


def deserialize_json(data: dict) -> PutSuppressedDestinationRequest:
    out: PutSuppressedDestinationRequest = {}  # type: ignore[typeddict-item]
    if data.get("EmailAddress") is not None:
        out["email_address"] = data["EmailAddress"]
    else:
        out["email_address"] = ""
    if data.get("Reason") is not None:
        import capo_sesv2.types.suppression_list_reason

        out["reason"] = capo_sesv2.types.suppression_list_reason.deserialize_json(
            data["Reason"]
        )
    else:
        import typing

        out["reason"] = typing.cast(
            "capo_sesv2.types.suppression_list_reason.SuppressionListReason", ""
        )
    if data.get("TenantName") is not None:
        out["tenant_name"] = data["TenantName"]
    return out
