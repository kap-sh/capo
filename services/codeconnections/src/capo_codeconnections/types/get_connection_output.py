"""Generated from Smithy shape ``com.amazonaws.codeconnections#GetConnectionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeconnections.types.connection


class GetConnectionOutput(TypedDict, closed=True):
    connection: NotRequired["capo_codeconnections.types.connection.Connection"]
    """<p>The connection details, such as status, owner, and provider type.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetConnectionOutput) -> dict:
    out: dict = {}
    if "connection" in value:
        import capo_codeconnections.types.connection

        out["Connection"] = (
            capo_codeconnections.types.connection.serialize_aws_json_1_0(
                value["connection"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetConnectionOutput:
    out: GetConnectionOutput = {}  # type: ignore[typeddict-item]
    if data.get("Connection") is not None:
        import capo_codeconnections.types.connection

        out["connection"] = (
            capo_codeconnections.types.connection.deserialize_aws_json_1_0(
                data["Connection"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetConnectionOutput) -> dict:
    out: dict = {}
    if "connection" in value:
        import capo_codeconnections.types.connection

        out["Connection"] = capo_codeconnections.types.connection.serialize_cbor(
            value["connection"]
        )
    return out


def deserialize_cbor(data: dict) -> GetConnectionOutput:
    out: GetConnectionOutput = {}  # type: ignore[typeddict-item]
    if data.get("Connection") is not None:
        import capo_codeconnections.types.connection

        out["connection"] = capo_codeconnections.types.connection.deserialize_cbor(
            data["Connection"]
        )
    return out
