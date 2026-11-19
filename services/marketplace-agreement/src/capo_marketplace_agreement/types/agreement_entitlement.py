"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementEntitlement``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_entitlement_status
    import capo_marketplace_agreement.types.agreement_entitlement_status_reason_code
    import capo_marketplace_agreement.types.aws_arn
    import capo_marketplace_agreement.types.entitlement_type
    import capo_marketplace_agreement.types.registration_token
    import capo_marketplace_agreement.types.resource


class AgreementEntitlement(TypedDict, closed=True):
    resource: NotRequired["capo_marketplace_agreement.types.resource.Resource"]
    """<p>The resource that the entitlement is provisioned to, such as a product.</p>"""
    type: NotRequired[
        "capo_marketplace_agreement.types.entitlement_type.EntitlementType"
    ]
    """<p>The type of entitlement.</p>"""
    registration_token: NotRequired[
        "capo_marketplace_agreement.types.registration_token.RegistrationToken"
    ]
    """<p>A short-lived token required by acceptors to register their account with the product provider. The token is only valid for 30 minutes after creation and is only applicable for purchase agreements.</p>"""
    status: NotRequired[
        "capo_marketplace_agreement.types.agreement_entitlement_status.AgreementEntitlementStatus"
    ]
    """<p>The current state of an entitlement.</p>"""
    status_reason_code: NotRequired[
        "capo_marketplace_agreement.types.agreement_entitlement_status_reason_code.AgreementEntitlementStatusReasonCode"
    ]
    """<p>Provides more information about the status of an entitlement.</p>"""
    license_arn: NotRequired["capo_marketplace_agreement.types.aws_arn.AwsArn"]
    """<p>The Amazon Resource Name (ARN) of the AWS License Manager license associated with the entitlement.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementEntitlement) -> dict:
    out: dict = {}
    if "resource" in value:
        import capo_marketplace_agreement.types.resource

        out["resource"] = (
            capo_marketplace_agreement.types.resource.serialize_aws_json_1_0(
                value["resource"]
            )
        )
    if "type" in value:
        out["type"] = value["type"]
    if "registration_token" in value:
        out["registrationToken"] = value["registration_token"]
    if "status" in value:
        import capo_marketplace_agreement.types.agreement_entitlement_status

        out["status"] = (
            capo_marketplace_agreement.types.agreement_entitlement_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "status_reason_code" in value:
        import capo_marketplace_agreement.types.agreement_entitlement_status_reason_code

        out["statusReasonCode"] = (
            capo_marketplace_agreement.types.agreement_entitlement_status_reason_code.serialize_aws_json_1_0(
                value["status_reason_code"]
            )
        )
    if "license_arn" in value:
        out["licenseArn"] = value["license_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AgreementEntitlement:
    out: AgreementEntitlement = {}  # type: ignore[typeddict-item]
    if data.get("resource") is not None:
        import capo_marketplace_agreement.types.resource

        out["resource"] = (
            capo_marketplace_agreement.types.resource.deserialize_aws_json_1_0(
                data["resource"]
            )
        )
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("registrationToken") is not None:
        out["registration_token"] = data["registrationToken"]
    if data.get("status") is not None:
        import capo_marketplace_agreement.types.agreement_entitlement_status

        out["status"] = (
            capo_marketplace_agreement.types.agreement_entitlement_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if data.get("statusReasonCode") is not None:
        import capo_marketplace_agreement.types.agreement_entitlement_status_reason_code

        out["status_reason_code"] = (
            capo_marketplace_agreement.types.agreement_entitlement_status_reason_code.deserialize_aws_json_1_0(
                data["statusReasonCode"]
            )
        )
    if data.get("licenseArn") is not None:
        out["license_arn"] = data["licenseArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AgreementEntitlement) -> dict:
    out: dict = {}
    if "resource" in value:
        import capo_marketplace_agreement.types.resource

        out["resource"] = capo_marketplace_agreement.types.resource.serialize_cbor(
            value["resource"]
        )
    if "type" in value:
        out["type"] = value["type"]
    if "registration_token" in value:
        out["registrationToken"] = value["registration_token"]
    if "status" in value:
        import capo_marketplace_agreement.types.agreement_entitlement_status

        out["status"] = (
            capo_marketplace_agreement.types.agreement_entitlement_status.serialize_cbor(
                value["status"]
            )
        )
    if "status_reason_code" in value:
        import capo_marketplace_agreement.types.agreement_entitlement_status_reason_code

        out["statusReasonCode"] = (
            capo_marketplace_agreement.types.agreement_entitlement_status_reason_code.serialize_cbor(
                value["status_reason_code"]
            )
        )
    if "license_arn" in value:
        out["licenseArn"] = value["license_arn"]
    return out


def deserialize_cbor(data: dict) -> AgreementEntitlement:
    out: AgreementEntitlement = {}  # type: ignore[typeddict-item]
    if data.get("resource") is not None:
        import capo_marketplace_agreement.types.resource

        out["resource"] = capo_marketplace_agreement.types.resource.deserialize_cbor(
            data["resource"]
        )
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("registrationToken") is not None:
        out["registration_token"] = data["registrationToken"]
    if data.get("status") is not None:
        import capo_marketplace_agreement.types.agreement_entitlement_status

        out["status"] = (
            capo_marketplace_agreement.types.agreement_entitlement_status.deserialize_cbor(
                data["status"]
            )
        )
    if data.get("statusReasonCode") is not None:
        import capo_marketplace_agreement.types.agreement_entitlement_status_reason_code

        out["status_reason_code"] = (
            capo_marketplace_agreement.types.agreement_entitlement_status_reason_code.deserialize_cbor(
                data["statusReasonCode"]
            )
        )
    if data.get("licenseArn") is not None:
        out["license_arn"] = data["licenseArn"]
    return out


def redact_sensitive(value: AgreementEntitlement) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "registration_token" in value:
        out["registration_token"] = "*** Sensitive Data Redacted ***"
    return out
