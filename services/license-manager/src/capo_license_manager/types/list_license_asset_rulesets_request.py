"""Generated from Smithy shape ``com.amazonaws.licensemanager#ListLicenseAssetRulesetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.boolean
    import capo_license_manager.types.box_integer
    import capo_license_manager.types.filters
    import capo_license_manager.types.string


class ListLicenseAssetRulesetsRequest(TypedDict, closed=True):
    filters: NotRequired["capo_license_manager.types.filters.Filters"]
    """<p>Filters to scope the results. Following filters are supported</p> <ul> <li> <p> <code>Name</code> </p> </li> </ul>"""
    show_aws_managed_license_asset_rulesets: NotRequired[
        "capo_license_manager.types.boolean.Boolean"
    ]
    """<p>Specifies whether to show License Manager managed license asset rulesets.</p>"""
    max_results: NotRequired["capo_license_manager.types.box_integer.BoxInteger"]
    """<p>Maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["capo_license_manager.types.string.String"]
    """<p>Token for the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLicenseAssetRulesetsRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_license_manager.types.filters

        out["Filters"] = capo_license_manager.types.filters.serialize_aws_json_1_1(
            value["filters"]
        )
    if "show_aws_managed_license_asset_rulesets" in value:
        out["ShowAWSManagedLicenseAssetRulesets"] = value[
            "show_aws_managed_license_asset_rulesets"
        ]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLicenseAssetRulesetsRequest:
    out: ListLicenseAssetRulesetsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Filters") is not None:
        import capo_license_manager.types.filters

        out["filters"] = capo_license_manager.types.filters.deserialize_aws_json_1_1(
            data["Filters"]
        )
    if data.get("ShowAWSManagedLicenseAssetRulesets") is not None:
        out["show_aws_managed_license_asset_rulesets"] = data[
            "ShowAWSManagedLicenseAssetRulesets"
        ]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
