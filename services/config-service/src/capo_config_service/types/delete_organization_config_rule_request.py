"""Generated from Smithy shape ``com.amazonaws.configservice#DeleteOrganizationConfigRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.organization_config_rule_name


class DeleteOrganizationConfigRuleRequest(TypedDict, closed=True):
    organization_config_rule_name: "capo_config_service.types.organization_config_rule_name.OrganizationConfigRuleName"
    """<p>The name of organization Config rule that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteOrganizationConfigRuleRequest) -> dict:
    out: dict = {}
    out["OrganizationConfigRuleName"] = value["organization_config_rule_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteOrganizationConfigRuleRequest:
    out: DeleteOrganizationConfigRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationConfigRuleName") is not None:
        out["organization_config_rule_name"] = data["OrganizationConfigRuleName"]
    else:
        out["organization_config_rule_name"] = ""
    return out
