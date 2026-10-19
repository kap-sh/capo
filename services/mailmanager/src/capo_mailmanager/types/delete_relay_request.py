"""Generated from Smithy shape ``com.amazonaws.mailmanager#DeleteRelayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.relay_id


class DeleteRelayRequest(TypedDict, closed=True):
    relay_id: "capo_mailmanager.types.relay_id.RelayId"
    """<p>The unique relay identifier.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteRelayRequest) -> dict:
    out: dict = {}
    out["RelayId"] = value["relay_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteRelayRequest:
    out: DeleteRelayRequest = {}  # type: ignore[typeddict-item]
    if data.get("RelayId") is not None:
        out["relay_id"] = data["RelayId"]
    else:
        out["relay_id"] = ""
    return out
