"""Generated from Smithy shape ``com.amazonaws.interconnect#UpdateConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_interconnect.types.connection_bandwidth
    import capo_interconnect.types.connection_description
    import capo_interconnect.types.connection_id


class UpdateConnectionRequest(TypedDict, closed=True):
    identifier: "capo_interconnect.types.connection_id.ConnectionId"
    """<p>The identifier of the <a>Connection</a> that should be updated.</p>"""
    description: NotRequired[
        "capo_interconnect.types.connection_description.ConnectionDescription"
    ]
    """<p>An updated description to apply to the <a>Connection</a> </p>"""
    bandwidth: NotRequired[
        "capo_interconnect.types.connection_bandwidth.ConnectionBandwidth"
    ]
    """<p>Request a new bandwidth size on the given <a>Connection</a>.</p> <p>Note that changes to the size may be subject to additional policy, and does require the remote partner provider to acknowledge and permit this new bandwidth size.</p>"""
    client_token: NotRequired["str"]
    """<p>Idempotency token used for the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateConnectionRequest) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    if "description" in value:
        out["description"] = value["description"]
    if "bandwidth" in value:
        out["bandwidth"] = value["bandwidth"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateConnectionRequest:
    out: UpdateConnectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        out["identifier"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("bandwidth") is not None:
        out["bandwidth"] = data["bandwidth"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
