"""Generated from Smithy shape ``com.amazonaws.ssm#AzureSubscription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.azure_subscription_display_name
    import capo_ssm.types.azure_subscription_id


class AzureSubscription(TypedDict, closed=True):
    id: "capo_ssm.types.azure_subscription_id.AzureSubscriptionId"
    """<p>The ID of the Azure subscription.</p>"""
    display_name: NotRequired[
        "capo_ssm.types.azure_subscription_display_name.AzureSubscriptionDisplayName"
    ]
    """<p>The display name of the Azure subscription.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AzureSubscription) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AzureSubscription:
    out: AzureSubscription = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    return out
