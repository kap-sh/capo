"""Generated from Smithy shape ``com.amazonaws.evs#CreateEnvironmentHostRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_evs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_evs.types.client_token
    import capo_evs.types.environment_id
    import capo_evs.types.esx_version
    import capo_evs.types.host_info_for_create


class CreateEnvironmentHostRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_evs.types.client_token.ClientToken"]
    """<note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the host creation request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>"""
    environment_id: "capo_evs.types.environment_id.EnvironmentId"
    """<p>A unique ID for the environment that the host is added to.</p>"""
    host: "capo_evs.types.host_info_for_create.HostInfoForCreate"
    """<p>The host that is created and added to the environment.</p>"""
    esx_version: NotRequired["capo_evs.types.esx_version.EsxVersion"]
    """<p>The ESX version to use for the host.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateEnvironmentHostRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["environmentId"] = value["environment_id"]
    import capo_evs.types.host_info_for_create

    out["host"] = capo_evs.types.host_info_for_create.serialize_aws_json_1_0(
        value["host"]
    )
    if "esx_version" in value:
        out["esxVersion"] = value["esx_version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateEnvironmentHostRequest:
    out: CreateEnvironmentHostRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    else:
        out["environment_id"] = ""
    if data.get("host") is not None:
        import capo_evs.types.host_info_for_create

        out["host"] = capo_evs.types.host_info_for_create.deserialize_aws_json_1_0(
            data["host"]
        )
    else:
        raise DeserializationError("CreateEnvironmentHostRequest.host required")
    if data.get("esxVersion") is not None:
        out["esx_version"] = data["esxVersion"]
    return out
