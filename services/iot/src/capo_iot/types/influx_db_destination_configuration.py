"""Generated from Smithy shape ``com.amazonaws.iot#InfluxDBDestinationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.influx_db_secret_id
    import capo_iot.types.influx_db_secret_key
    import capo_iot.types.influx_db_secret_type
    import capo_iot.types.influx_db_version
    import capo_iot.types.url


class InfluxDBDestinationConfiguration(TypedDict, closed=True):
    endpoint: "capo_iot.types.url.Url"
    """<p>The URL of the InfluxDB instance to write to.</p>"""
    influx_db_version: "capo_iot.types.influx_db_version.InfluxDBVersion"
    """<p>The major version of the InfluxDB instance. Valid values are <code>V2</code> and <code>V3</code>.</p>"""
    secret_id: "capo_iot.types.influx_db_secret_id.InfluxDBSecretId"
    """<p>The ARN or name of the Amazon Web Services Secrets Manager secret that contains the InfluxDB API token.</p>"""
    secret_type: NotRequired["capo_iot.types.influx_db_secret_type.InfluxDBSecretType"]
    """<p>The type of the secret that contains the InfluxDB API token. Valid values are <code>SecretString</code> and <code>SecretBinary</code>.</p> <p>If omitted, IoT reads the secret as a string.</p>"""
    secret_key: NotRequired["capo_iot.types.influx_db_secret_key.InfluxDBSecretKey"]
    """<p>The key to read from the secret value when the secret contains a JSON object. If omitted, IoT uses the entire secret value as the InfluxDB API token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InfluxDBDestinationConfiguration) -> dict:
    out: dict = {}
    out["endpoint"] = value["endpoint"]
    import capo_iot.types.influx_db_version

    out["influxDBVersion"] = capo_iot.types.influx_db_version.serialize_json(
        value["influx_db_version"]
    )
    out["secretId"] = value["secret_id"]
    if "secret_type" in value:
        import capo_iot.types.influx_db_secret_type

        out["secretType"] = capo_iot.types.influx_db_secret_type.serialize_json(
            value["secret_type"]
        )
    if "secret_key" in value:
        out["secretKey"] = value["secret_key"]
    return out


def deserialize_json(data: dict) -> InfluxDBDestinationConfiguration:
    out: InfluxDBDestinationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("endpoint") is not None:
        out["endpoint"] = data["endpoint"]
    else:
        out["endpoint"] = ""
    if data.get("influxDBVersion") is not None:
        import capo_iot.types.influx_db_version

        out["influx_db_version"] = capo_iot.types.influx_db_version.deserialize_json(
            data["influxDBVersion"]
        )
    else:
        import typing

        out["influx_db_version"] = typing.cast(
            "capo_iot.types.influx_db_version.InfluxDBVersion", ""
        )
    if data.get("secretId") is not None:
        out["secret_id"] = data["secretId"]
    else:
        out["secret_id"] = ""
    if data.get("secretType") is not None:
        import capo_iot.types.influx_db_secret_type

        out["secret_type"] = capo_iot.types.influx_db_secret_type.deserialize_json(
            data["secretType"]
        )
    if data.get("secretKey") is not None:
        out["secret_key"] = data["secretKey"]
    return out
