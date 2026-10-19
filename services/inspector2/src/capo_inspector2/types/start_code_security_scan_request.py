"""Generated from Smithy shape ``com.amazonaws.inspector2#StartCodeSecurityScanRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.code_security_client_token
    import capo_inspector2.types.code_security_resource


class StartCodeSecurityScanRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_inspector2.types.code_security_client_token.CodeSecurityClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    resource: "capo_inspector2.types.code_security_resource.CodeSecurityResource"
    """<p>The resource identifier for the code repository to scan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartCodeSecurityScanRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import capo_inspector2.types.code_security_resource

    out["resource"] = capo_inspector2.types.code_security_resource.serialize_json(
        value["resource"]
    )
    return out


def deserialize_json(data: dict) -> StartCodeSecurityScanRequest:
    out: StartCodeSecurityScanRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("resource") is not None:
        import capo_inspector2.types.code_security_resource

        out["resource"] = capo_inspector2.types.code_security_resource.deserialize_json(
            data["resource"]
        )
    else:
        import capo_inspector2.types._unknown

        out["resource"] = capo_inspector2.types._unknown.UnknownUnionMember("")
    return out
