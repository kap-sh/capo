"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#RecallBenefitApplicationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.benefit_application_identifier
    import capo_partnercentral_benefits.types.catalog_name


class RecallBenefitApplicationInput(TypedDict, closed=True):
    catalog: "capo_partnercentral_benefits.types.catalog_name.CatalogName"
    """<p>The catalog identifier that specifies which benefit catalog the application belongs to.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier to ensure idempotent processing of the recall request.</p>"""
    identifier: "capo_partnercentral_benefits.types.benefit_application_identifier.BenefitApplicationIdentifier"
    """<p>The unique identifier of the benefit application to recall.</p>"""
    reason: "str"
    """<p>A descriptive reason explaining why the benefit application is being recalled.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecallBenefitApplicationInput) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["Identifier"] = value["identifier"]
    out["Reason"] = value["reason"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RecallBenefitApplicationInput:
    out: RecallBenefitApplicationInput = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    if data.get("Reason") is not None:
        out["reason"] = data["Reason"]
    else:
        out["reason"] = ""
    return out
