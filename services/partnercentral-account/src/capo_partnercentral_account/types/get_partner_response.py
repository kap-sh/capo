"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#GetPartnerResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_account.types.catalog
    import capo_partnercentral_account.types.date_time
    import capo_partnercentral_account.types.partner_arn
    import capo_partnercentral_account.types.partner_domain_list
    import capo_partnercentral_account.types.partner_id
    import capo_partnercentral_account.types.partner_profile
    import capo_partnercentral_account.types.sensitive_unicode_string


class GetPartnerResponse(TypedDict, closed=True):
    catalog: "capo_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier for the partner account.</p>"""
    arn: "capo_partnercentral_account.types.partner_arn.PartnerArn"
    """<p>The Amazon Resource Name (ARN) of the partner account.</p>"""
    id: "capo_partnercentral_account.types.partner_id.PartnerId"
    """<p>The unique identifier of the partner account.</p>"""
    legal_name: "capo_partnercentral_account.types.sensitive_unicode_string.SensitiveUnicodeString"
    """<p>The legal name of the partner organization.</p>"""
    created_at: "capo_partnercentral_account.types.date_time.DateTime"
    """<p>The timestamp when the partner account was created.</p>"""
    profile: "capo_partnercentral_account.types.partner_profile.PartnerProfile"
    """<p>The partner profile information including display name, description, and other public details.</p>"""
    aws_training_certification_email_domains: NotRequired[
        "capo_partnercentral_account.types.partner_domain_list.PartnerDomainList"
    ]
    """<p>The list of verified email domains associated with AWS training and certification credentials for the partner organization.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetPartnerResponse) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Arn"] = value["arn"]
    out["Id"] = value["id"]
    out["LegalName"] = value["legal_name"]
    import capo_partnercentral_account.types.date_time

    out["CreatedAt"] = (
        capo_partnercentral_account.types.date_time.serialize_aws_json_1_0(
            value["created_at"]
        )
    )
    import capo_partnercentral_account.types.partner_profile

    out["Profile"] = (
        capo_partnercentral_account.types.partner_profile.serialize_aws_json_1_0(
            value["profile"]
        )
    )
    if "aws_training_certification_email_domains" in value:
        import capo_partnercentral_account.types.partner_domain_list

        out["AwsTrainingCertificationEmailDomains"] = (
            capo_partnercentral_account.types.partner_domain_list.serialize_aws_json_1_0(
                value["aws_training_certification_email_domains"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetPartnerResponse:
    out: GetPartnerResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("LegalName") is not None:
        out["legal_name"] = data["LegalName"]
    else:
        out["legal_name"] = ""
    if data.get("CreatedAt") is not None:
        import capo_partnercentral_account.types.date_time

        out["created_at"] = (
            capo_partnercentral_account.types.date_time.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("Profile") is not None:
        import capo_partnercentral_account.types.partner_profile

        out["profile"] = (
            capo_partnercentral_account.types.partner_profile.deserialize_aws_json_1_0(
                data["Profile"]
            )
        )
    else:
        raise DeserializationError("GetPartnerResponse.profile required")
    if data.get("AwsTrainingCertificationEmailDomains") is not None:
        import capo_partnercentral_account.types.partner_domain_list

        out["aws_training_certification_email_domains"] = (
            capo_partnercentral_account.types.partner_domain_list.deserialize_aws_json_1_0(
                data["AwsTrainingCertificationEmailDomains"]
            )
        )
    return out


def redact_sensitive(value: GetPartnerResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "legal_name" in value:
        out["legal_name"] = "*** Sensitive Data Redacted ***"
    return out
