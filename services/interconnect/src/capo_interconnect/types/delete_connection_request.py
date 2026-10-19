"""Generated from Smithy shape ``com.amazonaws.interconnect#DeleteConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_interconnect.types.connection_id


class DeleteConnectionRequest(TypedDict, closed=True):
    identifier: "capo_interconnect.types.connection_id.ConnectionId"
    """<p>The identifier of the <a>Connection</a> to be deleted. </p>"""
    client_token: NotRequired["str"]
    """<p>Idempotency token used for the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteConnectionRequest) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteConnectionRequest:
    out: DeleteConnectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        out["identifier"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
