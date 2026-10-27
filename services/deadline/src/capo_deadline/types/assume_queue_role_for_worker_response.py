"""Generated from Smithy shape ``com.amazonaws.deadline#AssumeQueueRoleForWorkerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.aws_credentials


class AssumeQueueRoleForWorkerResponse(TypedDict, closed=True):
    credentials: NotRequired["capo_deadline.types.aws_credentials.AwsCredentials"]
    """The Amazon Web Services credentials for the role that the worker is assuming."""


# --- restJson1 ser/de ---
def serialize_json(value: AssumeQueueRoleForWorkerResponse) -> dict:
    out: dict = {}
    if "credentials" in value:
        import capo_deadline.types.aws_credentials

        out["credentials"] = capo_deadline.types.aws_credentials.serialize_json(
            value["credentials"]
        )
    return out


def deserialize_json(data: dict) -> AssumeQueueRoleForWorkerResponse:
    out: AssumeQueueRoleForWorkerResponse = {}  # type: ignore[typeddict-item]
    if data.get("credentials") is not None:
        import capo_deadline.types.aws_credentials

        out["credentials"] = capo_deadline.types.aws_credentials.deserialize_json(
            data["credentials"]
        )
    return out
