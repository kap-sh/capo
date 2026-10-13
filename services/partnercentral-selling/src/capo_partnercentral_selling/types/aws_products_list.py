"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsProductsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.aws_product_details

AwsProductsList: TypeAlias = list[
    "capo_partnercentral_selling.types.aws_product_details.AwsProductDetails"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsProductsList) -> list:
    import capo_partnercentral_selling.types.aws_product_details

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_selling.types.aws_product_details.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AwsProductsList:
    import capo_partnercentral_selling.types.aws_product_details

    out: AwsProductsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_selling.types.aws_product_details.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: AwsProductsList) -> list[Any]:
    import capo_partnercentral_selling.types.aws_product_details

    return [
        capo_partnercentral_selling.types.aws_product_details.redact_sensitive(item)
        for item in value
    ]
