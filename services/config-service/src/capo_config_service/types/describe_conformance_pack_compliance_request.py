"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeConformancePackComplianceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_config_service.types.conformance_pack_compliance_filters
    import capo_config_service.types.conformance_pack_name
    import capo_config_service.types.describe_conformance_pack_compliance_limit
    import capo_config_service.types.next_token


class DescribeConformancePackComplianceRequest(TypedDict, closed=True):
    conformance_pack_name: (
        "capo_config_service.types.conformance_pack_name.ConformancePackName"
    )
    """<p>Name of the conformance pack.</p>"""
    filters: NotRequired[
        "capo_config_service.types.conformance_pack_compliance_filters.ConformancePackComplianceFilters"
    ]
    """<p>A <code>ConformancePackComplianceFilters</code> object.</p>"""
    limit: NotRequired[
        "capo_config_service.types.describe_conformance_pack_compliance_limit.DescribeConformancePackComplianceLimit"
    ]
    """<p>The maximum number of Config rules within a conformance pack are returned on each page.</p>"""
    next_token: NotRequired["capo_config_service.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> string returned in a previous request that you use to request the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConformancePackComplianceRequest) -> dict:
    out: dict = {}
    out["ConformancePackName"] = value["conformance_pack_name"]
    if "filters" in value:
        import capo_config_service.types.conformance_pack_compliance_filters

        out["Filters"] = (
            capo_config_service.types.conformance_pack_compliance_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConformancePackComplianceRequest:
    out: DescribeConformancePackComplianceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConformancePackName") is not None:
        out["conformance_pack_name"] = data["ConformancePackName"]
    else:
        raise DeserializationError(
            "DescribeConformancePackComplianceRequest.conformance_pack_name required"
        )
    if data.get("Filters") is not None:
        import capo_config_service.types.conformance_pack_compliance_filters

        out["filters"] = (
            capo_config_service.types.conformance_pack_compliance_filters.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
