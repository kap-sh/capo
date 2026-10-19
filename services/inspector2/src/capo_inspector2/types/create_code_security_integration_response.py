"""Generated from Smithy shape ``com.amazonaws.inspector2#CreateCodeSecurityIntegrationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.authorization_url
    import capo_inspector2.types.code_security_integration_arn
    import capo_inspector2.types.integration_status


class CreateCodeSecurityIntegrationResponse(TypedDict, closed=True):
    integration_arn: (
        "capo_inspector2.types.code_security_integration_arn.CodeSecurityIntegrationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the created code security integration.</p>"""
    status: "capo_inspector2.types.integration_status.IntegrationStatus"
    """<p>The current status of the code security integration.</p>"""
    authorization_url: NotRequired[
        "capo_inspector2.types.authorization_url.AuthorizationUrl"
    ]
    """<p>The URL used to authorize the integration with the repository provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCodeSecurityIntegrationResponse) -> dict:
    out: dict = {}
    out["integrationArn"] = value["integration_arn"]
    import capo_inspector2.types.integration_status

    out["status"] = capo_inspector2.types.integration_status.serialize_json(
        value["status"]
    )
    if "authorization_url" in value:
        out["authorizationUrl"] = value["authorization_url"]
    return out


def deserialize_json(data: dict) -> CreateCodeSecurityIntegrationResponse:
    out: CreateCodeSecurityIntegrationResponse = {}  # type: ignore[typeddict-item]
    if data.get("integrationArn") is not None:
        out["integration_arn"] = data["integrationArn"]
    else:
        out["integration_arn"] = ""
    if data.get("status") is not None:
        import capo_inspector2.types.integration_status

        out["status"] = capo_inspector2.types.integration_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_inspector2.types.integration_status.IntegrationStatus", ""
        )
    if data.get("authorizationUrl") is not None:
        out["authorization_url"] = data["authorizationUrl"]
    return out


def redact_sensitive(value: CreateCodeSecurityIntegrationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authorization_url" in value:
        out["authorization_url"] = "*** Sensitive Data Redacted ***"
    return out
