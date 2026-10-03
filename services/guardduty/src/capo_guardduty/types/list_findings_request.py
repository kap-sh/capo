"""Generated from Smithy shape ``com.amazonaws.guardduty#ListFindingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.detector_id
    import capo_guardduty.types.finding_criteria
    import capo_guardduty.types.max_results
    import capo_guardduty.types.sort_criteria
    import capo_guardduty.types.string


class ListFindingsRequest(TypedDict, closed=True):
    detector_id: "capo_guardduty.types.detector_id.DetectorId"
    """<p>The ID of the detector that specifies the GuardDuty service whose findings you want to list.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>"""
    finding_criteria: NotRequired[
        "capo_guardduty.types.finding_criteria.FindingCriteria"
    ]
    """<p>Represents the criteria used for querying findings. Valid values include:</p> <ul> <li> <p>JSON field name</p> </li> <li> <p>accountId</p> </li> <li> <p>region</p> </li> <li> <p>confidence</p> </li> <li> <p>id</p> </li> <li> <p>resource.accessKeyDetails.accessKeyId</p> </li> <li> <p>resource.accessKeyDetails.principalId</p> </li> <li> <p>resource.accessKeyDetails.userName</p> </li> <li> <p>resource.accessKeyDetails.userType</p> </li> <li> <p>resource.instanceDetails.iamInstanceProfile.id</p> </li> <li> <p>resource.instanceDetails.imageId</p> </li> <li> <p>resource.instanceDetails.instanceId</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.ipv6Addresses</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.privateIpAddresses.privateIpAddress</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.publicDnsName</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.publicIp</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.securityGroups.groupId</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.securityGroups.groupName</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.subnetId</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.vpcId</p> </li> <li> <p>resource.instanceDetails.tags.key</p> </li> <li> <p>resource.instanceDetails.tags.value</p> </li> <li> <p>resource.resourceType</p> </li> <li> <p>service.action.actionType</p> </li> <li> <p>service.action.awsApiCallAction.api</p> </li> <li> <p>service.action.awsApiCallAction.callerType</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.city.cityName</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.country.countryName</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.ipAddressV4</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.organization.asn</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.organization.asnOrg</p> </li> <li> <p>service.action.awsApiCallAction.serviceName</p> </li> <li> <p>service.action.dnsRequestAction.domain</p> </li> <li> <p>service.action.dnsRequestAction.domainWithSuffix</p> </li> <li> <p>service.action.networkConnectionAction.blocked</p> </li> <li> <p>service.action.networkConnectionAction.connectionDirection</p> </li> <li> <p>service.action.networkConnectionAction.localPortDetails.port</p> </li> <li> <p>service.action.networkConnectionAction.protocol</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.country.countryName</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.ipAddressV4</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.organization.asn</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.organization.asnOrg</p> </li> <li> <p>service.action.networkConnectionAction.remotePortDetails.port</p> </li> <li> <p>service.additionalInfo.threatListName</p> </li> <li> <p>service.archived</p> <p>When this attribute is set to 'true', only archived findings are listed. When it's set to 'false', only unarchived findings are listed. When this attribute is not set, all existing findings are listed.</p> </li> <li> <p>service.ebsVolumeScanDetails.scanId</p> </li> <li> <p>service.resourceRole</p> </li> <li> <p>severity</p> </li> <li> <p>type</p> </li> <li> <p>updatedAt</p> <p>Type: Timestamp in Unix Epoch millisecond format: 1486685375000</p> </li> </ul>"""
    sort_criteria: NotRequired["capo_guardduty.types.sort_criteria.SortCriteria"]
    """<p>Represents the criteria used for sorting findings.</p>"""
    max_results: NotRequired["capo_guardduty.types.max_results.MaxResults"]
    """<p>You can use this parameter to indicate the maximum number of items you want in the response. The default value is 50. The maximum value is 50.</p>"""
    next_token: NotRequired["capo_guardduty.types.string.String"]
    """<p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFindingsRequest) -> dict:
    out: dict = {}
    if "finding_criteria" in value:
        import capo_guardduty.types.finding_criteria

        out["findingCriteria"] = capo_guardduty.types.finding_criteria.serialize_json(
            value["finding_criteria"]
        )
    if "sort_criteria" in value:
        import capo_guardduty.types.sort_criteria

        out["sortCriteria"] = capo_guardduty.types.sort_criteria.serialize_json(
            value["sort_criteria"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFindingsRequest:
    out: ListFindingsRequest = {}  # type: ignore[typeddict-item]
    if data.get("findingCriteria") is not None:
        import capo_guardduty.types.finding_criteria

        out["finding_criteria"] = (
            capo_guardduty.types.finding_criteria.deserialize_json(
                data["findingCriteria"]
            )
        )
    if data.get("sortCriteria") is not None:
        import capo_guardduty.types.sort_criteria

        out["sort_criteria"] = capo_guardduty.types.sort_criteria.deserialize_json(
            data["sortCriteria"]
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
