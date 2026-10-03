"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceCreditSpecificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.instance_credit_specification_list_request
    import capo_ec2.types.string


class ModifyInstanceCreditSpecificationRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring Idempotency</a>.</p>"""
    instance_credit_specifications: NotRequired[
        "capo_ec2.types.instance_credit_specification_list_request.InstanceCreditSpecificationListRequest"
    ]
    """<p>Information about the credit option for CPU usage.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyInstanceCreditSpecificationRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "instance_credit_specifications" in value:
        import capo_ec2.types.instance_credit_specification_list_request

        capo_ec2.types.instance_credit_specification_list_request.serialize_ec2_query(
            value["instance_credit_specifications"],
            pairs,
            f"{key_prefix}InstanceCreditSpecification",
        )


def deserialize_ec2_query(el: Element) -> ModifyInstanceCreditSpecificationRequest:
    out: ModifyInstanceCreditSpecificationRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_instance_credit_specifications = el.find("InstanceCreditSpecification")
    if child_instance_credit_specifications is not None:
        import capo_ec2.types.instance_credit_specification_list_request

        out["instance_credit_specifications"] = (
            capo_ec2.types.instance_credit_specification_list_request.deserialize_ec2_query(
                child_instance_credit_specifications
            )
        )
    return out
