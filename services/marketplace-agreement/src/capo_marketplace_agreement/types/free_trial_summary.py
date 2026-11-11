"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#FreeTrialSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.timestamp


class FreeTrialSummary(TypedDict, closed=True):
    trial_end_time: NotRequired["capo_marketplace_agreement.types.timestamp.Timestamp"]
    """<p>The date and time when the free trial ends. For an agreement that includes both a free trial and usage-based pricing, the agreement converts to paid usage at this time.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FreeTrialSummary) -> dict:
    out: dict = {}
    if "trial_end_time" in value:
        import capo_marketplace_agreement.types.timestamp

        out["trialEndTime"] = (
            capo_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
                value["trial_end_time"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> FreeTrialSummary:
    out: FreeTrialSummary = {}  # type: ignore[typeddict-item]
    if data.get("trialEndTime") is not None:
        import capo_marketplace_agreement.types.timestamp

        out["trial_end_time"] = (
            capo_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["trialEndTime"]
            )
        )
    return out
