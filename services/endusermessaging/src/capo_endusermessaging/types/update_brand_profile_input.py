"""Generated from Smithy shape ``com.amazonaws.endusermessaging#UpdateBrandProfileInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_endusermessaging.types.brand_profile_id_or_arn
    import capo_endusermessaging.types.brand_profile_name


class UpdateBrandProfileInput(TypedDict, closed=True):
    brand_profile_id: (
        "capo_endusermessaging.types.brand_profile_id_or_arn.BrandProfileIdOrArn"
    )
    """<p>The unique identifier of the brand profile. You can specify either the bare ID or the full Amazon Resource Name (ARN).</p>"""
    brand_profile_name: NotRequired[
        "capo_endusermessaging.types.brand_profile_name.BrandProfileName"
    ]
    """<p>The name of the brand profile. The name can contain alphanumeric characters, underscores, hyphens, and spaces.</p>"""
    deletion_protection_enabled: NotRequired["bool"]
    """<p>Specifies whether deletion protection is enabled. When enabled, the resource cannot be deleted until deletion protection is turned off.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBrandProfileInput) -> dict:
    out: dict = {}
    if "brand_profile_name" in value:
        out["brandProfileName"] = value["brand_profile_name"]
    if "deletion_protection_enabled" in value:
        out["deletionProtectionEnabled"] = value["deletion_protection_enabled"]
    return out


def deserialize_json(data: dict) -> UpdateBrandProfileInput:
    out: UpdateBrandProfileInput = {}  # type: ignore[typeddict-item]
    if data.get("brandProfileName") is not None:
        out["brand_profile_name"] = data["brandProfileName"]
    if data.get("deletionProtectionEnabled") is not None:
        out["deletion_protection_enabled"] = data["deletionProtectionEnabled"]
    return out
