"""Generated from Smithy shape ``com.amazonaws.wafv2#PhoneNumberField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.field_identifier


class PhoneNumberField(TypedDict, closed=True):
    identifier: "capo_wafv2.types.field_identifier.FieldIdentifier"
    """<p>The name of a single primary phone number field. </p> <p>How you specify the phone number fields depends on the request inspection payload type.</p> <ul> <li> <p>For JSON payloads, specify the field identifiers in JSON pointer syntax. For information about the JSON Pointer syntax, see the Internet Engineering Task Force (IETF) documentation <a href="https://tools.ietf.org/html/rfc6901">JavaScript Object Notation (JSON) Pointer</a>. </p> <p>For example, for the JSON payload <code>{ "form": { "primaryphoneline1": "THE_PHONE1", "primaryphoneline2": "THE_PHONE2", "primaryphoneline3": "THE_PHONE3" } }</code>, the phone number field identifiers are <code>/form/primaryphoneline1</code>, <code>/form/primaryphoneline2</code>, and <code>/form/primaryphoneline3</code>.</p> </li> <li> <p>For form encoded payload types, use the HTML form names.</p> <p>For example, for an HTML form with input elements named <code>primaryphoneline1</code>, <code>primaryphoneline2</code>, and <code>primaryphoneline3</code>, the phone number field identifiers are <code>primaryphoneline1</code>, <code>primaryphoneline2</code>, and <code>primaryphoneline3</code>. </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PhoneNumberField) -> dict:
    out: dict = {}
    out["Identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PhoneNumberField:
    out: PhoneNumberField = {}  # type: ignore[typeddict-item]
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError("PhoneNumberField.identifier required")
    return out
