"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVerifiedAccessGroupPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.string
    import capo_ec2.types.verified_access_group_id
    import capo_ec2.types.verified_access_sse_specification_request


class ModifyVerifiedAccessGroupPolicyRequest(TypedDict, closed=True):
    verified_access_group_id: NotRequired[
        "capo_ec2.types.verified_access_group_id.VerifiedAccessGroupId"
    ]
    """<p>The ID of the Verified Access group.</p>"""
    policy_enabled: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>The status of the Verified Access policy.</p>"""
    policy_document: NotRequired["capo_ec2.types.string.String"]
    """<p>The Verified Access policy document.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency</a>.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    sse_specification: NotRequired[
        "capo_ec2.types.verified_access_sse_specification_request.VerifiedAccessSseSpecificationRequest"
    ]
    """<p>The options for server side encryption.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVerifiedAccessGroupPolicyRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "verified_access_group_id" in value:
        pairs.append(
            (
                f"{key_prefix}VerifiedAccessGroupId",
                str(value["verified_access_group_id"]),
            )
        )
    if "policy_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}PolicyEnabled",
                "true" if value["policy_enabled"] else "false",
            )
        )
    if "policy_document" in value:
        pairs.append((f"{key_prefix}PolicyDocument", str(value["policy_document"])))
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "sse_specification" in value:
        import capo_ec2.types.verified_access_sse_specification_request

        capo_ec2.types.verified_access_sse_specification_request.serialize_ec2_query(
            value["sse_specification"], pairs, f"{key_prefix}SseSpecification"
        )


def deserialize_ec2_query(el: Element) -> ModifyVerifiedAccessGroupPolicyRequest:
    out: ModifyVerifiedAccessGroupPolicyRequest = {}  # type: ignore[typeddict-item]
    child_verified_access_group_id = el.find("VerifiedAccessGroupId")
    if child_verified_access_group_id is not None:
        out["verified_access_group_id"] = str(child_verified_access_group_id.text or "")
    child_policy_enabled = el.find("PolicyEnabled")
    if child_policy_enabled is not None:
        out["policy_enabled"] = (child_policy_enabled.text or "").lower() == "true"
    child_policy_document = el.find("PolicyDocument")
    if child_policy_document is not None:
        out["policy_document"] = str(child_policy_document.text or "")
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_sse_specification = el.find("SseSpecification")
    if child_sse_specification is not None:
        import capo_ec2.types.verified_access_sse_specification_request

        out["sse_specification"] = (
            capo_ec2.types.verified_access_sse_specification_request.deserialize_ec2_query(
                child_sse_specification
            )
        )
    return out
