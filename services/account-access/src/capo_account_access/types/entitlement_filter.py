"""Generated from Smithy shape ``com.amazonaws.accountaccess#EntitlementFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_account_access.types.principal_role_entitlement_filter


class EntitlementFilter(TypedDict, closed=True):
    principal_role: NotRequired[
        "capo_account_access.types.principal_role_entitlement_filter.PrincipalRoleEntitlementFilter"
    ]
    """<p>The principal-to-role filter criteria for narrowing entitlement results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EntitlementFilter) -> dict:
    out: dict = {}
    if "principal_role" in value:
        import capo_account_access.types.principal_role_entitlement_filter

        out["principalRole"] = (
            capo_account_access.types.principal_role_entitlement_filter.serialize_json(
                value["principal_role"]
            )
        )
    return out


def deserialize_json(data: dict) -> EntitlementFilter:
    out: EntitlementFilter = {}  # type: ignore[typeddict-item]
    if data.get("principalRole") is not None:
        import capo_account_access.types.principal_role_entitlement_filter

        out["principal_role"] = (
            capo_account_access.types.principal_role_entitlement_filter.deserialize_json(
                data["principalRole"]
            )
        )
    return out
