"""Generated from Smithy shape ``com.amazonaws.configservice#ScopeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.boolean
    import capo_config_service.types.included_regions
    import capo_config_service.types.scope_type
    import capo_config_service.types.scope_values


class ScopeConfiguration(TypedDict, closed=True):
    scope_type: "capo_config_service.types.scope_type.ScopeType"
    """<p>The type of scope for the third-party cloud resources. Valid values include <code>tenant</code> and <code>subscription</code>.</p>"""
    scope_values: NotRequired["capo_config_service.types.scope_values.ScopeValues"]
    """<p>The list of specific scope values for the third-party cloud resources. For example, a list of Azure subscriptions or management groups.</p>"""
    all_regions: "capo_config_service.types.boolean.Boolean"
    """<p>Specifies whether to record resources from all supported regions for the third-party cloud service provider.</p>"""
    included_regions: NotRequired[
        "capo_config_service.types.included_regions.IncludedRegions"
    ]
    """<p>The list of regions from the third-party cloud service provider to include when recording resources. Used when <code>allRegions</code> is set to <code>false</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScopeConfiguration) -> dict:
    out: dict = {}
    out["scopeType"] = value["scope_type"]
    if "scope_values" in value:
        import capo_config_service.types.scope_values

        out["scopeValues"] = (
            capo_config_service.types.scope_values.serialize_aws_json_1_1(
                value["scope_values"]
            )
        )
    out["allRegions"] = value.get("all_regions", False)
    if "included_regions" in value:
        import capo_config_service.types.included_regions

        out["includedRegions"] = (
            capo_config_service.types.included_regions.serialize_aws_json_1_1(
                value["included_regions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ScopeConfiguration:
    out: ScopeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("scopeType") is not None:
        out["scope_type"] = data["scopeType"]
    else:
        out["scope_type"] = ""
    if data.get("scopeValues") is not None:
        import capo_config_service.types.scope_values

        out["scope_values"] = (
            capo_config_service.types.scope_values.deserialize_aws_json_1_1(
                data["scopeValues"]
            )
        )
    if data.get("allRegions") is not None:
        out["all_regions"] = data["allRegions"]
    else:
        out["all_regions"] = False
    if data.get("includedRegions") is not None:
        import capo_config_service.types.included_regions

        out["included_regions"] = (
            capo_config_service.types.included_regions.deserialize_aws_json_1_1(
                data["includedRegions"]
            )
        )
    return out
