"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#UpdateApplicationComponentConfigRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.app_type
    import capo_migrationhubstrategy.types.application_component_id
    import capo_migrationhubstrategy.types.boolean
    import capo_migrationhubstrategy.types.inclusion_status
    import capo_migrationhubstrategy.types.secrets_manager_key
    import capo_migrationhubstrategy.types.source_code_list
    import capo_migrationhubstrategy.types.strategy_option


class UpdateApplicationComponentConfigRequest(TypedDict, closed=True):
    application_component_id: "capo_migrationhubstrategy.types.application_component_id.ApplicationComponentId"
    """<p> The ID of the application component. The ID is unique within an AWS account. </p>"""
    inclusion_status: NotRequired[
        "capo_migrationhubstrategy.types.inclusion_status.InclusionStatus"
    ]
    """<p> Indicates whether the application component has been included for server recommendation or not. </p>"""
    strategy_option: NotRequired[
        "capo_migrationhubstrategy.types.strategy_option.StrategyOption"
    ]
    """<p> The preferred strategy options for the application component. Use values from the <a>GetApplicationComponentStrategies</a> response. </p>"""
    source_code_list: NotRequired[
        "capo_migrationhubstrategy.types.source_code_list.SourceCodeList"
    ]
    """<p> The list of source code configurations to update for the application component. </p>"""
    secrets_manager_key: NotRequired[
        "capo_migrationhubstrategy.types.secrets_manager_key.SecretsManagerKey"
    ]
    """<p> Database credentials. </p>"""
    configure_only: NotRequired["capo_migrationhubstrategy.types.boolean.Boolean"]
    """<p>Update the configuration request of an application component. If it is set to true, the source code and/or database credentials are updated. If it is set to false, the source code and/or database credentials are updated and an analysis is initiated.</p>"""
    app_type: NotRequired["capo_migrationhubstrategy.types.app_type.AppType"]
    """<p>The type of known component.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApplicationComponentConfigRequest) -> dict:
    out: dict = {}
    out["applicationComponentId"] = value["application_component_id"]
    if "inclusion_status" in value:
        out["inclusionStatus"] = value["inclusion_status"]
    if "strategy_option" in value:
        import capo_migrationhubstrategy.types.strategy_option

        out["strategyOption"] = (
            capo_migrationhubstrategy.types.strategy_option.serialize_json(
                value["strategy_option"]
            )
        )
    if "source_code_list" in value:
        import capo_migrationhubstrategy.types.source_code_list

        out["sourceCodeList"] = (
            capo_migrationhubstrategy.types.source_code_list.serialize_json(
                value["source_code_list"]
            )
        )
    if "secrets_manager_key" in value:
        out["secretsManagerKey"] = value["secrets_manager_key"]
    if "configure_only" in value:
        out["configureOnly"] = value["configure_only"]
    if "app_type" in value:
        out["appType"] = value["app_type"]
    return out


def deserialize_json(data: dict) -> UpdateApplicationComponentConfigRequest:
    out: UpdateApplicationComponentConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("applicationComponentId") is not None:
        out["application_component_id"] = data["applicationComponentId"]
    else:
        out["application_component_id"] = ""
    if data.get("inclusionStatus") is not None:
        out["inclusion_status"] = data["inclusionStatus"]
    if data.get("strategyOption") is not None:
        import capo_migrationhubstrategy.types.strategy_option

        out["strategy_option"] = (
            capo_migrationhubstrategy.types.strategy_option.deserialize_json(
                data["strategyOption"]
            )
        )
    if data.get("sourceCodeList") is not None:
        import capo_migrationhubstrategy.types.source_code_list

        out["source_code_list"] = (
            capo_migrationhubstrategy.types.source_code_list.deserialize_json(
                data["sourceCodeList"]
            )
        )
    if data.get("secretsManagerKey") is not None:
        out["secrets_manager_key"] = data["secretsManagerKey"]
    if data.get("configureOnly") is not None:
        out["configure_only"] = data["configureOnly"]
    if data.get("appType") is not None:
        out["app_type"] = data["appType"]
    return out


def redact_sensitive(value: UpdateApplicationComponentConfigRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "secrets_manager_key" in value:
        out["secrets_manager_key"] = "*** Sensitive Data Redacted ***"
    return out
