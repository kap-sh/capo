"""Generated from Smithy shape ``com.amazonaws.inspector2#DeleteCodeSecurityIntegrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.code_security_integration_arn


class DeleteCodeSecurityIntegrationRequest(TypedDict, closed=True):
    integration_arn: (
        "capo_inspector2.types.code_security_integration_arn.CodeSecurityIntegrationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the code security integration to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCodeSecurityIntegrationRequest) -> dict:
    out: dict = {}
    out["integrationArn"] = value["integration_arn"]
    return out


def deserialize_json(data: dict) -> DeleteCodeSecurityIntegrationRequest:
    out: DeleteCodeSecurityIntegrationRequest = {}  # type: ignore[typeddict-item]
    if data.get("integrationArn") is not None:
        out["integration_arn"] = data["integrationArn"]
    else:
        out["integration_arn"] = ""
    return out
