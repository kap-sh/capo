"""Generated from Smithy shape ``com.amazonaws.wafregional#DeleteLoggingConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.resource_arn


class DeleteLoggingConfigurationRequest(TypedDict, closed=True):
    resource_arn: "capo_waf_regional.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the web ACL from which you want to delete the <a>LoggingConfiguration</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteLoggingConfigurationRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteLoggingConfigurationRequest:
    out: DeleteLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    return out
