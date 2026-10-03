"""Generated from Smithy shape ``com.amazonaws.interconnect#CreateConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_interconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_interconnect.types.attach_point
    import capo_interconnect.types.connection_bandwidth
    import capo_interconnect.types.connection_description
    import capo_interconnect.types.environment_id
    import capo_interconnect.types.remote_account_identifier
    import capo_interconnect.types.tag_map


class CreateConnectionRequest(TypedDict, closed=True):
    description: NotRequired[
        "capo_interconnect.types.connection_description.ConnectionDescription"
    ]
    """<p>A description to distinguish this <a>Connection</a>.</p>"""
    bandwidth: "capo_interconnect.types.connection_bandwidth.ConnectionBandwidth"
    """<p>The desired bandwidth of the requested <a>Connection</a> </p>"""
    attach_point: "capo_interconnect.types.attach_point.AttachPoint"
    """<p>The Attach Point to which the connection should be associated."</p>"""
    environment_id: "capo_interconnect.types.environment_id.EnvironmentId"
    """<p>The identifier of the <a>Environment</a> across which this <a>Connection</a> should be created.</p> <p>The available <a>Environment</a> objects can be determined using <a>ListEnvironments</a>.</p>"""
    remote_account: NotRequired[
        "capo_interconnect.types.remote_account_identifier.RemoteAccountIdentifier"
    ]
    """<p>Account and/or principal identifying information that can be verified by the partner of this specific Environment.</p>"""
    tags: NotRequired["capo_interconnect.types.tag_map.TagMap"]
    """<p>The tag to associate with the resulting <a>Connection</a>.</p>"""
    client_token: NotRequired["str"]
    """<p>Idempotency token used for the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateConnectionRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    out["bandwidth"] = value["bandwidth"]
    import capo_interconnect.types.attach_point

    out["attachPoint"] = capo_interconnect.types.attach_point.serialize_aws_json_1_0(
        value["attach_point"]
    )
    out["environmentId"] = value["environment_id"]
    if "remote_account" in value:
        import capo_interconnect.types.remote_account_identifier

        out["remoteAccount"] = (
            capo_interconnect.types.remote_account_identifier.serialize_aws_json_1_0(
                value["remote_account"]
            )
        )
    if "tags" in value:
        import capo_interconnect.types.tag_map

        out["tags"] = capo_interconnect.types.tag_map.serialize_aws_json_1_0(
            value["tags"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateConnectionRequest:
    out: CreateConnectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("bandwidth") is not None:
        out["bandwidth"] = data["bandwidth"]
    else:
        raise DeserializationError("CreateConnectionRequest.bandwidth required")
    if data.get("attachPoint") is not None:
        import capo_interconnect.types.attach_point

        out["attach_point"] = (
            capo_interconnect.types.attach_point.deserialize_aws_json_1_0(
                data["attachPoint"]
            )
        )
    else:
        raise DeserializationError("CreateConnectionRequest.attach_point required")
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    else:
        raise DeserializationError("CreateConnectionRequest.environment_id required")
    if data.get("remoteAccount") is not None:
        import capo_interconnect.types.remote_account_identifier

        out["remote_account"] = (
            capo_interconnect.types.remote_account_identifier.deserialize_aws_json_1_0(
                data["remoteAccount"]
            )
        )
    if data.get("tags") is not None:
        import capo_interconnect.types.tag_map

        out["tags"] = capo_interconnect.types.tag_map.deserialize_aws_json_1_0(
            data["tags"]
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
