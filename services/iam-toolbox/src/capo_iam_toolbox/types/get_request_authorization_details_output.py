"""Generated from Smithy shape ``com.amazonaws.iamtoolbox#GetRequestAuthorizationDetailsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam_toolbox.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam_toolbox.types.authorization_context
    import capo_iam_toolbox.types.evaluations
    import capo_iam_toolbox.types.policy_info_list


class GetRequestAuthorizationDetailsOutput(TypedDict, closed=True):
    request_context: "capo_iam_toolbox.types.authorization_context.AuthorizationContext"
    """<p>The request context is the set of context keys and values that apply to the entire request and are shared by all evaluations.</p>"""
    evaluations: "capo_iam_toolbox.types.evaluations.Evaluations"
    """<p>The list of evaluations for this request. Each evaluation shows how a single action and resource pair was evaluated. This includes the context, the effect, and any policies that matched.</p>"""
    policies: "capo_iam_toolbox.types.policy_info_list.PolicyInfoList"
    """<p>The list of policies that were evaluated.</p>"""
    next_token: NotRequired["str"]
    """<p>The pagination token for retrieving the next page of evaluations. This value is absent when there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRequestAuthorizationDetailsOutput) -> dict:
    out: dict = {}
    import capo_iam_toolbox.types.authorization_context

    out["requestContext"] = capo_iam_toolbox.types.authorization_context.serialize_json(
        value["request_context"]
    )
    import capo_iam_toolbox.types.evaluations

    out["evaluations"] = capo_iam_toolbox.types.evaluations.serialize_json(
        value["evaluations"]
    )
    import capo_iam_toolbox.types.policy_info_list

    out["policies"] = capo_iam_toolbox.types.policy_info_list.serialize_json(
        value["policies"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetRequestAuthorizationDetailsOutput:
    out: GetRequestAuthorizationDetailsOutput = {}  # type: ignore[typeddict-item]
    if data.get("requestContext") is not None:
        import capo_iam_toolbox.types.authorization_context

        out["request_context"] = (
            capo_iam_toolbox.types.authorization_context.deserialize_json(
                data["requestContext"]
            )
        )
    else:
        raise DeserializationError(
            "GetRequestAuthorizationDetailsOutput.request_context required"
        )
    if data.get("evaluations") is not None:
        import capo_iam_toolbox.types.evaluations

        out["evaluations"] = capo_iam_toolbox.types.evaluations.deserialize_json(
            data["evaluations"]
        )
    else:
        raise DeserializationError(
            "GetRequestAuthorizationDetailsOutput.evaluations required"
        )
    if data.get("policies") is not None:
        import capo_iam_toolbox.types.policy_info_list

        out["policies"] = capo_iam_toolbox.types.policy_info_list.deserialize_json(
            data["policies"]
        )
    else:
        raise DeserializationError(
            "GetRequestAuthorizationDetailsOutput.policies required"
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
