"""Generated from Smithy shape ``com.amazonaws.lightsail#DeleteContactMethodRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.contact_protocol


class DeleteContactMethodRequest(TypedDict, closed=True):
    protocol: "capo_lightsail.types.contact_protocol.ContactProtocol"
    """<p>The protocol that will be deleted, such as <code>Email</code> or <code>SMS</code> (text messaging).</p> <note> <p>To delete an <code>Email</code> and an <code>SMS</code> contact method if you added both, you must run separate <code>DeleteContactMethod</code> actions to delete each protocol.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteContactMethodRequest) -> dict:
    out: dict = {}
    import capo_lightsail.types.contact_protocol

    out["protocol"] = capo_lightsail.types.contact_protocol.serialize_aws_json_1_1(
        value["protocol"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteContactMethodRequest:
    out: DeleteContactMethodRequest = {}  # type: ignore[typeddict-item]
    if data.get("protocol") is not None:
        import capo_lightsail.types.contact_protocol

        out["protocol"] = (
            capo_lightsail.types.contact_protocol.deserialize_aws_json_1_1(
                data["protocol"]
            )
        )
    else:
        import typing

        out["protocol"] = typing.cast(
            "capo_lightsail.types.contact_protocol.ContactProtocol", ""
        )
    return out
