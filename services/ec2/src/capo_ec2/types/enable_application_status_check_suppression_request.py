"""Generated from Smithy shape ``com.amazonaws.ec2#EnableApplicationStatusCheckSuppressionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.boxed_integer
    import capo_ec2.types.instance_id_list
    import capo_ec2.types.string


class EnableApplicationStatusCheckSuppressionRequest(TypedDict, closed=True):
    instance_ids: NotRequired["capo_ec2.types.instance_id_list.InstanceIdList"]
    """<p>The IDs of the instances for which to suppress application status checks.</p>"""
    duration_seconds: NotRequired["capo_ec2.types.boxed_integer.BoxedInteger"]
    """<p>The duration, in seconds, for which to suppress application status checks. If omitted, the application status check is suppressed indefinitely until you call <code>DisableApplicationStatusCheckSuppression</code>.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If you retry a request with the same token, the service ignores the request but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnableApplicationStatusCheckSuppressionRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_ids" in value:
        import capo_ec2.types.instance_id_list

        capo_ec2.types.instance_id_list.serialize_ec2_query(
            value["instance_ids"], pairs, f"{key_prefix}InstanceId"
        )
    if "duration_seconds" in value:
        pairs.append((f"{key_prefix}DurationSeconds", str(value["duration_seconds"])))
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> EnableApplicationStatusCheckSuppressionRequest:
    out: EnableApplicationStatusCheckSuppressionRequest = {}  # type: ignore[typeddict-item]
    child_instance_ids = el.find("InstanceId")
    if child_instance_ids is not None:
        import capo_ec2.types.instance_id_list

        out["instance_ids"] = capo_ec2.types.instance_id_list.deserialize_ec2_query(
            child_instance_ids
        )
    child_duration_seconds = el.find("DurationSeconds")
    if child_duration_seconds is not None:
        out["duration_seconds"] = int(child_duration_seconds.text or "")
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
