"""Generated from Smithy shape ``com.amazonaws.fms#GetAdminAccountResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.account_role_status
    import capo_fms.types.aws_account_id


class GetAdminAccountResponse(TypedDict, closed=True):
    admin_account: NotRequired["capo_fms.types.aws_account_id.AWSAccountId"]
    """<p>The account that is set as the Firewall Manager default administrator.</p>"""
    role_status: NotRequired["capo_fms.types.account_role_status.AccountRoleStatus"]
    """<p>The status of the account that you set as the Firewall Manager default administrator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAdminAccountResponse) -> dict:
    out: dict = {}
    if "admin_account" in value:
        out["AdminAccount"] = value["admin_account"]
    if "role_status" in value:
        import capo_fms.types.account_role_status

        out["RoleStatus"] = capo_fms.types.account_role_status.serialize_aws_json_1_1(
            value["role_status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAdminAccountResponse:
    out: GetAdminAccountResponse = {}  # type: ignore[typeddict-item]
    if data.get("AdminAccount") is not None:
        out["admin_account"] = data["AdminAccount"]
    if data.get("RoleStatus") is not None:
        import capo_fms.types.account_role_status

        out["role_status"] = (
            capo_fms.types.account_role_status.deserialize_aws_json_1_1(
                data["RoleStatus"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetAdminAccountResponse) -> dict:
    out: dict = {}
    if "admin_account" in value:
        out["AdminAccount"] = value["admin_account"]
    if "role_status" in value:
        import capo_fms.types.account_role_status

        out["RoleStatus"] = capo_fms.types.account_role_status.serialize_cbor(
            value["role_status"]
        )
    return out


def deserialize_cbor(data: dict) -> GetAdminAccountResponse:
    out: GetAdminAccountResponse = {}  # type: ignore[typeddict-item]
    if data.get("AdminAccount") is not None:
        out["admin_account"] = data["AdminAccount"]
    if data.get("RoleStatus") is not None:
        import capo_fms.types.account_role_status

        out["role_status"] = capo_fms.types.account_role_status.deserialize_cbor(
            data["RoleStatus"]
        )
    return out
