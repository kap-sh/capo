"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ApproverOutcome``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_marketplace_agreement.errors import DeserializationError, SerializationError
from capo_marketplace_agreement.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.aws_organization_approver_outcome
    import capo_marketplace_agreement.types.email_approver_outcome
    import capo_marketplace_agreement.types.procurement_tool_approver_outcome


class ApproverOutcomeEmailApproverOutcomeMember(TypedDict, closed=True):
    emailApproverOutcome: (
        "capo_marketplace_agreement.types.email_approver_outcome.EmailApproverOutcome"
    )


class ApproverOutcomeProcurementToolApproverOutcomeMember(TypedDict, closed=True):
    procurementToolApproverOutcome: "capo_marketplace_agreement.types.procurement_tool_approver_outcome.ProcurementToolApproverOutcome"


class ApproverOutcomeAwsOrganizationApproverOutcomeMember(TypedDict, closed=True):
    awsOrganizationApproverOutcome: "capo_marketplace_agreement.types.aws_organization_approver_outcome.AwsOrganizationApproverOutcome"


ApproverOutcome: TypeAlias = (
    ApproverOutcomeEmailApproverOutcomeMember
    | ApproverOutcomeProcurementToolApproverOutcomeMember
    | ApproverOutcomeAwsOrganizationApproverOutcomeMember
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ApproverOutcome) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ApproverOutcome: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "emailApproverOutcome" in value:
        import capo_marketplace_agreement.types.email_approver_outcome

        return {
            "emailApproverOutcome": capo_marketplace_agreement.types.email_approver_outcome.serialize_aws_json_1_0(
                value["emailApproverOutcome"]
            )
        }
    elif "procurementToolApproverOutcome" in value:
        import capo_marketplace_agreement.types.procurement_tool_approver_outcome

        return {
            "procurementToolApproverOutcome": capo_marketplace_agreement.types.procurement_tool_approver_outcome.serialize_aws_json_1_0(
                value["procurementToolApproverOutcome"]
            )
        }
    elif "awsOrganizationApproverOutcome" in value:
        import capo_marketplace_agreement.types.aws_organization_approver_outcome

        return {
            "awsOrganizationApproverOutcome": capo_marketplace_agreement.types.aws_organization_approver_outcome.serialize_aws_json_1_0(
                value["awsOrganizationApproverOutcome"]
            )
        }
    else:
        raise SerializationError("ApproverOutcome: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ApproverOutcome:
    if data.get("emailApproverOutcome") is not None:
        import capo_marketplace_agreement.types.email_approver_outcome

        return {
            "emailApproverOutcome": capo_marketplace_agreement.types.email_approver_outcome.deserialize_aws_json_1_0(
                data["emailApproverOutcome"]
            )
        }
    elif data.get("procurementToolApproverOutcome") is not None:
        import capo_marketplace_agreement.types.procurement_tool_approver_outcome

        return {
            "procurementToolApproverOutcome": capo_marketplace_agreement.types.procurement_tool_approver_outcome.deserialize_aws_json_1_0(
                data["procurementToolApproverOutcome"]
            )
        }
    elif data.get("awsOrganizationApproverOutcome") is not None:
        import capo_marketplace_agreement.types.aws_organization_approver_outcome

        return {
            "awsOrganizationApproverOutcome": capo_marketplace_agreement.types.aws_organization_approver_outcome.deserialize_aws_json_1_0(
                data["awsOrganizationApproverOutcome"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ApproverOutcome: no recognized variant key")


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ApproverOutcome) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ApproverOutcome: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "emailApproverOutcome" in value:
        import capo_marketplace_agreement.types.email_approver_outcome

        return {
            "emailApproverOutcome": capo_marketplace_agreement.types.email_approver_outcome.serialize_cbor(
                value["emailApproverOutcome"]
            )
        }
    elif "procurementToolApproverOutcome" in value:
        import capo_marketplace_agreement.types.procurement_tool_approver_outcome

        return {
            "procurementToolApproverOutcome": capo_marketplace_agreement.types.procurement_tool_approver_outcome.serialize_cbor(
                value["procurementToolApproverOutcome"]
            )
        }
    elif "awsOrganizationApproverOutcome" in value:
        import capo_marketplace_agreement.types.aws_organization_approver_outcome

        return {
            "awsOrganizationApproverOutcome": capo_marketplace_agreement.types.aws_organization_approver_outcome.serialize_cbor(
                value["awsOrganizationApproverOutcome"]
            )
        }
    else:
        raise SerializationError("ApproverOutcome: no variant present")


def deserialize_cbor(data: dict) -> ApproverOutcome:
    if data.get("emailApproverOutcome") is not None:
        import capo_marketplace_agreement.types.email_approver_outcome

        return {
            "emailApproverOutcome": capo_marketplace_agreement.types.email_approver_outcome.deserialize_cbor(
                data["emailApproverOutcome"]
            )
        }
    elif data.get("procurementToolApproverOutcome") is not None:
        import capo_marketplace_agreement.types.procurement_tool_approver_outcome

        return {
            "procurementToolApproverOutcome": capo_marketplace_agreement.types.procurement_tool_approver_outcome.deserialize_cbor(
                data["procurementToolApproverOutcome"]
            )
        }
    elif data.get("awsOrganizationApproverOutcome") is not None:
        import capo_marketplace_agreement.types.aws_organization_approver_outcome

        return {
            "awsOrganizationApproverOutcome": capo_marketplace_agreement.types.aws_organization_approver_outcome.deserialize_cbor(
                data["awsOrganizationApproverOutcome"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ApproverOutcome: no recognized variant key")


def redact_sensitive(value: ApproverOutcome) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "emailApproverOutcome" in value:
        import capo_marketplace_agreement.types.email_approver_outcome

        out["emailApproverOutcome"] = (
            capo_marketplace_agreement.types.email_approver_outcome.redact_sensitive(
                value["emailApproverOutcome"]
            )
        )
    if "procurementToolApproverOutcome" in value:
        import capo_marketplace_agreement.types.procurement_tool_approver_outcome

        out["procurementToolApproverOutcome"] = (
            capo_marketplace_agreement.types.procurement_tool_approver_outcome.redact_sensitive(
                value["procurementToolApproverOutcome"]
            )
        )
    if "awsOrganizationApproverOutcome" in value:
        import capo_marketplace_agreement.types.aws_organization_approver_outcome

        out["awsOrganizationApproverOutcome"] = (
            capo_marketplace_agreement.types.aws_organization_approver_outcome.redact_sensitive(
                value["awsOrganizationApproverOutcome"]
            )
        )
    return out
