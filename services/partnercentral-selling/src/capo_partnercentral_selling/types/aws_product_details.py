"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsProductDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.aws_product_optimizations_list
    import capo_partnercentral_selling.types.monetary_amount
    import capo_partnercentral_selling.types.string_list


class AwsProductDetails(TypedDict, closed=True):
    product_code: "str"
    """<p>AWS Partner Central product identifier used for opportunity association.</p>"""
    service_code: NotRequired["str"]
    """<p>Pricing Calculator service code.</p>"""
    categories: "capo_partnercentral_selling.types.string_list.StringList"
    """<p>List of program and pathway categories this product is eligible for.</p>"""
    amount: NotRequired[
        "capo_partnercentral_selling.types.monetary_amount.MonetaryAmount"
    ]
    """<p>Baseline service cost before optimizations.</p>"""
    optimized_amount: NotRequired[
        "capo_partnercentral_selling.types.monetary_amount.MonetaryAmount"
    ]
    """<p>Service cost after applying optimizations.</p>"""
    potential_savings_amount: NotRequired[
        "capo_partnercentral_selling.types.monetary_amount.MonetaryAmount"
    ]
    """<p>Service-specific cost reduction through optimizations.</p>"""
    optimizations: "capo_partnercentral_selling.types.aws_product_optimizations_list.AwsProductOptimizationsList"
    """<p>List of specific optimization recommendations for this product.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsProductDetails) -> dict:
    out: dict = {}
    out["ProductCode"] = value["product_code"]
    if "service_code" in value:
        out["ServiceCode"] = value["service_code"]
    import capo_partnercentral_selling.types.string_list

    out["Categories"] = (
        capo_partnercentral_selling.types.string_list.serialize_aws_json_1_0(
            value["categories"]
        )
    )
    if "amount" in value:
        out["Amount"] = value["amount"]
    if "optimized_amount" in value:
        out["OptimizedAmount"] = value["optimized_amount"]
    if "potential_savings_amount" in value:
        out["PotentialSavingsAmount"] = value["potential_savings_amount"]
    import capo_partnercentral_selling.types.aws_product_optimizations_list

    out["Optimizations"] = (
        capo_partnercentral_selling.types.aws_product_optimizations_list.serialize_aws_json_1_0(
            value["optimizations"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> AwsProductDetails:
    out: AwsProductDetails = {}  # type: ignore[typeddict-item]
    if data.get("ProductCode") is not None:
        out["product_code"] = data["ProductCode"]
    else:
        raise DeserializationError("AwsProductDetails.product_code required")
    if data.get("ServiceCode") is not None:
        out["service_code"] = data["ServiceCode"]
    if data.get("Categories") is not None:
        import capo_partnercentral_selling.types.string_list

        out["categories"] = (
            capo_partnercentral_selling.types.string_list.deserialize_aws_json_1_0(
                data["Categories"]
            )
        )
    else:
        raise DeserializationError("AwsProductDetails.categories required")
    if data.get("Amount") is not None:
        out["amount"] = data["Amount"]
    if data.get("OptimizedAmount") is not None:
        out["optimized_amount"] = data["OptimizedAmount"]
    if data.get("PotentialSavingsAmount") is not None:
        out["potential_savings_amount"] = data["PotentialSavingsAmount"]
    if data.get("Optimizations") is not None:
        import capo_partnercentral_selling.types.aws_product_optimizations_list

        out["optimizations"] = (
            capo_partnercentral_selling.types.aws_product_optimizations_list.deserialize_aws_json_1_0(
                data["Optimizations"]
            )
        )
    else:
        raise DeserializationError("AwsProductDetails.optimizations required")
    return out


def redact_sensitive(value: AwsProductDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "amount" in value:
        out["amount"] = "*** Sensitive Data Redacted ***"
    if "optimized_amount" in value:
        out["optimized_amount"] = "*** Sensitive Data Redacted ***"
    if "potential_savings_amount" in value:
        out["potential_savings_amount"] = "*** Sensitive Data Redacted ***"
    if "optimizations" in value:
        import capo_partnercentral_selling.types.aws_product_optimizations_list

        out["optimizations"] = (
            capo_partnercentral_selling.types.aws_product_optimizations_list.redact_sensitive(
                value["optimizations"]
            )
        )
    return out
