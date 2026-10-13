"""Generated from Smithy shape ``com.amazonaws.datazone#PhysicalEndpoint``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.aws_location
    import capo_datazone.types.glue_connection
    import capo_datazone.types.glue_connection_names
    import capo_datazone.types.protocol


class PhysicalEndpoint(TypedDict, closed=True):
    aws_location: NotRequired["capo_datazone.types.aws_location.AwsLocation"]
    """<p>The location of a connection.</p>"""
    glue_connection_name: NotRequired["str"]
    """<p>The Amazon Web Services Glue connection name.</p>"""
    glue_connection_names: NotRequired[
        "capo_datazone.types.glue_connection_names.GlueConnectionNames"
    ]
    """<p>The Amazon Web Services Glue connection names in the physical endpoint.</p>"""
    glue_connection: NotRequired["capo_datazone.types.glue_connection.GlueConnection"]
    """<p>The Amazon Web Services Glue connection.</p>"""
    enable_trusted_identity_propagation: NotRequired["bool"]
    """<p>Specified whether trusted identity propagation for the connection is enabled.</p>"""
    host: NotRequired["str"]
    """<p>The host in the physical endpoints of a connection.</p>"""
    port: NotRequired["int"]
    """<p>The port in the physical endpoints of a connection.</p>"""
    protocol: NotRequired["capo_datazone.types.protocol.Protocol"]
    """<p>The protocol in the physical endpoints of a connection.</p>"""
    stage: NotRequired["str"]
    """<p>The stage in the physical endpoints of a connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PhysicalEndpoint) -> dict:
    out: dict = {}
    if "aws_location" in value:
        import capo_datazone.types.aws_location

        out["awsLocation"] = capo_datazone.types.aws_location.serialize_json(
            value["aws_location"]
        )
    if "glue_connection_name" in value:
        out["glueConnectionName"] = value["glue_connection_name"]
    if "glue_connection_names" in value:
        import capo_datazone.types.glue_connection_names

        out["glueConnectionNames"] = (
            capo_datazone.types.glue_connection_names.serialize_json(
                value["glue_connection_names"]
            )
        )
    if "glue_connection" in value:
        import capo_datazone.types.glue_connection

        out["glueConnection"] = capo_datazone.types.glue_connection.serialize_json(
            value["glue_connection"]
        )
    if "enable_trusted_identity_propagation" in value:
        out["enableTrustedIdentityPropagation"] = value[
            "enable_trusted_identity_propagation"
        ]
    if "host" in value:
        out["host"] = value["host"]
    if "port" in value:
        out["port"] = value["port"]
    if "protocol" in value:
        import capo_datazone.types.protocol

        out["protocol"] = capo_datazone.types.protocol.serialize_json(value["protocol"])
    if "stage" in value:
        out["stage"] = value["stage"]
    return out


def deserialize_json(data: dict) -> PhysicalEndpoint:
    out: PhysicalEndpoint = {}  # type: ignore[typeddict-item]
    if data.get("awsLocation") is not None:
        import capo_datazone.types.aws_location

        out["aws_location"] = capo_datazone.types.aws_location.deserialize_json(
            data["awsLocation"]
        )
    if data.get("glueConnectionName") is not None:
        out["glue_connection_name"] = data["glueConnectionName"]
    if data.get("glueConnectionNames") is not None:
        import capo_datazone.types.glue_connection_names

        out["glue_connection_names"] = (
            capo_datazone.types.glue_connection_names.deserialize_json(
                data["glueConnectionNames"]
            )
        )
    if data.get("glueConnection") is not None:
        import capo_datazone.types.glue_connection

        out["glue_connection"] = capo_datazone.types.glue_connection.deserialize_json(
            data["glueConnection"]
        )
    if data.get("enableTrustedIdentityPropagation") is not None:
        out["enable_trusted_identity_propagation"] = data[
            "enableTrustedIdentityPropagation"
        ]
    if data.get("host") is not None:
        out["host"] = data["host"]
    if data.get("port") is not None:
        out["port"] = data["port"]
    if data.get("protocol") is not None:
        import capo_datazone.types.protocol

        out["protocol"] = capo_datazone.types.protocol.deserialize_json(
            data["protocol"]
        )
    if data.get("stage") is not None:
        out["stage"] = data["stage"]
    return out


def redact_sensitive(value: PhysicalEndpoint) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "glue_connection" in value:
        import capo_datazone.types.glue_connection

        out["glue_connection"] = capo_datazone.types.glue_connection.redact_sensitive(
            value["glue_connection"]
        )
    return out
