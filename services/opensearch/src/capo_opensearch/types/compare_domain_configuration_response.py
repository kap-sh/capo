"""Generated from Smithy shape ``com.amazonaws.opensearch#CompareDomainConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.compare_domain_configuration_category_map
    import capo_opensearch.types.domain_arn


class CompareDomainConfigurationResponse(TypedDict, closed=True):
    source_domain_arn: NotRequired["capo_opensearch.types.domain_arn.DomainArn"]
    """<p>The Amazon Resource Name (ARN) of the domain that was compared from.</p>"""
    target_domain_arn: NotRequired["capo_opensearch.types.domain_arn.DomainArn"]
    """<p>The Amazon Resource Name (ARN) of the domain that was compared against.</p>"""
    categories: NotRequired[
        "capo_opensearch.types.compare_domain_configuration_category_map.CompareDomainConfigurationCategoryMap"
    ]
    """<p>The comparison result for each category you requested, keyed by category name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CompareDomainConfigurationResponse) -> dict:
    out: dict = {}
    if "source_domain_arn" in value:
        out["SourceDomainArn"] = value["source_domain_arn"]
    if "target_domain_arn" in value:
        out["TargetDomainArn"] = value["target_domain_arn"]
    if "categories" in value:
        import capo_opensearch.types.compare_domain_configuration_category_map

        out["Categories"] = (
            capo_opensearch.types.compare_domain_configuration_category_map.serialize_json(
                value["categories"]
            )
        )
    return out


def deserialize_json(data: dict) -> CompareDomainConfigurationResponse:
    out: CompareDomainConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("SourceDomainArn") is not None:
        out["source_domain_arn"] = data["SourceDomainArn"]
    if data.get("TargetDomainArn") is not None:
        out["target_domain_arn"] = data["TargetDomainArn"]
    if data.get("Categories") is not None:
        import capo_opensearch.types.compare_domain_configuration_category_map

        out["categories"] = (
            capo_opensearch.types.compare_domain_configuration_category_map.deserialize_json(
                data["Categories"]
            )
        )
    return out
