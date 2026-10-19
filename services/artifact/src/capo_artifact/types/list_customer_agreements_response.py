"""Generated from Smithy shape ``com.amazonaws.artifact#ListCustomerAgreementsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_artifact.types.customer_agreement_list
    import capo_artifact.types.next_token_attribute


class ListCustomerAgreementsResponse(TypedDict, closed=True):
    customer_agreements: (
        "capo_artifact.types.customer_agreement_list.CustomerAgreementList"
    )
    """<p>List of customer-agreement resources.</p>"""
    next_token: NotRequired[
        "capo_artifact.types.next_token_attribute.NextTokenAttribute"
    ]
    """<p>Pagination token to request the next page of resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomerAgreementsResponse) -> dict:
    out: dict = {}
    import capo_artifact.types.customer_agreement_list

    out["customerAgreements"] = (
        capo_artifact.types.customer_agreement_list.serialize_json(
            value["customer_agreements"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCustomerAgreementsResponse:
    out: ListCustomerAgreementsResponse = {}  # type: ignore[typeddict-item]
    if data.get("customerAgreements") is not None:
        import capo_artifact.types.customer_agreement_list

        out["customer_agreements"] = (
            capo_artifact.types.customer_agreement_list.deserialize_json(
                data["customerAgreements"]
            )
        )
    else:
        out["customer_agreements"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
