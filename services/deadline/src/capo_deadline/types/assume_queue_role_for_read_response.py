"""Generated from Smithy shape ``com.amazonaws.deadline#AssumeQueueRoleForReadResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.aws_credentials


class AssumeQueueRoleForReadResponse(TypedDict, closed=True):
    credentials: "capo_deadline.types.aws_credentials.AwsCredentials"
    """The credentials for the queue role."""


# --- restJson1 ser/de ---
def serialize_json(value: AssumeQueueRoleForReadResponse) -> dict:
    out: dict = {}
    import capo_deadline.types.aws_credentials

    out["credentials"] = capo_deadline.types.aws_credentials.serialize_json(
        value["credentials"]
    )
    return out


def deserialize_json(data: dict) -> AssumeQueueRoleForReadResponse:
    out: AssumeQueueRoleForReadResponse = {}  # type: ignore[typeddict-item]
    if data.get("credentials") is not None:
        import capo_deadline.types.aws_credentials

        out["credentials"] = capo_deadline.types.aws_credentials.deserialize_json(
            data["credentials"]
        )
    else:
        raise DeserializationError(
            "AssumeQueueRoleForReadResponse.credentials required"
        )
    return out
