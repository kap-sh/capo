"""Generated from Smithy shape ``com.amazonaws.securityagent#CreateAgentSpaceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.agent_name
    import capo_securityagent.types.aws_resources
    import capo_securityagent.types.code_review_settings
    import capo_securityagent.types.kms_key_id
    import capo_securityagent.types.tag_map
    import capo_securityagent.types.target_domain_id_list


class CreateAgentSpaceInput(TypedDict, closed=True):
    name: "capo_securityagent.types.agent_name.AgentName"
    """<p>The name of the agent space.</p>"""
    description: NotRequired["str"]
    """<p>A description of the agent space.</p>"""
    aws_resources: NotRequired["capo_securityagent.types.aws_resources.AWSResources"]
    """<p>The AWS resources to associate with the agent space.</p>"""
    target_domain_ids: NotRequired[
        "capo_securityagent.types.target_domain_id_list.TargetDomainIdList"
    ]
    """<p>The list of target domain identifiers to associate with the agent space.</p>"""
    code_review_settings: NotRequired[
        "capo_securityagent.types.code_review_settings.CodeReviewSettings"
    ]
    """<p>The code review settings for the agent space.</p>"""
    kms_key_id: NotRequired["capo_securityagent.types.kms_key_id.KmsKeyId"]
    """<p>The identifier of the AWS KMS key to use for encrypting data in the agent space.</p>"""
    tags: NotRequired["capo_securityagent.types.tag_map.TagMap"]
    """<p>The tags to associate with the agent space.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAgentSpaceInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "aws_resources" in value:
        import capo_securityagent.types.aws_resources

        out["awsResources"] = capo_securityagent.types.aws_resources.serialize_json(
            value["aws_resources"]
        )
    if "target_domain_ids" in value:
        import capo_securityagent.types.target_domain_id_list

        out["targetDomainIds"] = (
            capo_securityagent.types.target_domain_id_list.serialize_json(
                value["target_domain_ids"]
            )
        )
    if "code_review_settings" in value:
        import capo_securityagent.types.code_review_settings

        out["codeReviewSettings"] = (
            capo_securityagent.types.code_review_settings.serialize_json(
                value["code_review_settings"]
            )
        )
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "tags" in value:
        import capo_securityagent.types.tag_map

        out["tags"] = capo_securityagent.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateAgentSpaceInput:
    out: CreateAgentSpaceInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("awsResources") is not None:
        import capo_securityagent.types.aws_resources

        out["aws_resources"] = capo_securityagent.types.aws_resources.deserialize_json(
            data["awsResources"]
        )
    if data.get("targetDomainIds") is not None:
        import capo_securityagent.types.target_domain_id_list

        out["target_domain_ids"] = (
            capo_securityagent.types.target_domain_id_list.deserialize_json(
                data["targetDomainIds"]
            )
        )
    if data.get("codeReviewSettings") is not None:
        import capo_securityagent.types.code_review_settings

        out["code_review_settings"] = (
            capo_securityagent.types.code_review_settings.deserialize_json(
                data["codeReviewSettings"]
            )
        )
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("tags") is not None:
        import capo_securityagent.types.tag_map

        out["tags"] = capo_securityagent.types.tag_map.deserialize_json(data["tags"])
    return out
