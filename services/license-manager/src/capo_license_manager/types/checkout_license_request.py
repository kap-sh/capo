"""Generated from Smithy shape ``com.amazonaws.licensemanager#CheckoutLicenseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.checkout_type
    import capo_license_manager.types.client_token
    import capo_license_manager.types.entitlement_data_list
    import capo_license_manager.types.string


class CheckoutLicenseRequest(TypedDict, closed=True):
    product_sku: "capo_license_manager.types.string.String"
    """<p>Product SKU.</p>"""
    checkout_type: "capo_license_manager.types.checkout_type.CheckoutType"
    """<p>Checkout type.</p>"""
    key_fingerprint: "capo_license_manager.types.string.String"
    """<p>Key fingerprint identifying the license.</p>"""
    entitlements: "capo_license_manager.types.entitlement_data_list.EntitlementDataList"
    """<p>License entitlements.</p>"""
    client_token: "capo_license_manager.types.client_token.ClientToken"
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    beneficiary: NotRequired["capo_license_manager.types.string.String"]
    """<p>License beneficiary.</p>"""
    node_id: NotRequired["capo_license_manager.types.string.String"]
    """<p>Node ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CheckoutLicenseRequest) -> dict:
    out: dict = {}
    out["ProductSKU"] = value["product_sku"]
    import capo_license_manager.types.checkout_type

    out["CheckoutType"] = (
        capo_license_manager.types.checkout_type.serialize_aws_json_1_1(
            value["checkout_type"]
        )
    )
    out["KeyFingerprint"] = value["key_fingerprint"]
    import capo_license_manager.types.entitlement_data_list

    out["Entitlements"] = (
        capo_license_manager.types.entitlement_data_list.serialize_aws_json_1_1(
            value["entitlements"]
        )
    )
    out["ClientToken"] = value["client_token"]
    if "beneficiary" in value:
        out["Beneficiary"] = value["beneficiary"]
    if "node_id" in value:
        out["NodeId"] = value["node_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CheckoutLicenseRequest:
    out: CheckoutLicenseRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProductSKU") is not None:
        out["product_sku"] = data["ProductSKU"]
    else:
        out["product_sku"] = ""
    if data.get("CheckoutType") is not None:
        import capo_license_manager.types.checkout_type

        out["checkout_type"] = (
            capo_license_manager.types.checkout_type.deserialize_aws_json_1_1(
                data["CheckoutType"]
            )
        )
    else:
        import typing

        out["checkout_type"] = typing.cast(
            "capo_license_manager.types.checkout_type.CheckoutType", ""
        )
    if data.get("KeyFingerprint") is not None:
        out["key_fingerprint"] = data["KeyFingerprint"]
    else:
        out["key_fingerprint"] = ""
    if data.get("Entitlements") is not None:
        import capo_license_manager.types.entitlement_data_list

        out["entitlements"] = (
            capo_license_manager.types.entitlement_data_list.deserialize_aws_json_1_1(
                data["Entitlements"]
            )
        )
    else:
        out["entitlements"] = []
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        out["client_token"] = ""
    if data.get("Beneficiary") is not None:
        out["beneficiary"] = data["Beneficiary"]
    if data.get("NodeId") is not None:
        out["node_id"] = data["NodeId"]
    return out
