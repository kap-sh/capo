"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ContextContent``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.application_type
    import capo_wellarchitected.types.context_account_id_list
    import capo_wellarchitected.types.context_aws_service_list
    import capo_wellarchitected.types.context_region_list
    import capo_wellarchitected.types.context_resource_tag_list
    import capo_wellarchitected.types.context_resource_type_list
    import capo_wellarchitected.types.criticality
    import capo_wellarchitected.types.sensitive_string


class ContextContent(TypedDict, closed=True):
    account_ids: NotRequired[
        "capo_wellarchitected.types.context_account_id_list.ContextAccountIdList"
    ]
    """<p>The Amazon Web Services account IDs associated with this application context.</p>"""
    regions: NotRequired[
        "capo_wellarchitected.types.context_region_list.ContextRegionList"
    ]
    """<p>The Amazon Web Services Regions where this application operates.</p>"""
    aws_services: NotRequired[
        "capo_wellarchitected.types.context_aws_service_list.ContextAwsServiceList"
    ]
    """<p>The Amazon Web Services services used by this application.</p>"""
    resource_types: NotRequired[
        "capo_wellarchitected.types.context_resource_type_list.ContextResourceTypeList"
    ]
    """<p>The Amazon Web Services resource types relevant to this application.</p>"""
    resource_tags: NotRequired[
        "capo_wellarchitected.types.context_resource_tag_list.ContextResourceTagList"
    ]
    """<p>Resource tags used to scope this application context.</p>"""
    application_overview: NotRequired[
        "capo_wellarchitected.types.sensitive_string.SensitiveString"
    ]
    """<p>A free-form overview of the application.</p>"""
    industry: NotRequired["capo_wellarchitected.types.sensitive_string.SensitiveString"]
    """<p>The industry vertical for this application.</p>"""
    application_type: NotRequired[
        "capo_wellarchitected.types.application_type.ApplicationType"
    ]
    """<p>The type of the application.</p>"""
    criticality: NotRequired["capo_wellarchitected.types.criticality.Criticality"]
    """<p>The business criticality of the application.</p>"""
    architecture_overview: NotRequired[
        "capo_wellarchitected.types.sensitive_string.SensitiveString"
    ]
    """<p>A free-form description of the application architecture.</p>"""
    additional_context: NotRequired[
        "capo_wellarchitected.types.sensitive_string.SensitiveString"
    ]
    """<p>Additional context not captured by other fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContextContent) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import capo_wellarchitected.types.context_account_id_list

        out["accountIds"] = (
            capo_wellarchitected.types.context_account_id_list.serialize_json(
                value["account_ids"]
            )
        )
    if "regions" in value:
        import capo_wellarchitected.types.context_region_list

        out["regions"] = capo_wellarchitected.types.context_region_list.serialize_json(
            value["regions"]
        )
    if "aws_services" in value:
        import capo_wellarchitected.types.context_aws_service_list

        out["awsServices"] = (
            capo_wellarchitected.types.context_aws_service_list.serialize_json(
                value["aws_services"]
            )
        )
    if "resource_types" in value:
        import capo_wellarchitected.types.context_resource_type_list

        out["resourceTypes"] = (
            capo_wellarchitected.types.context_resource_type_list.serialize_json(
                value["resource_types"]
            )
        )
    if "resource_tags" in value:
        import capo_wellarchitected.types.context_resource_tag_list

        out["resourceTags"] = (
            capo_wellarchitected.types.context_resource_tag_list.serialize_json(
                value["resource_tags"]
            )
        )
    if "application_overview" in value:
        out["applicationOverview"] = value["application_overview"]
    if "industry" in value:
        out["industry"] = value["industry"]
    if "application_type" in value:
        import capo_wellarchitected.types.application_type

        out["applicationType"] = (
            capo_wellarchitected.types.application_type.serialize_json(
                value["application_type"]
            )
        )
    if "criticality" in value:
        import capo_wellarchitected.types.criticality

        out["criticality"] = capo_wellarchitected.types.criticality.serialize_json(
            value["criticality"]
        )
    if "architecture_overview" in value:
        out["architectureOverview"] = value["architecture_overview"]
    if "additional_context" in value:
        out["additionalContext"] = value["additional_context"]
    return out


def deserialize_json(data: dict) -> ContextContent:
    out: ContextContent = {}  # type: ignore[typeddict-item]
    if data.get("accountIds") is not None:
        import capo_wellarchitected.types.context_account_id_list

        out["account_ids"] = (
            capo_wellarchitected.types.context_account_id_list.deserialize_json(
                data["accountIds"]
            )
        )
    if data.get("regions") is not None:
        import capo_wellarchitected.types.context_region_list

        out["regions"] = (
            capo_wellarchitected.types.context_region_list.deserialize_json(
                data["regions"]
            )
        )
    if data.get("awsServices") is not None:
        import capo_wellarchitected.types.context_aws_service_list

        out["aws_services"] = (
            capo_wellarchitected.types.context_aws_service_list.deserialize_json(
                data["awsServices"]
            )
        )
    if data.get("resourceTypes") is not None:
        import capo_wellarchitected.types.context_resource_type_list

        out["resource_types"] = (
            capo_wellarchitected.types.context_resource_type_list.deserialize_json(
                data["resourceTypes"]
            )
        )
    if data.get("resourceTags") is not None:
        import capo_wellarchitected.types.context_resource_tag_list

        out["resource_tags"] = (
            capo_wellarchitected.types.context_resource_tag_list.deserialize_json(
                data["resourceTags"]
            )
        )
    if data.get("applicationOverview") is not None:
        out["application_overview"] = data["applicationOverview"]
    if data.get("industry") is not None:
        out["industry"] = data["industry"]
    if data.get("applicationType") is not None:
        import capo_wellarchitected.types.application_type

        out["application_type"] = (
            capo_wellarchitected.types.application_type.deserialize_json(
                data["applicationType"]
            )
        )
    if data.get("criticality") is not None:
        import capo_wellarchitected.types.criticality

        out["criticality"] = capo_wellarchitected.types.criticality.deserialize_json(
            data["criticality"]
        )
    if data.get("architectureOverview") is not None:
        out["architecture_overview"] = data["architectureOverview"]
    if data.get("additionalContext") is not None:
        out["additional_context"] = data["additionalContext"]
    return out


def redact_sensitive(value: ContextContent) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "application_overview" in value:
        out["application_overview"] = "*** Sensitive Data Redacted ***"
    if "industry" in value:
        out["industry"] = "*** Sensitive Data Redacted ***"
    if "architecture_overview" in value:
        out["architecture_overview"] = "*** Sensitive Data Redacted ***"
    if "additional_context" in value:
        out["additional_context"] = "*** Sensitive Data Redacted ***"
    return out
