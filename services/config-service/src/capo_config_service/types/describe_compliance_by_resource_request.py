"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeComplianceByResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.base_resource_id
    import capo_config_service.types.compliance_types
    import capo_config_service.types.limit
    import capo_config_service.types.next_token
    import capo_config_service.types.string_with_char_limit256


class DescribeComplianceByResourceRequest(TypedDict, closed=True):
    resource_type: NotRequired[
        "capo_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    ]
    """<p>The types of Amazon Web Services resources for which you want compliance information (for example, <code>AWS::EC2::Instance</code>). For this operation, you can specify that the resource type is an Amazon Web Services account by specifying <code>AWS::::Account</code>.</p>"""
    resource_id: NotRequired[
        "capo_config_service.types.base_resource_id.BaseResourceId"
    ]
    """<p>The ID of the Amazon Web Services resource for which you want compliance information. You can specify only one resource ID. If you specify a resource ID, you must also specify a type for <code>ResourceType</code>.</p>"""
    compliance_types: NotRequired[
        "capo_config_service.types.compliance_types.ComplianceTypes"
    ]
    """<p>Filters the results by compliance.</p>"""
    limit: NotRequired["capo_config_service.types.limit.Limit"]
    """<p>The maximum number of evaluation results returned on each page. The default is 10. You cannot specify a number greater than 100. If you specify 0, Config uses the default.</p>"""
    next_token: NotRequired["capo_config_service.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeComplianceByResourceRequest) -> dict:
    out: dict = {}
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "compliance_types" in value:
        import capo_config_service.types.compliance_types

        out["ComplianceTypes"] = (
            capo_config_service.types.compliance_types.serialize_aws_json_1_1(
                value["compliance_types"]
            )
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeComplianceByResourceRequest:
    out: DescribeComplianceByResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    if data.get("ComplianceTypes") is not None:
        import capo_config_service.types.compliance_types

        out["compliance_types"] = (
            capo_config_service.types.compliance_types.deserialize_aws_json_1_1(
                data["ComplianceTypes"]
            )
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
