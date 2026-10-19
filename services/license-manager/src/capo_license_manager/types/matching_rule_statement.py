"""Generated from Smithy shape ``com.amazonaws.licensemanager#MatchingRuleStatement``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.string
    import capo_license_manager.types.string_list


class MatchingRuleStatement(TypedDict, closed=True):
    key_to_match: "capo_license_manager.types.string.String"
    """<p>Key to match.</p> <p>The following keys and are supported when the RuleStatement type is <code>Instance</code>: </p> <ul> <li> <p> <code>Platform</code> - The name of the platform. Logical operators are <code>EQUALS</code> and <code>NOT_EQUALS</code>. </p> </li> <li> <p> <code>EC2BillingProduct</code> - The billing product code. Logical operators are <code>EQUALS</code> and <code>NOT_EQUALS</code>. Possible values are: <code>windows-server-enterprise</code> | <code>windows-byol</code> | <code>rhel</code> | <code>rhel-byol</code> | <code>rhel-high-availability</code> | <code>ubuntu-pro</code> | <code>suse-linux</code> | <code>sql-server-standard</code> | <code>sql-server-enterprise</code>. </p> </li> <li> <p> <code>MarketPlaceProductCode</code> - The Marketplace product code. Logical operators are <code>EQUALS</code> and <code>NOT_EQUALS</code>. </p> </li> <li> <p> <code>AMIId</code> - The ID of the AMI. Logical operators are <code>EQUALS</code> and <code>NOT_EQUALS</code>. </p> </li> <li> <p> <code>InstanceType</code> - The instance type. Logical operators are <code>EQUALS</code> and <code>NOT_EQUALS</code>. </p> </li> <li> <p> <code>InstanceId</code> - The ID of the instance. Logical operators are <code>EQUALS</code> and <code>NOT_EQUALS</code>. </p> </li> <li> <p> <code>HostId</code> - The ID of the host. Logical operators are <code>EQUALS</code> and <code>NOT_EQUALS</code>. </p> </li> <li> <p> <code>AccountId</code> - The ID of the account. Logical operators are <code>EQUALS</code> and <code>NOT_EQUALS</code>. </p> </li> </ul> <p>The following keys and are supported when the RuleStatement type is <code>License</code>: </p> <ul> <li> <p> <code>LicenseArn</code> - The ARN of a Managed Entitlement License. Logical operators are <code>EQUALS</code> and <code>NOT_EQUALS</code>. </p> </li> <li> <p> <code>ProductSKU</code> - The productSKU of the license. Logical operators are <code>EQUALS</code> and <code>NOT_EQUALS</code>. </p> </li> <li> <p> <code>Issuer</code> - The issuer of the license. Logical operators are <code>EQUALS</code> and <code>NOT_EQUALS</code>. </p> </li> <li> <p> <code>Beneficiary</code> - The beneficiary of the license. Logical operators are <code>EQUALS</code> and <code>NOT_EQUALS</code>. </p> </li> <li> <p> <code>LicenseStatus</code> - The status of the license. Logical operators are <code>EQUALS</code> and <code>NOT_EQUALS</code>. </p> </li> <li> <p> <code>HomeRegion</code> - The home region of the license. Logical operators are <code>EQUALS</code> and <code>NOT_EQUALS</code>. </p> </li> </ul> <p>The following keys and are supported when the RuleStatement type is <code>License Configuration</code>: </p> <ul> <li> <p> <code>LicenseConfigurationArn</code> - The ARN of a self-managed license configuration. Logical operators are <code>EQUALS</code> and <code>NOT_EQUALS</code>. </p> </li> <li> <p> <code>AccountId</code> - The account of the license configuration. Logical operators are <code>EQUALS</code> and <code>NOT_EQUALS</code>. </p> </li> </ul>"""
    constraint: "capo_license_manager.types.string.String"
    """<p>Constraint.</p>"""
    value_to_match: "capo_license_manager.types.string_list.StringList"
    """<p>Value to match.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MatchingRuleStatement) -> dict:
    out: dict = {}
    out["KeyToMatch"] = value["key_to_match"]
    out["Constraint"] = value["constraint"]
    import capo_license_manager.types.string_list

    out["ValueToMatch"] = capo_license_manager.types.string_list.serialize_aws_json_1_1(
        value["value_to_match"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> MatchingRuleStatement:
    out: MatchingRuleStatement = {}  # type: ignore[typeddict-item]
    if data.get("KeyToMatch") is not None:
        out["key_to_match"] = data["KeyToMatch"]
    else:
        out["key_to_match"] = ""
    if data.get("Constraint") is not None:
        out["constraint"] = data["Constraint"]
    else:
        out["constraint"] = ""
    if data.get("ValueToMatch") is not None:
        import capo_license_manager.types.string_list

        out["value_to_match"] = (
            capo_license_manager.types.string_list.deserialize_aws_json_1_1(
                data["ValueToMatch"]
            )
        )
    else:
        out["value_to_match"] = []
    return out
