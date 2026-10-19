"""Generated from Smithy shape ``com.amazonaws.licensemanager#ProductInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.product_information_filter_list
    import capo_license_manager.types.string


class ProductInformation(TypedDict, closed=True):
    resource_type: "capo_license_manager.types.string.String"
    """<p>Resource type. The possible values are <code>SSM_MANAGED</code> | <code>RDS</code>.</p>"""
    product_information_filter_list: "capo_license_manager.types.product_information_filter_list.ProductInformationFilterList"
    """<p>A Product information filter consists of a <code>ProductInformationFilterComparator</code> which is a logical operator, a <code>ProductInformationFilterName</code> which specifies the type of filter being declared, and a <code>ProductInformationFilterValue</code> that specifies the value to filter on. </p> <p>Accepted values for <code>ProductInformationFilterName</code> are listed here along with descriptions and valid options for <code>ProductInformationFilterComparator</code>. </p> <p>The following filters and are supported when the resource type is <code>SSM_MANAGED</code>:</p> <ul> <li> <p> <code>Application Name</code> - The name of the application. Logical operator is <code>EQUALS</code>.</p> </li> <li> <p> <code>Application Publisher</code> - The publisher of the application. Logical operator is <code>EQUALS</code>.</p> </li> <li> <p> <code>Application Version</code> - The version of the application. Logical operator is <code>EQUALS</code>.</p> </li> <li> <p> <code>Platform Name</code> - The name of the platform. Logical operator is <code>EQUALS</code>.</p> </li> <li> <p> <code>Platform Type</code> - The platform type. Logical operator is <code>EQUALS</code>.</p> </li> <li> <p> <code>Tag:key</code> - The key of a tag attached to an Amazon Web Services resource you wish to exclude from automated discovery. Logical operator is <code>NOT_EQUALS</code>. The key for your tag must be appended to <code>Tag:</code> following the example: <code>Tag:name-of-your-key</code>. <code>ProductInformationFilterValue</code> is optional if you are not using values for the key. </p> </li> <li> <p> <code>AccountId</code> - The 12-digit ID of an Amazon Web Services account you wish to exclude from automated discovery. Logical operator is <code>NOT_EQUALS</code>.</p> </li> <li> <p> <code>License Included</code> - The type of license included. Logical operators are <code>EQUALS</code> and <code>NOT_EQUALS</code>. Possible values are: <code>sql-server-enterprise</code> | <code>sql-server-standard</code> | <code>sql-server-web</code> | <code>windows-server-datacenter</code>.</p> </li> </ul> <p>The following filters and logical operators are supported when the resource type is <code>RDS</code>:</p> <ul> <li> <p> <code>Engine Edition</code> - The edition of the database engine. Logical operator is <code>EQUALS</code>. Possible values are: <code>oracle-ee</code> | <code>oracle-se</code> | <code>oracle-se1</code> | <code>oracle-se2</code> | <code>db2-se</code> | <code>db2-ae</code>.</p> </li> <li> <p> <code>License Pack</code> - The license pack. Logical operator is <code>EQUALS</code>. Possible values are: <code>data guard</code> | <code>diagnostic pack sqlt</code> | <code>tuning pack sqlt</code> | <code>ols</code> | <code>olap</code>.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductInformation) -> dict:
    out: dict = {}
    out["ResourceType"] = value["resource_type"]
    import capo_license_manager.types.product_information_filter_list

    out["ProductInformationFilterList"] = (
        capo_license_manager.types.product_information_filter_list.serialize_aws_json_1_1(
            value["product_information_filter_list"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProductInformation:
    out: ProductInformation = {}  # type: ignore[typeddict-item]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    else:
        out["resource_type"] = ""
    if data.get("ProductInformationFilterList") is not None:
        import capo_license_manager.types.product_information_filter_list

        out["product_information_filter_list"] = (
            capo_license_manager.types.product_information_filter_list.deserialize_aws_json_1_1(
                data["ProductInformationFilterList"]
            )
        )
    else:
        out["product_information_filter_list"] = []
    return out
