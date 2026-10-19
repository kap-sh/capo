"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#SolutionBase``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.aws_marketplace_solution_arn
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.date_time
    import capo_partnercentral_selling.types.solution_arn
    import capo_partnercentral_selling.types.solution_identifier
    import capo_partnercentral_selling.types.solution_status


class SolutionBase(TypedDict, closed=True):
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog in which the solution is hosted, either <code>AWS</code> or <code>Sandbox</code>. This helps partners differentiate between live solutions and those in testing environments.</p>"""
    id: "capo_partnercentral_selling.types.solution_identifier.SolutionIdentifier"
    """<p>Enables the association of solutions (offerings) to opportunities.</p>"""
    arn: NotRequired["capo_partnercentral_selling.types.solution_arn.SolutionArn"]
    """<p> The SolutionBase structure provides essential information about a solution. </p>"""
    name: "str"
    """<p>Specifies the solution name.</p>"""
    status: "capo_partnercentral_selling.types.solution_status.SolutionStatus"
    """<p>Specifies the solution's current status, which indicates its state in the system. Valid values: <code>Active</code> | <code>Inactive</code> | <code>Draft</code>. The status helps partners and Amazon Web Services track the solution's lifecycle and availability. Filter for <code>Active</code> solutions for association to an opportunity.</p>"""
    category: "str"
    """<p>Specifies the solution category, which helps to categorize and organize the solutions partners offer. Valid values: <code>Software Product</code> | <code>Consulting Service</code> | <code>Hardware Product</code> | <code>Communications Product</code> | <code>Professional Service</code> | <code>Managed Service</code> | <code>Value-Added Resale Amazon Web Services Service</code> | <code>Distribution Service</code> | <code>Training Service</code> | <code>Merger and Acquisition Advising Service</code>.</p>"""
    created_date: "capo_partnercentral_selling.types.date_time.DateTime"
    """<p>Indicates the solution creation date. This is useful to track and audit.</p>"""
    aws_marketplace_solution_arn: NotRequired[
        "capo_partnercentral_selling.types.aws_marketplace_solution_arn.AwsMarketplaceSolutionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the AWS Marketplace solution associated with this partner solution.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SolutionBase) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    out["Name"] = value["name"]
    import capo_partnercentral_selling.types.solution_status

    out["Status"] = (
        capo_partnercentral_selling.types.solution_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    out["Category"] = value["category"]
    import capo_partnercentral_selling.types.date_time

    out["CreatedDate"] = (
        capo_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
            value["created_date"]
        )
    )
    if "aws_marketplace_solution_arn" in value:
        out["AwsMarketplaceSolutionArn"] = value["aws_marketplace_solution_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SolutionBase:
    out: SolutionBase = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Status") is not None:
        import capo_partnercentral_selling.types.solution_status

        out["status"] = (
            capo_partnercentral_selling.types.solution_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_partnercentral_selling.types.solution_status.SolutionStatus", ""
        )
    if data.get("Category") is not None:
        out["category"] = data["Category"]
    else:
        out["category"] = ""
    if data.get("CreatedDate") is not None:
        import capo_partnercentral_selling.types.date_time

        out["created_date"] = (
            capo_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["CreatedDate"]
            )
        )
    else:
        import datetime

        out["created_date"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("AwsMarketplaceSolutionArn") is not None:
        out["aws_marketplace_solution_arn"] = data["AwsMarketplaceSolutionArn"]
    return out
