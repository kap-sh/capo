"""Generated from Smithy shape ``com.amazonaws.opensearch#UpgradeDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.advanced_options
    import capo_opensearch.types.boolean
    import capo_opensearch.types.domain_name
    import capo_opensearch.types.version_string


class UpgradeDomainRequest(TypedDict, closed=True):
    domain_name: "capo_opensearch.types.domain_name.DomainName"
    """<p>Name of the OpenSearch Service domain that you want to upgrade.</p>"""
    target_version: "capo_opensearch.types.version_string.VersionString"
    """<p>OpenSearch or Elasticsearch version to which you want to upgrade, in the format Opensearch_X.Y or Elasticsearch_X.Y.</p>"""
    perform_check_only: NotRequired["capo_opensearch.types.boolean.Boolean"]
    """<p>When true, indicates that an upgrade eligibility check needs to be performed. Does not actually perform the upgrade.</p>"""
    advanced_options: NotRequired[
        "capo_opensearch.types.advanced_options.AdvancedOptions"
    ]
    """<p>Only supports the <code>override_main_response_version</code> parameter and not other advanced options. You can only include this option when upgrading to an OpenSearch version. Specifies whether the domain reports its version as 7.10 so that it continues to work with Elasticsearch OSS clients and plugins.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpgradeDomainRequest) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    out["TargetVersion"] = value["target_version"]
    if "perform_check_only" in value:
        out["PerformCheckOnly"] = value["perform_check_only"]
    if "advanced_options" in value:
        import capo_opensearch.types.advanced_options

        out["AdvancedOptions"] = capo_opensearch.types.advanced_options.serialize_json(
            value["advanced_options"]
        )
    return out


def deserialize_json(data: dict) -> UpgradeDomainRequest:
    out: UpgradeDomainRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("AdvancedOptions") is not None:
        import capo_opensearch.types.advanced_options

        out["advanced_options"] = (
            capo_opensearch.types.advanced_options.deserialize_json(
                data["AdvancedOptions"]
            )
        )
    return out
