"""Generated from Smithy shape ``com.amazonaws.marketplaceentitlementservice#Entitlement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_entitlement_service.types.entitlement_value
    import capo_marketplace_entitlement_service.types.non_empty_string
    import capo_marketplace_entitlement_service.types.product_code
    import capo_marketplace_entitlement_service.types.string
    import capo_marketplace_entitlement_service.types.timestamp


class Entitlement(TypedDict, closed=True):
    product_code: NotRequired[
        "capo_marketplace_entitlement_service.types.product_code.ProductCode"
    ]
    """<p>The product code for which the given entitlement applies. Product codes are provided by AWS Marketplace when the product listing is created.</p>"""
    dimension: NotRequired[
        "capo_marketplace_entitlement_service.types.non_empty_string.NonEmptyString"
    ]
    """<p>The dimension for which the given entitlement applies. Dimensions represent categories of capacity in a product and are specified when the product is listed in AWS Marketplace.</p>"""
    customer_identifier: NotRequired[
        "capo_marketplace_entitlement_service.types.non_empty_string.NonEmptyString"
    ]
    """<p>The customer identifier is a handle to each unique customer in an application. Customer identifiers are obtained through the ResolveCustomer operation in AWS Marketplace Metering Service.</p>"""
    customer_aws_account_id: NotRequired[
        "capo_marketplace_entitlement_service.types.non_empty_string.NonEmptyString"
    ]
    """<p> The <code>CustomerAWSAccountId</code> parameter specifies the AWS account ID of the buyer. </p>"""
    value: NotRequired[
        "capo_marketplace_entitlement_service.types.entitlement_value.EntitlementValue"
    ]
    """<p>The EntitlementValue represents the amount of capacity that the customer is entitled to for the product.</p>"""
    expiration_date: NotRequired[
        "capo_marketplace_entitlement_service.types.timestamp.Timestamp"
    ]
    """<p>The expiration date represents the minimum date through which this entitlement is expected to remain valid. For contractual products listed on AWS Marketplace, the expiration date is the date at which the customer will renew or cancel their contract. Customers who are opting to renew their contract will still have entitlements with an expiration date.</p>"""
    license_arn: NotRequired["capo_marketplace_entitlement_service.types.string.String"]
    """<p>The <code>LicenseArn</code> is a unique identifier for a specific granted license. These are used for software purchased through AWS Marketplace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Entitlement) -> dict:
    out: dict = {}
    if "product_code" in value:
        out["ProductCode"] = value["product_code"]
    if "dimension" in value:
        out["Dimension"] = value["dimension"]
    if "customer_identifier" in value:
        out["CustomerIdentifier"] = value["customer_identifier"]
    if "customer_aws_account_id" in value:
        out["CustomerAWSAccountId"] = value["customer_aws_account_id"]
    if "value" in value:
        import capo_marketplace_entitlement_service.types.entitlement_value

        out["Value"] = (
            capo_marketplace_entitlement_service.types.entitlement_value.serialize_aws_json_1_1(
                value["value"]
            )
        )
    if "expiration_date" in value:
        import capo_marketplace_entitlement_service.types.timestamp

        out["ExpirationDate"] = (
            capo_marketplace_entitlement_service.types.timestamp.serialize_aws_json_1_1(
                value["expiration_date"]
            )
        )
    if "license_arn" in value:
        out["LicenseArn"] = value["license_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Entitlement:
    out: Entitlement = {}  # type: ignore[typeddict-item]
    if data.get("ProductCode") is not None:
        out["product_code"] = data["ProductCode"]
    if data.get("Dimension") is not None:
        out["dimension"] = data["Dimension"]
    if data.get("CustomerIdentifier") is not None:
        out["customer_identifier"] = data["CustomerIdentifier"]
    if data.get("CustomerAWSAccountId") is not None:
        out["customer_aws_account_id"] = data["CustomerAWSAccountId"]
    if data.get("Value") is not None:
        import capo_marketplace_entitlement_service.types.entitlement_value

        out["value"] = (
            capo_marketplace_entitlement_service.types.entitlement_value.deserialize_aws_json_1_1(
                data["Value"]
            )
        )
    if data.get("ExpirationDate") is not None:
        import capo_marketplace_entitlement_service.types.timestamp

        out["expiration_date"] = (
            capo_marketplace_entitlement_service.types.timestamp.deserialize_aws_json_1_1(
                data["ExpirationDate"]
            )
        )
    if data.get("LicenseArn") is not None:
        out["license_arn"] = data["LicenseArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Entitlement) -> dict:
    out: dict = {}
    if "product_code" in value:
        out["ProductCode"] = value["product_code"]
    if "dimension" in value:
        out["Dimension"] = value["dimension"]
    if "customer_identifier" in value:
        out["CustomerIdentifier"] = value["customer_identifier"]
    if "customer_aws_account_id" in value:
        out["CustomerAWSAccountId"] = value["customer_aws_account_id"]
    if "value" in value:
        import capo_marketplace_entitlement_service.types.entitlement_value

        out["Value"] = (
            capo_marketplace_entitlement_service.types.entitlement_value.serialize_cbor(
                value["value"]
            )
        )
    if "expiration_date" in value:
        import capo_marketplace_entitlement_service.types.timestamp

        out["ExpirationDate"] = (
            capo_marketplace_entitlement_service.types.timestamp.serialize_cbor(
                value["expiration_date"]
            )
        )
    if "license_arn" in value:
        out["LicenseArn"] = value["license_arn"]
    return out


def deserialize_cbor(data: dict) -> Entitlement:
    out: Entitlement = {}  # type: ignore[typeddict-item]
    if data.get("ProductCode") is not None:
        out["product_code"] = data["ProductCode"]
    if data.get("Dimension") is not None:
        out["dimension"] = data["Dimension"]
    if data.get("CustomerIdentifier") is not None:
        out["customer_identifier"] = data["CustomerIdentifier"]
    if data.get("CustomerAWSAccountId") is not None:
        out["customer_aws_account_id"] = data["CustomerAWSAccountId"]
    if data.get("Value") is not None:
        import capo_marketplace_entitlement_service.types.entitlement_value

        out["value"] = (
            capo_marketplace_entitlement_service.types.entitlement_value.deserialize_cbor(
                data["Value"]
            )
        )
    if data.get("ExpirationDate") is not None:
        import capo_marketplace_entitlement_service.types.timestamp

        out["expiration_date"] = (
            capo_marketplace_entitlement_service.types.timestamp.deserialize_cbor(
                data["ExpirationDate"]
            )
        )
    if data.get("LicenseArn") is not None:
        out["license_arn"] = data["LicenseArn"]
    return out
