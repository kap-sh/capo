"""Generated from Smithy shape ``com.amazonaws.billing#AssociateSourceViewsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_billing.types.billing_view_arn
    import capo_billing.types.billing_view_source_views_list


class AssociateSourceViewsRequest(TypedDict, closed=True):
    arn: "capo_billing.types.billing_view_arn.BillingViewArn"
    """<p> The Amazon Resource Name (ARN) of the billing view to associate source views with. </p>"""
    source_views: (
        "capo_billing.types.billing_view_source_views_list.BillingViewSourceViewsList"
    )
    """<p>A list of ARNs of the source billing views to associate. Source views can be of the following types:</p> <ul> <li> <p> <code>PRIMARY</code> - The billing view that contains all cost management data associated with an account.</p> </li> <li> <p> <code>CUSTOM</code> - A billing view that a customer creates from one or more source views.</p> </li> <li> <p> <code>BILLING_GROUP</code> - The billing view for an Billing Conductor billing group.</p> </li> <li> <p> <code>BILLING_TRANSFER</code> - The billing view for the billing data that a bill transfer account is financially responsible for.</p> </li> <li> <p> <code>BILLING_TRANSFER_SHOWBACK</code> - The billing view for billing data configured for showback or chargeback purposes.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociateSourceViewsRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    import capo_billing.types.billing_view_source_views_list

    out["sourceViews"] = (
        capo_billing.types.billing_view_source_views_list.serialize_aws_json_1_0(
            value["source_views"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociateSourceViewsRequest:
    out: AssociateSourceViewsRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("sourceViews") is not None:
        import capo_billing.types.billing_view_source_views_list

        out["source_views"] = (
            capo_billing.types.billing_view_source_views_list.deserialize_aws_json_1_0(
                data["sourceViews"]
            )
        )
    else:
        out["source_views"] = []
    return out
