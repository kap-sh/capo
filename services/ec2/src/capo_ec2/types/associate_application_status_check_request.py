"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateApplicationStatusCheckRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.application_status_check_id
    import capo_ec2.types.boolean
    import capo_ec2.types.custom_key_value_pair_request_set
    import capo_ec2.types.instance_id_list
    import capo_ec2.types.string


class AssociateApplicationStatusCheckRequest(TypedDict, closed=True):
    application_status_check_id: NotRequired[
        "capo_ec2.types.application_status_check_id.ApplicationStatusCheckId"
    ]
    """<p>The ID of the application status check to associate.</p>"""
    target_tag_associations: NotRequired[
        "capo_ec2.types.custom_key_value_pair_request_set.CustomKeyValuePairRequestSet"
    ]
    """<p>The <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html">tags</a> to associate the application status check with. Each tag is a key-value pair. When you associate tags, the application status check automatically monitors all instances that have the specified tags.</p>"""
    instance_ids: NotRequired["capo_ec2.types.instance_id_list.InstanceIdList"]
    """<p>The IDs of the instances to associate with the application status check.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If you retry a request with the same token, the service ignores the request but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssociateApplicationStatusCheckRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "application_status_check_id" in value:
        pairs.append(
            (
                f"{key_prefix}ApplicationStatusCheckId",
                str(value["application_status_check_id"]),
            )
        )
    if "target_tag_associations" in value:
        import capo_ec2.types.custom_key_value_pair_request_set

        capo_ec2.types.custom_key_value_pair_request_set.serialize_ec2_query(
            value["target_tag_associations"], pairs, f"{key_prefix}TargetTagAssociation"
        )
    if "instance_ids" in value:
        import capo_ec2.types.instance_id_list

        capo_ec2.types.instance_id_list.serialize_ec2_query(
            value["instance_ids"], pairs, f"{key_prefix}InstanceId"
        )
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> AssociateApplicationStatusCheckRequest:
    out: AssociateApplicationStatusCheckRequest = {}  # type: ignore[typeddict-item]
    child_application_status_check_id = el.find("ApplicationStatusCheckId")
    if child_application_status_check_id is not None:
        out["application_status_check_id"] = str(
            child_application_status_check_id.text or ""
        )
    child_target_tag_associations = el.find("TargetTagAssociation")
    if child_target_tag_associations is not None:
        import capo_ec2.types.custom_key_value_pair_request_set

        out["target_tag_associations"] = (
            capo_ec2.types.custom_key_value_pair_request_set.deserialize_ec2_query(
                child_target_tag_associations
            )
        )
    child_instance_ids = el.find("InstanceId")
    if child_instance_ids is not None:
        import capo_ec2.types.instance_id_list

        out["instance_ids"] = capo_ec2.types.instance_id_list.deserialize_ec2_query(
            child_instance_ids
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
