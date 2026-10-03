"""Generated from Smithy shape ``com.amazonaws.connect#UpdateContactFlowContentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.contact_flow_content
    import capo_connect.types.contact_flow_id
    import capo_connect.types.instance_id


class UpdateContactFlowContentRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance.</p>"""
    contact_flow_id: "capo_connect.types.contact_flow_id.ContactFlowId"
    """<p>The identifier of the flow.</p>"""
    content: "capo_connect.types.contact_flow_content.ContactFlowContent"
    """<p>The JSON string that represents the content of the flow. For an example, see <a href="https://docs.aws.amazon.com/connect/latest/APIReference/flow-language-example.html">Example flow in Connect Customer Flow language</a>. </p> <p>Length Constraints: Minimum length of 1. Maximum length of 256000.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateContactFlowContentRequest) -> dict:
    out: dict = {}
    out["Content"] = value["content"]
    return out


def deserialize_json(data: dict) -> UpdateContactFlowContentRequest:
    out: UpdateContactFlowContentRequest = {}  # type: ignore[typeddict-item]
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    else:
        raise DeserializationError("UpdateContactFlowContentRequest.content required")
    return out
