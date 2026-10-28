"""Generated from Smithy shape ``com.amazonaws.groundstation#ConfigTypeData``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_groundstation.errors import DeserializationError, SerializationError
from capo_groundstation.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_groundstation.types.antenna_downlink_config
    import capo_groundstation.types.antenna_downlink_demod_decode_config
    import capo_groundstation.types.antenna_uplink_config
    import capo_groundstation.types.dataflow_endpoint_config
    import capo_groundstation.types.s3_recording_config
    import capo_groundstation.types.telemetry_sink_config
    import capo_groundstation.types.tracking_config
    import capo_groundstation.types.uplink_echo_config


class ConfigTypeDataAntennaDownlinkConfigMember(TypedDict, closed=True):
    antennaDownlinkConfig: (
        "capo_groundstation.types.antenna_downlink_config.AntennaDownlinkConfig"
    )


class ConfigTypeDataTrackingConfigMember(TypedDict, closed=True):
    trackingConfig: "capo_groundstation.types.tracking_config.TrackingConfig"


class ConfigTypeDataDataflowEndpointConfigMember(TypedDict, closed=True):
    dataflowEndpointConfig: (
        "capo_groundstation.types.dataflow_endpoint_config.DataflowEndpointConfig"
    )


class ConfigTypeDataAntennaDownlinkDemodDecodeConfigMember(TypedDict, closed=True):
    antennaDownlinkDemodDecodeConfig: "capo_groundstation.types.antenna_downlink_demod_decode_config.AntennaDownlinkDemodDecodeConfig"


class ConfigTypeDataAntennaUplinkConfigMember(TypedDict, closed=True):
    antennaUplinkConfig: (
        "capo_groundstation.types.antenna_uplink_config.AntennaUplinkConfig"
    )


class ConfigTypeDataUplinkEchoConfigMember(TypedDict, closed=True):
    uplinkEchoConfig: "capo_groundstation.types.uplink_echo_config.UplinkEchoConfig"


class ConfigTypeDataS3RecordingConfigMember(TypedDict, closed=True):
    s3RecordingConfig: "capo_groundstation.types.s3_recording_config.S3RecordingConfig"


class ConfigTypeDataTelemetrySinkConfigMember(TypedDict, closed=True):
    telemetrySinkConfig: (
        "capo_groundstation.types.telemetry_sink_config.TelemetrySinkConfig"
    )


ConfigTypeData: TypeAlias = (
    ConfigTypeDataAntennaDownlinkConfigMember
    | ConfigTypeDataTrackingConfigMember
    | ConfigTypeDataDataflowEndpointConfigMember
    | ConfigTypeDataAntennaDownlinkDemodDecodeConfigMember
    | ConfigTypeDataAntennaUplinkConfigMember
    | ConfigTypeDataUplinkEchoConfigMember
    | ConfigTypeDataS3RecordingConfigMember
    | ConfigTypeDataTelemetrySinkConfigMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ConfigTypeData) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ConfigTypeData: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "antennaDownlinkConfig" in value:
        import capo_groundstation.types.antenna_downlink_config

        return {
            "antennaDownlinkConfig": capo_groundstation.types.antenna_downlink_config.serialize_json(
                value["antennaDownlinkConfig"]
            )
        }
    elif "trackingConfig" in value:
        import capo_groundstation.types.tracking_config

        return {
            "trackingConfig": capo_groundstation.types.tracking_config.serialize_json(
                value["trackingConfig"]
            )
        }
    elif "dataflowEndpointConfig" in value:
        import capo_groundstation.types.dataflow_endpoint_config

        return {
            "dataflowEndpointConfig": capo_groundstation.types.dataflow_endpoint_config.serialize_json(
                value["dataflowEndpointConfig"]
            )
        }
    elif "antennaDownlinkDemodDecodeConfig" in value:
        import capo_groundstation.types.antenna_downlink_demod_decode_config

        return {
            "antennaDownlinkDemodDecodeConfig": capo_groundstation.types.antenna_downlink_demod_decode_config.serialize_json(
                value["antennaDownlinkDemodDecodeConfig"]
            )
        }
    elif "antennaUplinkConfig" in value:
        import capo_groundstation.types.antenna_uplink_config

        return {
            "antennaUplinkConfig": capo_groundstation.types.antenna_uplink_config.serialize_json(
                value["antennaUplinkConfig"]
            )
        }
    elif "uplinkEchoConfig" in value:
        import capo_groundstation.types.uplink_echo_config

        return {
            "uplinkEchoConfig": capo_groundstation.types.uplink_echo_config.serialize_json(
                value["uplinkEchoConfig"]
            )
        }
    elif "s3RecordingConfig" in value:
        import capo_groundstation.types.s3_recording_config

        return {
            "s3RecordingConfig": capo_groundstation.types.s3_recording_config.serialize_json(
                value["s3RecordingConfig"]
            )
        }
    elif "telemetrySinkConfig" in value:
        import capo_groundstation.types.telemetry_sink_config

        return {
            "telemetrySinkConfig": capo_groundstation.types.telemetry_sink_config.serialize_json(
                value["telemetrySinkConfig"]
            )
        }
    else:
        raise SerializationError("ConfigTypeData: no variant present")


def deserialize_json(data: dict) -> ConfigTypeData:
    if data.get("antennaDownlinkConfig") is not None:
        import capo_groundstation.types.antenna_downlink_config

        return {
            "antennaDownlinkConfig": capo_groundstation.types.antenna_downlink_config.deserialize_json(
                data["antennaDownlinkConfig"]
            )
        }
    elif data.get("trackingConfig") is not None:
        import capo_groundstation.types.tracking_config

        return {
            "trackingConfig": capo_groundstation.types.tracking_config.deserialize_json(
                data["trackingConfig"]
            )
        }
    elif data.get("dataflowEndpointConfig") is not None:
        import capo_groundstation.types.dataflow_endpoint_config

        return {
            "dataflowEndpointConfig": capo_groundstation.types.dataflow_endpoint_config.deserialize_json(
                data["dataflowEndpointConfig"]
            )
        }
    elif data.get("antennaDownlinkDemodDecodeConfig") is not None:
        import capo_groundstation.types.antenna_downlink_demod_decode_config

        return {
            "antennaDownlinkDemodDecodeConfig": capo_groundstation.types.antenna_downlink_demod_decode_config.deserialize_json(
                data["antennaDownlinkDemodDecodeConfig"]
            )
        }
    elif data.get("antennaUplinkConfig") is not None:
        import capo_groundstation.types.antenna_uplink_config

        return {
            "antennaUplinkConfig": capo_groundstation.types.antenna_uplink_config.deserialize_json(
                data["antennaUplinkConfig"]
            )
        }
    elif data.get("uplinkEchoConfig") is not None:
        import capo_groundstation.types.uplink_echo_config

        return {
            "uplinkEchoConfig": capo_groundstation.types.uplink_echo_config.deserialize_json(
                data["uplinkEchoConfig"]
            )
        }
    elif data.get("s3RecordingConfig") is not None:
        import capo_groundstation.types.s3_recording_config

        return {
            "s3RecordingConfig": capo_groundstation.types.s3_recording_config.deserialize_json(
                data["s3RecordingConfig"]
            )
        }
    elif data.get("telemetrySinkConfig") is not None:
        import capo_groundstation.types.telemetry_sink_config

        return {
            "telemetrySinkConfig": capo_groundstation.types.telemetry_sink_config.deserialize_json(
                data["telemetrySinkConfig"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ConfigTypeData: no recognized variant key")
