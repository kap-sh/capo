"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#Identity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb_streams.types.string


class Identity(TypedDict, closed=True):
    principal_id: NotRequired["capo_dynamodb_streams.types.string.String"]
    """<p>A unique identifier for the entity that made the call. For Time To Live, the principalId is "dynamodb.amazonaws.com".</p>"""
    type: NotRequired["capo_dynamodb_streams.types.string.String"]
    """<p>The type of the identity. For Time To Live, the type is "Service".</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Identity) -> dict:
    out: dict = {}
    if "principal_id" in value:
        out["PrincipalId"] = value["principal_id"]
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Identity:
    out: Identity = {}  # type: ignore[typeddict-item]
    if data.get("PrincipalId") is not None:
        out["principal_id"] = data["PrincipalId"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    return out
