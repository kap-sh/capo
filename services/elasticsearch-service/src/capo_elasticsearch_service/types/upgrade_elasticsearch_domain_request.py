"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#UpgradeElasticsearchDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.boolean
    import capo_elasticsearch_service.types.deployment_strategy_override_options
    import capo_elasticsearch_service.types.domain_name
    import capo_elasticsearch_service.types.elasticsearch_version_string


class UpgradeElasticsearchDomainRequest(TypedDict, closed=True):
    domain_name: "capo_elasticsearch_service.types.domain_name.DomainName"
    target_version: "capo_elasticsearch_service.types.elasticsearch_version_string.ElasticsearchVersionString"
    """<p>The version of Elasticsearch that you intend to upgrade the domain to.</p>"""
    perform_check_only: NotRequired["capo_elasticsearch_service.types.boolean.Boolean"]
    """<p> This flag, when set to True, indicates that an Upgrade Eligibility Check needs to be performed. This will not actually perform the Upgrade. </p>"""
    deployment_strategy_options: NotRequired[
        "capo_elasticsearch_service.types.deployment_strategy_override_options.DeploymentStrategyOverrideOptions"
    ]
    """<p>Overrides the deployment strategy for this upgrade. To run a cloned blue/green upgrade, set <code>DeploymentStrategy</code> to <code>ClonedBlueGreen</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpgradeElasticsearchDomainRequest) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
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
    return out


def deserialize_json(data: dict) -> UpgradeElasticsearchDomainRequest:
    out: UpgradeElasticsearchDomainRequest = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        out["domain_name"] = ""
    if data.get("TargetVersion") is not None:
        out["target_version"] = data["TargetVersion"]
    else:
        out["target_version"] = ""
    if data.get("PerformCheckOnly") is not None:
        out["perform_check_only"] = data["PerformCheckOnly"]
    if data.get("DeploymentStrategyOptions") is not None:
        import capo_elasticsearch_service.types.deployment_strategy_override_options

        out["deployment_strategy_options"] = (
            capo_elasticsearch_service.types.deployment_strategy_override_options.deserialize_json(
                data["DeploymentStrategyOptions"]
            )
        )
    return out
