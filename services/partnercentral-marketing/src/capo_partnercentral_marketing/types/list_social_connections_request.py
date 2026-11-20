"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#ListSocialConnectionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.catalog
    import capo_partnercentral_marketing.types.max_results
    import capo_partnercentral_marketing.types.next_token
    import capo_partnercentral_marketing.types.platform


class ListSocialConnectionsRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_marketing.types.catalog.Catalog"
    """Catalog to list connections from."""
    platform: NotRequired["capo_partnercentral_marketing.types.platform.Platform"]
    """Restrict results to a single social platform."""
    max_results: NotRequired[
        "capo_partnercentral_marketing.types.max_results.MaxResults"
    ]
    """Maximum number of results to return per page."""
    next_token: NotRequired["capo_partnercentral_marketing.types.next_token.NextToken"]
    """Pagination token from a previous response."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListSocialConnectionsRequest) -> dict:
    out: dict = {}
    import capo_partnercentral_marketing.types.catalog

    out["Catalog"] = capo_partnercentral_marketing.types.catalog.serialize_cbor(
        value["catalog"]
    )
    if "platform" in value:
        import capo_partnercentral_marketing.types.platform

        out["Platform"] = capo_partnercentral_marketing.types.platform.serialize_cbor(
            value["platform"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListSocialConnectionsRequest:
    out: ListSocialConnectionsRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
