"""Generated from Smithy shape ``com.amazonaws.eventbridge#CreatePartnerEventSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.account_id
    import capo_eventbridge.types.event_source_name


class CreatePartnerEventSourceRequest(TypedDict, closed=True):
    name: "capo_eventbridge.types.event_source_name.EventSourceName"
    """<p>The name of the partner event source. This name must be unique and must be in the format <code> <i>partner_name</i>/<i>event_namespace</i>/<i>event_name</i> </code>. The Amazon Web Services account that wants to use this partner event source must create a partner event bus with a name that matches the name of the partner event source.</p>"""
    account: "capo_eventbridge.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID that is permitted to create a matching partner event bus for this partner event source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePartnerEventSourceRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Account"] = value["account"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePartnerEventSourceRequest:
    out: CreatePartnerEventSourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Account") is not None:
        out["account"] = data["Account"]
    else:
        out["account"] = ""
    return out
