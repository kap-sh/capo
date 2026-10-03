"""Generated from Smithy shape ``com.amazonaws.wafv2#RequestInspection``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.password_field
    import capo_wafv2.types.payload_type
    import capo_wafv2.types.username_field


class RequestInspection(TypedDict, closed=True):
    payload_type: "capo_wafv2.types.payload_type.PayloadType"
    """<p>The payload type for your login endpoint, either JSON or form encoded.</p>"""
    username_field: "capo_wafv2.types.username_field.UsernameField"
    """<p>The name of the field in the request payload that contains your customer's username. </p> <p>How you specify this depends on the request inspection payload type.</p> <ul> <li> <p>For JSON payloads, specify the field name in JSON pointer syntax. For information about the JSON Pointer syntax, see the Internet Engineering Task Force (IETF) documentation <a href="https://tools.ietf.org/html/rfc6901">JavaScript Object Notation (JSON) Pointer</a>. </p> <p>For example, for the JSON payload <code>{ "form": { "username": "THE_USERNAME" } }</code>, the username field specification is <code>/form/username</code>. </p> </li> <li> <p>For form encoded payload types, use the HTML form names.</p> <p>For example, for an HTML form with the input element named <code>username1</code>, the username field specification is <code>username1</code> </p> </li> </ul>"""
    password_field: "capo_wafv2.types.password_field.PasswordField"
    """<p>The name of the field in the request payload that contains your customer's password. </p> <p>How you specify this depends on the request inspection payload type.</p> <ul> <li> <p>For JSON payloads, specify the field name in JSON pointer syntax. For information about the JSON Pointer syntax, see the Internet Engineering Task Force (IETF) documentation <a href="https://tools.ietf.org/html/rfc6901">JavaScript Object Notation (JSON) Pointer</a>. </p> <p>For example, for the JSON payload <code>{ "form": { "password": "THE_PASSWORD" } }</code>, the password field specification is <code>/form/password</code>.</p> </li> <li> <p>For form encoded payload types, use the HTML form names.</p> <p>For example, for an HTML form with the input element named <code>password1</code>, the password field specification is <code>password1</code>.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RequestInspection) -> dict:
    out: dict = {}
    import capo_wafv2.types.payload_type

    out["PayloadType"] = capo_wafv2.types.payload_type.serialize_aws_json_1_1(
        value["payload_type"]
    )
    import capo_wafv2.types.username_field

    out["UsernameField"] = capo_wafv2.types.username_field.serialize_aws_json_1_1(
        value["username_field"]
    )
    import capo_wafv2.types.password_field

    out["PasswordField"] = capo_wafv2.types.password_field.serialize_aws_json_1_1(
        value["password_field"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RequestInspection:
    out: RequestInspection = {}  # type: ignore[typeddict-item]
    if data.get("PayloadType") is not None:
        import capo_wafv2.types.payload_type

        out["payload_type"] = capo_wafv2.types.payload_type.deserialize_aws_json_1_1(
            data["PayloadType"]
        )
    else:
        raise DeserializationError("RequestInspection.payload_type required")
    if data.get("UsernameField") is not None:
        import capo_wafv2.types.username_field

        out["username_field"] = (
            capo_wafv2.types.username_field.deserialize_aws_json_1_1(
                data["UsernameField"]
            )
        )
    else:
        raise DeserializationError("RequestInspection.username_field required")
    if data.get("PasswordField") is not None:
        import capo_wafv2.types.password_field

        out["password_field"] = (
            capo_wafv2.types.password_field.deserialize_aws_json_1_1(
                data["PasswordField"]
            )
        )
    else:
        raise DeserializationError("RequestInspection.password_field required")
    return out
