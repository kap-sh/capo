"""Generated from Smithy shape ``com.amazonaws.apprunner#DisassociateCustomDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_apprunner.types.app_runner_resource_arn
    import capo_apprunner.types.domain_name


class DisassociateCustomDomainRequest(TypedDict, closed=True):
    service_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    """<p>The Amazon Resource Name (ARN) of the App Runner service that you want to disassociate a custom domain name from.</p>"""
    domain_name: "capo_apprunner.types.domain_name.DomainName"
    """<p>The domain name that you want to disassociate from the App Runner service.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DisassociateCustomDomainRequest) -> dict:
    out: dict = {}
    out["ServiceArn"] = value["service_arn"]
    out["DomainName"] = value["domain_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DisassociateCustomDomainRequest:
    out: DisassociateCustomDomainRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServiceArn") is not None:
        out["service_arn"] = data["ServiceArn"]
    else:
        out["service_arn"] = ""
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        out["domain_name"] = ""
    return out
