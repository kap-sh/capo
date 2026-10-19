"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ListInstrumentationConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_application_signals.types.instrumentation_type
    import capo_application_signals.types.next_token


class ListInstrumentationConfigurationsRequest(TypedDict, closed=True):
    service: "str"
    """<p>The name of the service to retrieve instrumentation configurations for.</p>"""
    environment: "str"
    """<p>The environment that the service is running in.</p>"""
    instrumentation_type: (
        "capo_application_signals.types.instrumentation_type.InstrumentationType"
    )
    """Type of instrumentation configuration (BREAKPOINT or PROBE). Required to determine which backing store to query."""
    synced_at: NotRequired["datetime.datetime"]
    """<p>The timestamp from the last successful sync. When provided, the response returns <code>Changed</code> as <code>false</code> if nothing is new since this time, or returns the latest configurations when changes exist.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of configurations to return in one call. The default is 50 and the maximum is 100.</p>"""
    next_token: NotRequired["capo_application_signals.types.next_token.NextToken"]
    """<p>Use the token returned by a previous call to retrieve the next page of configurations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInstrumentationConfigurationsRequest) -> dict:
    out: dict = {}
    out["Service"] = value["service"]
    out["Environment"] = value["environment"]
    import capo_application_signals.types.instrumentation_type

    out["InstrumentationType"] = (
        capo_application_signals.types.instrumentation_type.serialize_json(
            value["instrumentation_type"]
        )
    )
    if "synced_at" in value:
        import capo_application_signals.types._prelude.timestamp

        out["SyncedAt"] = (
            capo_application_signals.types._prelude.timestamp.serialize_json(
                value["synced_at"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInstrumentationConfigurationsRequest:
    out: ListInstrumentationConfigurationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Service") is not None:
        out["service"] = data["Service"]
    else:
        raise DeserializationError(
            "ListInstrumentationConfigurationsRequest.service required"
        )
    if data.get("Environment") is not None:
        out["environment"] = data["Environment"]
    else:
        raise DeserializationError(
            "ListInstrumentationConfigurationsRequest.environment required"
        )
    if data.get("InstrumentationType") is not None:
        import capo_application_signals.types.instrumentation_type

        out["instrumentation_type"] = (
            capo_application_signals.types.instrumentation_type.deserialize_json(
                data["InstrumentationType"]
            )
        )
    else:
        raise DeserializationError(
            "ListInstrumentationConfigurationsRequest.instrumentation_type required"
        )
    if data.get("SyncedAt") is not None:
        import capo_application_signals.types._prelude.timestamp

        out["synced_at"] = (
            capo_application_signals.types._prelude.timestamp.deserialize_json(
                data["SyncedAt"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
