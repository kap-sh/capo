"""Generated from Smithy shape ``com.amazonaws.quicksight#GetIdentityContextResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.status_code2


class GetIdentityContextResponse(TypedDict, closed=True):
    status: "capo_quicksight.types.status_code2.StatusCode2"
    """<p>The HTTP status of the request.</p>"""
    request_id: "str"
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    context: NotRequired["str"]
    """<p>The identity context information for the user. This is an identity token that should be used as the ContextAssertion parameter in the <a href="https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html">STS AssumeRole API</a> call to obtain identity enhanced Amazon Web Services credentials.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIdentityContextResponse) -> dict:
    out: dict = {}
    out["RequestId"] = value["request_id"]
    if "context" in value:
        out["Context"] = value["context"]
    return out


def deserialize_json(data: dict) -> GetIdentityContextResponse:
    out: GetIdentityContextResponse = {}  # type: ignore[typeddict-item]
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    else:
        raise DeserializationError("GetIdentityContextResponse.request_id required")
    if data.get("Context") is not None:
        out["context"] = data["Context"]
    return out
