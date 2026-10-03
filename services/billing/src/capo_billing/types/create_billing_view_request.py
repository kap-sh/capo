"""Generated from Smithy shape ``com.amazonaws.billing#CreateBillingViewRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_billing.errors import DeserializationError

if TYPE_CHECKING:
    import capo_billing.types.billing_view_description
    import capo_billing.types.billing_view_name
    import capo_billing.types.billing_view_source_views_list
    import capo_billing.types.client_token
    import capo_billing.types.expression
    import capo_billing.types.resource_tag_list


class CreateBillingViewRequest(TypedDict, closed=True):
    name: "capo_billing.types.billing_view_name.BillingViewName"
    """<p> The name of the billing view. </p>"""
    description: NotRequired[
        "capo_billing.types.billing_view_description.BillingViewDescription"
    ]
    """<p> The description of the billing view. </p>"""
    source_views: (
        "capo_billing.types.billing_view_source_views_list.BillingViewSourceViewsList"
    )
    """<p>A list of billing views used as the data source for the custom billing view.</p>"""
    data_filter_expression: NotRequired["capo_billing.types.expression.Expression"]
    """<p> See <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_Expression.html">Expression</a>. Billing view only supports <code>LINKED_ACCOUNT</code>, <code>Tags</code>, and <code>CostCategories</code>. </p>"""
    client_token: NotRequired["capo_billing.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier you specify to ensure idempotency of the request. Idempotency ensures that an API request completes no more than one time. If the original request completes successfully, any subsequent retries complete successfully without performing any further actions with an idempotent request. </p>"""
    resource_tags: NotRequired["capo_billing.types.resource_tag_list.ResourceTagList"]
    """<p>A list of key value map specifying tags associated to the billing view being created. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateBillingViewRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_billing.types.billing_view_source_views_list

    out["sourceViews"] = (
        capo_billing.types.billing_view_source_views_list.serialize_aws_json_1_0(
            value["source_views"]
        )
    )
    if "data_filter_expression" in value:
        import capo_billing.types.expression

        out["dataFilterExpression"] = (
            capo_billing.types.expression.serialize_aws_json_1_0(
                value["data_filter_expression"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "resource_tags" in value:
        import capo_billing.types.resource_tag_list

        out["resourceTags"] = (
            capo_billing.types.resource_tag_list.serialize_aws_json_1_0(
                value["resource_tags"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateBillingViewRequest:
    out: CreateBillingViewRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateBillingViewRequest.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("sourceViews") is not None:
        import capo_billing.types.billing_view_source_views_list

        out["source_views"] = (
            capo_billing.types.billing_view_source_views_list.deserialize_aws_json_1_0(
                data["sourceViews"]
            )
        )
    else:
        raise DeserializationError("CreateBillingViewRequest.source_views required")
    if data.get("dataFilterExpression") is not None:
        import capo_billing.types.expression

        out["data_filter_expression"] = (
            capo_billing.types.expression.deserialize_aws_json_1_0(
                data["dataFilterExpression"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("resourceTags") is not None:
        import capo_billing.types.resource_tag_list

        out["resource_tags"] = (
            capo_billing.types.resource_tag_list.deserialize_aws_json_1_0(
                data["resourceTags"]
            )
        )
    return out
