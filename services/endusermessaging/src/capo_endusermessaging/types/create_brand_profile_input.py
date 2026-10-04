"""Generated from Smithy shape ``com.amazonaws.endusermessaging#CreateBrandProfileInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_endusermessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_endusermessaging.types.brand_profile_name
    import capo_endusermessaging.types.client_token
    import capo_endusermessaging.types.tag_list


class CreateBrandProfileInput(TypedDict, closed=True):
    brand_profile_name: (
        "capo_endusermessaging.types.brand_profile_name.BrandProfileName"
    )
    """<p>The name of the brand profile. The name can contain alphanumeric characters, underscores, hyphens, and spaces.</p>"""
    client_token: NotRequired["capo_endusermessaging.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you do not specify a client token, the AWS SDK automatically generates one.</p>"""
    deletion_protection_enabled: NotRequired["bool"]
    """<p>Specifies whether deletion protection is enabled. When enabled, the resource cannot be deleted until deletion protection is turned off.</p>"""
    tags: NotRequired["capo_endusermessaging.types.tag_list.TagList"]
    """<p>An array of key and value pair tags that are associated with the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBrandProfileInput) -> dict:
    out: dict = {}
    out["brandProfileName"] = value["brand_profile_name"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "deletion_protection_enabled" in value:
        out["deletionProtectionEnabled"] = value["deletion_protection_enabled"]
    if "tags" in value:
        import capo_endusermessaging.types.tag_list

        out["tags"] = capo_endusermessaging.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateBrandProfileInput:
    out: CreateBrandProfileInput = {}  # type: ignore[typeddict-item]
    if data.get("brandProfileName") is not None:
        out["brand_profile_name"] = data["brandProfileName"]
    else:
        raise DeserializationError(
            "CreateBrandProfileInput.brand_profile_name required"
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("deletionProtectionEnabled") is not None:
        out["deletion_protection_enabled"] = data["deletionProtectionEnabled"]
    if data.get("tags") is not None:
        import capo_endusermessaging.types.tag_list

        out["tags"] = capo_endusermessaging.types.tag_list.deserialize_json(
            data["tags"]
        )
    return out
