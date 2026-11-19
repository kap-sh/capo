"""Generated from Smithy shape ``com.amazonaws.servicecatalog#SourceConnection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import capo_service_catalog.types.source_connection_parameters
    import capo_service_catalog.types.source_type


class SourceConnection(TypedDict, closed=True):
    type: NotRequired["capo_service_catalog.types.source_type.SourceType"]
    """<p>The only supported <code>SourceConnection</code> type is Codestar. </p>"""
    connection_parameters: "capo_service_catalog.types.source_connection_parameters.SourceConnectionParameters"
    """<p>The connection details based on the connection <code>Type</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceConnection) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_service_catalog.types.source_type

        out["Type"] = capo_service_catalog.types.source_type.serialize_aws_json_1_1(
            value["type"]
        )
    import capo_service_catalog.types.source_connection_parameters

    out["ConnectionParameters"] = (
        capo_service_catalog.types.source_connection_parameters.serialize_aws_json_1_1(
            value["connection_parameters"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceConnection:
    out: SourceConnection = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_service_catalog.types.source_type

        out["type"] = capo_service_catalog.types.source_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if data.get("ConnectionParameters") is not None:
        import capo_service_catalog.types.source_connection_parameters

        out["connection_parameters"] = (
            capo_service_catalog.types.source_connection_parameters.deserialize_aws_json_1_1(
                data["ConnectionParameters"]
            )
        )
    else:
        raise DeserializationError("SourceConnection.connection_parameters required")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SourceConnection) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_service_catalog.types.source_type

        out["Type"] = capo_service_catalog.types.source_type.serialize_cbor(
            value["type"]
        )
    import capo_service_catalog.types.source_connection_parameters

    out["ConnectionParameters"] = (
        capo_service_catalog.types.source_connection_parameters.serialize_cbor(
            value["connection_parameters"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> SourceConnection:
    out: SourceConnection = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_service_catalog.types.source_type

        out["type"] = capo_service_catalog.types.source_type.deserialize_cbor(
            data["Type"]
        )
    if data.get("ConnectionParameters") is not None:
        import capo_service_catalog.types.source_connection_parameters

        out["connection_parameters"] = (
            capo_service_catalog.types.source_connection_parameters.deserialize_cbor(
                data["ConnectionParameters"]
            )
        )
    else:
        raise DeserializationError("SourceConnection.connection_parameters required")
    return out
