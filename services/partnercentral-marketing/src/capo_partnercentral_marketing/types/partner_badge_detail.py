"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#PartnerBadgeDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.timestamp


class PartnerBadgeDetail(TypedDict, closed=True):
    url: "str"
    """A presigned GET of the badge, which expires one hour after the read: fetch it again with `GetCampaign` when it returns 403."""
    attached_at: "capo_partnercentral_marketing.types.timestamp.Timestamp"
    """When the badge was set."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PartnerBadgeDetail) -> dict:
    out: dict = {}
    out["Url"] = value["url"]
    import capo_partnercentral_marketing.types.timestamp

    out["AttachedAt"] = capo_partnercentral_marketing.types.timestamp.serialize_cbor(
        value["attached_at"]
    )
    return out


def deserialize_cbor(data: dict) -> PartnerBadgeDetail:
    out: PartnerBadgeDetail = {}  # type: ignore[typeddict-item]
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    else:
        out["url"] = ""
    if data.get("AttachedAt") is not None:
        import capo_partnercentral_marketing.types.timestamp

        out["attached_at"] = (
            capo_partnercentral_marketing.types.timestamp.deserialize_cbor(
                data["AttachedAt"]
            )
        )
    else:
        import datetime

        out["attached_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
