"""Generated from Smithy shape ``com.amazonaws.devopsagent#IdpAuthConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime


class IdpAuthConfiguration(TypedDict, closed=True):
    issuer_url: "str"
    """<p>The OIDC issuer URL of the external Identity Provider</p>"""
    client_id: "str"
    """<p>The OIDC client ID for the IdP application</p>"""
    operator_app_role_arn: "str"
    """<p>The IAM role end users assume to access AIDevOps APIs</p>"""
    provider: "str"
    """<p>The Identity Provider name (e.g., Entra, Okta, Google)</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the Operator App IdP auth flow was enabled.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the Operator App IdP auth flow was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdpAuthConfiguration) -> dict:
    out: dict = {}
    out["issuerUrl"] = value["issuer_url"]
    out["clientId"] = value["client_id"]
    out["operatorAppRoleArn"] = value["operator_app_role_arn"]
    out["provider"] = value["provider"]
    import capo_devops_agent._protocol.serialize

    out["createdAt"] = capo_devops_agent._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    if "updated_at" in value:
        import capo_devops_agent._protocol.serialize

        out["updatedAt"] = capo_devops_agent._protocol.serialize.fmt_date_time(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> IdpAuthConfiguration:
    out: IdpAuthConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("issuerUrl") is not None:
        out["issuer_url"] = data["issuerUrl"]
    else:
        out["issuer_url"] = ""
    if data.get("clientId") is not None:
        out["client_id"] = data["clientId"]
    else:
        out["client_id"] = ""
    if data.get("operatorAppRoleArn") is not None:
        out["operator_app_role_arn"] = data["operatorAppRoleArn"]
    else:
        out["operator_app_role_arn"] = ""
    if data.get("provider") is not None:
        out["provider"] = data["provider"]
    else:
        out["provider"] = ""
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    return out
