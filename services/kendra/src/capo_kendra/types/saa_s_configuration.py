"""Generated from Smithy shape ``com.amazonaws.kendra#SaaSConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.organization_name
    import capo_kendra.types.url


class SaaSConfiguration(TypedDict, closed=True):
    organization_name: "capo_kendra.types.organization_name.OrganizationName"
    """<p>The name of the organization of the GitHub Enterprise Cloud (SaaS) account you want to connect to. You can find your organization name by logging into GitHub desktop and selecting <b>Your organizations</b> under your profile picture dropdown.</p>"""
    host_url: "capo_kendra.types.url.Url"
    """<p>The GitHub host URL or API endpoint URL. For example, <i>https://api.github.com</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SaaSConfiguration) -> dict:
    out: dict = {}
    out["OrganizationName"] = value["organization_name"]
    out["HostUrl"] = value["host_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SaaSConfiguration:
    out: SaaSConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationName") is not None:
        out["organization_name"] = data["OrganizationName"]
    else:
        out["organization_name"] = ""
    if data.get("HostUrl") is not None:
        out["host_url"] = data["HostUrl"]
    else:
        out["host_url"] = ""
    return out
