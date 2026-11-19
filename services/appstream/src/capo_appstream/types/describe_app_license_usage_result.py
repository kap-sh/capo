"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeAppLicenseUsageResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.admin_app_license_usage_list
    import capo_appstream.types.string


class DescribeAppLicenseUsageResult(TypedDict, closed=True):
    app_license_usages: NotRequired[
        "capo_appstream.types.admin_app_license_usage_list.AdminAppLicenseUsageList"
    ]
    """<p>Collection of license usage records.</p>"""
    next_token: NotRequired["capo_appstream.types.string.String"]
    """<p>Token for pagination of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAppLicenseUsageResult) -> dict:
    out: dict = {}
    if "app_license_usages" in value:
        import capo_appstream.types.admin_app_license_usage_list

        out["AppLicenseUsages"] = (
            capo_appstream.types.admin_app_license_usage_list.serialize_aws_json_1_1(
                value["app_license_usages"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAppLicenseUsageResult:
    out: DescribeAppLicenseUsageResult = {}  # type: ignore[typeddict-item]
    if data.get("AppLicenseUsages") is not None:
        import capo_appstream.types.admin_app_license_usage_list

        out["app_license_usages"] = (
            capo_appstream.types.admin_app_license_usage_list.deserialize_aws_json_1_1(
                data["AppLicenseUsages"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeAppLicenseUsageResult) -> dict:
    out: dict = {}
    if "app_license_usages" in value:
        import capo_appstream.types.admin_app_license_usage_list

        out["AppLicenseUsages"] = (
            capo_appstream.types.admin_app_license_usage_list.serialize_cbor(
                value["app_license_usages"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeAppLicenseUsageResult:
    out: DescribeAppLicenseUsageResult = {}  # type: ignore[typeddict-item]
    if data.get("AppLicenseUsages") is not None:
        import capo_appstream.types.admin_app_license_usage_list

        out["app_license_usages"] = (
            capo_appstream.types.admin_app_license_usage_list.deserialize_cbor(
                data["AppLicenseUsages"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
