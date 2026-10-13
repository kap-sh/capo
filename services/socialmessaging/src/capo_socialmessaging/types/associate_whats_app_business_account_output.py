"""Generated from Smithy shape ``com.amazonaws.socialmessaging#AssociateWhatsAppBusinessAccountOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.linked_whats_app_business_account_id
    import capo_socialmessaging.types.whats_app_signup_callback_result


class AssociateWhatsAppBusinessAccountOutput(TypedDict, closed=True):
    signup_callback_result: NotRequired[
        "capo_socialmessaging.types.whats_app_signup_callback_result.WhatsAppSignupCallbackResult"
    ]
    """<p>Contains your WhatsApp registration status.</p>"""
    status_code: NotRequired["int"]
    """<p>The status code for the response.</p>"""
    linked_whats_app_business_account_id: NotRequired[
        "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId"
    ]
    """<p>The ID of the WhatsApp Business Account that was linked to your Amazon Web Services account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateWhatsAppBusinessAccountOutput) -> dict:
    out: dict = {}
    if "signup_callback_result" in value:
        import capo_socialmessaging.types.whats_app_signup_callback_result

        out["signupCallbackResult"] = (
            capo_socialmessaging.types.whats_app_signup_callback_result.serialize_json(
                value["signup_callback_result"]
            )
        )
    if "status_code" in value:
        out["statusCode"] = value["status_code"]
    if "linked_whats_app_business_account_id" in value:
        out["linkedWhatsAppBusinessAccountId"] = value[
            "linked_whats_app_business_account_id"
        ]
    return out


def deserialize_json(data: dict) -> AssociateWhatsAppBusinessAccountOutput:
    out: AssociateWhatsAppBusinessAccountOutput = {}  # type: ignore[typeddict-item]
    if data.get("signupCallbackResult") is not None:
        import capo_socialmessaging.types.whats_app_signup_callback_result

        out["signup_callback_result"] = (
            capo_socialmessaging.types.whats_app_signup_callback_result.deserialize_json(
                data["signupCallbackResult"]
            )
        )
    if data.get("statusCode") is not None:
        out["status_code"] = data["statusCode"]
    if data.get("linkedWhatsAppBusinessAccountId") is not None:
        out["linked_whats_app_business_account_id"] = data[
            "linkedWhatsAppBusinessAccountId"
        ]
    return out


def redact_sensitive(value: AssociateWhatsAppBusinessAccountOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "signup_callback_result" in value:
        import capo_socialmessaging.types.whats_app_signup_callback_result

        out["signup_callback_result"] = (
            capo_socialmessaging.types.whats_app_signup_callback_result.redact_sensitive(
                value["signup_callback_result"]
            )
        )
    return out
