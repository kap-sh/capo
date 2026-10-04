"""Generated from Smithy shape ``com.amazonaws.securityhub#RemediationGuidanceSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.remediation_parameter_list
    import capo_securityhub.types.remediation_step_list
    import capo_securityhub.types.remediation_string_list


class RemediationGuidanceSpecification(TypedDict, closed=True):
    parameters: NotRequired[
        "capo_securityhub.types.remediation_parameter_list.RemediationParameterList"
    ]
    """<p>An array of the parameters used in running the steps provided.</p>"""
    steps: NotRequired[
        "capo_securityhub.types.remediation_step_list.RemediationStepList"
    ]
    """<p>An array of ordered steps for resolving the remediation targets.</p>"""
    expected_end_state: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The expected end state of the associated resources after completion of the steps.</p>"""
    required_permissions: NotRequired[
        "capo_securityhub.types.remediation_string_list.RemediationStringList"
    ]
    """<p>An array of required permissions to run the steps.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemediationGuidanceSpecification) -> dict:
    out: dict = {}
    if "parameters" in value:
        import capo_securityhub.types.remediation_parameter_list

        out["Parameters"] = (
            capo_securityhub.types.remediation_parameter_list.serialize_json(
                value["parameters"]
            )
        )
    if "steps" in value:
        import capo_securityhub.types.remediation_step_list

        out["Steps"] = capo_securityhub.types.remediation_step_list.serialize_json(
            value["steps"]
        )
    if "expected_end_state" in value:
        out["ExpectedEndState"] = value["expected_end_state"]
    if "required_permissions" in value:
        import capo_securityhub.types.remediation_string_list

        out["RequiredPermissions"] = (
            capo_securityhub.types.remediation_string_list.serialize_json(
                value["required_permissions"]
            )
        )
    return out


def deserialize_json(data: dict) -> RemediationGuidanceSpecification:
    out: RemediationGuidanceSpecification = {}  # type: ignore[typeddict-item]
    if data.get("Parameters") is not None:
        import capo_securityhub.types.remediation_parameter_list

        out["parameters"] = (
            capo_securityhub.types.remediation_parameter_list.deserialize_json(
                data["Parameters"]
            )
        )
    if data.get("Steps") is not None:
        import capo_securityhub.types.remediation_step_list

        out["steps"] = capo_securityhub.types.remediation_step_list.deserialize_json(
            data["Steps"]
        )
    if data.get("ExpectedEndState") is not None:
        out["expected_end_state"] = data["ExpectedEndState"]
    if data.get("RequiredPermissions") is not None:
        import capo_securityhub.types.remediation_string_list

        out["required_permissions"] = (
            capo_securityhub.types.remediation_string_list.deserialize_json(
                data["RequiredPermissions"]
            )
        )
    return out
