"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#DeleteAccessTokenOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.iso8601_time_string
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.token_status


class DeleteAccessTokenOutput(TypedDict, closed=True):
    id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the deleted access token.</p>"""
    status: "capo_route53globalresolver.types.token_status.TokenStatus"
    """<p>The final status of the deleted access token.</p>"""
    deleted_at: "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    """<p>The date and time when the access token was deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAccessTokenOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import capo_route53globalresolver.types.token_status

    out["status"] = capo_route53globalresolver.types.token_status.serialize_json(
        value["status"]
    )
    import capo_route53globalresolver.types.iso8601_time_string

    out["deletedAt"] = (
        capo_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["deleted_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteAccessTokenOutput:
    out: DeleteAccessTokenOutput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
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
    if data.get("deletedAt") is not None:
        import capo_route53globalresolver.types.iso8601_time_string

        out["deleted_at"] = (
            capo_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["deletedAt"]
            )
        )
    else:
        import datetime

        out["deleted_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
