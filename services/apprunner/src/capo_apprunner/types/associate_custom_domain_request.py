"""Generated from Smithy shape ``com.amazonaws.apprunner#AssociateCustomDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apprunner.types.app_runner_resource_arn
    import capo_apprunner.types.domain_name
    import capo_apprunner.types.nullable_boolean


class AssociateCustomDomainRequest(TypedDict, closed=True):
    service_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    """<p>The Amazon Resource Name (ARN) of the App Runner service that you want to associate a custom domain name with.</p>"""
    domain_name: "capo_apprunner.types.domain_name.DomainName"
    """<p>A custom domain endpoint to associate. Specify a root domain (for example, <code>example.com</code>), a subdomain (for example, <code>login.example.com</code> or <code>admin.login.example.com</code>), or a wildcard (for example, <code>*.example.com</code>).</p>"""
    enable_www_subdomain: NotRequired[
        "capo_apprunner.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Set to <code>true</code> to associate the subdomain <code>www.<i>DomainName</i> </code> with the App Runner service in addition to the base domain.</p> <p>Default: <code>true</code> </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociateCustomDomainRequest) -> dict:
    out: dict = {}
    out["ServiceArn"] = value["service_arn"]
    out["DomainName"] = value["domain_name"]
    if "enable_www_subdomain" in value:
        out["EnableWWWSubdomain"] = value["enable_www_subdomain"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociateCustomDomainRequest:
    out: AssociateCustomDomainRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServiceArn") is not None:
        out["service_arn"] = data["ServiceArn"]
    else:
        out["service_arn"] = ""
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        out["domain_name"] = ""
    if data.get("EnableWWWSubdomain") is not None:
        out["enable_www_subdomain"] = data["EnableWWWSubdomain"]
    return out
