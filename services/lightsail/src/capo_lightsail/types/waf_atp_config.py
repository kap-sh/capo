"""Generated from Smithy shape ``com.amazonaws.lightsail#WafAtpConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.string
    import capo_lightsail.types.waf_payload_type_enum
    import capo_lightsail.types.waf_response_inspection


class WafAtpConfig(TypedDict, closed=True):
    login_path: NotRequired["capo_lightsail.types.string.string"]
    """<p>The path of the login endpoint of your application (for example, <code>/login</code>). Login paths that start with the path that you specify are a match.</p> <p>Constraints:</p> <ul> <li> <p>Must start with a forward slash (<code>/</code>).</p> </li> <li> <p>Must contain from 1 to 256 characters.</p> </li> </ul>"""
    payload_type: NotRequired[
        "capo_lightsail.types.waf_payload_type_enum.WafPayloadTypeEnum"
    ]
    """<p>The content type of the request body of login requests.</p> <p>The following content types are possible:</p> <ul> <li> <p> <code>JSON</code> – The request body is in JSON format.</p> </li> <li> <p> <code>FORM_ENCODED</code> – The request body is form encoded.</p> </li> </ul>"""
    username_field: NotRequired["capo_lightsail.types.string.string"]
    """<p>The name of the field in the request body that contains the username (for example, <code>/username</code> for <code>JSON</code> or <code>username</code> for <code>FORM_ENCODED</code>).</p> <p>Constraints:</p> <ul> <li> <p>For a <code>JSON</code> payload, must be a JSON pointer that starts with a forward slash (<code>/</code>).</p> </li> <li> <p>Must contain from 1 to 512 characters.</p> </li> </ul>"""
    password_field: NotRequired["capo_lightsail.types.string.string"]
    """<p>The name of the field in the request body that contains the password (for example, <code>/password</code> for <code>JSON</code> or <code>password</code> for <code>FORM_ENCODED</code>).</p> <p>Constraints:</p> <ul> <li> <p>For a <code>JSON</code> payload, must be a JSON pointer that starts with a forward slash (<code>/</code>).</p> </li> <li> <p>Must contain from 1 to 512 characters.</p> </li> </ul>"""
    response_inspection: NotRequired[
        "capo_lightsail.types.waf_response_inspection.WafResponseInspection"
    ]
    """<p>An object that describes the HTTP status codes that your application returns for successful and failed login attempts.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WafAtpConfig) -> dict:
    out: dict = {}
    if "login_path" in value:
        out["loginPath"] = value["login_path"]
    if "payload_type" in value:
        import capo_lightsail.types.waf_payload_type_enum

        out["payloadType"] = (
            capo_lightsail.types.waf_payload_type_enum.serialize_aws_json_1_1(
                value["payload_type"]
            )
        )
    if "username_field" in value:
        out["usernameField"] = value["username_field"]
    if "password_field" in value:
        out["passwordField"] = value["password_field"]
    if "response_inspection" in value:
        import capo_lightsail.types.waf_response_inspection

        out["responseInspection"] = (
            capo_lightsail.types.waf_response_inspection.serialize_aws_json_1_1(
                value["response_inspection"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WafAtpConfig:
    out: WafAtpConfig = {}  # type: ignore[typeddict-item]
    if data.get("loginPath") is not None:
        out["login_path"] = data["loginPath"]
    if data.get("payloadType") is not None:
        import capo_lightsail.types.waf_payload_type_enum

        out["payload_type"] = (
            capo_lightsail.types.waf_payload_type_enum.deserialize_aws_json_1_1(
                data["payloadType"]
            )
        )
    if data.get("usernameField") is not None:
        out["username_field"] = data["usernameField"]
    if data.get("passwordField") is not None:
        out["password_field"] = data["passwordField"]
    if data.get("responseInspection") is not None:
        import capo_lightsail.types.waf_response_inspection

        out["response_inspection"] = (
            capo_lightsail.types.waf_response_inspection.deserialize_aws_json_1_1(
                data["responseInspection"]
            )
        )
    return out
