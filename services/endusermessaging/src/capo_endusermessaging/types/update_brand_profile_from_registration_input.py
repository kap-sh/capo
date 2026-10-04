"""Generated from Smithy shape ``com.amazonaws.endusermessaging#UpdateBrandProfileFromRegistrationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_endusermessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_endusermessaging.types.brand_profile_id_or_arn
    import capo_endusermessaging.types.client_token
    import capo_endusermessaging.types.on_attribute_conflict
    import capo_endusermessaging.types.registration_id_or_arn


class UpdateBrandProfileFromRegistrationInput(TypedDict, closed=True):
    brand_profile_id: (
        "capo_endusermessaging.types.brand_profile_id_or_arn.BrandProfileIdOrArn"
    )
    """<p>The unique identifier of the brand profile. You can specify either the bare ID or the full Amazon Resource Name (ARN).</p>"""
    registration_id: (
        "capo_endusermessaging.types.registration_id_or_arn.RegistrationIdOrArn"
    )
    """<p>The identifier or Amazon Resource Name (ARN) of the registration to import attributes from.</p>"""
    smart_match: NotRequired["bool"]
    """<p>Specifies whether to use semantic field mapping between brand profile attributes and registration fields. The default is true. When false, the service maps fields using a fixed set of standard field types.</p>"""
    on_attribute_conflict: NotRequired[
        "capo_endusermessaging.types.on_attribute_conflict.OnAttributeConflict"
    ]
    """<p>Specifies how the service resolves an attribute that already exists. REPLACE overwrites the existing value with the incoming value. PRESERVE keeps the existing value.</p>"""
    client_token: NotRequired["capo_endusermessaging.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you do not specify a client token, the AWS SDK automatically generates one.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBrandProfileFromRegistrationInput) -> dict:
    out: dict = {}
    out["registrationId"] = value["registration_id"]
    if "smart_match" in value:
        out["smartMatch"] = value["smart_match"]
    if "on_attribute_conflict" in value:
        import capo_endusermessaging.types.on_attribute_conflict

        out["onAttributeConflict"] = (
            capo_endusermessaging.types.on_attribute_conflict.serialize_json(
                value["on_attribute_conflict"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateBrandProfileFromRegistrationInput:
    out: UpdateBrandProfileFromRegistrationInput = {}  # type: ignore[typeddict-item]
    if data.get("registrationId") is not None:
        out["registration_id"] = data["registrationId"]
    else:
        raise DeserializationError(
            "UpdateBrandProfileFromRegistrationInput.registration_id required"
        )
    if data.get("smartMatch") is not None:
        out["smart_match"] = data["smartMatch"]
    if data.get("onAttributeConflict") is not None:
        import capo_endusermessaging.types.on_attribute_conflict

        out["on_attribute_conflict"] = (
            capo_endusermessaging.types.on_attribute_conflict.deserialize_json(
                data["onAttributeConflict"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
