"""Generated from Smithy shape ``com.amazonaws.evs#DeleteEnvironmentHostRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_evs.types.client_token
    import capo_evs.types.environment_id
    import capo_evs.types.host_name


class DeleteEnvironmentHostRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_evs.types.client_token.ClientToken"]
    """<note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the host deletion request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>"""
    environment_id: "capo_evs.types.environment_id.EnvironmentId"
    """<p>A unique ID for the host's environment.</p>"""
    host_name: "capo_evs.types.host_name.HostName"
    """<p>The DNS hostname associated with the host to be deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteEnvironmentHostRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["environmentId"] = value["environment_id"]
    out["hostName"] = value["host_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteEnvironmentHostRequest:
    out: DeleteEnvironmentHostRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    else:
        out["environment_id"] = ""
    if data.get("hostName") is not None:
        out["host_name"] = data["hostName"]
    else:
        out["host_name"] = ""
    return out
