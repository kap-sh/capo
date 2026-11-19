"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ListAgreementRequestsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_request_summary_list
    import capo_marketplace_agreement.types.next_token


class ListAgreementRequestsOutput(TypedDict, closed=True):
    items: NotRequired[
        "capo_marketplace_agreement.types.agreement_request_summary_list.AgreementRequestSummaryList"
    ]
    """<p>An array of <code>AgreementRequestSummary</code> objects containing summary information about each agreement request.</p>"""
    next_token: NotRequired["capo_marketplace_agreement.types.next_token.NextToken"]
    """<p>The token used for pagination. The field is <code>null</code> if there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAgreementRequestsOutput) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_marketplace_agreement.types.agreement_request_summary_list

        out["items"] = (
            capo_marketplace_agreement.types.agreement_request_summary_list.serialize_aws_json_1_0(
                value["items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAgreementRequestsOutput:
    out: ListAgreementRequestsOutput = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_marketplace_agreement.types.agreement_request_summary_list

        out["items"] = (
            capo_marketplace_agreement.types.agreement_request_summary_list.deserialize_aws_json_1_0(
                data["items"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
