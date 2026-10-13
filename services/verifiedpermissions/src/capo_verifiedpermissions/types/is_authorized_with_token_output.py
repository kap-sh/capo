"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#IsAuthorizedWithTokenOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.decision
    import capo_verifiedpermissions.types.determining_policy_list
    import capo_verifiedpermissions.types.entity_identifier
    import capo_verifiedpermissions.types.evaluation_error_list


class IsAuthorizedWithTokenOutput(TypedDict, closed=True):
    decision: "capo_verifiedpermissions.types.decision.Decision"
    """<p>An authorization decision that indicates if the authorization request should be allowed or denied.</p>"""
    determining_policies: (
        "capo_verifiedpermissions.types.determining_policy_list.DeterminingPolicyList"
    )
    """<p>The list of determining policies used to make the authorization decision. For example, if there are multiple matching policies, where at least one is a forbid policy, then because forbid always overrides permit the forbid policies are the determining policies. If all matching policies are permit policies, then those policies are the determining policies. When no policies match and the response is the default DENY, there are no determining policies.</p>"""
    errors: "capo_verifiedpermissions.types.evaluation_error_list.EvaluationErrorList"
    """<p>Errors that occurred while making an authorization decision. For example, a policy references an entity or entity attribute that does not exist in the slice.</p>"""
    principal: NotRequired[
        "capo_verifiedpermissions.types.entity_identifier.EntityIdentifier"
    ]
    """<p>The identifier of the principal in the ID or access token.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IsAuthorizedWithTokenOutput) -> dict:
    out: dict = {}
    import capo_verifiedpermissions.types.decision

    out["decision"] = capo_verifiedpermissions.types.decision.serialize_aws_json_1_0(
        value["decision"]
    )
    import capo_verifiedpermissions.types.determining_policy_list

    out["determiningPolicies"] = (
        capo_verifiedpermissions.types.determining_policy_list.serialize_aws_json_1_0(
            value["determining_policies"]
        )
    )
    import capo_verifiedpermissions.types.evaluation_error_list

    out["errors"] = (
        capo_verifiedpermissions.types.evaluation_error_list.serialize_aws_json_1_0(
            value["errors"]
        )
    )
    if "principal" in value:
        import capo_verifiedpermissions.types.entity_identifier

        out["principal"] = (
            capo_verifiedpermissions.types.entity_identifier.serialize_aws_json_1_0(
                value["principal"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> IsAuthorizedWithTokenOutput:
    out: IsAuthorizedWithTokenOutput = {}  # type: ignore[typeddict-item]
    if data.get("decision") is not None:
        import capo_verifiedpermissions.types.decision

        out["decision"] = (
            capo_verifiedpermissions.types.decision.deserialize_aws_json_1_0(
                data["decision"]
            )
        )
    else:
        raise DeserializationError("IsAuthorizedWithTokenOutput.decision required")
    if data.get("determiningPolicies") is not None:
        import capo_verifiedpermissions.types.determining_policy_list

        out["determining_policies"] = (
            capo_verifiedpermissions.types.determining_policy_list.deserialize_aws_json_1_0(
                data["determiningPolicies"]
            )
        )
    else:
        raise DeserializationError(
            "IsAuthorizedWithTokenOutput.determining_policies required"
        )
    if data.get("errors") is not None:
        import capo_verifiedpermissions.types.evaluation_error_list

        out["errors"] = (
            capo_verifiedpermissions.types.evaluation_error_list.deserialize_aws_json_1_0(
                data["errors"]
            )
        )
    else:
        raise DeserializationError("IsAuthorizedWithTokenOutput.errors required")
    if data.get("principal") is not None:
        import capo_verifiedpermissions.types.entity_identifier

        out["principal"] = (
            capo_verifiedpermissions.types.entity_identifier.deserialize_aws_json_1_0(
                data["principal"]
            )
        )
    return out


def redact_sensitive(value: IsAuthorizedWithTokenOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "errors" in value:
        import capo_verifiedpermissions.types.evaluation_error_list

        out["errors"] = (
            capo_verifiedpermissions.types.evaluation_error_list.redact_sensitive(
                value["errors"]
            )
        )
    if "principal" in value:
        import capo_verifiedpermissions.types.entity_identifier

        out["principal"] = (
            capo_verifiedpermissions.types.entity_identifier.redact_sensitive(
                value["principal"]
            )
        )
    return out
