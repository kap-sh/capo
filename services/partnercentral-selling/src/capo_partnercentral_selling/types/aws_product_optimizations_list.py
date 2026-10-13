"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsProductOptimizationsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.aws_product_optimization

AwsProductOptimizationsList: TypeAlias = list[
    "capo_partnercentral_selling.types.aws_product_optimization.AwsProductOptimization"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsProductOptimizationsList) -> list:
    import capo_partnercentral_selling.types.aws_product_optimization

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_selling.types.aws_product_optimization.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AwsProductOptimizationsList:
    import capo_partnercentral_selling.types.aws_product_optimization

    out: AwsProductOptimizationsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_selling.types.aws_product_optimization.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: AwsProductOptimizationsList) -> list[Any]:
    import capo_partnercentral_selling.types.aws_product_optimization

    return [
        capo_partnercentral_selling.types.aws_product_optimization.redact_sensitive(
            item
        )
        for item in value
    ]
