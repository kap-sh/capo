"""Generated from Smithy shape ``com.amazonaws.grafana#DescribeWorkspaceAuthenticationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import capo_grafana.types.authentication_description


class DescribeWorkspaceAuthenticationResponse(TypedDict, closed=True):
    authentication: (
        "capo_grafana.types.authentication_description.AuthenticationDescription"
    )
    """<p>A structure containing information about the authentication methods used in the workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeWorkspaceAuthenticationResponse) -> dict:
    out: dict = {}
    import capo_grafana.types.authentication_description

    out["authentication"] = (
        capo_grafana.types.authentication_description.serialize_json(
            value["authentication"]
        )
    )
    return out


def deserialize_json(data: dict) -> DescribeWorkspaceAuthenticationResponse:
    out: DescribeWorkspaceAuthenticationResponse = {}  # type: ignore[typeddict-item]
    if data.get("authentication") is not None:
        import capo_grafana.types.authentication_description

        out["authentication"] = (
            capo_grafana.types.authentication_description.deserialize_json(
                data["authentication"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeWorkspaceAuthenticationResponse.authentication required"
        )
    return out


def redact_sensitive(value: DescribeWorkspaceAuthenticationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authentication" in value:
        import capo_grafana.types.authentication_description

        out["authentication"] = (
            capo_grafana.types.authentication_description.redact_sensitive(
                value["authentication"]
            )
        )
    return out
