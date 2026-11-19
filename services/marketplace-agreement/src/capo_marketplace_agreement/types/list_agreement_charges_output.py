"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ListAgreementChargesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.charges
    import capo_marketplace_agreement.types.next_token


class ListAgreementChargesOutput(TypedDict, closed=True):
    items: NotRequired["capo_marketplace_agreement.types.charges.Charges"]
    """<p>A list of agreement charges.</p>"""
    next_token: NotRequired["capo_marketplace_agreement.types.next_token.NextToken"]
    """<p>The token used for pagination. The field is <code>null</code> if there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAgreementChargesOutput) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_marketplace_agreement.types.charges

        out["items"] = capo_marketplace_agreement.types.charges.serialize_aws_json_1_0(
            value["items"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAgreementChargesOutput:
    out: ListAgreementChargesOutput = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_marketplace_agreement.types.charges

        out["items"] = (
            capo_marketplace_agreement.types.charges.deserialize_aws_json_1_0(
                data["items"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListAgreementChargesOutput) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_marketplace_agreement.types.charges

        out["items"] = capo_marketplace_agreement.types.charges.serialize_cbor(
            value["items"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListAgreementChargesOutput:
    out: ListAgreementChargesOutput = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_marketplace_agreement.types.charges

        out["items"] = capo_marketplace_agreement.types.charges.deserialize_cbor(
            data["items"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
