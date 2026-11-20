"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CreateSocialConnectionAuthorizationUrlResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.authorization_url
    import capo_partnercentral_marketing.types.platform


class CreateSocialConnectionAuthorizationUrlResponse(TypedDict, closed=True):
    platform: "capo_partnercentral_marketing.types.platform.Platform"
    """Social platform the URL authorizes."""
    authorization_url: (
        "capo_partnercentral_marketing.types.authorization_url.AuthorizationUrl"
    )
    """Fresh single-use URL the partner visits to grant authorization."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateSocialConnectionAuthorizationUrlResponse) -> dict:
    out: dict = {}
    import capo_partnercentral_marketing.types.platform

    out["Platform"] = capo_partnercentral_marketing.types.platform.serialize_cbor(
        value["platform"]
    )
    out["AuthorizationUrl"] = value["authorization_url"]
    return out


def deserialize_cbor(data: dict) -> CreateSocialConnectionAuthorizationUrlResponse:
    out: CreateSocialConnectionAuthorizationUrlResponse = {}  # type: ignore[typeddict-item]
    if data.get("Platform") is not None:
        import capo_partnercentral_marketing.types.platform

        out["platform"] = capo_partnercentral_marketing.types.platform.deserialize_cbor(
            data["Platform"]
        )
    else:
        import typing

        out["platform"] = typing.cast(
            "capo_partnercentral_marketing.types.platform.Platform", ""
        )
    if data.get("AuthorizationUrl") is not None:
        out["authorization_url"] = data["AuthorizationUrl"]
    else:
        out["authorization_url"] = ""
    return out


def redact_sensitive(
    value: CreateSocialConnectionAuthorizationUrlResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authorization_url" in value:
        out["authorization_url"] = "*** Sensitive Data Redacted ***"
    return out
