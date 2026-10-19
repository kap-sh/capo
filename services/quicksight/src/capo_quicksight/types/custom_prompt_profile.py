"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomPromptProfile``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.model_profile_id
    import capo_quicksight.types.qbs_aws_account_id
    import capo_quicksight.types.subscription_id


class CustomPromptProfile(TypedDict, closed=True):
    model_profile_id: "capo_quicksight.types.model_profile_id.ModelProfileId"
    """<p>The identifier of the model profile.</p>"""
    subscription_id: "capo_quicksight.types.subscription_id.SubscriptionId"
    """<p>The subscription identifier.</p>"""
    qbs_aws_account_id: "capo_quicksight.types.qbs_aws_account_id.QbsAwsAccountId"
    """<p>The Amazon Web Services account ID for the Q Business service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomPromptProfile) -> dict:
    out: dict = {}
    out["ModelProfileId"] = value["model_profile_id"]
    out["SubscriptionId"] = value["subscription_id"]
    out["QbsAwsAccountId"] = value["qbs_aws_account_id"]
    return out


def deserialize_json(data: dict) -> CustomPromptProfile:
    out: CustomPromptProfile = {}  # type: ignore[typeddict-item]
    if data.get("ModelProfileId") is not None:
        out["model_profile_id"] = data["ModelProfileId"]
    else:
        out["model_profile_id"] = ""
    if data.get("SubscriptionId") is not None:
        out["subscription_id"] = data["SubscriptionId"]
    else:
        out["subscription_id"] = ""
    if data.get("QbsAwsAccountId") is not None:
        out["qbs_aws_account_id"] = data["QbsAwsAccountId"]
    else:
        out["qbs_aws_account_id"] = ""
    return out
