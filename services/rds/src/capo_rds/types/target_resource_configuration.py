"""Generated from Smithy shape ``com.amazonaws.rds#TargetResourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element
from capo_rds.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rds.types.db_and_cluster_arn
    import capo_rds.types.kms_key_id_or_arn


class TargetResourceConfiguration(TypedDict, closed=True):
    source_arn: "capo_rds.types.db_and_cluster_arn.DBAndClusterArn"
    """<p>The Amazon Resource Name (ARN) of the DB cluster or DB instance in the blue environment to which this configuration applies.</p>"""
    target_kms_key_id: NotRequired["capo_rds.types.kms_key_id_or_arn.KmsKeyIdOrArn"]
    """<p>The Amazon Web Services KMS key identifier for encryption of the corresponding resource in the green environment.</p> <p>The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.</p> <p>Specify this setting in either of the following cases:</p> <ul> <li> <p>You want the green resource to use a different KMS key than the blue resource.</p> </li> <li> <p>The blue resource is unencrypted and you want to encrypt the green resource.</p> </li> </ul> <p>For Aurora, encryption applies at the DB cluster level. Specify a DB cluster ARN in <code>SourceArn</code>. All DB instances in that cluster use the same KMS key.</p> <p>For RDS, encryption applies at the DB instance level. Specify a DB instance ARN in <code>SourceArn</code>. To encrypt read replicas, include a separate entry for each one. Each entry can specify a different KMS key.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TargetResourceConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}SourceArn", str(value["source_arn"])))
    if "target_kms_key_id" in value:
        pairs.append((f"{key_prefix}TargetKmsKeyId", str(value["target_kms_key_id"])))


def deserialize_query(el: Element) -> TargetResourceConfiguration:
    out: TargetResourceConfiguration = {}  # type: ignore[typeddict-item]
    child_source_arn = el.find("SourceArn")
    if child_source_arn is not None:
        out["source_arn"] = str(child_source_arn.text or "")
    else:
        raise DeserializationError("TargetResourceConfiguration.source_arn required")
    child_target_kms_key_id = el.find("TargetKmsKeyId")
    if child_target_kms_key_id is not None:
        out["target_kms_key_id"] = str(child_target_kms_key_id.text or "")
    return out
