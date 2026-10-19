"""Generated from Smithy shape ``com.amazonaws.applicationsignals#CreateInstrumentationConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_application_signals.types.capture_configuration
    import capo_application_signals.types.dynamic_instrumentation_attribute_filters
    import capo_application_signals.types.dynamic_instrumentation_signal_type
    import capo_application_signals.types.instrumentation_configuration_arn
    import capo_application_signals.types.instrumentation_type
    import capo_application_signals.types.location


class CreateInstrumentationConfigurationResponse(TypedDict, closed=True):
    instrumentation_type: (
        "capo_application_signals.types.instrumentation_type.InstrumentationType"
    )
    """<p>The type of instrumentation that was created, echoed from the request.</p>"""
    service: "str"
    """<p>The service name for the instrumentation configuration, echoed from the request.</p>"""
    environment: "str"
    """<p>The environment for the instrumentation configuration, echoed from the request.</p>"""
    signal_type: "capo_application_signals.types.dynamic_instrumentation_signal_type.DynamicInstrumentationSignalType"
    """<p>The telemetry signal type for the instrumentation configuration, echoed from the request.</p>"""
    location: "capo_application_signals.types.location.Location"
    """<p>The location where instrumentation is applied, echoed from the request.</p>"""
    location_hash: "str"
    """<p>A stable hash computed from the location that uniquely identifies this instrumentation point within the service, environment, and signal type.</p>"""
    description: NotRequired["str"]
    """<p>The optional description that was stored with the instrumentation configuration.</p>"""
    expires_at: NotRequired["datetime.datetime"]
    """<p>The timestamp after which this configuration is no longer served to clients. Present only for <code>BREAKPOINT</code> configurations; <code>PROBE</code> configurations do not expire.</p>"""
    attribute_filters: NotRequired[
        "capo_application_signals.types.dynamic_instrumentation_attribute_filters.DynamicInstrumentationAttributeFilters"
    ]
    """<p>The attribute filters returned with the configuration so SDKs can perform client-side targeting.</p>"""
    capture_configuration: (
        "capo_application_signals.types.capture_configuration.CaptureConfiguration"
    )
    """<p>The capture settings that were stored for this instrumentation configuration.</p>"""
    created_at: "datetime.datetime"
    """<p>The server-generated creation timestamp for this instrumentation configuration.</p>"""
    arn: "capo_application_signals.types.instrumentation_configuration_arn.InstrumentationConfigurationArn"
    """ARN for the created instrumentation configuration"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateInstrumentationConfigurationResponse) -> dict:
    out: dict = {}
    import capo_application_signals.types.instrumentation_type

    out["InstrumentationType"] = (
        capo_application_signals.types.instrumentation_type.serialize_json(
            value["instrumentation_type"]
        )
    )
    out["Service"] = value["service"]
    out["Environment"] = value["environment"]
    import capo_application_signals.types.dynamic_instrumentation_signal_type

    out["SignalType"] = (
        capo_application_signals.types.dynamic_instrumentation_signal_type.serialize_json(
            value["signal_type"]
        )
    )
    import capo_application_signals.types.location

    out["Location"] = capo_application_signals.types.location.serialize_json(
        value["location"]
    )
    out["LocationHash"] = value["location_hash"]
    if "description" in value:
        out["Description"] = value["description"]
    if "expires_at" in value:
        import capo_application_signals.types._prelude.timestamp

        out["ExpiresAt"] = (
            capo_application_signals.types._prelude.timestamp.serialize_json(
                value["expires_at"]
            )
        )
    if "attribute_filters" in value:
        import capo_application_signals.types.dynamic_instrumentation_attribute_filters

        out["AttributeFilters"] = (
            capo_application_signals.types.dynamic_instrumentation_attribute_filters.serialize_json(
                value["attribute_filters"]
            )
        )
    import capo_application_signals.types.capture_configuration

    out["CaptureConfiguration"] = (
        capo_application_signals.types.capture_configuration.serialize_json(
            value["capture_configuration"]
        )
    )
    import capo_application_signals.types._prelude.timestamp

    out["CreatedAt"] = capo_application_signals.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    out["ARN"] = value["arn"]
    return out


def deserialize_json(data: dict) -> CreateInstrumentationConfigurationResponse:
    out: CreateInstrumentationConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("InstrumentationType") is not None:
        import capo_application_signals.types.instrumentation_type

        out["instrumentation_type"] = (
            capo_application_signals.types.instrumentation_type.deserialize_json(
                data["InstrumentationType"]
            )
        )
    else:
        import typing

        out["instrumentation_type"] = typing.cast(
            "capo_application_signals.types.instrumentation_type.InstrumentationType",
            "",
        )
    if data.get("Service") is not None:
        out["service"] = data["Service"]
    else:
        out["service"] = ""
    if data.get("Environment") is not None:
        out["environment"] = data["Environment"]
    else:
        out["environment"] = ""
    if data.get("SignalType") is not None:
        import capo_application_signals.types.dynamic_instrumentation_signal_type

        out["signal_type"] = (
            capo_application_signals.types.dynamic_instrumentation_signal_type.deserialize_json(
                data["SignalType"]
            )
        )
    else:
        import typing

        out["signal_type"] = typing.cast(
            "capo_application_signals.types.dynamic_instrumentation_signal_type.DynamicInstrumentationSignalType",
            "",
        )
    if data.get("Location") is not None:
        import capo_application_signals.types.location

        out["location"] = capo_application_signals.types.location.deserialize_json(
            data["Location"]
        )
    else:
        import capo_application_signals.types._unknown

        out["location"] = capo_application_signals.types._unknown.UnknownUnionMember("")
    if data.get("LocationHash") is not None:
        out["location_hash"] = data["LocationHash"]
    else:
        out["location_hash"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ExpiresAt") is not None:
        import capo_application_signals.types._prelude.timestamp

        out["expires_at"] = (
            capo_application_signals.types._prelude.timestamp.deserialize_json(
                data["ExpiresAt"]
            )
        )
    if data.get("AttributeFilters") is not None:
        import capo_application_signals.types.dynamic_instrumentation_attribute_filters

        out["attribute_filters"] = (
            capo_application_signals.types.dynamic_instrumentation_attribute_filters.deserialize_json(
                data["AttributeFilters"]
            )
        )
    if data.get("CaptureConfiguration") is not None:
        import capo_application_signals.types.capture_configuration

        out["capture_configuration"] = (
            capo_application_signals.types.capture_configuration.deserialize_json(
                data["CaptureConfiguration"]
            )
        )
    else:
        import capo_application_signals.types._unknown

        out["capture_configuration"] = (
            capo_application_signals.types._unknown.UnknownUnionMember("")
        )
    if data.get("CreatedAt") is not None:
        import capo_application_signals.types._prelude.timestamp

        out["created_at"] = (
            capo_application_signals.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("ARN") is not None:
        out["arn"] = data["ARN"]
    else:
        out["arn"] = ""
    return out
