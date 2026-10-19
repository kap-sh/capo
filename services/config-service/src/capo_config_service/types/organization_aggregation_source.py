"""Generated from Smithy shape ``com.amazonaws.configservice#OrganizationAggregationSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.aggregator_region_list
    import capo_config_service.types.boolean
    import capo_config_service.types.string


class OrganizationAggregationSource(TypedDict, closed=True):
    role_arn: "capo_config_service.types.string.String"
    """<p>ARN of the IAM role used to retrieve Amazon Web Services Organization details associated with the aggregator account.</p>"""
    aws_regions: NotRequired[
        "capo_config_service.types.aggregator_region_list.AggregatorRegionList"
    ]
    """<p>The source regions being aggregated.</p>"""
    all_aws_regions: "capo_config_service.types.boolean.Boolean"
    """<p>If true, aggregate existing Config regions and future regions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationAggregationSource) -> dict:
    out: dict = {}
    out["RoleArn"] = value["role_arn"]
    if "aws_regions" in value:
        import capo_config_service.types.aggregator_region_list

        out["AwsRegions"] = (
            capo_config_service.types.aggregator_region_list.serialize_aws_json_1_1(
                value["aws_regions"]
            )
        )
    out["AllAwsRegions"] = value.get("all_aws_regions", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> OrganizationAggregationSource:
    out: OrganizationAggregationSource = {}  # type: ignore[typeddict-item]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        out["role_arn"] = ""
    if data.get("AwsRegions") is not None:
        import capo_config_service.types.aggregator_region_list

        out["aws_regions"] = (
            capo_config_service.types.aggregator_region_list.deserialize_aws_json_1_1(
                data["AwsRegions"]
            )
        )
    if data.get("AllAwsRegions") is not None:
        out["all_aws_regions"] = data["AllAwsRegions"]
    else:
        out["all_aws_regions"] = False
    return out
