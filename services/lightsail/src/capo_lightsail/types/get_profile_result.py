"""Generated from Smithy shape ``com.amazonaws.lightsail#GetProfileResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.partner_info
    import capo_lightsail.types.profile_type


class GetProfileResult(TypedDict, closed=True):
    profile_type: "capo_lightsail.types.profile_type.ProfileType"
    """<p>The type of the profile.</p> <p>The following profile types are possible:</p> <ul> <li> <p> <code>Lightsailor</code> – The account is not enrolled in the Lightsail partner program.</p> </li> <li> <p> <code>LightsailPartner</code> – The account is enrolled in the Lightsail partner program.</p> </li> </ul>"""
    partner: NotRequired["capo_lightsail.types.partner_info.PartnerInfo"]
    """<p>An object that describes the partner membership of the account, such as the tier of the membership, its status, and when the account was enrolled.</p> <p>This parameter is returned only for accounts that have a <code>profileType</code> of <code>LightsailPartner</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetProfileResult) -> dict:
    out: dict = {}
    import capo_lightsail.types.profile_type

    out["profileType"] = capo_lightsail.types.profile_type.serialize_aws_json_1_1(
        value["profile_type"]
    )
    if "partner" in value:
        import capo_lightsail.types.partner_info

        out["partner"] = capo_lightsail.types.partner_info.serialize_aws_json_1_1(
            value["partner"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetProfileResult:
    out: GetProfileResult = {}  # type: ignore[typeddict-item]
    if data.get("profileType") is not None:
        import capo_lightsail.types.profile_type

        out["profile_type"] = (
            capo_lightsail.types.profile_type.deserialize_aws_json_1_1(
                data["profileType"]
            )
        )
    else:
        import typing

        out["profile_type"] = typing.cast(
            "capo_lightsail.types.profile_type.ProfileType", ""
        )
    if data.get("partner") is not None:
        import capo_lightsail.types.partner_info

        out["partner"] = capo_lightsail.types.partner_info.deserialize_aws_json_1_1(
            data["partner"]
        )
    return out
