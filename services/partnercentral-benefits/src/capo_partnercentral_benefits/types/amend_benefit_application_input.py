"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#AmendBenefitApplicationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.amendment_list
    import capo_partnercentral_benefits.types.benefit_application_identifier
    import capo_partnercentral_benefits.types.catalog_name


class AmendBenefitApplicationInput(TypedDict, closed=True):
    catalog: "capo_partnercentral_benefits.types.catalog_name.CatalogName"
    """<p>The catalog identifier that specifies which benefit catalog the application belongs to.</p>"""
    client_token: "str"
    """<p>A unique, case-sensitive identifier to ensure idempotent processing of the amendment request.</p>"""
    revision: "str"
    """<p>The current revision number of the benefit application to ensure optimistic concurrency control.</p>"""
    identifier: "capo_partnercentral_benefits.types.benefit_application_identifier.BenefitApplicationIdentifier"
    """<p>The unique identifier of the benefit application to be amended.</p>"""
    amendment_reason: "str"
    """<p>A descriptive reason explaining why the benefit application is being amended.</p>"""
    amendments: "capo_partnercentral_benefits.types.amendment_list.AmendmentList"
    """<p>A list of specific field amendments to apply to the benefit application.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AmendBenefitApplicationInput) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["ClientToken"] = value["client_token"]
    out["Revision"] = value["revision"]
    out["Identifier"] = value["identifier"]
    out["AmendmentReason"] = value["amendment_reason"]
    import capo_partnercentral_benefits.types.amendment_list

    out["Amendments"] = (
        capo_partnercentral_benefits.types.amendment_list.serialize_aws_json_1_0(
            value["amendments"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> AmendBenefitApplicationInput:
    out: AmendBenefitApplicationInput = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        out["client_token"] = ""
    if data.get("Revision") is not None:
        out["revision"] = data["Revision"]
    else:
        out["revision"] = ""
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    if data.get("AmendmentReason") is not None:
        out["amendment_reason"] = data["AmendmentReason"]
    else:
        out["amendment_reason"] = ""
    if data.get("Amendments") is not None:
        import capo_partnercentral_benefits.types.amendment_list

        out["amendments"] = (
            capo_partnercentral_benefits.types.amendment_list.deserialize_aws_json_1_0(
                data["Amendments"]
            )
        )
    else:
        out["amendments"] = []
    return out
