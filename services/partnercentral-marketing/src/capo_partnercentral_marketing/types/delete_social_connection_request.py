"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#DeleteSocialConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.catalog
    import capo_partnercentral_marketing.types.client_token
    import capo_partnercentral_marketing.types.social_connection_identifier


class DeleteSocialConnectionRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_marketing.types.catalog.Catalog"
    """Catalog the connection belongs to."""
    identifier: "capo_partnercentral_marketing.types.social_connection_identifier.SocialConnectionIdentifier"
    """Identifier or ARN of the social connection to delete."""
    client_token: NotRequired[
        "capo_partnercentral_marketing.types.client_token.ClientToken"
    ]
    """Idempotency token."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteSocialConnectionRequest) -> dict:
    out: dict = {}
    import capo_partnercentral_marketing.types.catalog

    out["Catalog"] = capo_partnercentral_marketing.types.catalog.serialize_cbor(
        value["catalog"]
    )
    out["Identifier"] = value["identifier"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_cbor(data: dict) -> DeleteSocialConnectionRequest:
    out: DeleteSocialConnectionRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
