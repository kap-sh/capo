"""Generated from Smithy shape ``com.amazonaws.transfer#ListAgreementsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.listed_agreements
    import capo_transfer.types.next_token


class ListAgreementsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_transfer.types.next_token.NextToken"]
    """<p>Returns a token that you can use to call <code>ListAgreements</code> again and receive additional results, if there are any.</p>"""
    agreements: "capo_transfer.types.listed_agreements.ListedAgreements"
    """<p>Returns an array, where each item contains the details of an agreement.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAgreementsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import capo_transfer.types.listed_agreements

    out["Agreements"] = capo_transfer.types.listed_agreements.serialize_aws_json_1_1(
        value["agreements"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAgreementsResponse:
    out: ListAgreementsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Agreements") is not None:
        import capo_transfer.types.listed_agreements

        out["agreements"] = (
            capo_transfer.types.listed_agreements.deserialize_aws_json_1_1(
                data["Agreements"]
            )
        )
    else:
        out["agreements"] = []
    return out
