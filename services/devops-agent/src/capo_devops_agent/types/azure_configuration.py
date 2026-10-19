"""Generated from Smithy shape ``com.amazonaws.devopsagent#AzureConfiguration``."""

from typing_extensions import TypedDict


class AzureConfiguration(TypedDict, closed=True):
    subscription_id: "str"
    """<p>Azure subscription ID corresponding to provided resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzureConfiguration) -> dict:
    out: dict = {}
    out["subscriptionId"] = value["subscription_id"]
    return out


def deserialize_json(data: dict) -> AzureConfiguration:
    out: AzureConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("subscriptionId") is not None:
        out["subscription_id"] = data["subscriptionId"]
    else:
        out["subscription_id"] = ""
    return out
