"""Generated from Smithy shape ``com.amazonaws.fms#GetAdminScopeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.admin_scope
    import capo_fms.types.organization_status


class GetAdminScopeResponse(TypedDict, closed=True):
    admin_scope: NotRequired["capo_fms.types.admin_scope.AdminScope"]
    """<p>Contains details about the administrative scope of the requested account.</p>"""
    status: NotRequired["capo_fms.types.organization_status.OrganizationStatus"]
    """<p>The current status of the request to onboard a member account as an Firewall Manager administrator.</p> <ul> <li> <p> <code>ONBOARDING</code> - The account is onboarding to Firewall Manager as an administrator.</p> </li> <li> <p> <code>ONBOARDING_COMPLETE</code> - Firewall Manager The account is onboarded to Firewall Manager as an administrator, and can perform actions on the resources defined in their <a>AdminScope</a>.</p> </li> <li> <p> <code>OFFBOARDING</code> - The account is being removed as an Firewall Manager administrator.</p> </li> <li> <p> <code>OFFBOARDING_COMPLETE</code> - The account has been removed as an Firewall Manager administrator.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAdminScopeResponse) -> dict:
    out: dict = {}
    if "admin_scope" in value:
        import capo_fms.types.admin_scope

        out["AdminScope"] = capo_fms.types.admin_scope.serialize_aws_json_1_1(
            value["admin_scope"]
        )
    if "status" in value:
        import capo_fms.types.organization_status

        out["Status"] = capo_fms.types.organization_status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAdminScopeResponse:
    out: GetAdminScopeResponse = {}  # type: ignore[typeddict-item]
    if data.get("AdminScope") is not None:
        import capo_fms.types.admin_scope

        out["admin_scope"] = capo_fms.types.admin_scope.deserialize_aws_json_1_1(
            data["AdminScope"]
        )
    if data.get("Status") is not None:
        import capo_fms.types.organization_status

        out["status"] = capo_fms.types.organization_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetAdminScopeResponse) -> dict:
    out: dict = {}
    if "admin_scope" in value:
        import capo_fms.types.admin_scope

        out["AdminScope"] = capo_fms.types.admin_scope.serialize_cbor(
            value["admin_scope"]
        )
    if "status" in value:
        import capo_fms.types.organization_status

        out["Status"] = capo_fms.types.organization_status.serialize_cbor(
            value["status"]
        )
    return out


def deserialize_cbor(data: dict) -> GetAdminScopeResponse:
    out: GetAdminScopeResponse = {}  # type: ignore[typeddict-item]
    if data.get("AdminScope") is not None:
        import capo_fms.types.admin_scope

        out["admin_scope"] = capo_fms.types.admin_scope.deserialize_cbor(
            data["AdminScope"]
        )
    if data.get("Status") is not None:
        import capo_fms.types.organization_status

        out["status"] = capo_fms.types.organization_status.deserialize_cbor(
            data["Status"]
        )
    return out
