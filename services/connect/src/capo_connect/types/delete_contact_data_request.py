"""Generated from Smithy shape ``com.amazonaws.connect#DeleteContactDataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.contact_fields
    import capo_connect.types.contact_id
    import capo_connect.types.instance_id


class DeleteContactDataRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_id: "capo_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact. You can delete PII only from a contact that has been disconnected (is in a terminated state).</p>"""
    contact_fields: "capo_connect.types.contact_fields.ContactFields"
    """<p>The categories of PII to redact from the contact. Specify one or more of the following values:</p> <ul> <li> <p> <code>CUSTOMER_ENDPOINT</code> – The customer's contact endpoint.</p> </li> <li> <p> <code>ADDITIONAL_EMAIL_RECIPIENTS</code> – Additional recipients on an email contact (email channel only).</p> </li> <li> <p> <code>EMAIL_SUBJECT</code> – The subject line of an email contact (email channel only).</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteContactDataRequest) -> dict:
    out: dict = {}
    import capo_connect.types.contact_fields

    out["ContactFields"] = capo_connect.types.contact_fields.serialize_json(
        value["contact_fields"]
    )
    return out


def deserialize_json(data: dict) -> DeleteContactDataRequest:
    out: DeleteContactDataRequest = {}  # type: ignore[typeddict-item]
    if data.get("ContactFields") is not None:
        import capo_connect.types.contact_fields

        out["contact_fields"] = capo_connect.types.contact_fields.deserialize_json(
            data["ContactFields"]
        )
    else:
        raise DeserializationError("DeleteContactDataRequest.contact_fields required")
    return out
