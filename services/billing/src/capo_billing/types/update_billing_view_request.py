"""Generated from Smithy shape ``com.amazonaws.billing#UpdateBillingViewRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_billing.errors import DeserializationError

if TYPE_CHECKING:
    import capo_billing.types.billing_view_arn
    import capo_billing.types.billing_view_description
    import capo_billing.types.billing_view_name
    import capo_billing.types.expression


class UpdateBillingViewRequest(TypedDict, closed=True):
    arn: "capo_billing.types.billing_view_arn.BillingViewArn"
    """<p> The Amazon Resource Name (ARN) that can be used to uniquely identify the billing view. </p>"""
    name: NotRequired["capo_billing.types.billing_view_name.BillingViewName"]
    """<p> The name of the billing view. </p>"""
    description: NotRequired[
        "capo_billing.types.billing_view_description.BillingViewDescription"
    ]
    """<p> The description of the billing view. </p>"""
    data_filter_expression: NotRequired["capo_billing.types.expression.Expression"]
    """<p>See <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_Expression.html">Expression</a>. Billing view only supports <code>LINKED_ACCOUNT</code>, <code>Tags</code>, and <code>CostCategories</code>. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateBillingViewRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "data_filter_expression" in value:
        import capo_billing.types.expression

        out["dataFilterExpression"] = (
            capo_billing.types.expression.serialize_aws_json_1_0(
                value["data_filter_expression"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateBillingViewRequest:
    out: UpdateBillingViewRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("UpdateBillingViewRequest.arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("dataFilterExpression") is not None:
        import capo_billing.types.expression

        out["data_filter_expression"] = (
            capo_billing.types.expression.deserialize_aws_json_1_0(
                data["dataFilterExpression"]
            )
        )
    return out
