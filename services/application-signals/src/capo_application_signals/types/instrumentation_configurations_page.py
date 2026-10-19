"""Generated from Smithy shape ``com.amazonaws.applicationsignals#InstrumentationConfigurationsPage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_application_signals.types.instrumentation_configurations_without_service_env
    import capo_application_signals.types.next_token


class InstrumentationConfigurationsPage(TypedDict, closed=True):
    service: "str"
    """<p>The service name associated with the returned configurations.</p>"""
    environment: "str"
    """<p>The environment associated with the returned configurations.</p>"""
    changed: "bool"
    """<p>Indicates whether there are configuration changes since the provided <code>SyncedAt</code> timestamp.</p>"""
    latest_configurations: NotRequired[
        "capo_application_signals.types.instrumentation_configurations_without_service_env.InstrumentationConfigurationsWithoutServiceEnv"
    ]
    """<p>The current set of active instrumentation configurations for the service and environment. Items omit service and environment because they are provided in the request.</p>"""
    synced_at: "datetime.datetime"
    """<p>The server timestamp to supply on the next sync call.</p>"""
    sync_interval: "int"
    """<p>The suggested number of seconds to wait before the next sync request. This is at least 60 seconds to prevent excessive polling.</p>"""
    next_token: NotRequired["capo_application_signals.types.next_token.NextToken"]
    """<p>Pagination token to continue listing configurations when more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InstrumentationConfigurationsPage) -> dict:
    out: dict = {}
    out["Service"] = value["service"]
    out["Environment"] = value["environment"]
    out["Changed"] = value["changed"]
    if "latest_configurations" in value:
        import capo_application_signals.types.instrumentation_configurations_without_service_env

        out["LatestConfigurations"] = (
            capo_application_signals.types.instrumentation_configurations_without_service_env.serialize_json(
                value["latest_configurations"]
            )
        )
    import capo_application_signals.types._prelude.timestamp

    out["SyncedAt"] = capo_application_signals.types._prelude.timestamp.serialize_json(
        value["synced_at"]
    )
    out["SyncInterval"] = value["sync_interval"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> InstrumentationConfigurationsPage:
    out: InstrumentationConfigurationsPage = {}  # type: ignore[typeddict-item]
    if data.get("Service") is not None:
        out["service"] = data["Service"]
    else:
        out["service"] = ""
    if data.get("Environment") is not None:
        out["environment"] = data["Environment"]
    else:
        out["environment"] = ""
    if data.get("Changed") is not None:
        out["changed"] = data["Changed"]
    else:
        out["changed"] = False
    if data.get("LatestConfigurations") is not None:
        import capo_application_signals.types.instrumentation_configurations_without_service_env

        out["latest_configurations"] = (
            capo_application_signals.types.instrumentation_configurations_without_service_env.deserialize_json(
                data["LatestConfigurations"]
            )
        )
    if data.get("SyncedAt") is not None:
        import capo_application_signals.types._prelude.timestamp

        out["synced_at"] = (
            capo_application_signals.types._prelude.timestamp.deserialize_json(
                data["SyncedAt"]
            )
        )
    else:
        import datetime

        out["synced_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("SyncInterval") is not None:
        out["sync_interval"] = data["SyncInterval"]
    else:
        out["sync_interval"] = 0
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
