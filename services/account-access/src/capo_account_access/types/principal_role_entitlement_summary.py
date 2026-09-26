"""Generated from Smithy shape ``com.amazonaws.accountaccess#PrincipalRoleEntitlementSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_account_access.errors import DeserializationError

if TYPE_CHECKING:
    import capo_account_access.types.account
    import capo_account_access.types.principal
    import capo_account_access.types.role_arn


class PrincipalRoleEntitlementSummary(TypedDict, closed=True):
    principal: "capo_account_access.types.principal.Principal"
    """<p>The principal (user or group) that is granted access to assume the IAM role.</p>"""
    role_arn: "capo_account_access.types.role_arn.RoleArn"
    """<p>The ARN of the IAM role that the principal can assume.</p>"""
    account: "capo_account_access.types.account.Account"
    """<p>The 12-digit Amazon Web Services account ID where the IAM role resides.</p>"""
    account_name: NotRequired["str"]
    """<p>The friendly name of the Amazon Web Services account where the IAM role resides.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrincipalRoleEntitlementSummary) -> dict:
    out: dict = {}
    import capo_account_access.types.principal

    out["principal"] = capo_account_access.types.principal.serialize_json(
        value["principal"]
    )
    out["roleArn"] = value["role_arn"]
    out["account"] = value["account"]
    if "account_name" in value:
        out["accountName"] = value["account_name"]
    return out


def deserialize_json(data: dict) -> PrincipalRoleEntitlementSummary:
    out: PrincipalRoleEntitlementSummary = {}  # type: ignore[typeddict-item]
    if data.get("principal") is not None:
        import capo_account_access.types.principal

        out["principal"] = capo_account_access.types.principal.deserialize_json(
            data["principal"]
        )
    else:
        raise DeserializationError("PrincipalRoleEntitlementSummary.principal required")
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("PrincipalRoleEntitlementSummary.role_arn required")
    if data.get("account") is not None:
        out["account"] = data["account"]
    else:
        raise DeserializationError("PrincipalRoleEntitlementSummary.account required")
    if data.get("accountName") is not None:
        out["account_name"] = data["accountName"]
    return out
