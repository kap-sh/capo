"""Generated from Smithy shape ``com.amazonaws.billing#GetContractInformationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_billing.types.contract_details


class GetContractInformationResponse(TypedDict, closed=True):
    contract: "capo_billing.types.contract_details.ContractDetails"
    """<p>The contract details such as term (duration), eligible payer accounts, investment accounts, and legal entities.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetContractInformationResponse) -> dict:
    out: dict = {}
    import capo_billing.types.contract_details

    out["contract"] = capo_billing.types.contract_details.serialize_aws_json_1_0(
        value["contract"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetContractInformationResponse:
    out: GetContractInformationResponse = {}  # type: ignore[typeddict-item]
    if data.get("contract") is not None:
        import capo_billing.types.contract_details

        out["contract"] = capo_billing.types.contract_details.deserialize_aws_json_1_0(
            data["contract"]
        )
    else:
        out["contract"] = {"$unknown": {"name": ""}}
    return out


def redact_sensitive(value: GetContractInformationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "contract" in value:
        import capo_billing.types.contract_details

        out["contract"] = capo_billing.types.contract_details.redact_sensitive(
            value["contract"]
        )
    return out
