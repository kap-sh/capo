"""Generated from Smithy shape ``com.amazonaws.lightsail#WafAcfpConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.string
    import capo_lightsail.types.waf_payload_type_enum
    import capo_lightsail.types.waf_response_inspection


class WafAcfpConfig(TypedDict, closed=True):
    payload_type: NotRequired[
        "capo_lightsail.types.waf_payload_type_enum.WafPayloadTypeEnum"
    ]
    """<p>The content type of the request body of account creation requests.</p> <p>The following content types are possible:</p> <ul> <li> <p> <code>JSON</code> – The request body is in JSON format.</p> </li> <li> <p> <code>FORM_ENCODED</code> – The request body is form encoded.</p> </li> </ul>"""
    creation_path: NotRequired["capo_lightsail.types.string.string"]
    """<p>The path of the endpoint that accepts completed account creation forms (for example, <code>/signup/submit</code>). This endpoint must accept <code>POST</code> requests.</p> <p>Constraints:</p> <ul> <li> <p>Must start with a forward slash (<code>/</code>).</p> </li> <li> <p>Must contain from 1 to 256 characters.</p> </li> </ul>"""
    registration_page_path: NotRequired["capo_lightsail.types.string.string"]
    """<p>The path of the page that displays the account creation form (for example, <code>/signup</code>).</p> <p>Constraints:</p> <ul> <li> <p>Must start with a forward slash (<code>/</code>).</p> </li> <li> <p>Must contain from 1 to 256 characters.</p> </li> </ul>"""
    response_inspection: NotRequired[
        "capo_lightsail.types.waf_response_inspection.WafResponseInspection"
    ]
    """<p>An object that describes the HTTP status codes that your application returns for successful and failed account creation attempts.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WafAcfpConfig) -> dict:
    out: dict = {}
    if "payload_type" in value:
        import capo_lightsail.types.waf_payload_type_enum

        out["payloadType"] = (
            capo_lightsail.types.waf_payload_type_enum.serialize_aws_json_1_1(
                value["payload_type"]
            )
        )
    if "creation_path" in value:
        out["creationPath"] = value["creation_path"]
    if "registration_page_path" in value:
        out["registrationPagePath"] = value["registration_page_path"]
    if "response_inspection" in value:
        import capo_lightsail.types.waf_response_inspection

        out["responseInspection"] = (
            capo_lightsail.types.waf_response_inspection.serialize_aws_json_1_1(
                value["response_inspection"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WafAcfpConfig:
    out: WafAcfpConfig = {}  # type: ignore[typeddict-item]
    if data.get("payloadType") is not None:
        import capo_lightsail.types.waf_payload_type_enum

        out["payload_type"] = (
            capo_lightsail.types.waf_payload_type_enum.deserialize_aws_json_1_1(
                data["payloadType"]
            )
        )
    if data.get("creationPath") is not None:
        out["creation_path"] = data["creationPath"]
    if data.get("registrationPagePath") is not None:
        out["registration_page_path"] = data["registrationPagePath"]
    if data.get("responseInspection") is not None:
        import capo_lightsail.types.waf_response_inspection

        out["response_inspection"] = (
            capo_lightsail.types.waf_response_inspection.deserialize_aws_json_1_1(
                data["responseInspection"]
            )
        )
    return out
