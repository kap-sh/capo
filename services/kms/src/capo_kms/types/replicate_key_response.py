"""Generated from Smithy shape ``com.amazonaws.kms#ReplicateKeyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.key_metadata
    import capo_kms.types.policy_type
    import capo_kms.types.tag_list


class ReplicateKeyResponse(TypedDict, closed=True):
    replica_key_metadata: NotRequired["capo_kms.types.key_metadata.KeyMetadata"]
    """<p>Displays details about the new replica key, including its Amazon Resource Name (<a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN">key ARN</a>) and <a href="https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html">Key states of KMS keys</a>. It also includes the ARN and Amazon Web Services Region of its primary key and other replica keys.</p>"""
    replica_policy: NotRequired["capo_kms.types.policy_type.PolicyType"]
    """<p>The key policy of the new replica key. The value is a key policy document in JSON format.</p>"""
    replica_tags: NotRequired["capo_kms.types.tag_list.TagList"]
    """<p>The tags on the new replica key. The value is a list of tag key and tag value pairs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicateKeyResponse) -> dict:
    out: dict = {}
    if "replica_key_metadata" in value:
        import capo_kms.types.key_metadata

        out["ReplicaKeyMetadata"] = capo_kms.types.key_metadata.serialize_aws_json_1_1(
            value["replica_key_metadata"]
        )
    if "replica_policy" in value:
        out["ReplicaPolicy"] = value["replica_policy"]
    if "replica_tags" in value:
        import capo_kms.types.tag_list

        out["ReplicaTags"] = capo_kms.types.tag_list.serialize_aws_json_1_1(
            value["replica_tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReplicateKeyResponse:
    out: ReplicateKeyResponse = {}  # type: ignore[typeddict-item]
    if data.get("ReplicaKeyMetadata") is not None:
        import capo_kms.types.key_metadata

        out["replica_key_metadata"] = (
            capo_kms.types.key_metadata.deserialize_aws_json_1_1(
                data["ReplicaKeyMetadata"]
            )
        )
    if data.get("ReplicaPolicy") is not None:
        out["replica_policy"] = data["ReplicaPolicy"]
    if data.get("ReplicaTags") is not None:
        import capo_kms.types.tag_list

        out["replica_tags"] = capo_kms.types.tag_list.deserialize_aws_json_1_1(
            data["ReplicaTags"]
        )
    return out
