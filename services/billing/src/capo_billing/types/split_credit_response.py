"""Generated from Smithy shape ``com.amazonaws.billing#SplitCreditResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_billing.types.child_credits
    import capo_billing.types.credit_id


class SplitCreditResponse(TypedDict, closed=True):
    parent_credit_id: "capo_billing.types.credit_id.CreditId"
    """<p>The ID of the credit that was split.</p>"""
    child_credits: "capo_billing.types.child_credits.ChildCredits"
    """<p>The new credits, in the order of the requested portions.</p>"""
    dry_run: "bool"
    """<p>Specifies whether the request was a dry run. If <code>true</code>, the operation didn't change any credit.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SplitCreditResponse) -> dict:
    out: dict = {}
    out["parentCreditId"] = value["parent_credit_id"]
    import capo_billing.types.child_credits

    out["childCredits"] = capo_billing.types.child_credits.serialize_aws_json_1_0(
        value["child_credits"]
    )
    out["dryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SplitCreditResponse:
    out: SplitCreditResponse = {}  # type: ignore[typeddict-item]
    if data.get("parentCreditId") is not None:
        out["parent_credit_id"] = data["parentCreditId"]
    else:
        out["parent_credit_id"] = ""
    if data.get("childCredits") is not None:
        import capo_billing.types.child_credits

        out["child_credits"] = (
            capo_billing.types.child_credits.deserialize_aws_json_1_0(
                data["childCredits"]
            )
        )
    else:
        out["child_credits"] = []
    if data.get("dryRun") is not None:
        out["dry_run"] = data["dryRun"]
    else:
        out["dry_run"] = False
    return out
