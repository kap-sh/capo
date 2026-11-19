"""Generated from Smithy shape ``com.amazonaws.billing#SplitCreditRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billing.types.client_token
    import capo_billing.types.credit_id
    import capo_billing.types.split_portions


class SplitCreditRequest(TypedDict, closed=True):
    credit_id: "capo_billing.types.credit_id.CreditId"
    """<p>The ID of the credit to split.</p>"""
    portions: "capo_billing.types.split_portions.SplitPortions"
    """<p>The new credits to create, one for each portion, in the order listed.</p>"""
    client_token: NotRequired["capo_billing.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If you retry a successful request with the same client token and parameters, the retry completes without performing any further actions. If you reuse a client token with different parameters, the request fails with a <code>ValidationException</code>.</p>"""
    dry_run: NotRequired["bool"]
    """<p>Specifies whether to validate the request and return the result without changing any credit.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SplitCreditRequest) -> dict:
    out: dict = {}
    out["creditId"] = value["credit_id"]
    import capo_billing.types.split_portions

    out["portions"] = capo_billing.types.split_portions.serialize_aws_json_1_0(
        value["portions"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "dry_run" in value:
        out["dryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SplitCreditRequest:
    out: SplitCreditRequest = {}  # type: ignore[typeddict-item]
    if data.get("creditId") is not None:
        out["credit_id"] = data["creditId"]
    else:
        out["credit_id"] = ""
    if data.get("portions") is not None:
        import capo_billing.types.split_portions

        out["portions"] = capo_billing.types.split_portions.deserialize_aws_json_1_0(
            data["portions"]
        )
    else:
        out["portions"] = []
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("dryRun") is not None:
        out["dry_run"] = data["dryRun"]
    return out
