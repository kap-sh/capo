"""Generated from Smithy shape ``com.amazonaws.licensemanager#ListReceivedGrantsForOrganizationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.arn
    import capo_license_manager.types.filter_list
    import capo_license_manager.types.max_size100
    import capo_license_manager.types.string


class ListReceivedGrantsForOrganizationRequest(TypedDict, closed=True):
    license_arn: "capo_license_manager.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the received license.</p>"""
    filters: NotRequired["capo_license_manager.types.filter_list.FilterList"]
    """<p>Filters to scope the results. The following filters are supported:</p> <ul> <li> <p> <code>ParentArn</code> </p> </li> <li> <p> <code>GranteePrincipalArn</code> </p> </li> </ul>"""
    next_token: NotRequired["capo_license_manager.types.string.String"]
    """<p>Token for the next set of results.</p>"""
    max_results: NotRequired["capo_license_manager.types.max_size100.MaxSize100"]
    """<p>Maximum number of results to return in a single call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListReceivedGrantsForOrganizationRequest) -> dict:
    out: dict = {}
    out["LicenseArn"] = value["license_arn"]
    if "filters" in value:
        import capo_license_manager.types.filter_list

        out["Filters"] = capo_license_manager.types.filter_list.serialize_aws_json_1_1(
            value["filters"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListReceivedGrantsForOrganizationRequest:
    out: ListReceivedGrantsForOrganizationRequest = {}  # type: ignore[typeddict-item]
    if data.get("LicenseArn") is not None:
        out["license_arn"] = data["LicenseArn"]
    else:
        out["license_arn"] = ""
    if data.get("Filters") is not None:
        import capo_license_manager.types.filter_list

        out["filters"] = (
            capo_license_manager.types.filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
