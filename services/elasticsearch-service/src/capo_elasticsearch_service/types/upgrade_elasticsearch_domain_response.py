"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#UpgradeElasticsearchDomainResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.boolean
    import capo_elasticsearch_service.types.change_progress_details
    import capo_elasticsearch_service.types.deployment_strategy_override_options
    import capo_elasticsearch_service.types.domain_name
    import capo_elasticsearch_service.types.elasticsearch_version_string


class UpgradeElasticsearchDomainResponse(TypedDict, closed=True):
    domain_name: NotRequired["capo_elasticsearch_service.types.domain_name.DomainName"]
    target_version: NotRequired[
        "capo_elasticsearch_service.types.elasticsearch_version_string.ElasticsearchVersionString"
    ]
    """<p>The version of Elasticsearch that you intend to upgrade the domain to.</p>"""
    perform_check_only: NotRequired["capo_elasticsearch_service.types.boolean.Boolean"]
    """<p> This flag, when set to True, indicates that an Upgrade Eligibility Check needs to be performed. This will not actually perform the Upgrade. </p>"""
    deployment_strategy_options: NotRequired[
        "capo_elasticsearch_service.types.deployment_strategy_override_options.DeploymentStrategyOverrideOptions"
    ]
    """<p>The deployment strategy override used for the upgrade.</p>"""
    change_progress_details: NotRequired[
        "capo_elasticsearch_service.types.change_progress_details.ChangeProgressDetails"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpgradeElasticsearchDomainResponse) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "target_version" in value:
        out["TargetVersion"] = value["target_version"]
    if "perform_check_only" in value:
        out["PerformCheckOnly"] = value["perform_check_only"]
    if "deployment_strategy_options" in value:
        import capo_elasticsearch_service.types.deployment_strategy_override_options

        out["DeploymentStrategyOptions"] = (
            capo_elasticsearch_service.types.deployment_strategy_override_options.serialize_json(
                value["deployment_strategy_options"]
            )
        )
    if "change_progress_details" in value:
        import capo_elasticsearch_service.types.change_progress_details

        out["ChangeProgressDetails"] = (
            capo_elasticsearch_service.types.change_progress_details.serialize_json(
                value["change_progress_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpgradeElasticsearchDomainResponse:
    out: UpgradeElasticsearchDomainResponse = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    if data.get("TargetVersion") is not None:
        out["target_version"] = data["TargetVersion"]
    if data.get("PerformCheckOnly") is not None:
        out["perform_check_only"] = data["PerformCheckOnly"]
    if data.get("DeploymentStrategyOptions") is not None:
        import capo_elasticsearch_service.types.deployment_strategy_override_options

        out["deployment_strategy_options"] = (
            capo_elasticsearch_service.types.deployment_strategy_override_options.deserialize_json(
                data["DeploymentStrategyOptions"]
            )
        )
    if data.get("ChangeProgressDetails") is not None:
        import capo_elasticsearch_service.types.change_progress_details

        out["change_progress_details"] = (
            capo_elasticsearch_service.types.change_progress_details.deserialize_json(
                data["ChangeProgressDetails"]
            )
        )
    return out
