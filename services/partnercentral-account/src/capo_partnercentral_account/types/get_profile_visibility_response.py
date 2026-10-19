"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#GetProfileVisibilityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_account.types.catalog
    import capo_partnercentral_account.types.partner_arn
    import capo_partnercentral_account.types.partner_id
    import capo_partnercentral_account.types.partner_profile_id
    import capo_partnercentral_account.types.profile_visibility


class GetProfileVisibilityResponse(TypedDict, closed=True):
    catalog: "capo_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier for the partner account.</p>"""
    arn: "capo_partnercentral_account.types.partner_arn.PartnerArn"
    """<p>The Amazon Resource Name (ARN) of the partner account.</p>"""
    id: "capo_partnercentral_account.types.partner_id.PartnerId"
    """<p>The unique identifier of the partner account.</p>"""
    visibility: "capo_partnercentral_account.types.profile_visibility.ProfileVisibility"
    """<p>The visibility setting for the partner profile (public, private, restricted, etc.).</p>"""
    profile_id: "capo_partnercentral_account.types.partner_profile_id.PartnerProfileId"
    """<p>The unique identifier of the partner profile.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetProfileVisibilityResponse) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Arn"] = value["arn"]
    out["Id"] = value["id"]
    import capo_partnercentral_account.types.profile_visibility

    out["Visibility"] = (
        capo_partnercentral_account.types.profile_visibility.serialize_aws_json_1_0(
            value["visibility"]
        )
    )
    out["ProfileId"] = value["profile_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetProfileVisibilityResponse:
    out: GetProfileVisibilityResponse = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Visibility") is not None:
        import capo_partnercentral_account.types.profile_visibility

        out["visibility"] = (
            capo_partnercentral_account.types.profile_visibility.deserialize_aws_json_1_0(
                data["Visibility"]
            )
        )
    else:
        import typing

        out["visibility"] = typing.cast(
            "capo_partnercentral_account.types.profile_visibility.ProfileVisibility", ""
        )
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    else:
        out["profile_id"] = ""
    return out
