"""Generated from Smithy shape ``com.amazonaws.inspector2#UpdateCodeSecurityIntegrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.code_security_integration_arn
    import capo_inspector2.types.integration_status


class UpdateCodeSecurityIntegrationResponse(TypedDict, closed=True):
    integration_arn: (
        "capo_inspector2.types.code_security_integration_arn.CodeSecurityIntegrationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the updated code security integration.</p>"""
    status: "capo_inspector2.types.integration_status.IntegrationStatus"
    """<p>The current status of the updated code security integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCodeSecurityIntegrationResponse) -> dict:
    out: dict = {}
    out["integrationArn"] = value["integration_arn"]
    import capo_inspector2.types.integration_status

    out["status"] = capo_inspector2.types.integration_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> UpdateCodeSecurityIntegrationResponse:
    out: UpdateCodeSecurityIntegrationResponse = {}  # type: ignore[typeddict-item]
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
    return out
