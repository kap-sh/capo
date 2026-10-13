"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#GetEnvironmentResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_thin_client.types.environment


class GetEnvironmentResponse(TypedDict, closed=True):
    environment: NotRequired[
        "capo_workspaces_thin_client.types.environment.Environment"
    ]
    """<p>Describes an environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEnvironmentResponse) -> dict:
    out: dict = {}
    if "environment" in value:
        import capo_workspaces_thin_client.types.environment

        out["environment"] = (
            capo_workspaces_thin_client.types.environment.serialize_json(
                value["environment"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetEnvironmentResponse:
    out: GetEnvironmentResponse = {}  # type: ignore[typeddict-item]
    if data.get("environment") is not None:
        import capo_workspaces_thin_client.types.environment

        out["environment"] = (
            capo_workspaces_thin_client.types.environment.deserialize_json(
                data["environment"]
            )
        )
    return out


def redact_sensitive(value: GetEnvironmentResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "environment" in value:
        import capo_workspaces_thin_client.types.environment

        out["environment"] = (
            capo_workspaces_thin_client.types.environment.redact_sensitive(
                value["environment"]
            )
        )
    return out
