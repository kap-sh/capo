"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#UpdateEnvironmentResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_thin_client.types.environment_summary


class UpdateEnvironmentResponse(TypedDict, closed=True):
    environment: NotRequired[
        "capo_workspaces_thin_client.types.environment_summary.EnvironmentSummary"
    ]
    """<p>Describes an environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEnvironmentResponse) -> dict:
    out: dict = {}
    if "environment" in value:
        import capo_workspaces_thin_client.types.environment_summary

        out["environment"] = (
            capo_workspaces_thin_client.types.environment_summary.serialize_json(
                value["environment"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateEnvironmentResponse:
    out: UpdateEnvironmentResponse = {}  # type: ignore[typeddict-item]
    if data.get("environment") is not None:
        import capo_workspaces_thin_client.types.environment_summary

        out["environment"] = (
            capo_workspaces_thin_client.types.environment_summary.deserialize_json(
                data["environment"]
            )
        )
    return out


def redact_sensitive(value: UpdateEnvironmentResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "environment" in value:
        import capo_workspaces_thin_client.types.environment_summary

        out["environment"] = (
            capo_workspaces_thin_client.types.environment_summary.redact_sensitive(
                value["environment"]
            )
        )
    return out
