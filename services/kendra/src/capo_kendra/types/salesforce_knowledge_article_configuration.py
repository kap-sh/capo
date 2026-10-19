"""Generated from Smithy shape ``com.amazonaws.kendra#SalesforceKnowledgeArticleConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.salesforce_custom_knowledge_article_type_configuration_list
    import capo_kendra.types.salesforce_knowledge_article_state_list
    import capo_kendra.types.salesforce_standard_knowledge_article_type_configuration


class SalesforceKnowledgeArticleConfiguration(TypedDict, closed=True):
    included_states: "capo_kendra.types.salesforce_knowledge_article_state_list.SalesforceKnowledgeArticleStateList"
    """<p>Specifies the document states that should be included when Amazon Kendra indexes knowledge articles. You must specify at least one state.</p>"""
    standard_knowledge_article_type_configuration: NotRequired[
        "capo_kendra.types.salesforce_standard_knowledge_article_type_configuration.SalesforceStandardKnowledgeArticleTypeConfiguration"
    ]
    """<p>Configuration information for standard Salesforce knowledge articles.</p>"""
    custom_knowledge_article_type_configurations: NotRequired[
        "capo_kendra.types.salesforce_custom_knowledge_article_type_configuration_list.SalesforceCustomKnowledgeArticleTypeConfigurationList"
    ]
    """<p>Configuration information for custom Salesforce knowledge articles.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SalesforceKnowledgeArticleConfiguration) -> dict:
    out: dict = {}
    import capo_kendra.types.salesforce_knowledge_article_state_list

    out["IncludedStates"] = (
        capo_kendra.types.salesforce_knowledge_article_state_list.serialize_aws_json_1_1(
            value["included_states"]
        )
    )
    if "standard_knowledge_article_type_configuration" in value:
        import capo_kendra.types.salesforce_standard_knowledge_article_type_configuration

        out["StandardKnowledgeArticleTypeConfiguration"] = (
            capo_kendra.types.salesforce_standard_knowledge_article_type_configuration.serialize_aws_json_1_1(
                value["standard_knowledge_article_type_configuration"]
            )
        )
    if "custom_knowledge_article_type_configurations" in value:
        import capo_kendra.types.salesforce_custom_knowledge_article_type_configuration_list

        out["CustomKnowledgeArticleTypeConfigurations"] = (
            capo_kendra.types.salesforce_custom_knowledge_article_type_configuration_list.serialize_aws_json_1_1(
                value["custom_knowledge_article_type_configurations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SalesforceKnowledgeArticleConfiguration:
    out: SalesforceKnowledgeArticleConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("IncludedStates") is not None:
        import capo_kendra.types.salesforce_knowledge_article_state_list

        out["included_states"] = (
            capo_kendra.types.salesforce_knowledge_article_state_list.deserialize_aws_json_1_1(
                data["IncludedStates"]
            )
        )
    else:
        out["included_states"] = []
    if data.get("StandardKnowledgeArticleTypeConfiguration") is not None:
        import capo_kendra.types.salesforce_standard_knowledge_article_type_configuration

        out["standard_knowledge_article_type_configuration"] = (
            capo_kendra.types.salesforce_standard_knowledge_article_type_configuration.deserialize_aws_json_1_1(
                data["StandardKnowledgeArticleTypeConfiguration"]
            )
        )
    if data.get("CustomKnowledgeArticleTypeConfigurations") is not None:
        import capo_kendra.types.salesforce_custom_knowledge_article_type_configuration_list

        out["custom_knowledge_article_type_configurations"] = (
            capo_kendra.types.salesforce_custom_knowledge_article_type_configuration_list.deserialize_aws_json_1_1(
                data["CustomKnowledgeArticleTypeConfigurations"]
            )
        )
    return out
