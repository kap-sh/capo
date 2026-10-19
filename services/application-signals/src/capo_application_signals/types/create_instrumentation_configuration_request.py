"""Generated from Smithy shape ``com.amazonaws.applicationsignals#CreateInstrumentationConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_application_signals.types.capture_configuration
    import capo_application_signals.types.dynamic_instrumentation_attribute_filters
    import capo_application_signals.types.dynamic_instrumentation_signal_type
    import capo_application_signals.types.instrumentation_type
    import capo_application_signals.types.location
    import capo_application_signals.types.tag_list


class CreateInstrumentationConfigurationRequest(TypedDict, closed=True):
    instrumentation_type: (
        "capo_application_signals.types.instrumentation_type.InstrumentationType"
    )
    """Type of instrumentation: BREAKPOINT (temporary) or PROBE (permanent)"""
    service: "str"
    """<p>The name of the service to instrument. This should match the <code>service.name</code> resource attribute reported by the application.</p>"""
    environment: "str"
    """<p>The environment that the service is running in, such as <code>eks:cluster-prod/namespace</code> or <code>ec2:production</code>.</p>"""
    signal_type: "capo_application_signals.types.dynamic_instrumentation_signal_type.DynamicInstrumentationSignalType"
    """<p>The telemetry signal type to emit for this instrumentation. The supported value is <code>SNAPSHOT</code>.</p>"""
    location: "capo_application_signals.types.location.Location"
    """<p>The location where instrumentation should be applied. Specify a <code>CodeLocation</code> for code-level instrumentation.</p>"""
    description: NotRequired["str"]
    """<p>An optional short description (up to 50 characters) that explains the purpose of this instrumentation.</p>"""
    expires_at: NotRequired["datetime.datetime"]
    """For BREAKPOINT: optional, defaults to 24 hours, must be between 5 min and 24 hours. For PROBE: not supported. PROBE configurations are permanent and persist until explicitly deleted."""
    attribute_filters: NotRequired[
        "capo_application_signals.types.dynamic_instrumentation_attribute_filters.DynamicInstrumentationAttributeFilters"
    ]
    """<p>Client-side filters that target specific instances. Each object in the array is AND-matched on its keys, and multiple objects are OR-matched to decide where to apply the instrumentation.</p>"""
    capture_configuration: (
        "capo_application_signals.types.capture_configuration.CaptureConfiguration"
    )
    """<p>Specifies what to capture when the instrumentation point is hit. Specify <code>CodeCapture</code> for code-level capture settings.</p>"""
    tags: NotRequired["capo_application_signals.types.tag_list.TagList"]
    """<p>An optional list of key-value pairs to associate with the instrumentation configuration. Tags can help you organize and categorize your resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateInstrumentationConfigurationRequest) -> dict:
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
    if "tags" in value:
        import capo_application_signals.types.tag_list

        out["Tags"] = capo_application_signals.types.tag_list.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateInstrumentationConfigurationRequest:
    out: CreateInstrumentationConfigurationRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("Tags") is not None:
        import capo_application_signals.types.tag_list

        out["tags"] = capo_application_signals.types.tag_list.deserialize_json(
            data["Tags"]
        )
    return out
