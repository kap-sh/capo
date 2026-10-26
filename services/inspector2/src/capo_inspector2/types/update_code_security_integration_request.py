"""Generated from Smithy shape ``com.amazonaws.inspector2#UpdateCodeSecurityIntegrationRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.code_security_integration_arn
    import capo_inspector2.types.update_integration_details


class UpdateCodeSecurityIntegrationRequest(TypedDict, closed=True):
    integration_arn: (
        "capo_inspector2.types.code_security_integration_arn.CodeSecurityIntegrationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the code security integration to update.</p>"""
    details: "capo_inspector2.types.update_integration_details.UpdateIntegrationDetails"
    """<p>The updated integration details specific to the repository provider type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCodeSecurityIntegrationRequest) -> dict:
    out: dict = {}
    out["integrationArn"] = value["integration_arn"]
    import capo_inspector2.types.update_integration_details

    out["details"] = capo_inspector2.types.update_integration_details.serialize_json(
        value["details"]
    )
    return out


def deserialize_json(data: dict) -> UpdateCodeSecurityIntegrationRequest:
    out: UpdateCodeSecurityIntegrationRequest = {}  # type: ignore[typeddict-item]
    if data.get("integrationArn") is not None:
        out["integration_arn"] = data["integrationArn"]
    else:
        out["integration_arn"] = ""
    if data.get("details") is not None:
        import capo_inspector2.types.update_integration_details

        out["details"] = (
            capo_inspector2.types.update_integration_details.deserialize_json(
                data["details"]
            )
        )
    else:
        out["details"] = {"$unknown": {"name": ""}}
    return out


def redact_sensitive(value: UpdateCodeSecurityIntegrationRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "details" in value:
        import capo_inspector2.types.update_integration_details

        out["details"] = (
            capo_inspector2.types.update_integration_details.redact_sensitive(
                value["details"]
            )
        )
    return out
