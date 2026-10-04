"""Generated from Smithy shape ``com.amazonaws.endusermessaging#CreateBrandProfileFromRegistrationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_endusermessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_endusermessaging.types.brand_profile_name
    import capo_endusermessaging.types.client_token
    import capo_endusermessaging.types.registration_id_or_arn
    import capo_endusermessaging.types.tag_list


class CreateBrandProfileFromRegistrationInput(TypedDict, closed=True):
    registration_id: (
        "capo_endusermessaging.types.registration_id_or_arn.RegistrationIdOrArn"
    )
    """<p>The identifier or Amazon Resource Name (ARN) of the registration to populate the brand profile from.</p>"""
    brand_profile_name: (
        "capo_endusermessaging.types.brand_profile_name.BrandProfileName"
    )
    """<p>The name of the brand profile. The name can contain alphanumeric characters, underscores, hyphens, and spaces.</p>"""
    smart_match: NotRequired["bool"]
    """<p>Specifies whether to use semantic field mapping between brand profile attributes and registration fields. The default is true. When false, the service maps fields using a fixed set of standard field types.</p>"""
    tags: NotRequired["capo_endusermessaging.types.tag_list.TagList"]
    """<p>An array of key and value pair tags that are associated with the resource.</p>"""
    client_token: NotRequired["capo_endusermessaging.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you do not specify a client token, the AWS SDK automatically generates one.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBrandProfileFromRegistrationInput) -> dict:
    out: dict = {}
    out["registrationId"] = value["registration_id"]
    out["brandProfileName"] = value["brand_profile_name"]
    if "smart_match" in value:
        out["smartMatch"] = value["smart_match"]
    if "tags" in value:
        import capo_endusermessaging.types.tag_list

        out["tags"] = capo_endusermessaging.types.tag_list.serialize_json(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateBrandProfileFromRegistrationInput:
    out: CreateBrandProfileFromRegistrationInput = {}  # type: ignore[typeddict-item]
    if data.get("registrationId") is not None:
        out["registration_id"] = data["registrationId"]
    else:
        raise DeserializationError(
            "CreateBrandProfileFromRegistrationInput.registration_id required"
        )
    if data.get("brandProfileName") is not None:
        out["brand_profile_name"] = data["brandProfileName"]
    else:
        raise DeserializationError(
            "CreateBrandProfileFromRegistrationInput.brand_profile_name required"
        )
    if data.get("smartMatch") is not None:
        out["smart_match"] = data["smartMatch"]
    if data.get("tags") is not None:
        import capo_endusermessaging.types.tag_list

        out["tags"] = capo_endusermessaging.types.tag_list.deserialize_json(
            data["tags"]
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
