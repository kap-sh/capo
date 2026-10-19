"""Generated from Smithy shape ``com.amazonaws.s3control#PutAccessPointPolicyForObjectLambdaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.object_lambda_access_point_name
    import capo_s3_control.types.object_lambda_policy


class PutAccessPointPolicyForObjectLambdaRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The account ID for the account that owns the specified Object Lambda Access Point.</p>"""
    name: "capo_s3_control.types.object_lambda_access_point_name.ObjectLambdaAccessPointName"
    """<p>The name of the Object Lambda Access Point.</p>"""
    policy: "capo_s3_control.types.object_lambda_policy.ObjectLambdaPolicy"
    """<p>Object Lambda Access Point resource policy document.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: PutAccessPointPolicyForObjectLambdaRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Policy").text = str(value["policy"])


def deserialize_xml(el: Element) -> PutAccessPointPolicyForObjectLambdaRequest:
    out: PutAccessPointPolicyForObjectLambdaRequest = {}  # type: ignore[typeddict-item]
    child_policy = el.find("Policy")
    if child_policy is not None:
        out["policy"] = str(child_policy.text or "")
    else:
        out["policy"] = ""
    return out
