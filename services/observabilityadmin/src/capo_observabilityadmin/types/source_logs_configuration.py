"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#SourceLogsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.data_source_filter_string
    import capo_observabilityadmin.types.encrypted_log_group_strategy
    import capo_observabilityadmin.types.logs_filter_string


class SourceLogsConfiguration(TypedDict, closed=True):
    log_group_selection_criteria: (
        "capo_observabilityadmin.types.logs_filter_string.LogsFilterString"
    )
    """<p>The selection criteria that specifies which source log groups to centralize. The selection criteria uses the same format as OAM link filters.</p>"""
    data_source_selection_criteria: NotRequired[
        "capo_observabilityadmin.types.data_source_filter_string.DataSourceFilterString"
    ]
    """<p>The selection criteria that specifies which data sources to centralize. The selection criteria uses the same filter expression format as <code>LogGroupSelectionCriteria</code>, but operates on <code>DataSourceName</code> and <code>DataSourceType</code> operands. When both <code>LogGroupSelectionCriteria</code> and <code>DataSourceSelectionCriteria</code> are specified, a log event must match both criteria to be centralized.</p>"""
    encrypted_log_group_strategy: "capo_observabilityadmin.types.encrypted_log_group_strategy.EncryptedLogGroupStrategy"
    """<p>A strategy determining whether to centralize source log groups that are encrypted with customer managed KMS keys (CMK). ALLOW will consider CMK encrypted source log groups for centralization while SKIP will skip CMK encrypted source log groups from centralization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceLogsConfiguration) -> dict:
    out: dict = {}
    out["LogGroupSelectionCriteria"] = value.get("log_group_selection_criteria", "*")
    if "data_source_selection_criteria" in value:
        out["DataSourceSelectionCriteria"] = value["data_source_selection_criteria"]
    import capo_observabilityadmin.types.encrypted_log_group_strategy

    out["EncryptedLogGroupStrategy"] = (
        capo_observabilityadmin.types.encrypted_log_group_strategy.serialize_json(
            value["encrypted_log_group_strategy"]
        )
    )
    return out


def deserialize_json(data: dict) -> SourceLogsConfiguration:
    out: SourceLogsConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("LogGroupSelectionCriteria") is not None:
        out["log_group_selection_criteria"] = data["LogGroupSelectionCriteria"]
    else:
        out["log_group_selection_criteria"] = "*"
    if data.get("DataSourceSelectionCriteria") is not None:
        out["data_source_selection_criteria"] = data["DataSourceSelectionCriteria"]
    if data.get("EncryptedLogGroupStrategy") is not None:
        import capo_observabilityadmin.types.encrypted_log_group_strategy

        out["encrypted_log_group_strategy"] = (
            capo_observabilityadmin.types.encrypted_log_group_strategy.deserialize_json(
                data["EncryptedLogGroupStrategy"]
            )
        )
    else:
        import typing

        out["encrypted_log_group_strategy"] = typing.cast(
            "capo_observabilityadmin.types.encrypted_log_group_strategy.EncryptedLogGroupStrategy",
            "",
        )
    return out
