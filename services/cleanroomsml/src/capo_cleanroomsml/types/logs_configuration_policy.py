"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#LogsConfigurationPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.account_id_list
    import capo_cleanroomsml.types.log_redaction_configuration
    import capo_cleanroomsml.types.log_type


class LogsConfigurationPolicy(TypedDict, closed=True):
    allowed_account_ids: "capo_cleanroomsml.types.account_id_list.AccountIdList"
    """<p>A list of account IDs that are allowed to access the logs.</p>"""
    filter_pattern: NotRequired["str"]
    """<p>A regular expression pattern that is used to parse the logs and return information that matches the pattern.</p>"""
    log_type: "capo_cleanroomsml.types.log_type.LogType"
    """<p>Specifies the type of log this policy applies to. The currently supported policies are ALL or ERROR_SUMMARY.</p>"""
    log_redaction_configuration: NotRequired[
        "capo_cleanroomsml.types.log_redaction_configuration.LogRedactionConfiguration"
    ]
    """<p>Specifies the log redaction configuration for this policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogsConfigurationPolicy) -> dict:
    out: dict = {}
    import capo_cleanroomsml.types.account_id_list

    out["allowedAccountIds"] = capo_cleanroomsml.types.account_id_list.serialize_json(
        value["allowed_account_ids"]
    )
    if "filter_pattern" in value:
        out["filterPattern"] = value["filter_pattern"]
    import capo_cleanroomsml.types.log_type

    out["logType"] = capo_cleanroomsml.types.log_type.serialize_json(
        value.get("log_type", "ALL")
    )
    if "log_redaction_configuration" in value:
        import capo_cleanroomsml.types.log_redaction_configuration

        out["logRedactionConfiguration"] = (
            capo_cleanroomsml.types.log_redaction_configuration.serialize_json(
                value["log_redaction_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> LogsConfigurationPolicy:
    out: LogsConfigurationPolicy = {}  # type: ignore[typeddict-item]
    if data.get("allowedAccountIds") is not None:
        import capo_cleanroomsml.types.account_id_list

        out["allowed_account_ids"] = (
            capo_cleanroomsml.types.account_id_list.deserialize_json(
                data["allowedAccountIds"]
            )
        )
    else:
        out["allowed_account_ids"] = []
    if data.get("filterPattern") is not None:
        out["filter_pattern"] = data["filterPattern"]
    if data.get("logType") is not None:
        import capo_cleanroomsml.types.log_type

        out["log_type"] = capo_cleanroomsml.types.log_type.deserialize_json(
            data["logType"]
        )
    else:
        out["log_type"] = "ALL"
    if data.get("logRedactionConfiguration") is not None:
        import capo_cleanroomsml.types.log_redaction_configuration

        out["log_redaction_configuration"] = (
            capo_cleanroomsml.types.log_redaction_configuration.deserialize_json(
                data["logRedactionConfiguration"]
            )
        )
    return out
