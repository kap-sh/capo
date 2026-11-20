"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CreateSocialConnectionAuthorizationUrlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.catalog
    import capo_partnercentral_marketing.types.platform


class CreateSocialConnectionAuthorizationUrlRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_marketing.types.catalog.Catalog"
    """Catalog the connection belongs to."""
    platform: "capo_partnercentral_marketing.types.platform.Platform"
    """Social platform to authorize."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateSocialConnectionAuthorizationUrlRequest) -> dict:
    out: dict = {}
    import capo_partnercentral_marketing.types.catalog

    out["Catalog"] = capo_partnercentral_marketing.types.catalog.serialize_cbor(
        value["catalog"]
    )
    import capo_partnercentral_marketing.types.platform

    out["Platform"] = capo_partnercentral_marketing.types.platform.serialize_cbor(
        value["platform"]
    )
    return out


def deserialize_cbor(data: dict) -> CreateSocialConnectionAuthorizationUrlRequest:
    out: CreateSocialConnectionAuthorizationUrlRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        import capo_partnercentral_marketing.types.catalog

        out["catalog"] = capo_partnercentral_marketing.types.catalog.deserialize_cbor(
            data["Catalog"]
        )
    else:
        import typing

        out["catalog"] = typing.cast(
            "capo_partnercentral_marketing.types.catalog.Catalog", ""
        )
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
    return out
