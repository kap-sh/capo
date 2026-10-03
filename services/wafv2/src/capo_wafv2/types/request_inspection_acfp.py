"""Generated from Smithy shape ``com.amazonaws.wafv2#RequestInspectionACFP``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.address_fields
    import capo_wafv2.types.email_field
    import capo_wafv2.types.password_field
    import capo_wafv2.types.payload_type
    import capo_wafv2.types.phone_number_fields
    import capo_wafv2.types.username_field


class RequestInspectionACFP(TypedDict, closed=True):
    payload_type: "capo_wafv2.types.payload_type.PayloadType"
    """<p>The payload type for your account creation endpoint, either JSON or form encoded.</p>"""
    username_field: NotRequired["capo_wafv2.types.username_field.UsernameField"]
    """<p>The name of the field in the request payload that contains your customer's username. </p> <p>How you specify this depends on the request inspection payload type.</p> <ul> <li> <p>For JSON payloads, specify the field name in JSON pointer syntax. For information about the JSON Pointer syntax, see the Internet Engineering Task Force (IETF) documentation <a href="https://tools.ietf.org/html/rfc6901">JavaScript Object Notation (JSON) Pointer</a>. </p> <p>For example, for the JSON payload <code>{ "form": { "username": "THE_USERNAME" } }</code>, the username field specification is <code>/form/username</code>. </p> </li> <li> <p>For form encoded payload types, use the HTML form names.</p> <p>For example, for an HTML form with the input element named <code>username1</code>, the username field specification is <code>username1</code> </p> </li> </ul>"""
    password_field: NotRequired["capo_wafv2.types.password_field.PasswordField"]
    """<p>The name of the field in the request payload that contains your customer's password. </p> <p>How you specify this depends on the request inspection payload type.</p> <ul> <li> <p>For JSON payloads, specify the field name in JSON pointer syntax. For information about the JSON Pointer syntax, see the Internet Engineering Task Force (IETF) documentation <a href="https://tools.ietf.org/html/rfc6901">JavaScript Object Notation (JSON) Pointer</a>. </p> <p>For example, for the JSON payload <code>{ "form": { "password": "THE_PASSWORD" } }</code>, the password field specification is <code>/form/password</code>.</p> </li> <li> <p>For form encoded payload types, use the HTML form names.</p> <p>For example, for an HTML form with the input element named <code>password1</code>, the password field specification is <code>password1</code>.</p> </li> </ul>"""
    email_field: NotRequired["capo_wafv2.types.email_field.EmailField"]
    """<p>The name of the field in the request payload that contains your customer's email. </p> <p>How you specify this depends on the request inspection payload type.</p> <ul> <li> <p>For JSON payloads, specify the field name in JSON pointer syntax. For information about the JSON Pointer syntax, see the Internet Engineering Task Force (IETF) documentation <a href="https://tools.ietf.org/html/rfc6901">JavaScript Object Notation (JSON) Pointer</a>. </p> <p>For example, for the JSON payload <code>{ "form": { "email": "THE_EMAIL" } }</code>, the email field specification is <code>/form/email</code>.</p> </li> <li> <p>For form encoded payload types, use the HTML form names.</p> <p>For example, for an HTML form with the input element named <code>email1</code>, the email field specification is <code>email1</code>.</p> </li> </ul>"""
    phone_number_fields: NotRequired[
        "capo_wafv2.types.phone_number_fields.PhoneNumberFields"
    ]
    """<p>The names of the fields in the request payload that contain your customer's primary phone number. </p> <p>Order the phone number fields in the array exactly as they are ordered in the request payload. </p> <p>How you specify the phone number fields depends on the request inspection payload type.</p> <ul> <li> <p>For JSON payloads, specify the field identifiers in JSON pointer syntax. For information about the JSON Pointer syntax, see the Internet Engineering Task Force (IETF) documentation <a href="https://tools.ietf.org/html/rfc6901">JavaScript Object Notation (JSON) Pointer</a>. </p> <p>For example, for the JSON payload <code>{ "form": { "primaryphoneline1": "THE_PHONE1", "primaryphoneline2": "THE_PHONE2", "primaryphoneline3": "THE_PHONE3" } }</code>, the phone number field identifiers are <code>/form/primaryphoneline1</code>, <code>/form/primaryphoneline2</code>, and <code>/form/primaryphoneline3</code>.</p> </li> <li> <p>For form encoded payload types, use the HTML form names.</p> <p>For example, for an HTML form with input elements named <code>primaryphoneline1</code>, <code>primaryphoneline2</code>, and <code>primaryphoneline3</code>, the phone number field identifiers are <code>primaryphoneline1</code>, <code>primaryphoneline2</code>, and <code>primaryphoneline3</code>. </p> </li> </ul>"""
    address_fields: NotRequired["capo_wafv2.types.address_fields.AddressFields"]
    """<p>The names of the fields in the request payload that contain your customer's primary physical address. </p> <p>Order the address fields in the array exactly as they are ordered in the request payload. </p> <p>How you specify the address fields depends on the request inspection payload type.</p> <ul> <li> <p>For JSON payloads, specify the field identifiers in JSON pointer syntax. For information about the JSON Pointer syntax, see the Internet Engineering Task Force (IETF) documentation <a href="https://tools.ietf.org/html/rfc6901">JavaScript Object Notation (JSON) Pointer</a>. </p> <p>For example, for the JSON payload <code>{ "form": { "primaryaddressline1": "THE_ADDRESS1", "primaryaddressline2": "THE_ADDRESS2", "primaryaddressline3": "THE_ADDRESS3" } }</code>, the address field idenfiers are <code>/form/primaryaddressline1</code>, <code>/form/primaryaddressline2</code>, and <code>/form/primaryaddressline3</code>.</p> </li> <li> <p>For form encoded payload types, use the HTML form names.</p> <p>For example, for an HTML form with input elements named <code>primaryaddressline1</code>, <code>primaryaddressline2</code>, and <code>primaryaddressline3</code>, the address fields identifiers are <code>primaryaddressline1</code>, <code>primaryaddressline2</code>, and <code>primaryaddressline3</code>. </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RequestInspectionACFP) -> dict:
    out: dict = {}
    import capo_wafv2.types.payload_type

    out["PayloadType"] = capo_wafv2.types.payload_type.serialize_aws_json_1_1(
        value["payload_type"]
    )
    if "username_field" in value:
        import capo_wafv2.types.username_field

        out["UsernameField"] = capo_wafv2.types.username_field.serialize_aws_json_1_1(
            value["username_field"]
        )
    if "password_field" in value:
        import capo_wafv2.types.password_field

        out["PasswordField"] = capo_wafv2.types.password_field.serialize_aws_json_1_1(
            value["password_field"]
        )
    if "email_field" in value:
        import capo_wafv2.types.email_field

        out["EmailField"] = capo_wafv2.types.email_field.serialize_aws_json_1_1(
            value["email_field"]
        )
    if "phone_number_fields" in value:
        import capo_wafv2.types.phone_number_fields

        out["PhoneNumberFields"] = (
            capo_wafv2.types.phone_number_fields.serialize_aws_json_1_1(
                value["phone_number_fields"]
            )
        )
    if "address_fields" in value:
        import capo_wafv2.types.address_fields

        out["AddressFields"] = capo_wafv2.types.address_fields.serialize_aws_json_1_1(
            value["address_fields"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RequestInspectionACFP:
    out: RequestInspectionACFP = {}  # type: ignore[typeddict-item]
    if data.get("PayloadType") is not None:
        import capo_wafv2.types.payload_type

        out["payload_type"] = capo_wafv2.types.payload_type.deserialize_aws_json_1_1(
            data["PayloadType"]
        )
    else:
        raise DeserializationError("RequestInspectionACFP.payload_type required")
    if data.get("UsernameField") is not None:
        import capo_wafv2.types.username_field

        out["username_field"] = (
            capo_wafv2.types.username_field.deserialize_aws_json_1_1(
                data["UsernameField"]
            )
        )
    if data.get("PasswordField") is not None:
        import capo_wafv2.types.password_field

        out["password_field"] = (
            capo_wafv2.types.password_field.deserialize_aws_json_1_1(
                data["PasswordField"]
            )
        )
    if data.get("EmailField") is not None:
        import capo_wafv2.types.email_field

        out["email_field"] = capo_wafv2.types.email_field.deserialize_aws_json_1_1(
            data["EmailField"]
        )
    if data.get("PhoneNumberFields") is not None:
        import capo_wafv2.types.phone_number_fields

        out["phone_number_fields"] = (
            capo_wafv2.types.phone_number_fields.deserialize_aws_json_1_1(
                data["PhoneNumberFields"]
            )
        )
    if data.get("AddressFields") is not None:
        import capo_wafv2.types.address_fields

        out["address_fields"] = (
            capo_wafv2.types.address_fields.deserialize_aws_json_1_1(
                data["AddressFields"]
            )
        )
    return out
