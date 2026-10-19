"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#GetBillScenarioRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.resource_id


class GetBillScenarioRequest(TypedDict, closed=True):
    identifier: "capo_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The unique identifier of the bill scenario to retrieve. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetBillScenarioRequest) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetBillScenarioRequest:
    out: GetBillScenarioRequest = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        out["identifier"] = ""
    return out
