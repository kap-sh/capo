"""Generated from Smithy shape ``com.amazonaws.fms#AdminScope``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.account_scope
    import capo_fms.types.organizational_unit_scope
    import capo_fms.types.policy_type_scope
    import capo_fms.types.region_scope


class AdminScope(TypedDict, closed=True):
    account_scope: NotRequired["capo_fms.types.account_scope.AccountScope"]
    """<p>Defines the accounts that the specified Firewall Manager administrator can apply policies to.</p>"""
    organizational_unit_scope: NotRequired[
        "capo_fms.types.organizational_unit_scope.OrganizationalUnitScope"
    ]
    """<p>Defines the Organizations organizational units that the specified Firewall Manager administrator can apply policies to. For more information about OUs in Organizations, see <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous.html">Managing organizational units (OUs) </a> in the <i>Organizations User Guide</i>.</p>"""
    region_scope: NotRequired["capo_fms.types.region_scope.RegionScope"]
    """<p>Defines the Amazon Web Services Regions that the specified Firewall Manager administrator can perform actions in.</p>"""
    policy_type_scope: NotRequired["capo_fms.types.policy_type_scope.PolicyTypeScope"]
    """<p>Defines the Firewall Manager policy types that the specified Firewall Manager administrator can create and manage.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminScope) -> dict:
    out: dict = {}
    if "account_scope" in value:
        import capo_fms.types.account_scope

        out["AccountScope"] = capo_fms.types.account_scope.serialize_aws_json_1_1(
            value["account_scope"]
        )
    if "organizational_unit_scope" in value:
        import capo_fms.types.organizational_unit_scope

        out["OrganizationalUnitScope"] = (
            capo_fms.types.organizational_unit_scope.serialize_aws_json_1_1(
                value["organizational_unit_scope"]
            )
        )
    if "region_scope" in value:
        import capo_fms.types.region_scope

        out["RegionScope"] = capo_fms.types.region_scope.serialize_aws_json_1_1(
            value["region_scope"]
        )
    if "policy_type_scope" in value:
        import capo_fms.types.policy_type_scope

        out["PolicyTypeScope"] = (
            capo_fms.types.policy_type_scope.serialize_aws_json_1_1(
                value["policy_type_scope"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AdminScope:
    out: AdminScope = {}  # type: ignore[typeddict-item]
    if data.get("AccountScope") is not None:
        import capo_fms.types.account_scope

        out["account_scope"] = capo_fms.types.account_scope.deserialize_aws_json_1_1(
            data["AccountScope"]
        )
    if data.get("OrganizationalUnitScope") is not None:
        import capo_fms.types.organizational_unit_scope

        out["organizational_unit_scope"] = (
            capo_fms.types.organizational_unit_scope.deserialize_aws_json_1_1(
                data["OrganizationalUnitScope"]
            )
        )
    if data.get("RegionScope") is not None:
        import capo_fms.types.region_scope

        out["region_scope"] = capo_fms.types.region_scope.deserialize_aws_json_1_1(
            data["RegionScope"]
        )
    if data.get("PolicyTypeScope") is not None:
        import capo_fms.types.policy_type_scope

        out["policy_type_scope"] = (
            capo_fms.types.policy_type_scope.deserialize_aws_json_1_1(
                data["PolicyTypeScope"]
            )
        )
    return out
