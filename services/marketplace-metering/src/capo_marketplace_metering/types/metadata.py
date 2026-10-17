"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#Metadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_metering.types.agreement_id


class Metadata(TypedDict, closed=True):
    agreement_id: NotRequired[
        "capo_marketplace_metering.types.agreement_id.AgreementId"
    ]
    """<p>The unique identifier of the Amazon Web Services Marketplace agreement the customer accepted. Use it to call Amazon Web Services Marketplace Agreement APIs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Metadata) -> dict:
    out: dict = {}
    if "agreement_id" in value:
        out["AgreementId"] = value["agreement_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Metadata:
    out: Metadata = {}  # type: ignore[typeddict-item]
    if data.get("AgreementId") is not None:
        out["agreement_id"] = data["AgreementId"]
    return out
