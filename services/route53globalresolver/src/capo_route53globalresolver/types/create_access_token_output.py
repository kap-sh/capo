"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#CreateAccessTokenOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.access_token_value
    import capo_route53globalresolver.types.client_token
    import capo_route53globalresolver.types.iso8601_time_string
    import capo_route53globalresolver.types.resource_arn
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.resource_name_short
    import capo_route53globalresolver.types.token_status


class CreateAccessTokenOutput(TypedDict, closed=True):
    id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier for the access token.</p>"""
    arn: "capo_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the access token.</p>"""
    client_token: NotRequired[
        "capo_route53globalresolver.types.client_token.ClientToken"
    ]
    """<p>The unique string that identifies the request and ensures idempotency.</p>"""
    created_at: "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    """<p>The date and time when the access token was created.</p>"""
    dns_view_id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the DNS view associated with this access token.</p>"""
    expires_at: "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    """<p>The date and time when the access token expires.</p>"""
    name: NotRequired[
        "capo_route53globalresolver.types.resource_name_short.ResourceNameShort"
    ]
    """<p>The name of the access token.</p>"""
    status: "capo_route53globalresolver.types.token_status.TokenStatus"
    """<p>The operational status of the access token.</p>"""
    value: "capo_route53globalresolver.types.access_token_value.AccessTokenValue"
    """<p>The access token value. This token should be included in DoH and DoT requests for authentication. Keep this value secure as it provides access to your Route 53 Global Resolver.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAccessTokenOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import capo_route53globalresolver.types.iso8601_time_string

    out["createdAt"] = (
        capo_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["created_at"]
        )
    )
    out["dnsViewId"] = value["dns_view_id"]
    import capo_route53globalresolver.types.iso8601_time_string

    out["expiresAt"] = (
        capo_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["expires_at"]
        )
    )
    if "name" in value:
        out["name"] = value["name"]
    import capo_route53globalresolver.types.token_status

    out["status"] = capo_route53globalresolver.types.token_status.serialize_json(
        value["status"]
    )
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> CreateAccessTokenOutput:
    out: CreateAccessTokenOutput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("createdAt") is not None:
        import capo_route53globalresolver.types.iso8601_time_string

        out["created_at"] = (
            capo_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("dnsViewId") is not None:
        out["dns_view_id"] = data["dnsViewId"]
    else:
        out["dns_view_id"] = ""
    if data.get("expiresAt") is not None:
        import capo_route53globalresolver.types.iso8601_time_string

        out["expires_at"] = (
            capo_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["expiresAt"]
            )
        )
    else:
        import datetime

        out["expires_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("status") is not None:
        import capo_route53globalresolver.types.token_status

        out["status"] = capo_route53globalresolver.types.token_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_route53globalresolver.types.token_status.TokenStatus", ""
        )
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out


def redact_sensitive(value: CreateAccessTokenOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "value" in value:
        out["value"] = "*** Sensitive Data Redacted ***"
    return out
