"""Generated from Smithy shape ``com.amazonaws.lightsail#WafResponseInspection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.waf_status_code_list


class WafResponseInspection(TypedDict, closed=True):
    success_codes: NotRequired[
        "capo_lightsail.types.waf_status_code_list.WafStatusCodeList"
    ]
    """<p>The HTTP status codes that indicate a successful attempt (for example, <code>200</code>).</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 10 status codes.</p> </li> <li> <p>Each status code must be from <code>0</code> to <code>999</code>.</p> </li> <li> <p>Can't contain a status code that is also in <code>failureCodes</code>.</p> </li> </ul>"""
    failure_codes: NotRequired[
        "capo_lightsail.types.waf_status_code_list.WafStatusCodeList"
    ]
    """<p>The HTTP status codes that indicate a failed attempt (for example, <code>401</code>).</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 10 status codes.</p> </li> <li> <p>Each status code must be from <code>0</code> to <code>999</code>.</p> </li> <li> <p>Can't contain a status code that is also in <code>successCodes</code>.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WafResponseInspection) -> dict:
    out: dict = {}
    if "success_codes" in value:
        import capo_lightsail.types.waf_status_code_list

        out["successCodes"] = (
            capo_lightsail.types.waf_status_code_list.serialize_aws_json_1_1(
                value["success_codes"]
            )
        )
    if "failure_codes" in value:
        import capo_lightsail.types.waf_status_code_list

        out["failureCodes"] = (
            capo_lightsail.types.waf_status_code_list.serialize_aws_json_1_1(
                value["failure_codes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WafResponseInspection:
    out: WafResponseInspection = {}  # type: ignore[typeddict-item]
    if data.get("successCodes") is not None:
        import capo_lightsail.types.waf_status_code_list

        out["success_codes"] = (
            capo_lightsail.types.waf_status_code_list.deserialize_aws_json_1_1(
                data["successCodes"]
            )
        )
    if data.get("failureCodes") is not None:
        import capo_lightsail.types.waf_status_code_list

        out["failure_codes"] = (
            capo_lightsail.types.waf_status_code_list.deserialize_aws_json_1_1(
                data["failureCodes"]
            )
        )
    return out
