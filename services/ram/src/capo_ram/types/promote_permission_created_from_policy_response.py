"""Generated from Smithy shape ``com.amazonaws.ram#PromotePermissionCreatedFromPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ram.types.resource_share_permission_summary
    import capo_ram.types.string


class PromotePermissionCreatedFromPolicyResponse(TypedDict, closed=True):
    permission: NotRequired[
        "capo_ram.types.resource_share_permission_summary.ResourceSharePermissionSummary"
    ]
    """<p>The details of the promoted customer managed permission, including its <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a>, version, and status.</p>"""
    client_token: NotRequired["capo_ram.types.string.String"]
    """<p>The idempotency identifier associated with this request. If you want to repeat the same operation in an idempotent manner then you must include this value in the <code>clientToken</code> request parameter of that later call. All other parameters must also have the same values that you used in the first call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PromotePermissionCreatedFromPolicyResponse) -> dict:
    out: dict = {}
    if "permission" in value:
        import capo_ram.types.resource_share_permission_summary

        out["permission"] = (
            capo_ram.types.resource_share_permission_summary.serialize_json(
                value["permission"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> PromotePermissionCreatedFromPolicyResponse:
    out: PromotePermissionCreatedFromPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("permission") is not None:
        import capo_ram.types.resource_share_permission_summary

        out["permission"] = (
            capo_ram.types.resource_share_permission_summary.deserialize_json(
                data["permission"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
