"""Generated from Smithy shape ``com.amazonaws.configservice#GetOrganizationConformancePackDetailedStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_config_service.types.cosmos_page_limit
    import capo_config_service.types.organization_conformance_pack_name
    import capo_config_service.types.organization_resource_detailed_status_filters
    import capo_config_service.types.string


class GetOrganizationConformancePackDetailedStatusRequest(TypedDict, closed=True):
    organization_conformance_pack_name: "capo_config_service.types.organization_conformance_pack_name.OrganizationConformancePackName"
    """<p>The name of organization conformance pack for which you want status details for member accounts.</p>"""
    filters: NotRequired[
        "capo_config_service.types.organization_resource_detailed_status_filters.OrganizationResourceDetailedStatusFilters"
    ]
    """<p>An <code>OrganizationResourceDetailedStatusFilters</code> object.</p>"""
    limit: NotRequired["capo_config_service.types.cosmos_page_limit.CosmosPageLimit"]
    """<p>The maximum number of <code>OrganizationConformancePackDetailedStatuses</code> returned on each page. If you do not specify a number, Config uses the default. The default is 100. </p>"""
    next_token: NotRequired["capo_config_service.types.string.String"]
    """<p>The nextToken string returned on a previous page that you use to get the next page of results in a paginated response. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: GetOrganizationConformancePackDetailedStatusRequest,
) -> dict:
    out: dict = {}
    out["OrganizationConformancePackName"] = value["organization_conformance_pack_name"]
    if "filters" in value:
        import capo_config_service.types.organization_resource_detailed_status_filters

        out["Filters"] = (
            capo_config_service.types.organization_resource_detailed_status_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetOrganizationConformancePackDetailedStatusRequest:
    out: GetOrganizationConformancePackDetailedStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationConformancePackName") is not None:
        out["organization_conformance_pack_name"] = data[
            "OrganizationConformancePackName"
        ]
    else:
        raise DeserializationError(
            "GetOrganizationConformancePackDetailedStatusRequest.organization_conformance_pack_name required"
        )
    if data.get("Filters") is not None:
        import capo_config_service.types.organization_resource_detailed_status_filters

        out["filters"] = (
            capo_config_service.types.organization_resource_detailed_status_filters.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
