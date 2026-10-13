"""Generated from Smithy shape ``com.amazonaws.grafana#UpdateWorkspaceAuthenticationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import capo_grafana.types.authentication_description


class UpdateWorkspaceAuthenticationResponse(TypedDict, closed=True):
    authentication: (
        "capo_grafana.types.authentication_description.AuthenticationDescription"
    )
    """<p>A structure that describes the user authentication for this workspace after the update is made.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkspaceAuthenticationResponse) -> dict:
    out: dict = {}
    import capo_grafana.types.authentication_description

    out["authentication"] = (
        capo_grafana.types.authentication_description.serialize_json(
            value["authentication"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateWorkspaceAuthenticationResponse:
    out: UpdateWorkspaceAuthenticationResponse = {}  # type: ignore[typeddict-item]
    if data.get("authentication") is not None:
        import capo_grafana.types.authentication_description

        out["authentication"] = (
            capo_grafana.types.authentication_description.deserialize_json(
                data["authentication"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateWorkspaceAuthenticationResponse.authentication required"
        )
    return out


def redact_sensitive(value: UpdateWorkspaceAuthenticationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authentication" in value:
        import capo_grafana.types.authentication_description

        out["authentication"] = (
            capo_grafana.types.authentication_description.redact_sensitive(
                value["authentication"]
            )
        )
    return out
