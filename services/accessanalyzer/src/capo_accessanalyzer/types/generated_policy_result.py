"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#GeneratedPolicyResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_accessanalyzer.types.generated_policy_list
    import capo_accessanalyzer.types.generated_policy_properties


class GeneratedPolicyResult(TypedDict, closed=True):
    properties: "capo_accessanalyzer.types.generated_policy_properties.GeneratedPolicyProperties"
    """<p>A <code>GeneratedPolicyProperties</code> object that contains properties of the generated policy.</p>"""
    generated_policies: NotRequired[
        "capo_accessanalyzer.types.generated_policy_list.GeneratedPolicyList"
    ]
    """<p>The text to use as the content for the new policy. The policy is created using the <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreatePolicy.html">CreatePolicy</a> action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeneratedPolicyResult) -> dict:
    out: dict = {}
    import capo_accessanalyzer.types.generated_policy_properties

    out["properties"] = (
        capo_accessanalyzer.types.generated_policy_properties.serialize_json(
            value["properties"]
        )
    )
    if "generated_policies" in value:
        import capo_accessanalyzer.types.generated_policy_list

        out["generatedPolicies"] = (
            capo_accessanalyzer.types.generated_policy_list.serialize_json(
                value["generated_policies"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeneratedPolicyResult:
    out: GeneratedPolicyResult = {}  # type: ignore[typeddict-item]
    if data.get("properties") is not None:
        import capo_accessanalyzer.types.generated_policy_properties

        out["properties"] = (
            capo_accessanalyzer.types.generated_policy_properties.deserialize_json(
                data["properties"]
            )
        )
    else:
        raise DeserializationError("GeneratedPolicyResult.properties required")
    if data.get("generatedPolicies") is not None:
        import capo_accessanalyzer.types.generated_policy_list

        out["generated_policies"] = (
            capo_accessanalyzer.types.generated_policy_list.deserialize_json(
                data["generatedPolicies"]
            )
        )
    return out
