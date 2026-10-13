"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ExpectedCustomerSpendList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.expected_customer_spend

ExpectedCustomerSpendList: TypeAlias = list[
    "capo_partnercentral_selling.types.expected_customer_spend.ExpectedCustomerSpend"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExpectedCustomerSpendList) -> list:
    import capo_partnercentral_selling.types.expected_customer_spend

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_selling.types.expected_customer_spend.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ExpectedCustomerSpendList:
    import capo_partnercentral_selling.types.expected_customer_spend

    out: ExpectedCustomerSpendList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_selling.types.expected_customer_spend.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: ExpectedCustomerSpendList) -> list[Any]:
    import capo_partnercentral_selling.types.expected_customer_spend

    return [
        capo_partnercentral_selling.types.expected_customer_spend.redact_sensitive(item)
        for item in value
    ]
