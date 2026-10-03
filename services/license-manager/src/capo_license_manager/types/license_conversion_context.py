"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseConversionContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.product_code_list
    import capo_license_manager.types.usage_operation


class LicenseConversionContext(TypedDict, closed=True):
    usage_operation: NotRequired[
        "capo_license_manager.types.usage_operation.UsageOperation"
    ]
    """<p>The Usage operation value that corresponds to the license type you are converting your resource from. For more information about which platforms correspond to which usage operation values see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/billing-info-fields.html#billing-info">Sample data: usage operation by platform </a> </p>"""
    product_codes: NotRequired[
        "capo_license_manager.types.product_code_list.ProductCodeList"
    ]
    """<p>Product codes referred to in the license conversion process.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseConversionContext) -> dict:
    out: dict = {}
    if "usage_operation" in value:
        out["UsageOperation"] = value["usage_operation"]
    if "product_codes" in value:
        import capo_license_manager.types.product_code_list

        out["ProductCodes"] = (
            capo_license_manager.types.product_code_list.serialize_aws_json_1_1(
                value["product_codes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LicenseConversionContext:
    out: LicenseConversionContext = {}  # type: ignore[typeddict-item]
    if data.get("UsageOperation") is not None:
        out["usage_operation"] = data["UsageOperation"]
    if data.get("ProductCodes") is not None:
        import capo_license_manager.types.product_code_list

        out["product_codes"] = (
            capo_license_manager.types.product_code_list.deserialize_aws_json_1_1(
                data["ProductCodes"]
            )
        )
    return out
