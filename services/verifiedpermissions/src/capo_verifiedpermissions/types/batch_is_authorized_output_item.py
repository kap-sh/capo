"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#BatchIsAuthorizedOutputItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.batch_is_authorized_input_item
    import capo_verifiedpermissions.types.decision
    import capo_verifiedpermissions.types.determining_policy_list
    import capo_verifiedpermissions.types.evaluation_error_list


class BatchIsAuthorizedOutputItem(TypedDict, closed=True):
    request: "capo_verifiedpermissions.types.batch_is_authorized_input_item.BatchIsAuthorizedInputItem"
    """<p>The authorization request that initiated the decision.</p>"""
    decision: "capo_verifiedpermissions.types.decision.Decision"
    """<p>An authorization decision that indicates if the authorization request should be allowed or denied.</p>"""
    determining_policies: (
        "capo_verifiedpermissions.types.determining_policy_list.DeterminingPolicyList"
    )
    """<p>The list of determining policies used to make the authorization decision. For example, if there are two matching policies, where one is a forbid and the other is a permit, then the forbid policy will be the determining policy. In the case of multiple matching permit policies then there would be multiple determining policies. In the case that no policies match, and hence the response is DENY, there would be no determining policies.</p>"""
    errors: "capo_verifiedpermissions.types.evaluation_error_list.EvaluationErrorList"
    """<p>Errors that occurred while making an authorization decision. For example, a policy might reference an entity or attribute that doesn't exist in the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchIsAuthorizedOutputItem) -> dict:
    out: dict = {}
    import capo_verifiedpermissions.types.batch_is_authorized_input_item

    out["request"] = (
        capo_verifiedpermissions.types.batch_is_authorized_input_item.serialize_aws_json_1_0(
            value["request"]
        )
    )
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
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchIsAuthorizedOutputItem:
    out: BatchIsAuthorizedOutputItem = {}  # type: ignore[typeddict-item]
    if data.get("request") is not None:
        import capo_verifiedpermissions.types.batch_is_authorized_input_item

        out["request"] = (
            capo_verifiedpermissions.types.batch_is_authorized_input_item.deserialize_aws_json_1_0(
                data["request"]
            )
        )
    else:
        raise DeserializationError("BatchIsAuthorizedOutputItem.request required")
    if data.get("decision") is not None:
        import capo_verifiedpermissions.types.decision

        out["decision"] = (
            capo_verifiedpermissions.types.decision.deserialize_aws_json_1_0(
                data["decision"]
            )
        )
    else:
        import typing

        out["decision"] = typing.cast(
            "capo_verifiedpermissions.types.decision.Decision", ""
        )
    if data.get("determiningPolicies") is not None:
        import capo_verifiedpermissions.types.determining_policy_list

        out["determining_policies"] = (
            capo_verifiedpermissions.types.determining_policy_list.deserialize_aws_json_1_0(
                data["determiningPolicies"]
            )
        )
    else:
        out["determining_policies"] = []
    if data.get("errors") is not None:
        import capo_verifiedpermissions.types.evaluation_error_list

        out["errors"] = (
            capo_verifiedpermissions.types.evaluation_error_list.deserialize_aws_json_1_0(
                data["errors"]
            )
        )
    else:
        out["errors"] = []
    return out


def redact_sensitive(value: BatchIsAuthorizedOutputItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "request" in value:
        import capo_verifiedpermissions.types.batch_is_authorized_input_item

        out["request"] = (
            capo_verifiedpermissions.types.batch_is_authorized_input_item.redact_sensitive(
                value["request"]
            )
        )
    if "errors" in value:
        import capo_verifiedpermissions.types.evaluation_error_list

        out["errors"] = (
            capo_verifiedpermissions.types.evaluation_error_list.redact_sensitive(
                value["errors"]
            )
        )
    return out
