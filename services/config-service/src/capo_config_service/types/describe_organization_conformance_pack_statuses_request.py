"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeOrganizationConformancePackStatusesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.cosmos_page_limit
    import capo_config_service.types.organization_conformance_pack_names
    import capo_config_service.types.string


class DescribeOrganizationConformancePackStatusesRequest(TypedDict, closed=True):
    organization_conformance_pack_names: NotRequired[
        "capo_config_service.types.organization_conformance_pack_names.OrganizationConformancePackNames"
    ]
    """<p>The names of organization conformance packs for which you want status details. If you do not specify any names, Config returns details for all your organization conformance packs. </p>"""
    limit: NotRequired["capo_config_service.types.cosmos_page_limit.CosmosPageLimit"]
    """<p>The maximum number of OrganizationConformancePackStatuses returned on each page. If you do no specify a number, Config uses the default. The default is 100. </p>"""
    next_token: NotRequired["capo_config_service.types.string.String"]
    """<p>The nextToken string returned on a previous page that you use to get the next page of results in a paginated response. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeOrganizationConformancePackStatusesRequest,
) -> dict:
    out: dict = {}
    if "organization_conformance_pack_names" in value:
        import capo_config_service.types.organization_conformance_pack_names

        out["OrganizationConformancePackNames"] = (
            capo_config_service.types.organization_conformance_pack_names.serialize_aws_json_1_1(
                value["organization_conformance_pack_names"]
            )
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeOrganizationConformancePackStatusesRequest:
    out: DescribeOrganizationConformancePackStatusesRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationConformancePackNames") is not None:
        import capo_config_service.types.organization_conformance_pack_names

        out["organization_conformance_pack_names"] = (
            capo_config_service.types.organization_conformance_pack_names.deserialize_aws_json_1_1(
                data["OrganizationConformancePackNames"]
            )
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
