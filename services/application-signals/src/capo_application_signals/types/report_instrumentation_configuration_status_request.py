"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ReportInstrumentationConfigurationStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.instrumentation_configuration_status_list


class ReportInstrumentationConfigurationStatusRequest(TypedDict, closed=True):
    service: "str"
    """<p>The service that the reported configurations belong to.</p>"""
    environment: "str"
    """<p>The environment that the service is running in.</p>"""
    configurations: "capo_application_signals.types.instrumentation_configuration_status_list.InstrumentationConfigurationStatusList"
    """<p>An array of configuration status reports (up to 100) that include the instrumentation type, signal type, location hash, status, timestamp, and optional error cause.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReportInstrumentationConfigurationStatusRequest) -> dict:
    out: dict = {}
    out["Service"] = value["service"]
    out["Environment"] = value["environment"]
    import capo_application_signals.types.instrumentation_configuration_status_list

    out["Configurations"] = (
        capo_application_signals.types.instrumentation_configuration_status_list.serialize_json(
            value["configurations"]
        )
    )
    return out


def deserialize_json(data: dict) -> ReportInstrumentationConfigurationStatusRequest:
    out: ReportInstrumentationConfigurationStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("Service") is not None:
        out["service"] = data["Service"]
    else:
        out["service"] = ""
    if data.get("Environment") is not None:
        out["environment"] = data["Environment"]
    else:
        out["environment"] = ""
    if data.get("Configurations") is not None:
        import capo_application_signals.types.instrumentation_configuration_status_list

        out["configurations"] = (
            capo_application_signals.types.instrumentation_configuration_status_list.deserialize_json(
                data["Configurations"]
            )
        )
    else:
        out["configurations"] = []
    return out
