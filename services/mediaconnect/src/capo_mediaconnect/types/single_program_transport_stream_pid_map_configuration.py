"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SingleProgramTransportStreamPidMapConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.action_string
    import capo_mediaconnect.types.auto_pid_map_configuration
    import capo_mediaconnect.types.pid_map_rules
    import capo_mediaconnect.types.program_clock_reference_pid_configuration
    import capo_mediaconnect.types.program_map_table_pid_configuration
    import capo_mediaconnect.types.program_number_configuration
    import capo_mediaconnect.types.transport_stream_id_configuration


class SingleProgramTransportStreamPidMapConfiguration(TypedDict, closed=True):
    rules: "capo_mediaconnect.types.pid_map_rules.PidMapRules"
    """<p>The ordered list of up to 32 rules that determine the action for each elementary stream. MediaConnect applies the first rule that matches.</p>"""
    default_action: "capo_mediaconnect.types.action_string.ActionString"
    """<p>The action to apply to an elementary stream that doesn't match any rule.</p>"""
    transport_stream_id: NotRequired[
        "capo_mediaconnect.types.transport_stream_id_configuration.TransportStreamIdConfiguration"
    ]
    """<p>The transport stream ID (TSID) settings for the router output. By default, the router output passes through the TSID from the source.</p>"""
    program_number: NotRequired[
        "capo_mediaconnect.types.program_number_configuration.ProgramNumberConfiguration"
    ]
    """<p>The program number settings for the router output. By default, the router output passes through the program number from the source.</p>"""
    program_map_table_pid: NotRequired[
        "capo_mediaconnect.types.program_map_table_pid_configuration.ProgramMapTablePidConfiguration"
    ]
    """<p>The Program Map Table (PMT) PID settings for the router output. By default, the router output passes through the PMT PID from the source.</p>"""
    program_clock_reference_pid: NotRequired[
        "capo_mediaconnect.types.program_clock_reference_pid_configuration.ProgramClockReferencePidConfiguration"
    ]
    """<p>The Program Clock Reference (PCR) PID settings for the router output. By default, the router output passes through the PCR PID from the source.</p>"""
    auto: NotRequired[
        "capo_mediaconnect.types.auto_pid_map_configuration.AutoPidMapConfiguration"
    ]
    """<p>The settings for automatic Packet ID (PID) assignment. The default start PID is 512, with 32 PIDs per program.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SingleProgramTransportStreamPidMapConfiguration) -> dict:
    out: dict = {}
    import capo_mediaconnect.types.pid_map_rules

    out["rules"] = capo_mediaconnect.types.pid_map_rules.serialize_json(value["rules"])
    out["defaultAction"] = value["default_action"]
    if "transport_stream_id" in value:
        import capo_mediaconnect.types.transport_stream_id_configuration

        out["transportStreamId"] = (
            capo_mediaconnect.types.transport_stream_id_configuration.serialize_json(
                value["transport_stream_id"]
            )
        )
    if "program_number" in value:
        import capo_mediaconnect.types.program_number_configuration

        out["programNumber"] = (
            capo_mediaconnect.types.program_number_configuration.serialize_json(
                value["program_number"]
            )
        )
    if "program_map_table_pid" in value:
        import capo_mediaconnect.types.program_map_table_pid_configuration

        out["programMapTablePid"] = (
            capo_mediaconnect.types.program_map_table_pid_configuration.serialize_json(
                value["program_map_table_pid"]
            )
        )
    if "program_clock_reference_pid" in value:
        import capo_mediaconnect.types.program_clock_reference_pid_configuration

        out["programClockReferencePid"] = (
            capo_mediaconnect.types.program_clock_reference_pid_configuration.serialize_json(
                value["program_clock_reference_pid"]
            )
        )
    if "auto" in value:
        import capo_mediaconnect.types.auto_pid_map_configuration

        out["auto"] = capo_mediaconnect.types.auto_pid_map_configuration.serialize_json(
            value["auto"]
        )
    return out


def deserialize_json(data: dict) -> SingleProgramTransportStreamPidMapConfiguration:
    out: SingleProgramTransportStreamPidMapConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("rules") is not None:
        import capo_mediaconnect.types.pid_map_rules

        out["rules"] = capo_mediaconnect.types.pid_map_rules.deserialize_json(
            data["rules"]
        )
    else:
        out["rules"] = []
    if data.get("defaultAction") is not None:
        out["default_action"] = data["defaultAction"]
    else:
        out["default_action"] = ""
    if data.get("transportStreamId") is not None:
        import capo_mediaconnect.types.transport_stream_id_configuration

        out["transport_stream_id"] = (
            capo_mediaconnect.types.transport_stream_id_configuration.deserialize_json(
                data["transportStreamId"]
            )
        )
    if data.get("programNumber") is not None:
        import capo_mediaconnect.types.program_number_configuration

        out["program_number"] = (
            capo_mediaconnect.types.program_number_configuration.deserialize_json(
                data["programNumber"]
            )
        )
    if data.get("programMapTablePid") is not None:
        import capo_mediaconnect.types.program_map_table_pid_configuration

        out["program_map_table_pid"] = (
            capo_mediaconnect.types.program_map_table_pid_configuration.deserialize_json(
                data["programMapTablePid"]
            )
        )
    if data.get("programClockReferencePid") is not None:
        import capo_mediaconnect.types.program_clock_reference_pid_configuration

        out["program_clock_reference_pid"] = (
            capo_mediaconnect.types.program_clock_reference_pid_configuration.deserialize_json(
                data["programClockReferencePid"]
            )
        )
    if data.get("auto") is not None:
        import capo_mediaconnect.types.auto_pid_map_configuration

        out["auto"] = (
            capo_mediaconnect.types.auto_pid_map_configuration.deserialize_json(
                data["auto"]
            )
        )
    return out
