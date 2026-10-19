"""Generated from Smithy shape ``com.amazonaws.billing#DisassociateSourceViewsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_billing.types.billing_view_arn
    import capo_billing.types.billing_view_source_views_list


class DisassociateSourceViewsRequest(TypedDict, closed=True):
    arn: "capo_billing.types.billing_view_arn.BillingViewArn"
    """<p> The Amazon Resource Name (ARN) of the billing view to disassociate source views from. </p>"""
    source_views: (
        "capo_billing.types.billing_view_source_views_list.BillingViewSourceViewsList"
    )
    """<p> A list of ARNs of the source billing views to disassociate. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DisassociateSourceViewsRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    import capo_billing.types.billing_view_source_views_list

    out["sourceViews"] = (
        capo_billing.types.billing_view_source_views_list.serialize_aws_json_1_0(
            value["source_views"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DisassociateSourceViewsRequest:
    out: DisassociateSourceViewsRequest = {}  # type: ignore[typeddict-item]
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
