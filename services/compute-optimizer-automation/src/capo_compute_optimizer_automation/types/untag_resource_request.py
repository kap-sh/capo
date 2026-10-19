"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.client_token
    import capo_compute_optimizer_automation.types.rule_arn
    import capo_compute_optimizer_automation.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_compute_optimizer_automation.types.rule_arn.RuleArn"
    """<p> The ARN of the resource to untag. </p>"""
    rule_revision: "int"
    """<p>The revision number of the automation rule to untag. This ensures you're untagging the correct version of the rule.</p>"""
    tag_keys: "capo_compute_optimizer_automation.types.tag_key_list.TagKeyList"
    """<p> The keys of the tags to remove from the resource. </p>"""
    client_token: NotRequired[
        "capo_compute_optimizer_automation.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Must be 1-64 characters long and contain only alphanumeric characters, underscores, and hyphens.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["ruleRevision"] = value["rule_revision"]
    import capo_compute_optimizer_automation.types.tag_key_list

    out["tagKeys"] = (
        capo_compute_optimizer_automation.types.tag_key_list.serialize_aws_json_1_0(
            value["tag_keys"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("ruleRevision") is not None:
        out["rule_revision"] = data["ruleRevision"]
    else:
        out["rule_revision"] = 0
    if data.get("tagKeys") is not None:
        import capo_compute_optimizer_automation.types.tag_key_list

        out["tag_keys"] = (
            capo_compute_optimizer_automation.types.tag_key_list.deserialize_aws_json_1_0(
                data["tagKeys"]
            )
        )
    else:
        out["tag_keys"] = []
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
