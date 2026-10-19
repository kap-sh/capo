"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#CancelBenefitApplicationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.benefit_application_identifier
    import capo_partnercentral_benefits.types.catalog_name


class CancelBenefitApplicationInput(TypedDict, closed=True):
    catalog: "capo_partnercentral_benefits.types.catalog_name.CatalogName"
    """<p>The catalog identifier that specifies which benefit catalog the application belongs to.</p>"""
    client_token: "str"
    """<p>A unique, case-sensitive identifier to ensure idempotent processing of the cancellation request.</p>"""
    identifier: "capo_partnercentral_benefits.types.benefit_application_identifier.BenefitApplicationIdentifier"
    """<p>The unique identifier of the benefit application to cancel.</p>"""
    reason: NotRequired["str"]
    """<p>A descriptive reason explaining why the benefit application is being cancelled.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelBenefitApplicationInput) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["ClientToken"] = value["client_token"]
    out["Identifier"] = value["identifier"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelBenefitApplicationInput:
    out: CancelBenefitApplicationInput = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        out["client_token"] = ""
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    if data.get("Reason") is not None:
        out["reason"] = data["Reason"]
    return out
