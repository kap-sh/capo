"""Generated from Smithy shape ``com.amazonaws.iam#DelegationPermission``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.arn_type
    import capo_iam.types.policy_parameter_list_type


class DelegationPermission(TypedDict, closed=True):
    policy_template_arn: NotRequired["capo_iam.types.arn_type.arnType"]
    """<p>This ARN maps to a pre-registered policy content for this partner. See the <a href="">partner onboarding documentation</a> to understand how to create a delegation template.</p>"""
    parameters: NotRequired[
        "capo_iam.types.policy_parameter_list_type.policyParameterListType"
    ]
    """<p>A list of policy parameters that define the scope and constraints of the delegated permissions.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DelegationPermission, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "policy_template_arn" in value:
        pairs.append(
            (f"{key_prefix}PolicyTemplateArn", str(value["policy_template_arn"]))
        )
    if "parameters" in value:
        import capo_iam.types.policy_parameter_list_type

        capo_iam.types.policy_parameter_list_type.serialize_query(
            value["parameters"], pairs, f"{key_prefix}Parameters"
        )


def deserialize_query(el: Element) -> DelegationPermission:
    out: DelegationPermission = {}  # type: ignore[typeddict-item]
    child_policy_template_arn = el.find("PolicyTemplateArn")
    if child_policy_template_arn is not None:
        out["policy_template_arn"] = str(child_policy_template_arn.text or "")
    child_parameters = el.find("Parameters")
    if child_parameters is not None:
        import capo_iam.types.policy_parameter_list_type

        out["parameters"] = capo_iam.types.policy_parameter_list_type.deserialize_query(
            child_parameters
        )
    return out
