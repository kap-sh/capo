"""Generated from Smithy shape ``com.amazonaws.licensemanager#CheckoutBorrowLicenseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_license_manager.types.arn
    import capo_license_manager.types.client_token
    import capo_license_manager.types.digital_signature_method
    import capo_license_manager.types.entitlement_data_list
    import capo_license_manager.types.metadata_list
    import capo_license_manager.types.string


class CheckoutBorrowLicenseRequest(TypedDict, closed=True):
    license_arn: "capo_license_manager.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the license. The license must use the borrow consumption configuration.</p>"""
    entitlements: "capo_license_manager.types.entitlement_data_list.EntitlementDataList"
    """<p>License entitlements. Partial checkouts are not supported.</p>"""
    digital_signature_method: (
        "capo_license_manager.types.digital_signature_method.DigitalSignatureMethod"
    )
    """<p>Digital signature method. The possible value is JSON Web Signature (JWS) algorithm PS384. For more information, see <a href="https://tools.ietf.org/html/rfc7518#section-3.5">RFC 7518 Digital Signature with RSASSA-PSS</a>.</p>"""
    node_id: NotRequired["capo_license_manager.types.string.String"]
    """<p>Node ID.</p>"""
    checkout_metadata: NotRequired[
        "capo_license_manager.types.metadata_list.MetadataList"
    ]
    """<p>Information about constraints.</p>"""
    client_token: "capo_license_manager.types.client_token.ClientToken"
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CheckoutBorrowLicenseRequest) -> dict:
    out: dict = {}
    out["LicenseArn"] = value["license_arn"]
    import capo_license_manager.types.entitlement_data_list

    out["Entitlements"] = (
        capo_license_manager.types.entitlement_data_list.serialize_aws_json_1_1(
            value["entitlements"]
        )
    )
    import capo_license_manager.types.digital_signature_method

    out["DigitalSignatureMethod"] = (
        capo_license_manager.types.digital_signature_method.serialize_aws_json_1_1(
            value["digital_signature_method"]
        )
    )
    if "node_id" in value:
        out["NodeId"] = value["node_id"]
    if "checkout_metadata" in value:
        import capo_license_manager.types.metadata_list

        out["CheckoutMetadata"] = (
            capo_license_manager.types.metadata_list.serialize_aws_json_1_1(
                value["checkout_metadata"]
            )
        )
    out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CheckoutBorrowLicenseRequest:
    out: CheckoutBorrowLicenseRequest = {}  # type: ignore[typeddict-item]
    if data.get("LicenseArn") is not None:
        out["license_arn"] = data["LicenseArn"]
    else:
        raise DeserializationError("CheckoutBorrowLicenseRequest.license_arn required")
    if data.get("Entitlements") is not None:
        import capo_license_manager.types.entitlement_data_list

        out["entitlements"] = (
            capo_license_manager.types.entitlement_data_list.deserialize_aws_json_1_1(
                data["Entitlements"]
            )
        )
    else:
        raise DeserializationError("CheckoutBorrowLicenseRequest.entitlements required")
    if data.get("DigitalSignatureMethod") is not None:
        import capo_license_manager.types.digital_signature_method

        out["digital_signature_method"] = (
            capo_license_manager.types.digital_signature_method.deserialize_aws_json_1_1(
                data["DigitalSignatureMethod"]
            )
        )
    else:
        raise DeserializationError(
            "CheckoutBorrowLicenseRequest.digital_signature_method required"
        )
    if data.get("NodeId") is not None:
        out["node_id"] = data["NodeId"]
    if data.get("CheckoutMetadata") is not None:
        import capo_license_manager.types.metadata_list

        out["checkout_metadata"] = (
            capo_license_manager.types.metadata_list.deserialize_aws_json_1_1(
                data["CheckoutMetadata"]
            )
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError("CheckoutBorrowLicenseRequest.client_token required")
    return out
