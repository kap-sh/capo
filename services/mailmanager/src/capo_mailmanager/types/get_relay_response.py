"""Generated from Smithy shape ``com.amazonaws.mailmanager#GetRelayResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mailmanager.types.relay_arn
    import capo_mailmanager.types.relay_authentication
    import capo_mailmanager.types.relay_id
    import capo_mailmanager.types.relay_name
    import capo_mailmanager.types.relay_server_name
    import capo_mailmanager.types.relay_server_port


class GetRelayResponse(TypedDict, closed=True):
    relay_id: "capo_mailmanager.types.relay_id.RelayId"
    """<p>The unique relay identifier.</p>"""
    relay_arn: NotRequired["capo_mailmanager.types.relay_arn.RelayArn"]
    """<p>The Amazon Resource Name (ARN) of the relay.</p>"""
    relay_name: NotRequired["capo_mailmanager.types.relay_name.RelayName"]
    """<p>The unique name of the relay.</p>"""
    server_name: NotRequired["capo_mailmanager.types.relay_server_name.RelayServerName"]
    """<p>The destination relay server address.</p>"""
    server_port: NotRequired["capo_mailmanager.types.relay_server_port.RelayServerPort"]
    """<p>The destination relay server port.</p>"""
    authentication: NotRequired[
        "capo_mailmanager.types.relay_authentication.RelayAuthentication"
    ]
    """<p>The authentication attribute—contains the secret ARN where the customer relay server credentials are stored. </p>"""
    created_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the relay was created.</p>"""
    last_modified_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp of when relay was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRelayResponse) -> dict:
    out: dict = {}
    out["RelayId"] = value["relay_id"]
    if "relay_arn" in value:
        out["RelayArn"] = value["relay_arn"]
    if "relay_name" in value:
        out["RelayName"] = value["relay_name"]
    if "server_name" in value:
        out["ServerName"] = value["server_name"]
    if "server_port" in value:
        out["ServerPort"] = value["server_port"]
    if "authentication" in value:
        import capo_mailmanager.types.relay_authentication

        out["Authentication"] = (
            capo_mailmanager.types.relay_authentication.serialize_aws_json_1_0(
                value["authentication"]
            )
        )
    if "created_timestamp" in value:
        import capo_mailmanager.types._prelude.timestamp

        out["CreatedTimestamp"] = (
            capo_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
                value["created_timestamp"]
            )
        )
    if "last_modified_timestamp" in value:
        import capo_mailmanager.types._prelude.timestamp

        out["LastModifiedTimestamp"] = (
            capo_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
                value["last_modified_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRelayResponse:
    out: GetRelayResponse = {}  # type: ignore[typeddict-item]
    if data.get("RelayId") is not None:
        out["relay_id"] = data["RelayId"]
    else:
        out["relay_id"] = ""
    if data.get("RelayArn") is not None:
        out["relay_arn"] = data["RelayArn"]
    if data.get("RelayName") is not None:
        out["relay_name"] = data["RelayName"]
    if data.get("ServerName") is not None:
        out["server_name"] = data["ServerName"]
    if data.get("ServerPort") is not None:
        out["server_port"] = data["ServerPort"]
    if data.get("Authentication") is not None:
        import capo_mailmanager.types.relay_authentication

        out["authentication"] = (
            capo_mailmanager.types.relay_authentication.deserialize_aws_json_1_0(
                data["Authentication"]
            )
        )
    if data.get("CreatedTimestamp") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["created_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    if data.get("LastModifiedTimestamp") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["last_modified_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["LastModifiedTimestamp"]
            )
        )
    return out
