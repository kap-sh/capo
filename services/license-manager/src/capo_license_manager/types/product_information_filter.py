"""Generated from Smithy shape ``com.amazonaws.licensemanager#ProductInformationFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.string
    import capo_license_manager.types.string_list


class ProductInformationFilter(TypedDict, closed=True):
    product_information_filter_name: "capo_license_manager.types.string.String"
    """<p>Filter name.</p>"""
    product_information_filter_value: NotRequired[
        "capo_license_manager.types.string_list.StringList"
    ]
    """<p>Filter value.</p>"""
    product_information_filter_comparator: "capo_license_manager.types.string.String"
    """<p>Logical operator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductInformationFilter) -> dict:
    out: dict = {}
    out["ProductInformationFilterName"] = value["product_information_filter_name"]
    if "product_information_filter_value" in value:
        import capo_license_manager.types.string_list

        out["ProductInformationFilterValue"] = (
            capo_license_manager.types.string_list.serialize_aws_json_1_1(
                value["product_information_filter_value"]
            )
        )
    out["ProductInformationFilterComparator"] = value[
        "product_information_filter_comparator"
    ]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProductInformationFilter:
    out: ProductInformationFilter = {}  # type: ignore[typeddict-item]
    if data.get("ProductInformationFilterName") is not None:
        out["product_information_filter_name"] = data["ProductInformationFilterName"]
    else:
        out["product_information_filter_name"] = ""
    if data.get("ProductInformationFilterValue") is not None:
        import capo_license_manager.types.string_list

        out["product_information_filter_value"] = (
            capo_license_manager.types.string_list.deserialize_aws_json_1_1(
                data["ProductInformationFilterValue"]
            )
        )
    if data.get("ProductInformationFilterComparator") is not None:
        out["product_information_filter_comparator"] = data[
            "ProductInformationFilterComparator"
        ]
    else:
        out["product_information_filter_comparator"] = ""
    return out
