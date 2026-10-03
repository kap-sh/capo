"""Generated from Smithy shape ``com.amazonaws.lightsail#AccountLevelBpaSync``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.account_level_bpa_sync_status
    import capo_lightsail.types.boolean
    import capo_lightsail.types.bpa_status_message
    import capo_lightsail.types.iso_date


class AccountLevelBpaSync(TypedDict, closed=True):
    status: NotRequired[
        "capo_lightsail.types.account_level_bpa_sync_status.AccountLevelBpaSyncStatus"
    ]
    """<p>The status of the account-level BPA synchronization.</p> <p>The following statuses are possible:</p> <ul> <li> <p> <code>InSync</code> - Account-level BPA is synchronized. The Amazon S3 account-level BPA configuration applies to your Lightsail buckets.</p> </li> <li> <p> <code>NeverSynced</code> - Synchronization has not yet happened. The Amazon S3 account-level BPA configuration does not apply to your Lightsail buckets.</p> </li> <li> <p> <code>Failed</code> - Synchronization failed. The Amazon S3 account-level BPA configuration does not apply to your Lightsail buckets.</p> </li> <li> <p> <code>Defaulted</code> - Synchronization failed and account-level BPA for your Lightsail buckets is defaulted to <i>active</i>.</p> </li> </ul> <note> <p>You might need to complete further actions if the status is <code>Failed</code> or <code>Defaulted</code>. The <code>message</code> parameter provides more information for those statuses.</p> </note>"""
    last_synced_at: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp of when the account-level BPA configuration was last synchronized. This value is null when the account-level BPA configuration has not been synchronized.</p>"""
    message: NotRequired["capo_lightsail.types.bpa_status_message.BPAStatusMessage"]
    """<p>A message that provides a reason for a <code>Failed</code> or <code>Defaulted</code> synchronization status.</p> <p>The following messages are possible:</p> <ul> <li> <p> <code>SYNC_ON_HOLD</code> - The synchronization has not yet happened. This status message occurs immediately after you create your first Lightsail bucket. This status message should change after the first synchronization happens, approximately 1 hour after the first bucket is created.</p> </li> <li> <p> <code>DEFAULTED_FOR_SLR_MISSING</code> - The synchronization failed because the required service-linked role is missing from your Amazon Web Services account. The account-level BPA configuration for your Lightsail buckets is defaulted to <i>active</i> until the synchronization can occur. This means that all your buckets are private and not publicly accessible. For more information about how to create the required service-linked role to allow synchronization, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-using-service-linked-roles">Using Service-Linked Roles for Amazon Lightsail</a> in the <i>Amazon Lightsail Developer Guide</i>.</p> </li> <li> <p> <code>DEFAULTED_FOR_SLR_MISSING_ON_HOLD</code> - The synchronization failed because the required service-linked role is missing from your Amazon Web Services account. Account-level BPA is not yet configured for your Lightsail buckets. Therefore, only the bucket access permissions and individual object access permissions apply to your Lightsail buckets. For more information about how to create the required service-linked role to allow synchronization, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-using-service-linked-roles">Using Service-Linked Roles for Amazon Lightsail</a> in the <i>Amazon Lightsail Developer Guide</i>.</p> </li> <li> <p> <code>Unknown</code> - The reason that synchronization failed is unknown. Contact Amazon Web Services Support for more information.</p> </li> </ul>"""
    bpa_impacts_lightsail: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>A Boolean value that indicates whether account-level block public access is affecting your Lightsail buckets.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountLevelBpaSync) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_lightsail.types.account_level_bpa_sync_status

        out["status"] = (
            capo_lightsail.types.account_level_bpa_sync_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "last_synced_at" in value:
        import capo_lightsail.types.iso_date

        out["lastSyncedAt"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["last_synced_at"]
        )
    if "message" in value:
        import capo_lightsail.types.bpa_status_message

        out["message"] = capo_lightsail.types.bpa_status_message.serialize_aws_json_1_1(
            value["message"]
        )
    if "bpa_impacts_lightsail" in value:
        out["bpaImpactsLightsail"] = value["bpa_impacts_lightsail"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AccountLevelBpaSync:
    out: AccountLevelBpaSync = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_lightsail.types.account_level_bpa_sync_status

        out["status"] = (
            capo_lightsail.types.account_level_bpa_sync_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("lastSyncedAt") is not None:
        import capo_lightsail.types.iso_date

        out["last_synced_at"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["lastSyncedAt"]
        )
    if data.get("message") is not None:
        import capo_lightsail.types.bpa_status_message

        out["message"] = (
            capo_lightsail.types.bpa_status_message.deserialize_aws_json_1_1(
                data["message"]
            )
        )
    if data.get("bpaImpactsLightsail") is not None:
        out["bpa_impacts_lightsail"] = data["bpaImpactsLightsail"]
    return out
