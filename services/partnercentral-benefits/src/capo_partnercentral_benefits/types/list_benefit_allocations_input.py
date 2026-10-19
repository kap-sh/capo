"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#ListBenefitAllocationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.benefit_allocation_status_list
    import capo_partnercentral_benefits.types.benefit_application_identifier_list
    import capo_partnercentral_benefits.types.benefit_identifiers
    import capo_partnercentral_benefits.types.catalog_name
    import capo_partnercentral_benefits.types.fulfillment_types


class ListBenefitAllocationsInput(TypedDict, closed=True):
    catalog: "capo_partnercentral_benefits.types.catalog_name.CatalogName"
    """<p>The catalog identifier to filter benefit allocations by catalog.</p>"""
    fulfillment_types: NotRequired[
        "capo_partnercentral_benefits.types.fulfillment_types.FulfillmentTypes"
    ]
    """<p>Filter benefit allocations by specific fulfillment types.</p>"""
    benefit_identifiers: NotRequired[
        "capo_partnercentral_benefits.types.benefit_identifiers.BenefitIdentifiers"
    ]
    """<p>Filter benefit allocations by specific benefit identifiers.</p>"""
    benefit_application_identifiers: NotRequired[
        "capo_partnercentral_benefits.types.benefit_application_identifier_list.BenefitApplicationIdentifierList"
    ]
    """<p>Filter benefit allocations by specific benefit application identifiers.</p>"""
    status: NotRequired[
        "capo_partnercentral_benefits.types.benefit_allocation_status_list.BenefitAllocationStatusList"
    ]
    """<p>Filter benefit allocations by their current status.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of benefit allocations to return in a single response.</p>"""
    next_token: NotRequired["str"]
    """<p>A pagination token to retrieve the next set of results from a previous request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListBenefitAllocationsInput) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    if "fulfillment_types" in value:
        import capo_partnercentral_benefits.types.fulfillment_types

        out["FulfillmentTypes"] = (
            capo_partnercentral_benefits.types.fulfillment_types.serialize_aws_json_1_0(
                value["fulfillment_types"]
            )
        )
    if "benefit_identifiers" in value:
        import capo_partnercentral_benefits.types.benefit_identifiers

        out["BenefitIdentifiers"] = (
            capo_partnercentral_benefits.types.benefit_identifiers.serialize_aws_json_1_0(
                value["benefit_identifiers"]
            )
        )
    if "benefit_application_identifiers" in value:
        import capo_partnercentral_benefits.types.benefit_application_identifier_list

        out["BenefitApplicationIdentifiers"] = (
            capo_partnercentral_benefits.types.benefit_application_identifier_list.serialize_aws_json_1_0(
                value["benefit_application_identifiers"]
            )
        )
    if "status" in value:
        import capo_partnercentral_benefits.types.benefit_allocation_status_list

        out["Status"] = (
            capo_partnercentral_benefits.types.benefit_allocation_status_list.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListBenefitAllocationsInput:
    out: ListBenefitAllocationsInput = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("FulfillmentTypes") is not None:
        import capo_partnercentral_benefits.types.fulfillment_types

        out["fulfillment_types"] = (
            capo_partnercentral_benefits.types.fulfillment_types.deserialize_aws_json_1_0(
                data["FulfillmentTypes"]
            )
        )
    if data.get("BenefitIdentifiers") is not None:
        import capo_partnercentral_benefits.types.benefit_identifiers

        out["benefit_identifiers"] = (
            capo_partnercentral_benefits.types.benefit_identifiers.deserialize_aws_json_1_0(
                data["BenefitIdentifiers"]
            )
        )
    if data.get("BenefitApplicationIdentifiers") is not None:
        import capo_partnercentral_benefits.types.benefit_application_identifier_list

        out["benefit_application_identifiers"] = (
            capo_partnercentral_benefits.types.benefit_application_identifier_list.deserialize_aws_json_1_0(
                data["BenefitApplicationIdentifiers"]
            )
        )
    if data.get("Status") is not None:
        import capo_partnercentral_benefits.types.benefit_allocation_status_list

        out["status"] = (
            capo_partnercentral_benefits.types.benefit_allocation_status_list.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
