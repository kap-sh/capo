"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#PartnerSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_account.types.catalog
    import capo_partnercentral_account.types.date_time
    import capo_partnercentral_account.types.partner_arn
    import capo_partnercentral_account.types.partner_id
    import capo_partnercentral_account.types.sensitive_unicode_string


class PartnerSummary(TypedDict, closed=True):
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


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PartnerSummary) -> dict:
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
    return out


def deserialize_aws_json_1_0(data: dict) -> PartnerSummary:
    out: PartnerSummary = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("PartnerSummary.catalog required")
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("PartnerSummary.arn required")
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("PartnerSummary.id required")
    if data.get("LegalName") is not None:
        out["legal_name"] = data["LegalName"]
    else:
        raise DeserializationError("PartnerSummary.legal_name required")
    if data.get("CreatedAt") is not None:
        import capo_partnercentral_account.types.date_time

        out["created_at"] = (
            capo_partnercentral_account.types.date_time.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    else:
        raise DeserializationError("PartnerSummary.created_at required")
    return out


def redact_sensitive(value: PartnerSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "legal_name" in value:
        out["legal_name"] = "*** Sensitive Data Redacted ***"
    return out
