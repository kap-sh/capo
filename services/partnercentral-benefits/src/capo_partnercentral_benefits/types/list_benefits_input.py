"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#ListBenefitsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.benefit_statuses
    import capo_partnercentral_benefits.types.catalog_name
    import capo_partnercentral_benefits.types.fulfillment_types
    import capo_partnercentral_benefits.types.programs


class ListBenefitsInput(TypedDict, closed=True):
    catalog: "capo_partnercentral_benefits.types.catalog_name.CatalogName"
    """<p>The catalog identifier to filter benefits by catalog.</p>"""
    programs: NotRequired["capo_partnercentral_benefits.types.programs.Programs"]
    """<p>Filter benefits by specific AWS partner programs.</p>"""
    fulfillment_types: NotRequired[
        "capo_partnercentral_benefits.types.fulfillment_types.FulfillmentTypes"
    ]
    """<p>Filter benefits by specific fulfillment types.</p>"""
    status: NotRequired[
        "capo_partnercentral_benefits.types.benefit_statuses.BenefitStatuses"
    ]
    """<p>Filter benefits by their current status.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of benefits to return in a single response.</p>"""
    next_token: NotRequired["str"]
    """<p>A pagination token to retrieve the next set of results from a previous request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListBenefitsInput) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    if "programs" in value:
        import capo_partnercentral_benefits.types.programs

        out["Programs"] = (
            capo_partnercentral_benefits.types.programs.serialize_aws_json_1_0(
                value["programs"]
            )
        )
    if "fulfillment_types" in value:
        import capo_partnercentral_benefits.types.fulfillment_types

        out["FulfillmentTypes"] = (
            capo_partnercentral_benefits.types.fulfillment_types.serialize_aws_json_1_0(
                value["fulfillment_types"]
            )
        )
    if "status" in value:
        import capo_partnercentral_benefits.types.benefit_statuses

        out["Status"] = (
            capo_partnercentral_benefits.types.benefit_statuses.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListBenefitsInput:
    out: ListBenefitsInput = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("Programs") is not None:
        import capo_partnercentral_benefits.types.programs

        out["programs"] = (
            capo_partnercentral_benefits.types.programs.deserialize_aws_json_1_0(
                data["Programs"]
            )
        )
    if data.get("FulfillmentTypes") is not None:
        import capo_partnercentral_benefits.types.fulfillment_types

        out["fulfillment_types"] = (
            capo_partnercentral_benefits.types.fulfillment_types.deserialize_aws_json_1_0(
                data["FulfillmentTypes"]
            )
        )
    if data.get("Status") is not None:
        import capo_partnercentral_benefits.types.benefit_statuses

        out["status"] = (
            capo_partnercentral_benefits.types.benefit_statuses.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
