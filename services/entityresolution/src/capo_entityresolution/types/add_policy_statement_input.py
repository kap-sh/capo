"""Generated from Smithy shape ``com.amazonaws.entityresolution#AddPolicyStatementInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.statement_action_list
    import capo_entityresolution.types.statement_condition
    import capo_entityresolution.types.statement_effect
    import capo_entityresolution.types.statement_id
    import capo_entityresolution.types.statement_principal_list
    import capo_entityresolution.types.venice_global_arn


class AddPolicyStatementInput(TypedDict, closed=True):
    arn: "capo_entityresolution.types.venice_global_arn.VeniceGlobalArn"
    """<p>The Amazon Resource Name (ARN) of the resource that will be accessed by the principal.</p>"""
    statement_id: "capo_entityresolution.types.statement_id.StatementId"
    """<p>A statement identifier that differentiates the statement from others in the same policy.</p>"""
    effect: "capo_entityresolution.types.statement_effect.StatementEffect"
    """<p>Determines whether the permissions specified in the policy are to be allowed (<code>Allow</code>) or denied (<code>Deny</code>).</p> <important> <p> If you set the value of the <code>effect</code> parameter to <code>Deny</code> for the <code>AddPolicyStatement</code> operation, you must also set the value of the <code>effect</code> parameter in the <code>policy</code> to <code>Deny</code> for the <code>PutPolicy</code> operation.</p> </important>"""
    action: "capo_entityresolution.types.statement_action_list.StatementActionList"
    """<p>The action that the principal can use on the resource. </p> <p>For example, <code>entityresolution:GetIdMappingJob</code>, <code>entityresolution:GetMatchingJob</code>.</p>"""
    principal: (
        "capo_entityresolution.types.statement_principal_list.StatementPrincipalList"
    )
    """<p>The Amazon Web Services service or Amazon Web Services account that can access the resource defined as ARN.</p>"""
    condition: NotRequired[
        "capo_entityresolution.types.statement_condition.StatementCondition"
    ]
    """<p>A set of condition keys that you can use in key policies.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddPolicyStatementInput) -> dict:
    out: dict = {}
    import capo_entityresolution.types.statement_effect

    out["effect"] = capo_entityresolution.types.statement_effect.serialize_json(
        value["effect"]
    )
    import capo_entityresolution.types.statement_action_list

    out["action"] = capo_entityresolution.types.statement_action_list.serialize_json(
        value["action"]
    )
    import capo_entityresolution.types.statement_principal_list

    out["principal"] = (
        capo_entityresolution.types.statement_principal_list.serialize_json(
            value["principal"]
        )
    )
    if "condition" in value:
        out["condition"] = value["condition"]
    return out


def deserialize_json(data: dict) -> AddPolicyStatementInput:
    out: AddPolicyStatementInput = {}  # type: ignore[typeddict-item]
    if data.get("effect") is not None:
        import capo_entityresolution.types.statement_effect

        out["effect"] = capo_entityresolution.types.statement_effect.deserialize_json(
            data["effect"]
        )
    else:
        import typing

        out["effect"] = typing.cast(
            "capo_entityresolution.types.statement_effect.StatementEffect", ""
        )
    if data.get("action") is not None:
        import capo_entityresolution.types.statement_action_list

        out["action"] = (
            capo_entityresolution.types.statement_action_list.deserialize_json(
                data["action"]
            )
        )
    else:
        out["action"] = []
    if data.get("principal") is not None:
        import capo_entityresolution.types.statement_principal_list

        out["principal"] = (
            capo_entityresolution.types.statement_principal_list.deserialize_json(
                data["principal"]
            )
        )
    else:
        out["principal"] = []
    if data.get("condition") is not None:
        out["condition"] = data["condition"]
    return out
