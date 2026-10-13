"""Generated from Smithy shape ``com.amazonaws.socialmessaging#AssociateWhatsAppBusinessAccountInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.whats_app_setup_finalization
    import capo_socialmessaging.types.whats_app_signup_callback


class AssociateWhatsAppBusinessAccountInput(TypedDict, closed=True):
    signup_callback: NotRequired[
        "capo_socialmessaging.types.whats_app_signup_callback.WhatsAppSignupCallback"
    ]
    """<p>Contains the callback access token.</p>"""
    setup_finalization: NotRequired[
        "capo_socialmessaging.types.whats_app_setup_finalization.WhatsAppSetupFinalization"
    ]
    """<p>A JSON object that contains the phone numbers and WhatsApp Business Account to link to your account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateWhatsAppBusinessAccountInput) -> dict:
    out: dict = {}
    if "signup_callback" in value:
        import capo_socialmessaging.types.whats_app_signup_callback

        out["signupCallback"] = (
            capo_socialmessaging.types.whats_app_signup_callback.serialize_json(
                value["signup_callback"]
            )
        )
    if "setup_finalization" in value:
        import capo_socialmessaging.types.whats_app_setup_finalization

        out["setupFinalization"] = (
            capo_socialmessaging.types.whats_app_setup_finalization.serialize_json(
                value["setup_finalization"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssociateWhatsAppBusinessAccountInput:
    out: AssociateWhatsAppBusinessAccountInput = {}  # type: ignore[typeddict-item]
    if data.get("signupCallback") is not None:
        import capo_socialmessaging.types.whats_app_signup_callback

        out["signup_callback"] = (
            capo_socialmessaging.types.whats_app_signup_callback.deserialize_json(
                data["signupCallback"]
            )
        )
    if data.get("setupFinalization") is not None:
        import capo_socialmessaging.types.whats_app_setup_finalization

        out["setup_finalization"] = (
            capo_socialmessaging.types.whats_app_setup_finalization.deserialize_json(
                data["setupFinalization"]
            )
        )
    return out


def redact_sensitive(value: AssociateWhatsAppBusinessAccountInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "setup_finalization" in value:
        import capo_socialmessaging.types.whats_app_setup_finalization

        out["setup_finalization"] = (
            capo_socialmessaging.types.whats_app_setup_finalization.redact_sensitive(
                value["setup_finalization"]
            )
        )
    return out
