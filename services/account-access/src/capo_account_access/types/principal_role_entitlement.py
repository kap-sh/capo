"""Generated from Smithy shape ``com.amazonaws.accountaccess#PrincipalRoleEntitlement``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_account_access.errors import DeserializationError

if TYPE_CHECKING:
    import capo_account_access.types.principal
    import capo_account_access.types.role_arn


class PrincipalRoleEntitlement(TypedDict, closed=True):
    principal: "capo_account_access.types.principal.Principal"
    """<p>The principal (user or group) that is granted access to assume the IAM role.</p>"""
    role_arn: "capo_account_access.types.role_arn.RoleArn"
    """<p>The ARN of the IAM role that the principal can assume.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrincipalRoleEntitlement) -> dict:
    out: dict = {}
    import capo_account_access.types.principal

    out["principal"] = capo_account_access.types.principal.serialize_json(
        value["principal"]
    )
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> PrincipalRoleEntitlement:
    out: PrincipalRoleEntitlement = {}  # type: ignore[typeddict-item]
    if data.get("principal") is not None:
        import capo_account_access.types.principal

        out["principal"] = capo_account_access.types.principal.deserialize_json(
            data["principal"]
        )
    else:
        raise DeserializationError("PrincipalRoleEntitlement.principal required")
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("PrincipalRoleEntitlement.role_arn required")
    return out
