"""Generated from Smithy shape ``com.amazonaws.interconnect#CreateConnectionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_interconnect.types.connection


class CreateConnectionResponse(TypedDict, closed=True):
    connection: NotRequired["capo_interconnect.types.connection.Connection"]
    """<p>The resulting <a>Connection</a>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateConnectionResponse) -> dict:
    out: dict = {}
    if "connection" in value:
        import capo_interconnect.types.connection

        out["connection"] = capo_interconnect.types.connection.serialize_aws_json_1_0(
            value["connection"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateConnectionResponse:
    out: CreateConnectionResponse = {}  # type: ignore[typeddict-item]
    if data.get("connection") is not None:
        import capo_interconnect.types.connection

        out["connection"] = capo_interconnect.types.connection.deserialize_aws_json_1_0(
            data["connection"]
        )
    return out


def redact_sensitive(value: CreateConnectionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "connection" in value:
        import capo_interconnect.types.connection

        out["connection"] = capo_interconnect.types.connection.redact_sensitive(
            value["connection"]
        )
    return out
