"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#DeleteEnvironmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_thin_client.types.client_token
    import capo_workspaces_thin_client.types.environment_id


class DeleteEnvironmentRequest(TypedDict, closed=True):
    id: "capo_workspaces_thin_client.types.environment_id.EnvironmentId"
    """<p>The ID of the environment to delete.</p>"""
    client_token: NotRequired[
        "capo_workspaces_thin_client.types.client_token.ClientToken"
    ]
    """<p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEnvironmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEnvironmentRequest:
    out: DeleteEnvironmentRequest = {}  # type: ignore[typeddict-item]
    return out
