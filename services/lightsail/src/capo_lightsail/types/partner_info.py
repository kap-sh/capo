"""Generated from Smithy shape ``com.amazonaws.lightsail#PartnerInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.iso_date
    import capo_lightsail.types.partner_status
    import capo_lightsail.types.tier_name


class PartnerInfo(TypedDict, closed=True):
    enrolled_at: "capo_lightsail.types.iso_date.IsoDate"
    """<p>The timestamp when the account was enrolled in the Lightsail partner program.</p>"""
    tier_name: NotRequired["capo_lightsail.types.tier_name.TierName"]
    """<p>The tier of the partner membership.</p>"""
    status: "capo_lightsail.types.partner_status.PartnerStatus"
    """<p>The status of the partner membership.</p> <p>The following statuses are possible:</p> <ul> <li> <p> <code>Active</code> – The membership is active, and the benefits of the current tier are available to the account.</p> </li> <li> <p> <code>Suspended</code> – The membership is suspended, and the benefits of the tier are not available to the account.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartnerInfo) -> dict:
    out: dict = {}
    import capo_lightsail.types.iso_date

    out["enrolledAt"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
        value["enrolled_at"]
    )
    if "tier_name" in value:
        import capo_lightsail.types.tier_name

        out["tierName"] = capo_lightsail.types.tier_name.serialize_aws_json_1_1(
            value["tier_name"]
        )
    import capo_lightsail.types.partner_status

    out["status"] = capo_lightsail.types.partner_status.serialize_aws_json_1_1(
        value["status"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PartnerInfo:
    out: PartnerInfo = {}  # type: ignore[typeddict-item]
    if data.get("enrolledAt") is not None:
        import capo_lightsail.types.iso_date

        out["enrolled_at"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["enrolledAt"]
        )
    else:
        import datetime

        out["enrolled_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("tierName") is not None:
        import capo_lightsail.types.tier_name

        out["tier_name"] = capo_lightsail.types.tier_name.deserialize_aws_json_1_1(
            data["tierName"]
        )
    if data.get("status") is not None:
        import capo_lightsail.types.partner_status

        out["status"] = capo_lightsail.types.partner_status.deserialize_aws_json_1_1(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_lightsail.types.partner_status.PartnerStatus", ""
        )
    return out
