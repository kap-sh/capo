"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#GetQualificationsAssociationDetailsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_account.types.associated_partner_list
    import capo_partnercentral_account.types.catalog
    import capo_partnercentral_account.types.date_time
    import capo_partnercentral_account.types.partner_arn
    import capo_partnercentral_account.types.partner_id
    import capo_partnercentral_account.types.qualifications_association_partner
    import capo_partnercentral_account.types.qualifications_association_status


class GetQualificationsAssociationDetailsResponse(TypedDict, closed=True):
    catalog: "capo_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier echoed from the request.</p>"""
    arn: "capo_partnercentral_account.types.partner_arn.PartnerArn"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies your partner resource.</p>"""
    id: "capo_partnercentral_account.types.partner_id.PartnerId"
    """<p>Your unique partner identifier in the AWS Partner Network.</p>"""
    status: "capo_partnercentral_account.types.qualifications_association_status.QualificationsAssociationStatus"
    """<p>The current qualifications association status. Valid values: <code>ASSOCIATED</code> (the partner is associated with a primary), <code>NOT_ASSOCIATED</code> (the partner has no active association).</p>"""
    primary_partner: NotRequired[
        "capo_partnercentral_account.types.qualifications_association_partner.QualificationsAssociationPartner"
    ]
    """<p>The primary partner's profile and account identifiers. This field is null when the status is <code>NOT_ASSOCIATED</code>.</p>"""
    associated_partners: NotRequired[
        "capo_partnercentral_account.types.associated_partner_list.AssociatedPartnerList"
    ]
    """<p>The list of all partner profile and account identifiers currently associated under the primary partner. This field is null when the status is <code>NOT_ASSOCIATED</code>.</p>"""
    updated_at: NotRequired["capo_partnercentral_account.types.date_time.DateTime"]
    """<p>The timestamp when the qualifications association was last updated, in ISO 8601 format. This field is null when the status is <code>NOT_ASSOCIATED</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetQualificationsAssociationDetailsResponse) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Arn"] = value["arn"]
    out["Id"] = value["id"]
    import capo_partnercentral_account.types.qualifications_association_status

    out["Status"] = (
        capo_partnercentral_account.types.qualifications_association_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    if "primary_partner" in value:
        import capo_partnercentral_account.types.qualifications_association_partner

        out["PrimaryPartner"] = (
            capo_partnercentral_account.types.qualifications_association_partner.serialize_aws_json_1_0(
                value["primary_partner"]
            )
        )
    if "associated_partners" in value:
        import capo_partnercentral_account.types.associated_partner_list

        out["AssociatedPartners"] = (
            capo_partnercentral_account.types.associated_partner_list.serialize_aws_json_1_0(
                value["associated_partners"]
            )
        )
    if "updated_at" in value:
        import capo_partnercentral_account.types.date_time

        out["UpdatedAt"] = (
            capo_partnercentral_account.types.date_time.serialize_aws_json_1_0(
                value["updated_at"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetQualificationsAssociationDetailsResponse:
    out: GetQualificationsAssociationDetailsResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("Status") is not None:
        import capo_partnercentral_account.types.qualifications_association_status

        out["status"] = (
            capo_partnercentral_account.types.qualifications_association_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_partnercentral_account.types.qualifications_association_status.QualificationsAssociationStatus",
            "",
        )
    if data.get("PrimaryPartner") is not None:
        import capo_partnercentral_account.types.qualifications_association_partner

        out["primary_partner"] = (
            capo_partnercentral_account.types.qualifications_association_partner.deserialize_aws_json_1_0(
                data["PrimaryPartner"]
            )
        )
    if data.get("AssociatedPartners") is not None:
        import capo_partnercentral_account.types.associated_partner_list

        out["associated_partners"] = (
            capo_partnercentral_account.types.associated_partner_list.deserialize_aws_json_1_0(
                data["AssociatedPartners"]
            )
        )
    if data.get("UpdatedAt") is not None:
        import capo_partnercentral_account.types.date_time

        out["updated_at"] = (
            capo_partnercentral_account.types.date_time.deserialize_aws_json_1_0(
                data["UpdatedAt"]
            )
        )
    return out
