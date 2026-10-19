"""Generated from Smithy shape ``com.amazonaws.athena#GetSessionEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_athena.types.string
    import capo_athena.types.timestamp


class GetSessionEndpointResponse(TypedDict, closed=True):
    endpoint_url: "capo_athena.types.string.String"
    """<p>The endpoint for connecting to the session.</p>"""
    auth_token: "capo_athena.types.string.String"
    """<p>Authentication token for the connection</p>"""
    auth_token_expiration_time: "capo_athena.types.timestamp.Timestamp"
    """<p>Expiration time of the auth token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSessionEndpointResponse) -> dict:
    out: dict = {}
    out["EndpointUrl"] = value["endpoint_url"]
    out["AuthToken"] = value["auth_token"]
    import capo_athena.types.timestamp

    out["AuthTokenExpirationTime"] = capo_athena.types.timestamp.serialize_aws_json_1_1(
        value["auth_token_expiration_time"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSessionEndpointResponse:
    out: GetSessionEndpointResponse = {}  # type: ignore[typeddict-item]
    if data.get("EndpointUrl") is not None:
        out["endpoint_url"] = data["EndpointUrl"]
    else:
        out["endpoint_url"] = ""
    if data.get("AuthToken") is not None:
        out["auth_token"] = data["AuthToken"]
    else:
        out["auth_token"] = ""
    if data.get("AuthTokenExpirationTime") is not None:
        import capo_athena.types.timestamp

        out["auth_token_expiration_time"] = (
            capo_athena.types.timestamp.deserialize_aws_json_1_1(
                data["AuthTokenExpirationTime"]
            )
        )
    else:
        import datetime

        out["auth_token_expiration_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
