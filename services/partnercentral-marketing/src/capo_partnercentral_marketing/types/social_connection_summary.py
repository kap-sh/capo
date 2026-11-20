"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#SocialConnectionSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.platform
    import capo_partnercentral_marketing.types.social_account_name
    import capo_partnercentral_marketing.types.social_connection_id
    import capo_partnercentral_marketing.types.social_connection_status
    import capo_partnercentral_marketing.types.social_page_name
    import capo_partnercentral_marketing.types.timestamp


class SocialConnectionSummary(TypedDict, closed=True):
    id: "capo_partnercentral_marketing.types.social_connection_id.SocialConnectionId"
    """Identifier of the social connection."""
    platform: "capo_partnercentral_marketing.types.platform.Platform"
    """Social platform this connection authorizes."""
    status: "capo_partnercentral_marketing.types.social_connection_status.SocialConnectionStatus"
    """Authorization state."""
    page_name: NotRequired[
        "capo_partnercentral_marketing.types.social_page_name.SocialPageName"
    ]
    """The Facebook Page this connection publishes to. Absent where no Page applies."""
    account_name: NotRequired[
        "capo_partnercentral_marketing.types.social_account_name.SocialAccountName"
    ]
    """Display name of the account behind this connection. Absent when the execution backend reports none."""
    connected_at: NotRequired["capo_partnercentral_marketing.types.timestamp.Timestamp"]
    """When the account was last authorized. Advances on every re-authorization."""
    expires_at: NotRequired["capo_partnercentral_marketing.types.timestamp.Timestamp"]
    """When the authorization lapses. Absent where the platform reports no expiry (X never does). A connection past this time reads EXPIRED only once the backend notices, so treat this as a warning date, not a status."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SocialConnectionSummary) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    import capo_partnercentral_marketing.types.platform

    out["Platform"] = capo_partnercentral_marketing.types.platform.serialize_cbor(
        value["platform"]
    )
    import capo_partnercentral_marketing.types.social_connection_status

    out["Status"] = (
        capo_partnercentral_marketing.types.social_connection_status.serialize_cbor(
            value["status"]
        )
    )
    if "page_name" in value:
        out["PageName"] = value["page_name"]
    if "account_name" in value:
        out["AccountName"] = value["account_name"]
    if "connected_at" in value:
        import capo_partnercentral_marketing.types.timestamp

        out["ConnectedAt"] = (
            capo_partnercentral_marketing.types.timestamp.serialize_cbor(
                value["connected_at"]
            )
        )
    if "expires_at" in value:
        import capo_partnercentral_marketing.types.timestamp

        out["ExpiresAt"] = capo_partnercentral_marketing.types.timestamp.serialize_cbor(
            value["expires_at"]
        )
    return out


def deserialize_cbor(data: dict) -> SocialConnectionSummary:
    out: SocialConnectionSummary = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
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
    if data.get("Status") is not None:
        import capo_partnercentral_marketing.types.social_connection_status

        out["status"] = (
            capo_partnercentral_marketing.types.social_connection_status.deserialize_cbor(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_partnercentral_marketing.types.social_connection_status.SocialConnectionStatus",
            "",
        )
    if data.get("PageName") is not None:
        out["page_name"] = data["PageName"]
    if data.get("AccountName") is not None:
        out["account_name"] = data["AccountName"]
    if data.get("ConnectedAt") is not None:
        import capo_partnercentral_marketing.types.timestamp

        out["connected_at"] = (
            capo_partnercentral_marketing.types.timestamp.deserialize_cbor(
                data["ConnectedAt"]
            )
        )
    if data.get("ExpiresAt") is not None:
        import capo_partnercentral_marketing.types.timestamp

        out["expires_at"] = (
            capo_partnercentral_marketing.types.timestamp.deserialize_cbor(
                data["ExpiresAt"]
            )
        )
    return out


def redact_sensitive(value: SocialConnectionSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "account_name" in value:
        out["account_name"] = "*** Sensitive Data Redacted ***"
    return out
