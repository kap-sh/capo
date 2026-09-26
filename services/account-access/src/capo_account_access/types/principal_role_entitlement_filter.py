"""Generated from Smithy shape ``com.amazonaws.accountaccess#PrincipalRoleEntitlementFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_account_access.types.account
    import capo_account_access.types.principal_filter
    import capo_account_access.types.role_arn


class PrincipalRoleEntitlementFilter(TypedDict, closed=True):
    principal: NotRequired["capo_account_access.types.principal_filter.PrincipalFilter"]
    """<p>The principal to filter entitlements by.</p>"""
    role_arn: NotRequired["capo_account_access.types.role_arn.RoleArn"]
    """<p>The IAM role ARN to filter entitlements by.</p>"""
    account: NotRequired["capo_account_access.types.account.Account"]
    """<p>The 12-digit Amazon Web Services account ID to filter entitlements by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrincipalRoleEntitlementFilter) -> dict:
    out: dict = {}
    if "principal" in value:
        import capo_account_access.types.principal_filter

        out["principal"] = capo_account_access.types.principal_filter.serialize_json(
            value["principal"]
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "account" in value:
        out["account"] = value["account"]
    return out


def deserialize_json(data: dict) -> PrincipalRoleEntitlementFilter:
    out: PrincipalRoleEntitlementFilter = {}  # type: ignore[typeddict-item]
    if data.get("principal") is not None:
        import capo_account_access.types.principal_filter

        out["principal"] = capo_account_access.types.principal_filter.deserialize_json(
            data["principal"]
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("account") is not None:
        out["account"] = data["account"]
    return out
