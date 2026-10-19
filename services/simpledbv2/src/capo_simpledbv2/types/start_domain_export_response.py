"""Generated from Smithy shape ``com.amazonaws.simpledbv2#StartDomainExportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_simpledbv2.types.export_arn
    import capo_simpledbv2.types.idempotency_token
    import capo_simpledbv2.types.requested_at


class StartDomainExportResponse(TypedDict, closed=True):
    client_token: "capo_simpledbv2.types.idempotency_token.IdempotencyToken"
    """The client token that was provided in the request."""
    export_arn: "capo_simpledbv2.types.export_arn.ExportArn"
    """Unique ARN identifier of the export."""
    requested_at: "capo_simpledbv2.types.requested_at.RequestedAt"
    """Timestamp when the export request was received by the service."""


# --- restJson1 ser/de ---
def serialize_json(value: StartDomainExportResponse) -> dict:
    out: dict = {}
    out["clientToken"] = value["client_token"]
    out["exportArn"] = value["export_arn"]
    import capo_simpledbv2.types.requested_at

    out["requestedAt"] = capo_simpledbv2.types.requested_at.serialize_json(
        value["requested_at"]
    )
    return out


def deserialize_json(data: dict) -> StartDomainExportResponse:
    out: StartDomainExportResponse = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        out["client_token"] = ""
    if data.get("exportArn") is not None:
        out["export_arn"] = data["exportArn"]
    else:
        out["export_arn"] = ""
    if data.get("requestedAt") is not None:
        import capo_simpledbv2.types.requested_at

        out["requested_at"] = capo_simpledbv2.types.requested_at.deserialize_json(
            data["requestedAt"]
        )
    else:
        import datetime

        out["requested_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
