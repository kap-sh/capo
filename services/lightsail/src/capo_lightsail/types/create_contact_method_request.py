"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateContactMethodRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lightsail.types.contact_protocol
    import capo_lightsail.types.string_max256
    import capo_lightsail.types.tag_list


class CreateContactMethodRequest(TypedDict, closed=True):
    protocol: "capo_lightsail.types.contact_protocol.ContactProtocol"
    """<p>The protocol of the contact method, such as <code>Email</code> or <code>SMS</code> (text messaging).</p> <p>The <code>SMS</code> protocol is supported only in the following Amazon Web Services Regions.</p> <ul> <li> <p>US East (N. Virginia) (<code>us-east-1</code>)</p> </li> <li> <p>US West (Oregon) (<code>us-west-2</code>)</p> </li> <li> <p>Europe (Ireland) (<code>eu-west-1</code>)</p> </li> <li> <p>Asia Pacific (Tokyo) (<code>ap-northeast-1</code>)</p> </li> <li> <p>Asia Pacific (Singapore) (<code>ap-southeast-1</code>)</p> </li> <li> <p>Asia Pacific (Sydney) (<code>ap-southeast-2</code>)</p> </li> </ul> <p>For a list of countries/regions where SMS text messages can be sent, and the latest Amazon Web Services Regions where SMS text messaging is supported, see <a href="https://docs.aws.amazon.com/sns/latest/dg/sns-supported-regions-countries.html">Supported Regions and Countries</a> in the <i>Amazon SNS Developer Guide</i>.</p> <p>For more information about notifications in Amazon Lightsail, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-notifications">Notifications in Amazon Lightsail</a>.</p>"""
    contact_endpoint: "capo_lightsail.types.string_max256.StringMax256"
    """<p>The destination of the contact method, such as an email address or a mobile phone number.</p> <p>Use the E.164 format when specifying a mobile phone number. E.164 is a standard for the phone number structure used for international telecommunication. Phone numbers that follow this format can have a maximum of 15 digits, and they are prefixed with the plus character (+) and the country code. For example, a U.S. phone number in E.164 format would be specified as +1XXX5550100. For more information, see <a href="https://en.wikipedia.org/wiki/E.164">E.164</a> on <i>Wikipedia</i>.</p>"""
    tags: NotRequired["capo_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values to add to the contact method during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateContactMethodRequest) -> dict:
    out: dict = {}
    import capo_lightsail.types.contact_protocol

    out["protocol"] = capo_lightsail.types.contact_protocol.serialize_aws_json_1_1(
        value["protocol"]
    )
    out["contactEndpoint"] = value["contact_endpoint"]
    if "tags" in value:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateContactMethodRequest:
    out: CreateContactMethodRequest = {}  # type: ignore[typeddict-item]
    if data.get("protocol") is not None:
        import capo_lightsail.types.contact_protocol

        out["protocol"] = (
            capo_lightsail.types.contact_protocol.deserialize_aws_json_1_1(
                data["protocol"]
            )
        )
    else:
        raise DeserializationError("CreateContactMethodRequest.protocol required")
    if data.get("contactEndpoint") is not None:
        out["contact_endpoint"] = data["contactEndpoint"]
    else:
        raise DeserializationError(
            "CreateContactMethodRequest.contact_endpoint required"
        )
    if data.get("tags") is not None:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
