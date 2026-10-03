"""Generated from Smithy shape ``com.amazonaws.iam#GetContextKeysForPrincipalPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.arn_type
    import capo_iam.types.simulation_policy_list_type


class GetContextKeysForPrincipalPolicyRequest(TypedDict, closed=True):
    policy_source_arn: "capo_iam.types.arn_type.arnType"
    """<p>The ARN of a user, group, or role whose policies contain the context keys that you want listed. If you specify a user, the list includes context keys that are found in all policies that are attached to the user. The list also includes all groups that the user is a member of. If you pick a group or a role, then it includes only those context keys that are found in policies attached to that entity. Note that all parameters are shown in unencoded form here for clarity, but must be URL encoded to be included as a part of a real HTML request.</p> <p>For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    policy_input_list: NotRequired[
        "capo_iam.types.simulation_policy_list_type.SimulationPolicyListType"
    ]
    r"""<p>An optional list of additional policies for which you want the list of context keys that are referenced.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> used to validate this parameter is a string of characters consisting of the following:</p> <ul> <li> <p>Any printable ASCII character ranging from the space character (<code>\u0020</code>) through the end of the ASCII character range</p> </li> <li> <p>The printable characters in the Basic Latin and Latin-1 Supplement character set (through <code>\u00FF</code>)</p> </li> <li> <p>The special characters tab (<code>\u0009</code>), line feed (<code>\u000A</code>), and carriage return (<code>\u000D</code>)</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetContextKeysForPrincipalPolicyRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}PolicySourceArn", str(value["policy_source_arn"])))
    if "policy_input_list" in value:
        import capo_iam.types.simulation_policy_list_type

        capo_iam.types.simulation_policy_list_type.serialize_query(
            value["policy_input_list"], pairs, f"{key_prefix}PolicyInputList"
        )


def deserialize_query(el: Element) -> GetContextKeysForPrincipalPolicyRequest:
    out: GetContextKeysForPrincipalPolicyRequest = {}  # type: ignore[typeddict-item]
    child_policy_source_arn = el.find("PolicySourceArn")
    if child_policy_source_arn is not None:
        out["policy_source_arn"] = str(child_policy_source_arn.text or "")
    else:
        raise DeserializationError(
            "GetContextKeysForPrincipalPolicyRequest.policy_source_arn required"
        )
    child_policy_input_list = el.find("PolicyInputList")
    if child_policy_input_list is not None:
        import capo_iam.types.simulation_policy_list_type

        out["policy_input_list"] = (
            capo_iam.types.simulation_policy_list_type.deserialize_query(
                child_policy_input_list
            )
        )
    return out
