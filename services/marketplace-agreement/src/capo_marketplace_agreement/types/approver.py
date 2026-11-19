"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#Approver``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_marketplace_agreement.errors import DeserializationError, SerializationError
from capo_marketplace_agreement.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.aws_organization_admin_approver
    import capo_marketplace_agreement.types.email_approver
    import capo_marketplace_agreement.types.procurement_tool_approver


class ApproverEmailApproverMember(TypedDict, closed=True):
    emailApprover: "capo_marketplace_agreement.types.email_approver.EmailApprover"


class ApproverProcurementToolApproverMember(TypedDict, closed=True):
    procurementToolApprover: "capo_marketplace_agreement.types.procurement_tool_approver.ProcurementToolApprover"


class ApproverAwsOrganizationAdminApproverMember(TypedDict, closed=True):
    awsOrganizationAdminApprover: "capo_marketplace_agreement.types.aws_organization_admin_approver.AwsOrganizationAdminApprover"


Approver: TypeAlias = (
    ApproverEmailApproverMember
    | ApproverProcurementToolApproverMember
    | ApproverAwsOrganizationAdminApproverMember
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Approver) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Approver: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "emailApprover" in value:
        import capo_marketplace_agreement.types.email_approver

        return {
            "emailApprover": capo_marketplace_agreement.types.email_approver.serialize_aws_json_1_0(
                value["emailApprover"]
            )
        }
    elif "procurementToolApprover" in value:
        import capo_marketplace_agreement.types.procurement_tool_approver

        return {
            "procurementToolApprover": capo_marketplace_agreement.types.procurement_tool_approver.serialize_aws_json_1_0(
                value["procurementToolApprover"]
            )
        }
    elif "awsOrganizationAdminApprover" in value:
        import capo_marketplace_agreement.types.aws_organization_admin_approver

        return {
            "awsOrganizationAdminApprover": capo_marketplace_agreement.types.aws_organization_admin_approver.serialize_aws_json_1_0(
                value["awsOrganizationAdminApprover"]
            )
        }
    else:
        raise SerializationError("Approver: no variant present")


def deserialize_aws_json_1_0(data: dict) -> Approver:
    if data.get("emailApprover") is not None:
        import capo_marketplace_agreement.types.email_approver

        return {
            "emailApprover": capo_marketplace_agreement.types.email_approver.deserialize_aws_json_1_0(
                data["emailApprover"]
            )
        }
    elif data.get("procurementToolApprover") is not None:
        import capo_marketplace_agreement.types.procurement_tool_approver

        return {
            "procurementToolApprover": capo_marketplace_agreement.types.procurement_tool_approver.deserialize_aws_json_1_0(
                data["procurementToolApprover"]
            )
        }
    elif data.get("awsOrganizationAdminApprover") is not None:
        import capo_marketplace_agreement.types.aws_organization_admin_approver

        return {
            "awsOrganizationAdminApprover": capo_marketplace_agreement.types.aws_organization_admin_approver.deserialize_aws_json_1_0(
                data["awsOrganizationAdminApprover"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Approver: no recognized variant key")


def redact_sensitive(value: Approver) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "emailApprover" in value:
        import capo_marketplace_agreement.types.email_approver

        out["emailApprover"] = (
            capo_marketplace_agreement.types.email_approver.redact_sensitive(
                value["emailApprover"]
            )
        )
    if "procurementToolApprover" in value:
        import capo_marketplace_agreement.types.procurement_tool_approver

        out["procurementToolApprover"] = (
            capo_marketplace_agreement.types.procurement_tool_approver.redact_sensitive(
                value["procurementToolApprover"]
            )
        )
    return out
