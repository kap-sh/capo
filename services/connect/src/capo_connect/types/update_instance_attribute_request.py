"""Generated from Smithy shape ``com.amazonaws.connect#UpdateInstanceAttributeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.client_token
    import capo_connect.types.instance_attribute_type
    import capo_connect.types.instance_attribute_value
    import capo_connect.types.instance_id


class UpdateInstanceAttributeRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    attribute_type: "capo_connect.types.instance_attribute_type.InstanceAttributeType"
    """<p>The type of attribute.</p> <note> <p>Only allowlisted customers can consume USE_CUSTOM_TTS_VOICES. To access this feature, contact Amazon Web Services Support for allowlisting.</p> </note> <note> <p>If you set the attribute type as <code>MESSAGE_STREAMING</code>, you need to update the Lex bot alias resource based policy to include the <code>lex:RecognizeMessageAsync</code> action for the connect instance ARN resource.</p> </note> <note> <p>If you set the attribute type <code>AUTO_MUTE_AGENT_ON_HOLD</code> to <code>true</code>, the system automatically mutes agents while they're on hold and unmutes them when they resume the contact. Agents can't change their mute state while on hold.</p> </note>"""
    value: "capo_connect.types.instance_attribute_value.InstanceAttributeValue"
    """<p>The value for the attribute. Maximum character limit is 100. </p>"""
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateInstanceAttributeRequest) -> dict:
    out: dict = {}
    out["Value"] = value["value"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateInstanceAttributeRequest:
    out: UpdateInstanceAttributeRequest = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("UpdateInstanceAttributeRequest.value required")
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
