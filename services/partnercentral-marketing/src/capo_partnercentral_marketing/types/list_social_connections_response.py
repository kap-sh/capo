"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#ListSocialConnectionsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.next_token
    import capo_partnercentral_marketing.types.social_connection_summary_list


class ListSocialConnectionsResponse(TypedDict, closed=True):
    items: "capo_partnercentral_marketing.types.social_connection_summary_list.SocialConnectionSummaryList"
    """The social connections for this partner and catalog."""
    next_token: NotRequired["capo_partnercentral_marketing.types.next_token.NextToken"]
    """Pagination token for the next page, absent on the last page."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListSocialConnectionsResponse) -> dict:
    out: dict = {}
    import capo_partnercentral_marketing.types.social_connection_summary_list

    out["Items"] = (
        capo_partnercentral_marketing.types.social_connection_summary_list.serialize_cbor(
            value["items"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListSocialConnectionsResponse:
    out: ListSocialConnectionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Items") is not None:
        import capo_partnercentral_marketing.types.social_connection_summary_list

        out["items"] = (
            capo_partnercentral_marketing.types.social_connection_summary_list.deserialize_cbor(
                data["Items"]
            )
        )
    else:
        out["items"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListSocialConnectionsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_partnercentral_marketing.types.social_connection_summary_list

        out["items"] = (
            capo_partnercentral_marketing.types.social_connection_summary_list.redact_sensitive(
                value["items"]
            )
        )
    return out
