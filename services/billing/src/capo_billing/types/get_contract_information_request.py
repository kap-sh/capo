"""Generated from Smithy shape ``com.amazonaws.billing#GetContractInformationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_billing.types.arn_string


class GetContractInformationRequest(TypedDict, closed=True):
    contract_arn: "capo_billing.types.arn_string.ArnString"
    """<p>The Amazon Resource Name (ARN) of the contract to retrieve information about.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetContractInformationRequest) -> dict:
    out: dict = {}
    out["contractArn"] = value["contract_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetContractInformationRequest:
    out: GetContractInformationRequest = {}  # type: ignore[typeddict-item]
    if data.get("contractArn") is not None:
        out["contract_arn"] = data["contractArn"]
    else:
        out["contract_arn"] = ""
    return out
