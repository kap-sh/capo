"""Generated from Smithy shape ``com.amazonaws.wafv2#EmailField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.field_identifier


class EmailField(TypedDict, closed=True):
    identifier: "capo_wafv2.types.field_identifier.FieldIdentifier"
    """<p>The name of the email field. </p> <p>How you specify this depends on the request inspection payload type.</p> <ul> <li> <p>For JSON payloads, specify the field name in JSON pointer syntax. For information about the JSON Pointer syntax, see the Internet Engineering Task Force (IETF) documentation <a href="https://tools.ietf.org/html/rfc6901">JavaScript Object Notation (JSON) Pointer</a>. </p> <p>For example, for the JSON payload <code>{ "form": { "email": "THE_EMAIL" } }</code>, the email field specification is <code>/form/email</code>.</p> </li> <li> <p>For form encoded payload types, use the HTML form names.</p> <p>For example, for an HTML form with the input element named <code>email1</code>, the email field specification is <code>email1</code>.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EmailField) -> dict:
    out: dict = {}
    out["Identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EmailField:
    out: EmailField = {}  # type: ignore[typeddict-item]
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError("EmailField.identifier required")
    return out
