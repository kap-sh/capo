"""Generated from Smithy shape ``com.amazonaws.connect#UpdateContactAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.attributes
    import capo_connect.types.contact_id
    import capo_connect.types.instance_id


class UpdateContactAttributesRequest(TypedDict, closed=True):
    initial_contact_id: "capo_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact. This is the identifier of the contact associated with the first interaction with the contact center.</p>"""
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    attributes: "capo_connect.types.attributes.Attributes"
    """<p>The Connect Customer attributes. These attributes can be accessed in flows just like any other contact attributes.</p> <p>You can have up to 32,768 UTF-8 bytes across all attributes for a contact. Attribute keys can include only alphanumeric, dash, and underscore characters.</p> <p>In the <a href="https://docs.aws.amazon.com/connect/latest/adminguide/set-contact-attributes.html">Set contact attributes</a> block, when the attributes for a contact exceed 32 KB, the contact is routed down the Error branch of the flow. As a mitigation, consider the following options:</p> <ul> <li> <p>Remove unnecessary attributes by setting their values to empty.</p> </li> <li> <p>If the attributes are only used in one flow and don't need to be referred to outside of that flow (for example, by a Lambda or another flow), then use flow attributes. This way you aren't needlessly persisting the 32 KB of information from one flow to another. For more information, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/set-contact-attributes.html">Flow block: Set contact attributes</a> in the <i>Connect Customer Administrator Guide</i>. </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateContactAttributesRequest) -> dict:
    out: dict = {}
    out["InitialContactId"] = value["initial_contact_id"]
    out["InstanceId"] = value["instance_id"]
    import capo_connect.types.attributes

    out["Attributes"] = capo_connect.types.attributes.serialize_json(
        value["attributes"]
    )
    return out


def deserialize_json(data: dict) -> UpdateContactAttributesRequest:
    out: UpdateContactAttributesRequest = {}  # type: ignore[typeddict-item]
    if data.get("InitialContactId") is not None:
        out["initial_contact_id"] = data["InitialContactId"]
    else:
        raise DeserializationError(
            "UpdateContactAttributesRequest.initial_contact_id required"
        )
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError(
            "UpdateContactAttributesRequest.instance_id required"
        )
    if data.get("Attributes") is not None:
        import capo_connect.types.attributes

        out["attributes"] = capo_connect.types.attributes.deserialize_json(
            data["Attributes"]
        )
    else:
        raise DeserializationError("UpdateContactAttributesRequest.attributes required")
    return out
