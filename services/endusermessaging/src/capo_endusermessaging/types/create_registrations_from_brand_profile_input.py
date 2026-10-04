"""Generated from Smithy shape ``com.amazonaws.endusermessaging#CreateRegistrationsFromBrandProfileInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_endusermessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_endusermessaging.types.brand_profile_id_or_arn
    import capo_endusermessaging.types.client_token
    import capo_endusermessaging.types.registration_type_list


class CreateRegistrationsFromBrandProfileInput(TypedDict, closed=True):
    brand_profile_id: (
        "capo_endusermessaging.types.brand_profile_id_or_arn.BrandProfileIdOrArn"
    )
    """<p>The unique identifier of the brand profile. You can specify either the bare ID or the full Amazon Resource Name (ARN).</p>"""
    registration_types: (
        "capo_endusermessaging.types.registration_type_list.RegistrationTypeList"
    )
    """<p>The registration types to create, for example US_TOLL_FREE_REGISTRATION or SENDER_ID.</p>"""
    smart_match: NotRequired["bool"]
    """<p>Specifies whether to use semantic field mapping between brand profile attributes and registration fields. The default is true. When false, the service maps fields using a fixed set of standard field types.</p>"""
    client_token: NotRequired["capo_endusermessaging.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you do not specify a client token, the AWS SDK automatically generates one.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRegistrationsFromBrandProfileInput) -> dict:
    out: dict = {}
    import capo_endusermessaging.types.registration_type_list

    out["registrationTypes"] = (
        capo_endusermessaging.types.registration_type_list.serialize_json(
            value["registration_types"]
        )
    )
    if "smart_match" in value:
        out["smartMatch"] = value["smart_match"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateRegistrationsFromBrandProfileInput:
    out: CreateRegistrationsFromBrandProfileInput = {}  # type: ignore[typeddict-item]
    if data.get("registrationTypes") is not None:
        import capo_endusermessaging.types.registration_type_list

        out["registration_types"] = (
            capo_endusermessaging.types.registration_type_list.deserialize_json(
                data["registrationTypes"]
            )
        )
    else:
        raise DeserializationError(
            "CreateRegistrationsFromBrandProfileInput.registration_types required"
        )
    if data.get("smartMatch") is not None:
        out["smart_match"] = data["smartMatch"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
