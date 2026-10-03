"""Generated from Smithy shape ``com.amazonaws.batch#EFSAuthorizationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.efs_authorization_config_iam
    import capo_batch.types.string


class EFSAuthorizationConfig(TypedDict, closed=True):
    access_point_id: NotRequired["capo_batch.types.string.String"]
    """<p>The Amazon EFS access point ID to use. If an access point is specified, the root directory value specified in the <code>EFSVolumeConfiguration</code> must either be omitted or set to <code>/</code> which enforces the path set on the EFS access point. If an access point is used, transit encryption must be enabled in the <code>EFSVolumeConfiguration</code>. For more information, see <a href="https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html">Working with Amazon EFS access points</a> in the <i>Amazon Elastic File System User Guide</i>.</p>"""
    iam: NotRequired[
        "capo_batch.types.efs_authorization_config_iam.EFSAuthorizationConfigIAM"
    ]
    """<p>Whether or not to use the Batch job IAM role defined in a job definition when mounting the Amazon EFS file system. If enabled, transit encryption must be enabled in the <code>EFSVolumeConfiguration</code>. If this parameter is omitted, the default value of <code>DISABLED</code> is used. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/efs-volumes.html#efs-volume-accesspoints">Using Amazon EFS access points</a> in the <i>Batch User Guide</i>. EFS IAM authorization requires that <code>TransitEncryption</code> be <code>ENABLED</code> and that a <code>JobRoleArn</code> is specified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EFSAuthorizationConfig) -> dict:
    out: dict = {}
    if "access_point_id" in value:
        out["accessPointId"] = value["access_point_id"]
    if "iam" in value:
        import capo_batch.types.efs_authorization_config_iam

        out["iam"] = capo_batch.types.efs_authorization_config_iam.serialize_json(
            value["iam"]
        )
    return out


def deserialize_json(data: dict) -> EFSAuthorizationConfig:
    out: EFSAuthorizationConfig = {}  # type: ignore[typeddict-item]
    if data.get("accessPointId") is not None:
        out["access_point_id"] = data["accessPointId"]
    if data.get("iam") is not None:
        import capo_batch.types.efs_authorization_config_iam

        out["iam"] = capo_batch.types.efs_authorization_config_iam.deserialize_json(
            data["iam"]
        )
    return out
