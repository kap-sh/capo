"""Generated from Smithy shape ``com.amazonaws.opensearch#CompareDomainConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.domain_arn
    import capo_opensearch.types.metadata_category_list


class CompareDomainConfigurationRequest(TypedDict, closed=True):
    source_domain_arn: "capo_opensearch.types.domain_arn.DomainArn"
    """<p>The Amazon Resource Name (ARN) of the domain to compare from.</p>"""
    target_domain_arn: "capo_opensearch.types.domain_arn.DomainArn"
    """<p>The Amazon Resource Name (ARN) of the domain to compare against.</p>"""
    categories: "capo_opensearch.types.metadata_category_list.MetadataCategoryList"
    """<p>The metadata categories to compare. At least one is required, and only the categories you name are read and returned.</p> <ul> <li> <p> <code>aliases</code> </p> </li> <li> <p> <code>alerting_monitors</code> </p> </li> <li> <p> <code>cluster_settings</code> </p> </li> <li> <p> <code>component_templates</code> </p> </li> <li> <p> <code>ingest_pipelines</code> </p> </li> <li> <p> <code>ism_policies</code> — index state management policies</p> </li> <li> <p> <code>security_action_groups</code> </p> </li> <li> <p> <code>security_internal_users</code> </p> </li> <li> <p> <code>security_role_mappings</code> </p> </li> <li> <p> <code>security_roles</code> </p> </li> <li> <p> <code>templates</code> — index templates</p> </li> </ul> <p>The set of categories grows over time, so this list is not fixed. A category the service does not recognise is rejected with the supported categories named in the error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CompareDomainConfigurationRequest) -> dict:
    out: dict = {}
    out["SourceDomainArn"] = value["source_domain_arn"]
    out["TargetDomainArn"] = value["target_domain_arn"]
    import capo_opensearch.types.metadata_category_list

    out["Categories"] = capo_opensearch.types.metadata_category_list.serialize_json(
        value["categories"]
    )
    return out


def deserialize_json(data: dict) -> CompareDomainConfigurationRequest:
    out: CompareDomainConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("SourceDomainArn") is not None:
        out["source_domain_arn"] = data["SourceDomainArn"]
    else:
        out["source_domain_arn"] = ""
    if data.get("TargetDomainArn") is not None:
        out["target_domain_arn"] = data["TargetDomainArn"]
    else:
        out["target_domain_arn"] = ""
    if data.get("Categories") is not None:
        import capo_opensearch.types.metadata_category_list

        out["categories"] = (
            capo_opensearch.types.metadata_category_list.deserialize_json(
                data["Categories"]
            )
        )
    else:
        out["categories"] = []
    return out
