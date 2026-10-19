"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#ListBenefitApplicationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.arns
    import capo_partnercentral_benefits.types.associated_resources
    import capo_partnercentral_benefits.types.benefit_identifiers
    import capo_partnercentral_benefits.types.catalog_name
    import capo_partnercentral_benefits.types.fulfillment_types
    import capo_partnercentral_benefits.types.programs
    import capo_partnercentral_benefits.types.stages
    import capo_partnercentral_benefits.types.statuses


class ListBenefitApplicationsInput(TypedDict, closed=True):
    catalog: "capo_partnercentral_benefits.types.catalog_name.CatalogName"
    """<p>The catalog identifier to filter benefit applications by catalog.</p>"""
    programs: NotRequired["capo_partnercentral_benefits.types.programs.Programs"]
    """<p>Filter benefit applications by specific AWS partner programs.</p>"""
    fulfillment_types: NotRequired[
        "capo_partnercentral_benefits.types.fulfillment_types.FulfillmentTypes"
    ]
    """<p>Filter benefit applications by specific fulfillment types.</p>"""
    benefit_identifiers: NotRequired[
        "capo_partnercentral_benefits.types.benefit_identifiers.BenefitIdentifiers"
    ]
    """<p>Filter benefit applications by specific benefit identifiers.</p>"""
    status: NotRequired["capo_partnercentral_benefits.types.statuses.Statuses"]
    """<p>Filter benefit applications by their current processing status.</p>"""
    stages: NotRequired["capo_partnercentral_benefits.types.stages.Stages"]
    """<p>Filter benefit applications by their current processing stage.</p>"""
    associated_resources: NotRequired[
        "capo_partnercentral_benefits.types.associated_resources.AssociatedResources"
    ]
    """<p>Filter benefit applications by associated AWS resources.</p>"""
    associated_resource_arns: NotRequired[
        "capo_partnercentral_benefits.types.arns.Arns"
    ]
    """<p>Filter benefit applications by specific AWS resource ARNs.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of benefit applications to return in a single response.</p>"""
    next_token: NotRequired["str"]
    """<p>A pagination token to retrieve the next set of results from a previous request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListBenefitApplicationsInput) -> dict:
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
    if "benefit_identifiers" in value:
        import capo_partnercentral_benefits.types.benefit_identifiers

        out["BenefitIdentifiers"] = (
            capo_partnercentral_benefits.types.benefit_identifiers.serialize_aws_json_1_0(
                value["benefit_identifiers"]
            )
        )
    if "status" in value:
        import capo_partnercentral_benefits.types.statuses

        out["Status"] = (
            capo_partnercentral_benefits.types.statuses.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "stages" in value:
        import capo_partnercentral_benefits.types.stages

        out["Stages"] = (
            capo_partnercentral_benefits.types.stages.serialize_aws_json_1_0(
                value["stages"]
            )
        )
    if "associated_resources" in value:
        import capo_partnercentral_benefits.types.associated_resources

        out["AssociatedResources"] = (
            capo_partnercentral_benefits.types.associated_resources.serialize_aws_json_1_0(
                value["associated_resources"]
            )
        )
    if "associated_resource_arns" in value:
        import capo_partnercentral_benefits.types.arns

        out["AssociatedResourceArns"] = (
            capo_partnercentral_benefits.types.arns.serialize_aws_json_1_0(
                value["associated_resource_arns"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListBenefitApplicationsInput:
    out: ListBenefitApplicationsInput = {}  # type: ignore[typeddict-item]
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
    if data.get("BenefitIdentifiers") is not None:
        import capo_partnercentral_benefits.types.benefit_identifiers

        out["benefit_identifiers"] = (
            capo_partnercentral_benefits.types.benefit_identifiers.deserialize_aws_json_1_0(
                data["BenefitIdentifiers"]
            )
        )
    if data.get("Status") is not None:
        import capo_partnercentral_benefits.types.statuses

        out["status"] = (
            capo_partnercentral_benefits.types.statuses.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if data.get("Stages") is not None:
        import capo_partnercentral_benefits.types.stages

        out["stages"] = (
            capo_partnercentral_benefits.types.stages.deserialize_aws_json_1_0(
                data["Stages"]
            )
        )
    if data.get("AssociatedResources") is not None:
        import capo_partnercentral_benefits.types.associated_resources

        out["associated_resources"] = (
            capo_partnercentral_benefits.types.associated_resources.deserialize_aws_json_1_0(
                data["AssociatedResources"]
            )
        )
    if data.get("AssociatedResourceArns") is not None:
        import capo_partnercentral_benefits.types.arns

        out["associated_resource_arns"] = (
            capo_partnercentral_benefits.types.arns.deserialize_aws_json_1_0(
                data["AssociatedResourceArns"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
