"""Generated from Smithy shape ``com.amazonaws.ec2#CreateSpotDatafeedSubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.string


class CreateSpotDatafeedSubscriptionRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    bucket: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the Amazon S3 bucket in which to store the Spot Instance data feed. For more information about bucket names, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html">Bucket naming rules</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    prefix: NotRequired["capo_ec2.types.string.String"]
    """<p>The prefix for the data feed file names.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateSpotDatafeedSubscriptionRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "bucket" in value:
        pairs.append((f"{key_prefix}Bucket", str(value["bucket"])))
    if "prefix" in value:
        pairs.append((f"{key_prefix}Prefix", str(value["prefix"])))


def deserialize_ec2_query(el: Element) -> CreateSpotDatafeedSubscriptionRequest:
    out: CreateSpotDatafeedSubscriptionRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_bucket = el.find("bucket")
    if child_bucket is not None:
        out["bucket"] = str(child_bucket.text or "")
    child_prefix = el.find("prefix")
    if child_prefix is not None:
        out["prefix"] = str(child_prefix.text or "")
    return out
