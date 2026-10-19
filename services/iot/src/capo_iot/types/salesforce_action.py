"""Generated from Smithy shape ``com.amazonaws.iot#SalesforceAction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.salesforce_endpoint
    import capo_iot.types.salesforce_token


class SalesforceAction(TypedDict, closed=True):
    token: "capo_iot.types.salesforce_token.SalesforceToken"
    """<p>The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token is available from the Salesforce IoT Cloud platform after creation of the Input Stream.</p>"""
    url: "capo_iot.types.salesforce_endpoint.SalesforceEndpoint"
    """<p>The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the Salesforce IoT Cloud platform after creation of the Input Stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SalesforceAction) -> dict:
    out: dict = {}
    out["token"] = value["token"]
    out["url"] = value["url"]
    return out


def deserialize_json(data: dict) -> SalesforceAction:
    out: SalesforceAction = {}  # type: ignore[typeddict-item]
    if data.get("token") is not None:
        out["token"] = data["token"]
    else:
        out["token"] = ""
    if data.get("url") is not None:
        out["url"] = data["url"]
    else:
        out["url"] = ""
    return out
